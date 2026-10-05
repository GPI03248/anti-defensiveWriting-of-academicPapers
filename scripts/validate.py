#!/usr/bin/env python3
"""Offline packaging and pinned-source checks; no manuscript quality claims."""
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'academic-paper-writing'


def git(*args, cwd=ROOT):
    return subprocess.check_output(['git', *args], cwd=cwd, text=True).strip()


def main():
    errors = []
    required = [ROOT / name for name in (
        'README.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md',
        'upstreams.lock.json', '.gitmodules', 'docs/integration.md',
        'docs/acceptance-cases.md')]
    required += [SKILL / name for name in (
        'SKILL.md', 'LICENSE', 'THIRD_PARTY_NOTICES.md', 'agents/openai.yaml')]
    for path in required:
        if not path.is_file():
            errors.append(f'Missing file: {path.relative_to(ROOT)}')
    if errors:
        print('\n'.join(errors))
        return 1

    text = (SKILL / 'SKILL.md').read_text()
    if not text.startswith('---\n') or '\n---\n' not in text[4:]:
        errors.append('SKILL.md requires YAML frontmatter')
    else:
        frontmatter = text.split('---', 2)[1]
        if not re.search(r'^name: academic-paper-writing$', frontmatter, re.M):
            errors.append('Skill name must match its folder')
        if not re.search(r'^description: .+', frontmatter, re.M):
            errors.append('Missing skill description')

    # Check integration-owned Markdown only. Upstream layouts remain upstream-owned.
    pages = list(ROOT.glob('*.md')) + list((ROOT / 'docs').rglob('*.md'))
    pages += list(SKILL.rglob('*.md'))
    for page in pages:
        for target in re.findall(r'\]\(([^)]+)\)', page.read_text()):
            if target.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            target = target.split('#', 1)[0]
            destination = (page.parent / target).resolve()
            if not destination.exists():
                errors.append(f'Broken link in {page.relative_to(ROOT)}: {target}')
            if page.is_relative_to(SKILL) and not destination.is_relative_to(SKILL):
                errors.append(f'Skill is not self-contained: {target}')

    for name in ('LICENSE', 'THIRD_PARTY_NOTICES.md'):
        if (ROOT / name).read_bytes() != (SKILL / name).read_bytes():
            errors.append(f'Root and skill copies differ: {name}')

    lock = json.loads((ROOT / 'upstreams.lock.json').read_text())
    expected = {'anti-defensive-writing', 'scholar-papercraft',
                'writing-skills', 'compass-skills'}
    records = lock['upstreams']
    if len(records) != 4 or {item['name'] for item in records} != expected:
        errors.append('Lock file must contain exactly the four selected upstreams')

    for item in records:
        path = ROOT / item['path']
        try:
            if not (path / '.git').exists():
                raise ValueError('Submodule not initialized')
            if git('rev-parse', 'HEAD', cwd=path) != item['commit']:
                errors.append(f"Checkout differs from lock: {item['name']}")
            index = git('ls-files', '--stage', '--', item['path']).split()
            if index[:2] != ['160000', item['commit']]:
                errors.append(f"Gitlink differs from lock: {item['name']}")
            url = git('config', '-f', '.gitmodules', '--get',
                      f"submodule.{item['path']}.url")
            if url != item['url']:
                errors.append(f"Submodule URL differs from lock: {item['name']}")
            if git('status', '--porcelain', cwd=path):
                errors.append(f"Upstream has local changes: {item['name']}")
            if not (path / item['entrypoint']).is_file():
                errors.append(f"Missing upstream entrypoint: {item['name']}")
            if item['license'] == 'MIT':
                upstream_license = (path / 'LICENSE').read_text().strip()
                if upstream_license not in (ROOT / 'THIRD_PARTY_NOTICES.md').read_text():
                    errors.append(f"Missing complete MIT notice: {item['name']}")
        except (subprocess.CalledProcessError, ValueError, OSError) as exc:
            errors.append(f"{item['name']}: {exc}")

    if errors:
        print('\n'.join(f'FAIL: {message}' for message in errors))
        return 1
    print(f'PASS: {len(pages)} Markdown files, self-contained skill, notices, '
          'and four clean pinned submodules verified.')
    print('Structural validation only; model writing behavior has not been evaluated.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
