# Research — Realtime / Web Material Learning Path for Weeks 7–9

> **文档定位**：本研究报告响应 GitHub Issue #21 契约及最新 Browser Review（技术 locator 规范化与运行时证据门禁）要求。报告回答本科材质课中引入 Realtime / Web 交付验证的教学价值、核心材质能力边界、技术格式与受控运行时选型、课时规划估算，以及对 Stage 4 全新期末项目（#22）的有条件接口建议。  
> **并行协作关系**：与 Issue #19（案例审计）及 Issue #20（材质行为图谱）互为并行汇合输入（Sibling Join Inputs），共同支撑后续整体课表与期末项目的决策。  
> **门禁状态**：`RESEARCH COMPLETE / RUNTIME GATE OPEN — CONDITIONAL RECOMMENDATION`（不开发 Web App，不单方面冻结期末项目，外部独立查看器未获机房实测前不向 #22 移交为已验收交付物）。

---

## 1. 核心问题与独立学习价值 (Core Questions & Pedagogical Value)

### 1.1 独立教学价值：跨运行时表征能力（Cross-Runtime Interoperability）
在本科材质教学中，引入 Realtime / Web 交付验证的独立教学价值在于建立学生的**工业资产交换认知（Interchange Standards）**，而非培养 Web 前端开发或游戏引擎关卡设计：
- **宿主节点逻辑 $\neq$ 物理资产交换格式**：Blender 内部着色器编辑器中的节点网络（如分形噪波、色阶计算）属于 DCC 专有过程逻辑；导出至外部实时环境时，必须被烘焙转译为遵循工业规范的物理贴图与参数。
- **通道语义显性化**：离线渲染器能自动解析灵活的单通道输入，而实时管线通常采用贴图通道打包以提升渲染效率。学生亲手核验通道映射，能真正理解底层数据存储格式与色彩空间规则。
- **渲染近似差异客观归因**：理解离线路径追踪（Cycles：多重光线反弹、精确微表面积分）与实时栅格化/环境贴图着色（WebGL / EEVEE：Split-Sum 预过滤近似、屏幕空间近似）之间的物理权衡，树立客观的跨平台 LookDev 评估意识，而非盲目归咎于“导出模型损坏”。

### 1.2 材质专业能力 vs 游戏/Web 编程的防御边界
为防止课程重心异化，本路径划定严格的认知与操作防火墙：

| 教学维度 | 必须守护的材质核心能力（IN-SCOPE） | 严禁引入的无关工程负担（OUT-OF-SCOPE） |
| :--- | :--- | :--- |
| **通道与数据** | 通道打包约定（ORM: AO, Roughness, Metallic）、色彩空间定义（sRGB vs Non-Color） | 游戏引擎蓝图编写、C# 脚本、GLSL/HLSL Shader 代码编程 |
| **几何与法线** | 切线空间法线（Tangent Space Normal）、OpenGL (+Y) 朝向规范与翻转排错 | 复杂多级 LOD 生成、物理碰撞体（Collider）设置、光照贴图 UV2 展开 |
| **性能与尺寸** | 纹理贴图 2 的幂次方（POT）兼容性惯例、分辨率对显存与传输的直观影响 | 网页 DOM 布局、CSS/JavaScript 前端工程、Web 框架开发 |
| **光照与观察** | 受控 HDR 环境旋转核验、色调映射（Tone Mapping）对材质对比度的影响 | 引擎关卡灯光烘焙、复杂后处理体积（Post-Process Volume）配置 |

---

## 2. 初学者最低达标要求（Minimal Learning Outcomes）

在 W7–W9 涉及实时交付时，初学者仅需在材质维度达成以下 5 项最低核心能力：

1. **通道打包惯例理解 (Packing Conventions)**：
   - 掌握常见的 ORM 通道打包约定（R=AO, G=Roughness, B=Metallic 作为广泛采用的工业交付惯例），理解贴图通道复用对纹理采样与资源管理的设计意图（具体采样器节省效果视硬件与引擎实现而定）。
2. **色彩空间防御 (Color Space Rigor)**：
   - 掌握“颜色贴图使用 sRGB，物理数据贴图（粗糙度、金属度、法线）必须标定为 Non-Color / Linear”的规则，能识别因色彩空间错误引起的高光发灰或法线黑斑。
3. **切线法线坐标系校验 (Tangent Normal Orientation)**：
   - 掌握切线空间法线坐标规范（glTF 2.0 规范明确为 +X 向右，+Y 向上，+Z 朝向观察者），能在实时视口中通过旋转受控光源识别凹凸朝向颠倒并执行翻转排错。
4. **跨运行时外观差异归因 (Cross-Runtime Attribution)**：
   - 能对照 Cycles 离线渲染图与实时视口效果，客观陈述由算法近似引起的合理视觉差异（如接触阴影柔化、环境反射遮蔽、间接光漫反射反弹）。
5. **五项闭环自检 (Five-Point Delivery Checklist)**：
   - 在受控环境中完成交付合规自查：① 材质槽赋予完好；② 金属/非金属高光特征分明；③ 粗糙度渐变合理；④ 法线凹凸方向正确；⑤ 旋转光照无异常破损暗斑。

---

## 3. 规范支撑与候选交付载体选型

### 3.1 权威规范支持与精确章节索引
本方案直接基于 Khronos 官方标准与 Blender 官方手册，其精确章节点索引如下：

- **Khronos Group, *glTF 2.0 Specification***：
  - §3.9.2 `Metallic-Roughness Material`：定义 `metallicRoughnessTexture` 的 B 通道采样金属度、G 通道采样粗糙度，以及因子乘法规则；
  - §3.9.3 `Additional Textures`：定义法线贴图（normalTexture）、环境光遮蔽（occlusionTexture）与自发光（emissiveTexture）；
  - §3.8.4 & §3.8.4.5 `sampler` 与 `Non-Power-Of-Two Textures`：明确贴图采样器规范与 NPOT 贴图兼容性；
  - 模式细节：§5.19.5 (`normalTexture`), §5.21 (`occlusionTexture`), §5.22.5 (`metallicRoughnessTexture`)。
- **Blender 5.2 Manual (*glTF 2.0 Export*)**：
  - 章节条目：`Material Support` $\to$ `Principled BSDF`；
  - 规范规则：`G = roughness / B = metallic in the shared metallic-roughness image`；
  - 色彩空间：`Color Space = Non-Color for that image`；
  - 遮蔽通道：`AO in R may optionally share the same image`；
  - 法线格式：`Tangent-space normal export with +Y`（OpenGL 格式输出）。

### 3.2 交付格式推荐：glTF 2.0 (`.glb`) 作为有界载体
- **推荐结论**：选用 glTF 2.0 单文件二进制格式 (`.glb`) 作为受控交付载体。
- **对比考量**：
  - 相比 OBJ/FBX，glTF 原生直接映射 Principled BSDF PBR 属性；`.glb` 将网格、材质描述与纹理流自包含封装，彻底杜绝相对路径丢失引起的贴图丢失故障；
  - 相比 USD 庞大工具链，glTF 在教学单资产交付与轻量查看上认知与环境负荷最低。
  - **贴图尺寸惯例**：glTF 规范虽允许 NPOT，但建议遵循 2 的幂次方（POT，如 1024 / 2048）作为硬件兼容性惯例。

---

## 4. 运行时验证探针现状与门禁状态 (Runtime Feasibility & Probe Status)

### 4.1 已知良好模型实证基准 (Known-Good Asset Baseline)
- 本地已知良好模型：`./.scratch/prototype/vintage_flashlight_1k/vintage_flashlight_step2_export.glb`；
- 二进制验证事实：文件大小 4,358,240 字节（4.16 MB），容器 Magic 为 `glTF`，版本为 2.0，属于自包含单文件二进制结构。

### 4.2 独立外部 Web 查看器技术路径与未决事实 (Open Runtime Gate)
- **技术可行性路径（理论推演）**：采用 HTML5 File API 监听本地文件拖拽（Drag-and-Drop），通过 `URL.createObjectURL(file)` 生成本地 Blob URL 交付 WebGL 渲染器加载。理论上，纯客户端 Blob 流不发起 HTTP 网络请求，可规避浏览器对 `file:///` 协议下 `fetch()` 调用的 CORS 同源拦截。
- **机房现场未决风险（Unresolved Classroom Risks）**：
  1. *无外网离线依赖*：若机房处于断网环境，单文件 HTML 必须离线内嵌完整的 WebGL 渲染引擎（如 Three.js / model-viewer 核心代码约 600KB–1MB）。若分发缺失或被机房还原卡拦截，学生无法打开；
  2. *硬件与浏览器权限未知*：当前高校公用机房的 GPU 驱动版本与浏览器 WebGL 硬件加速权限处于 `HARDWARE/SOFTWARE UNKNOWN` 状态。
- **门禁裁定**：
  - **`RUNTIME GATE OPEN (EXTERNAL WEB VIEWER UNPROVEN IN TARGET LAB)`**；
  - **在机房真实环境下完成端到端离线拖拽实测之前，外部独立 Web 查看器严禁作为已验收交付物移交给 Issue #22**；
  - **保底运行基准（Fallback Baseline）**：在外部查看器通过实测前，以 **Blender 内置 EEVEE Next 实时视口**（开启 Viewport Shading -> Rendered 并载入标准测试 HDRI）作为 100% 零外部依赖、免配置的实时对照基准。

---

## 5. W7–W9 课时容量规划估算 (Provisional Capacity Planning Estimate)

后三周（W7–W9）总教学容量为 480 分钟（3 × 160m）。为防止实时技术排错挤占材质本体，本估算将 Realtime 轴限定为辅助性验证出口。**所有课时数值均为临时性规划估算（Provisional Planning Estimate），受制于机房后续干跑与实测门禁**：

| 周次阶段 | 实时轴规划动作 (Realtime Bounded Action) | 课时规划估算 (Provisional Estimate) | 剩余主线课时与投向 (Remaining Capacity & Target) |
| :---: | :--- | :---: | :--- |
| **Week 7** | 教师示范通道导出约定与排错预设；学生完成独立导出并在受控环境中打开自检。 | **约 50m**<br>*(待实测)* | **约 110m**：完全交付给 Stage 4 全新综合期末项目（由 Issue #22 独立设计），不写回旧手电筒。 |
| **Week 8** | 解析 Cycles 离线光追与实时着色差异；学生双视口比对并记录可解释差异。 | **约 30m**<br>*(待实测)* | **约 130m**：期末大作业方案深化与教师巡回技术指导。 |
| **Week 9** | 学生将合规的 `.glb` 交付件随期末 LookDev 套件一并打包归档。 | **约 15m**<br>*(待实测)* | **约 145m**：作品展示互评、大作业讲评与全班复盘。 |
| **合计** | 三周内 Realtime 纯技术操作累计估算占用 | **约 95m** (19.8%) | **385m** (80.2%)：全盘聚焦于综合期末项目质感表现。 |

---

## 6. 与综合期末项目（#22）的接口建议与定位裁决 (Interfaces to #22)

### 6.1 处置状态裁决：`BOUNDED SUPPORT (CONDITIONAL)`
在 `CORE CANDIDATE`、`BOUNDED SUPPORT`、`DEMO ONLY` 与 `DEFER` 四种候选状态中，**推荐裁决为 `BOUNDED SUPPORT`（有界辅助验证出口），但保持为有条件状态（Conditional Recommendation）**：
- 角色假说（离线 LookDev 为主，实时为次要互操作合规交付）具备充分的工业标准与教学价值支撑；
- 但外部独立 Web 查看器载体因尚未经过机房实机验证，其最终采用状态取决于运行时门禁。

### 6.2 对 Issue #22（期末大作业）的定性接口规范
1. **成果物主次关系**：
   - **离线 LookDev 渲染成果包作为核心主交付载体**（多角度高质量渲染图、微表面细节特写、材质因果逻辑拆解）；
   - **实时模型作为次要辅助交付物**。
2. **考核边界约定**：
   - 实时交付物仅作为**合规性核验项（Compliance Deliverable）**，核查通道打包规范性与贴图完整性；
   - 严禁对网页交互复杂度或引擎优化实时帧率设定硬性评分权重；若外部 Web 查看器未能在机房通过实测，期末实时核验回退至 Blender EEVEE Next 视口内完成。

---

## 7. 结论与执行门禁记录 (Conclusion & Gate Standing)

- **最终处置建议**：`BOUNDED SUPPORT (CONDITIONAL / RUNTIME GATE OPEN)`
- **执行边界约束**：
  - 严禁开发任何 Web 前端应用或引入大型游戏引擎全流程；
  - 外部独立查看器暂不作为确定性交付成果向 #22 移交；
  - 严禁单方面预设或冻结 Issue #22 期末大作业的具体分值与要求；
  - 严禁修改 PR #18 现有分支；
  - 严禁启动 Week 2 可执行教案开发。
