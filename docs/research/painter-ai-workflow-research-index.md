# Substance 3D Painter + AI 工作流研究总览与案例索引 (Painter AI Workflow Index)

> **治理与门禁定位 (Governance & Status)**：  
> - **承载工单**：[Issue #42](https://github.com/carllx/corso-pbr-materials/issues/42)（关联主线工单 [Issue #40](https://github.com/carllx/corso-pbr-materials/issues/40)、Roadmap [Issue #1](https://github.com/carllx/corso-pbr-materials/issues/1)）  
> - **依据属性**：`RESEARCH CANDIDATE / RUNTIME REQUIRED / NOT TEACHER-APPROVED`  
> - **课程定位**：本系列为针对 Adobe Substance 3D Painter 内部两项 AI 辅助扩展（Python Plugin 自动化导出与 GLSL Custom Shader 视口着色规则修改）的独立可行性研究候选成果。  
> - **核心纪律**：
>   1. **非必修、非冻结**：严禁作为全员必修内容，严禁改变既有九讲顺序，严禁挤占 W7–W9 综合期末制作；
>   2. **运行未经验证**：当前官方文档证据已核验，机房真实环境与权限未实测（`RUNTIME REQUIRED`），严禁谎称脚本已在机房运行通过；
>   3. **术语规范**：严格执行 **English-first**（`Python Plugin`、`GLSL Shader`、`Shader Settings`、`Texture Set`、`Export Textures`、`Output Template`、`Base Color`、`Roughness`、`Metallic` 等），中文仅作辅助解释。

---

## 1. 案例导航与核心定位

| 案例编号与名称 | 核心教学问题 | 建议周次与形式 | 详细规范文档 |
|---|---|---|---|
| **Case A：Python Plugin**<br>规范化导出自动化工具 | 艺术专业学生能否借助 AI 编写 Painter 内部脚本，规范化重复导出流程并降低命名/通道配置错误？ | **W6 `Export Textures` 之后**<br>（5–8 分钟教师演示候选，学生选做） | [`painter-ai-python-export-best-practice.md`](painter-ai-python-export-best-practice.md) |
| **Case B：GLSL Shader**<br>实时 Toon 光影规则修改 | 学生能否理解视觉风格不仅取决于绘制贴图，还取决于实时着色计算规则，并借助 AI 自行定制光影明暗分级？ | **W8 自发光与视口呈现附近**<br>（6–10 分钟教师演示候选，学生选做） | [`painter-ai-glsl-toon-best-practice.md`](painter-ai-glsl-toon-best-practice.md) |

---

## 2. 教学问题与安全边界

这不是“向艺术专业学生教授两门编程语言”的课程计划，而是探索学生在具备 AI 辅助能力时，如何拓展材质工具链与理解底层渲染逻辑：

1. **规避纯素材生成误区**：
   - 使用通用多模态 AI 生成木纹/石纹位图导入 Painter，属于常规素材生成，无法体现 Painter 原生 API 的扩展价值；
   - 本研究聚焦 **Painter 内部环境的原生机制扩展**（Python 插件管线与 GLSL 视口着色规则）。
2. **轻量化宿主原则**：
   - 仅利用 Substance 3D Painter 内部自带的 Python 解释器与 Shader 编译接口；
   - **严禁要求学生额外安装系统 Python、Node.js、外部 SDK 或配置复杂 IDE**；外部远程控制或自动化 Agent 架构不作为本课程课堂方案。
3. **关键科学与流程边界**：
   - **视口效果 $\neq$ 导出贴图**：GLSL Shader 改变的是 Painter 视口实时光栅化着色规则，其 Toon 效果不会自动烘焙进 `Export Textures` 输出的标准 PBR 贴图；
   - **原生功能为先**：必须先掌握 Painter 原生 GUI（如 Native Export 对话框与预设 Shader），再对比脚本与自定义着色器，不能谎称“必须用脚本才能实现”。
4. **低配机房保护与教学预算**：
   - 不增加第一讲（W1 MeetMat）的认知与时间负担（160 分钟 Plan Budget 不变）；
   - 演示全部采用教师预备的低负荷轻量化独立测试资产，与学生正式平时/期末作业完全物理隔离。

---

## 3. Adobe 官方外部一手来源核验矩阵

所有案例必须严格建立在 Adobe 官方已公布的技术文档与接口规范之上：

| 来源与规范入口 | 实际可借鉴内容与技术事实 | 判定属性 | 关键技术提示 |
|---|---|---|---|
| Adobe [Create a Python plugin](https://experienceleague.adobe.com/en/docs/substance-3d-dev/painter-python/tutorials/create-a-python-plugin) | 从 `.py` 文件、菜单注册到导出当前 Texture Set 的官方原型代码与步骤 | **Primary reproduction basis** | 官方文档仍含 `PySide2` 与 `QtWidgets.QAction` 旧写法，现代版本不可盲目照抄。 |
| Adobe [Python API / export module](https://experienceleague.adobe.com/en/docs/substance-3d-dev/painter-python/api/substancepainter-package/export) | `export_project_textures()`、导出参数结构体、错误与结果回调接口 | **Primary technical authority** | 必须按目标版本 Painter 严格核验预设 ID 与数据格式。 |
| Adobe [Qt6 Migration](https://experienceleague.adobe.com/en/docs/substance-3d-dev/painter-python/tutorials/qt6-migration) | Painter 10.1+ 全面升级至 Qt6/PySide6，`QAction` 归属移至 `QtGui` | **Mandatory compatibility note** | 脚本生成时必须提示目标版本适配，避免导入失败。 |
| Adobe [Versioning Plugin Example](https://experienceleague.adobe.com/en/docs/substance-3d-dev/painter-python/examples/versioning-plugin) | 现代 PySide6 代码骨架、多 Texture Set 遍历、错误日志捕获模式 | **Teacher implementation reference** | 属于教学扩展参考骨架，非开箱即用的商用版本控制系统。 |
| Adobe [Native Export Textures](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/export/export) | 原生 `Export Textures`、`Output Templates` 预设配置与文件打包规范 | **Control group authority** | 作为基准对照组，用于验证 Python 自动化相比手动点击的真实教学增益。 |
| Adobe [Shader API Reference](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/scripting-and-development/shader-api-reference/shader-api) | `shade(V2F inputs)` 最小接口规范、内置 Uniform 与采样辅助函数 | **Primary reproduction basis** | Painter 仅开放特定表面着色接口，非通用全功能 GLSL 管线。 |
| Adobe [Toon Shader API](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/scripting-and-development/shader-api-reference/shaders-shader-api/toon-shader-api) | 官方 Toon 着色器源码：`Base Color` 采样、固定光源、四档明暗量化、轮廓线厚度 | **Primary Toon code basis** | 官方自带 Toon 效果；AI 案例必须聚焦于“如何按需修改量化规则”。 |
| Adobe [Shader Settings](https://experienceleague.adobe.com/en/docs/substance-3d-painter/using/interface/shader-settings/shader-settings) | 视口 Shader 切换、实例创建、Uniform 参数实时调节面板 | **Runtime workflow authority** | 验证自定义参数是否能在 UI 实例面板中正确暴露。 |
| [Pablo Muñoz Gómez (2025 视频)](https://www.youtube.com/watch?v=Vxk_ftSpKsA) | Toon 风格参数调整与视口 LookDev 的视觉流程参考 | **Secondary video precedent** | 仅作为视觉形态对照参考，第三方工程资产未授权再分发，不引入任何第三方代码。 |

---

## 4. 建议周次落位与教学容量矩阵

以下周次落位建议属于项目教学推论（`PROJECT INFERENCE / CANDIDATE PROPOSAL`），非冻结课表，须待机房实测与主讲教师最终裁定：

| 实施周次 | 课程主线已有知识点 | 建议插入的 AI 辅助案例 | 时长与组织形式 | 准入门禁条件 |
|---|---|---|---|---|
| **W6**<br>布料材质制作与跨软件连接 | `Export Textures`、`Output Templates`、Blender 原理化材质对接、颜色空间 | **Case A：Python 规范化导出工具**<br>先让学生熟练掌握 Native Export 对话框，再以教师演示对比脚本一键规范导出的效率与一致性 | **教师演示 5–8 分钟**<br>（替换原有同质演示时间，学生自由选做，绝非必修） | 1. 原生导出学生已熟练掌握；<br>2. 脚本在目标机房版本无报错运行；<br>3. 具备清晰的可量化错误预防增益。 |
| **W8**<br>自发光材质与综合视口呈现 | `Emissive` 通道、辉光 Bloom、曝光平衡、视口渲染 LookDev；期末资产准备 | **Case B：GLSL Toon 着色规则修改**<br>建立三段对照（默认 PBR $\to$ 官方 Toon $\to$ AI 定制三档 Toon），展示在贴图不变的前提下如何定制实时光影 | **教师演示 6–10 分钟**<br>（若与期末冲刺冲突，立即降级为课后选看） | 1. 官方案例与 AI 修订版在机房 GPU 编译通过；<br>2. 提供同机位同资产三帧严谨对照；<br>3. 无额外 GPU 编译崩溃风险。 |

---

## 5. 共同验收门禁标准 (Acceptance Gates)

两项案例在进入正式课堂教学前，必须通过以下四维门禁：

1. **技术维度 (Technical)**：
   - 锁定机房目标 Painter 确切版本号（如 9.x、10.x）；
   - 脚本/Shader 在受限学生操作系统账户下能够正常放置、加载与编译，无崩溃或静默失效；
   - 验证工程保存重开后的资源完整性，以及无损恢复默认 Shader / 卸载插件的安全性。
2. **教学维度 (Pedagogical)**：
   - 必须设置严格的原生 GUI 对照组；
   - 学生在演示结束后，能用一句话准确解释“自动化解决了什么操作痛点”或“Shader 改变了什么渲染规律”；
   - 操作耗时严格受控于 5–10 分钟预算之内，不得挤占学生实操与期末制作时间。
3. **资产与隔离维度 (Asset Isolation)**：
   - 必须使用教师准备的轻量化独立测试模型（如素模或独立测试头像）；
   - Python 导出文件严格限定写入独立的测试目录（如 `exports_demo/`），严禁覆盖学生正式工程；
   - 自定义 Shader 独立命名，不篡改软件安装目录自带的核心着色器文件。
4. **当前门禁状态**：
   - 外部官方文档证据：`PASS`
   - 真实机房 Runtime 验证：`NOT TESTED / RUNTIME REQUIRED`
   - 正式课堂教学采纳：`NOT TEACHER-APPROVED`

---

## 6. 后续受控验证任务指引 (IDE Work Unit Contract)

未来执行本地验证的智能体或教师在推进实测时，必须遵守以下契约：
- **必做**：查验真实安装的 Painter 版本；先跑通 Adobe 官方未修改的示例源码；对 PySide6 / Shader 语法做最小必要适配；在真实或受控机房环境下记录执行耗时与日志；保留同相机视口对比截图；
- **禁做**：严禁在未接入运行环境前声称通过；严禁修改既有 W1 教学材料；严禁将演示扩增为全员必修或计分作业；严禁引入外部重型运行环境；严禁直接覆盖学生工程文件。
