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

来源为创建者提供的 `TMP/学术论文修改要点.md`，由 Claude 根据其此前修改《高阶数值格式忠实复现的编程智能体工作流》的 PROMPT 整理。项目内 [原始副本](sources/personal-revision-checklist.md) 保持原文，用于追溯，不作为另一套并行执行指令；执行以统一 Skill 及其 references 为准。

| 原清单部分 | 整合到 Skill 的位置 | 处理 |
|---|---|---|
| 0 五个问题 | `references/argument-and-voice.md` | 作为信息用途判断，保留期刊要求的正式声明 |
| 1 突出创新、次要内容简述 | `references/argument-and-voice.md` | 删除无作用的自我降格，保留真实贡献边界 |
| 2 不反复自证数据来源 | `references/artifact-boundary.md` | 合并已有规则；区分改稿操作与真实回顾性研究设计 |
| 3 领域通行术语 | `references/terminology-and-register.md` | 通用形式、首次解释、全文一致；按领域和期刊选取 |
| 4 文件与存档信息 | `references/artifact-boundary.md` | 沿用材料分层，正式标识和科学研究对象除外 |
| 5 写作与投稿元信息 | `references/artifact-boundary.md` | 待办留在作者侧；草稿占位不进入最终成稿 |
| 6 附录与核心表格 | `references/argument-and-voice.md` | 核心证据可在正文评估，完整补充材料另附 |
| 7 口语、借喻与行话 | `references/terminology-and-register.md` | 提供语境化替换示例，保护真实专业含义与已定义名称 |
| 8 集中讨论局限 | `references/limitations.md` | 已覆盖；不将“写一次”变成机械次数限制 |
| 9 期刊格式 | `references/venue-adaptation.md` | 保留全部具体条目，明确历史笔记状态，使用前核对官方要求 |
| 自查清单与全文排查 | `SKILL.md`、`references/document-review.md` | 全文任务检查同类问题；局部任务保持授权范围 |

原文中的绝对表达按适用范围整合，例如“代码开源一句话”不取代关键方法，“我们认为”的改法不套用到所有英文论文，“探针”不替换真实 CFD 测点。原始清单中的论文题名仅记录规则来源，不推断该论文已发表或其结果已经验证。

## 2026-10 增量与通用化处理

[增量来源原文](sources/personal-revision-checklist-2026-10.md) 为创建者指定的 2026-10-13 更新文件，来源是作者后续反馈，不属于四个上游。按用户进一步要求，执行规则学习判断逻辑，不维护固定的保留、删除或替换词表。来源原文保留具体案例；它不是另一套执行指令。

原清单第 7 条的“闸 → 检查关卡”及“已定义的契约可保留”建议已被作者后续反馈更新，不能继续当作当前推荐；原始来源文件不改写。现行规则也不反向建立这些词的禁用清单，而是按概念、同领域用法、作者命名意图及歧义判断。

| 增量 | 执行落点 | 整合判断 |
|---|---|---|
| 术语及直译 | `references/terminology-and-register.md` | 用决策依据取代原替换词表；同词可因语境得到不同处理 |
| 摘要 | `references/abstract.md`、入口 | 优先形成问题到贡献的完整论证；字数、数字数量和顺序受科学含义及期刊要求约束 |
| 引言收尾 | `references/argument-and-voice.md` | 补齐触发条件、机制、检查盲区与切入点；不把模型日期或假说泛化为事实 |
| 讨论与结论 | 同上 | 解释与总结分工，按信息作用去重；结论形式由期刊和作者决定 |
| 直接结果图 | 同上 | 证据形式匹配复现主张；交代设置和参考解性质，区分耗散解释与因果证明 |
| 期刊笔记 | `references/venue-adaptation.md` | 保存《计算物理》记录，明确未官方核验；提示作者评估和披露 GenAI 使用 |
| 措辞审计 | `references/document-review.md`、入口 | 按授权追加记录，撤销留痕；检索词用于定位，不用于机械替换 |
| 附录 A、B | `references/examples.md` | 授权历史片段，与人工示例区分；不声称核验论文数据 |

已有正文边界、必要限定、核心证据位置和全文授权范围规则继续适用。新增行为案例用于后续试用，不代表本次进行了模型效果验证。
