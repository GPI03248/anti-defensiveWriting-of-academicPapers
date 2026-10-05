# 项目维护规则

- 本项目是四个上游写作规则的整合层。写作入口是 `skills/academic-paper-writing/SKILL.md`。
- 日常修改只涉及整合层；不要直接修改 `upstream/`。更新上游时检查各自 AGENTS.md、许可证、提交差异和锁文件。
- 保留 README 中的四方归属与 THIRD_PARTY_NOTICES.md；不要将所有子模块声明为本项目 MIT 内容。
- 修改规则时保持科学含义优先，不把集中局限变成删除必要限定，也不把正文边界变成删除关键方法。
- 保持 Skill 可独立复制，其 references 不依赖项目外的绝对路径。
- 完成后运行 `python3 scripts/validate.py`。行为验收标准见 `docs/acceptance-cases.md`；不要把结构校验报告成模型效果验证。
- 用户论文、实验数据和内部审计记录放在本项目之外，除非用户明确要求存放于此。
