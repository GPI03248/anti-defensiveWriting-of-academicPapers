# anti-defensiveWrting-of-academicPapers

面向中英文学术论文的非防御性写作与正文边界规范。项目名称保留创建者指定的拼写。

**本项目基于以下四个 GitHub 项目耦合整合而成，感谢原作者公开分享他们的规则、示例和工作流：**

| 上游项目 | 作者 / 维护者 | 在本项目中的作用 |
|---|---|---|
| [anti-defensive-writing](https://github.com/Kiterlin/anti-defensive-writing) | Kiterlin | 局限性放置、重复免责声明、论断范围与防御性措辞 |
| [scholar-papercraft](https://github.com/Tw6249/scholar-papercraft) | Tw6249 | 内部溯源与论文正文的边界、实验材料转化为科学描述 |
| [writing-skills](https://github.com/msimchowitz/writing-skills) | Max Simchowitz | 学术论证、读者理解、篇章结构与学术语体 |
| [compass-skills](https://github.com/dongshuyan/compass-skills) | dongshuyan / COMPASS Skills contributors | academic-humanizer 的语义保护、术语一致性和全文重复检查 |

整合层统一处理四类问题，并明确规则冲突时的优先级。四个原始项目以 Git submodule 保留在 `upstream/`，固定到具体提交；日常使用只需加载本项目的统一 Skill，不必同时启动四套流程。具体来源、整合选择和许可证见 [来源说明](THIRD_PARTY_NOTICES.md) 与 [整合设计](docs/integration.md)。本项目没有上游官方背书。

## 解决什么问题

- 同一项局限在摘要、引言、结果、图注和结论中反复出现。
- 论文正文夹带文件路径、SHA、脚本命令、核验日志和 agent 的工作汇报。
- 反复强调数据“真实”“已经核验”“可追溯”，挤占科学发现的表述。
- 逐个罗列所有实验，却没有围绕研究问题建立论证。
- 每段套用“结果—意义—局限”的同一模板，或为避免重复而改坏专业术语。

保留影响结果解释的实验条件、统计不确定性、负面结果和必要假设。一般局限集中讨论；使某项结论成立的条件在结论附近保留。正文、补充材料、公开复现仓库和作者内部记录各司其职。

## 直接使用

统一入口：[skills/academic-paper-writing/SKILL.md](skills/academic-paper-writing/SKILL.md)。它与同目录的 `references/`、`LICENSE`、`THIRD_PARTY_NOTICES.md` 构成可独立复制的 Skill 包。无需运行上游 Python 脚本，也无需安装额外库。

在当前机器上可以直接给 agent 以下指令：

```text
读取 /data/gpi/Gitcode/anti-defensiveWrting-of-academicPapers/skills/academic-paper-writing/SKILL.md，
按照其引用规则修改我提供的论文。保留科学含义和证据强度，
合并重复局限，将文件级溯源和复现操作说明移出正文，
检查全文机械重复。默认只返回修订正文。
```

对于支持 Skill 目录的 agent，可将 `skills/academic-paper-writing/` 整个复制到其技能目录；安装位置按使用环境选择。本次创建没有改动全局技能配置。

调用示例：

```text
使用 $academic-paper-writing 审查这篇论文，只诊断不改写。
给出问题位置、处理建议，以及必须保留的限定。
```

```text
使用 $academic-paper-writing 修改这段 Results。
输出干净正文；另附简短迁移记录，说明哪些内容适合放到 README。
```

```text
使用 $academic-paper-writing 根据给定结果和提纲起草 Discussion。
所有事实以给定材料为准，把一般局限集中到末尾小节。
```

## 耦合流程

1. 明确编辑范围，保留数值、比较关系、因果强度、术语与必要条件。
2. 分离论文内容和作者侧溯源信息。
3. 分类处理局限：必要局部限定、集中讨论、重复声明、无依据的自我否定。
4. 按研究问题与证据组织段落，形成可读的学术论证。
5. 检查全文重复模式，再逐项核对修改前后的科学含义。

任务只涉及一个段落时，仅检查这个段落及提供的必要上下文；不会强制启动全文审计。流程详见 [统一规则](skills/academic-paper-writing/SKILL.md)，中英文示例见 [示例](skills/academic-paper-writing/references/examples.md)。

## 目录

```text
skills/academic-paper-writing/   可独立使用的统一 Skill
docs/integration.md              四个上游的映射与冲突处理
upstream/                       四个固定版本的 Git submodule
upstreams.lock.json             来源 URL、提交号和许可证记录
scripts/validate.py              离线结构、链接和版本一致性检查
THIRD_PARTY_NOTICES.md           致谢与第三方许可证说明
LICENSE                         本项目整合层的 MIT 许可证
```

上游的提交号属于项目维护信息，只存放在这里和锁文件中，不应随写作过程进入论文正文。

## 获取与维护上游

获取本项目时使用 `git clone --recurse-submodules <本项目的仓库地址>`；本地新建项目尚未配置远程地址。

普通 clone 后，在项目根目录运行：

```bash
git submodule update --init --recursive
python3 scripts/validate.py
```

`upstreams.lock.json` 和 Git submodule 同时固定上游版本。更新时在相应子模块中选择并检出目标提交，阅读变化及许可证，再同步锁文件、整合说明和 Git gitlink；不要仅运行 `update --remote` 后忽略规则变化。

验证脚本不会访问网络或修改稿件，也不能判断一篇论文是否已经达到发表标准。可用 [行为验收案例](docs/acceptance-cases.md) 检查真实 agent 输出；其中案例是人工设计的测试材料，不是研究结果。

## 许可证与致谢

本项目新增整合层采用 MIT；归属于第三方的材料继续遵守各自条款。再次感谢 **Kiterlin、Tw6249、Max Simchowitz 和 COMPASS Skills contributors**。四者分别提供了防御性写作、正文边界、学术论证和全文语言检查方面的重要基础。

`scholar-papercraft` 在锁定版本中未发现明确许可证文件，因此通过独立 submodule 引用其仓库；没有将其原文件复制进统一 Skill 或纳入本项目 MIT 授权。完整说明及三个 MIT 上游的许可证保存在 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。
