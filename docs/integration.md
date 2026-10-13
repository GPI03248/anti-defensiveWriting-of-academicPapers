# 整合设计

本项目通过固定版本的四个 submodule 保留来源，以一个自包含 Skill 提供统一执行规则。上游仓库作为参考与维护来源；普通写作不运行四套完整工作流。

## 模块映射

| 来源 | 重点阅读的上游文件 | 整合目标 |
|---|---|---|
| anti-defensive-writing | `skill/anti-defensive-writing/SKILL.md` | `references/limitations.md`：识别重复限定、局限位置、指标取舍 |
| scholar-papercraft | `SKILL.md`、`references/reproducibility-reporting.md` | `references/artifact-boundary.md`：区分内部记录、复现说明与科学表达 |
| writing-skills | `for-agents/academic-voice/SKILL.md`、`for-agents/paper-writing/SKILL.md` | `references/argument-and-voice.md`：读者导向的论证与语体 |
| compass-skills | `skills/academic-humanizer/SKILL.md`、`references/global-pattern-contract.md` | `references/document-review.md`：保护含义、术语及功能性重复 |

表中整合目标相对于 `skills/academic-paper-writing/`。具体上游提交见 `upstreams.lock.json`，本项目 Git 索引中的 gitlink 应与其一致。

## 冲突处理

| 潜在冲突 | 本项目选择 |
|---|---|
| 集中局限 vs 保留推理所需条件 | 一般局限集中；局部条件、方法假设和摘要独立理解所需限定保留 |
| 移出文件信息 vs 保证方法可理解 | 移出操作定位；保留关键设计、实际方法、版本及正式标识 |
| 去除“AI 味” vs 学术规范 | 不设词汇、标点和句长配额；保护有效被动语态、转折与术语 |
| 加强表达 vs 保持证据强度 | 消除空泛示弱；不新增因果、显著性、泛化能力或优越性 |
| 完整工作流 vs 局部润色 | 按用户任务加载规则，不把段落编辑扩大为全文审计 |
| 强制收集作者判断 vs 已有充分材料 | 缺失判断影响叙事时询问；已明确的编辑继续执行 |
| 追溯每个结果 vs 反复自证真实性 | 对应关系留在内部；正文通过科学证据和图表支持结论 |

## 独立设计的部分

统一入口、优先级、材料分层、迁移状态规则、中英文组合示例、验收案例和离线校验脚本由本项目新增。没有导入上游的完整编排器、模型调用、安装器、论文数据或测试框架。

上游更新不会自动改变统一规则。更新维护时需检查实际差异，再决定哪些变化适合本项目；所有来源信息都属于项目维护记录，不属于论文内容。

## 个人改稿清单映射

[原始清单](sources/personal-revision-checklist.md) 和 [增量反馈](sources/personal-revision-checklist-2026-10.md) 原样保存为历史来源，不作为并行执行指令，也不由 Skill 引用。具体期刊、词例和稿件数据仅存在于来源档案；统一 Skill 提炼其中的判断依据。

| 经验主题 | 执行落点 | 通用判断 |
|---|---|---|
| 术语与语体 | `references/terminology-and-register.md` | 根据所指概念、领域习惯、定义和歧义决定操作，不设词汇替换表 |
| 摘要组织 | `references/abstract.md` | 形成独立可理解的论证，按核心回答取舍证据，不设数字配额 |
| 论证与章节 | `references/argument-and-voice.md` | 根据推理关系和章节功能组织内容，不预设段数或学科模板 |
| 结果呈现 | 同上 | 证据形式覆盖主张的关键维度，评估参考依据的局限，不设图数配额 |
| 局限与限定 | `references/limitations.md` | 合并无作用重复，保留局部解释所需条件 |
| 正文边界 | `references/artifact-boundary.md` | 按科学作用分配信息，保护关键方法，区分内部记录与正式披露 |
| 投稿适配 | `references/venue-adaptation.md` | 获取当前适用要求，区分官方规定与偏好，不内置具体期刊条目 |
| 全文复核与审计 | `references/document-review.md` | 依授权范围检查，追加记录并保留撤销历史，不将检索词当替换指令 |
| 判断情境 | `references/examples.md` | 解释适用边界，不收录真实稿件、结果参数或固定词语改写对 |

## 2026-10 增量与通用化处理

作者反馈属于本项目整合层的规则来源，不属于四个上游。后续抽象要求覆盖此前的具体替换建议、期刊笔记及稿件示例：它们保留在来源档案用于追溯，不再进入 README 的规则介绍或可独立复制的 Skill。

维护时检查规则能否用于新的领域和稿件：决策应依赖含义、证据、读者需要及当前要求，而非历史名称、数字或格式。保留足以指导操作的判断条件，避免把抽象化变成无从执行的口号。新增行为案例用于后续试用，不代表已经完成模型效果验证。
