# 教材发现与定稿方法论 (Textbook Discovery & Decision Method)

> **定位**：记录《三维数字材质制作》在 Stage 1 (Issue #2) 中经过实战检验、可复现的教材与教学资源发现、核实、清洗与决议工程方法。

---

## 核心流水线流程 (Pipeline)

```
[1. Discovery] 
       │
       ▼
[2. Independent Multi-model Lanes] 
       │
       ▼
[3. Owning-source Verification] 
       │
       ▼
[4. Accessibility & Acquisition] 
       │
       ▼
[5. Notebook Corpus Build] 
       │
       ▼
[6. Corpus Hygiene] 
       │
       ▼
[7. Available-corpus Gap Analysis] 
       │
       ▼
[8. Conditional Acquisition] 
       │
       ▼
[9. Role-based Textbook Decision]
```

---

## 关键阶段规范与工程纪律

### 1. Discovery（多源发现）
- 依据预先设立的严密边界（聚焦 Material/Texture Authoring，建模拓扑仅作支撑），在国际与国内专业出版物、高校培养方案及行业课程中广泛初筛候选教材与教学规范。

### 2. Independent Multi-model Lanes（独立多模型车道）
- 引入异构大模型独立运行搜索与筛选（如 Claude Code / Gemini / NotebookLM / Perplexity），互不干扰、独立产出候选名单；
- 避免单模型产生的幻觉与信息茧房，通过交叉比对发现重合的高置信度候选文献。

### 3. Owning-source Verification（第一方元数据核实）
- **绝不凭引用文本或第三方二手博客作结论**；
- 必须通过出版社官网、公开版权页（CIP/ISBN）、亚马逊/Google Books 官方 TOC（目录）或作者主页，核实出版年份、实际章节目录与具体作者身份，剔除出版年造假与拼凑教材。

### 4. Accessibility & Acquisition（可获得性分级）
- 贯彻 **“Ideal ≠ Accessible”** 原则：
  - *Acquired / Verified*: 用户已实际拥有物理/数字原版；
  - *Purchasable*: 国内外电商平台可买到现货/电子书；
  - *Desired but Unavailable*: 理想教材因绝版、无跨国版权或电子化渠道受阻当前拿不到，保留为待解参考，不硬编造为实际依赖。

### 5. Notebook Corpus Build（知识库语料构建）
- 将已获合法专著（PDF/ePub）与活体官方源（Living Official Sources，如 GitHub Raw Markdown、官方技术规范）统一录入 NotebookLM 等 AI 知识引擎；
- 确保涵盖旧教材版本老化点的最新官方事实基准。

### 6. Corpus Hygiene（语料清洗与去重）
- 严格定期审计知识库中的 Source：
  - 清理抓取失败的 ERROR 空源；
  - 完整版教材 PDF 入库后，彻底删除此前录入的重复碎片章节或镜像网页；
  - 清理纯营销页与已被官方替代的个人博客；
  - 维护高纯度、低噪声的知识库上下文，防止长文本检索溢出。

### 7. Available-corpus Gap Analysis（基于实际可用语料的缺口分析）
- 依托已就绪的真实语料，围绕大纲骨架、版本老化、分层思考模型、程序化深度及本土学生实操等核心维度进行交叉问答；
- 严格区分 **事实证据 (Source-supported Facts)** 与 **项目推论 (Project Inferences)**，形成可审计的 Gap Register。

### 8. Conditional Acquisition（按需条件采购决策）
- 绝不凭“书很有名”随意采购；
- 只有 Gap Analysis 证明现有免费/已获语料存在学生端无法逾越的实质性断层时，才触发采购评估；
- 采购动作实施 **“Buy-one-first”** 策略：先买最有针对性的一本样书做验证，费用由用户决策。

### 9. Role-based Textbook Decision（角色化教材体系定稿）
- 摒弃“单一主教材涵盖一切”的幻想，形成多层互补的现代化资源架构：
  - **Primary Textbook Skeleton**：提供主干实操案例与工作流骨架；
  - **PBR Theory Foundation**：提供物理光学与安全色阶基准；
  - **Observation & LookDev Reference**：提供质感观察、相机缺陷与审美拔高；
  - **Procedural Foundation**：提供有限边界的程序化思维训练；
  - **Living Technical Authority**：以官方实时文档修正软件版本老化；
  - **Chinese Student Companion**：按需提供学生本土化界面与实训支持；
  - **Teacher Graphics Reference**：提供教师底层渲染技术底座。
