# 《三维数字材质制作》课程知识与技能覆盖矩阵 (Curriculum Coverage Matrix)

> **研究阶段**：Phase 1 综合收敛基线（Curriculum Coverage Matrix）  
> **审阅锚点**：基于 `419947a727179d4f9c063a331deeb31080a686ec`，综合 `CONTEXT.md`、`pbr-course-foundations.md`、`textbook-source-map.md` 与 `course-design-ledger.md` 构建  
> **文档定位**：将 Phase 1 / 1B 的研究结论形式化为标准化的**知识与技能覆盖矩阵**，确立传统与当前工业界 PBR 材质教学的完整能力对照基线，作为进入 Phase 2（AI 影响与重构研究）前的对照标准。

---

## 目录
1. [课程边界与矩阵维护原则](#1-课程边界与矩阵维护原则)
2. [知识与技能覆盖总矩阵 (Master Coverage Matrix)](#2-知识与技能覆盖总矩阵-master-coverage-matrix)
3. [六大能力模块覆盖深度解析](#3-六大能力模块覆盖深度解析)
4. [前置与支撑知识边界控制](#4-前置与支撑知识边界控制)
5. [未决问题与证据缺口登记表 (Gap Register Before AI Phase 2)](#5-未决问题与证据缺口登记表-gap-register-before-ai-phase-2)

---

## 1. 课程边界与矩阵维护原则

本矩阵严格遵循已确立的课程定位与边界规范：

1. **核心对象聚焦**：严格限定为 **Material / Texture Authoring（材质与纹理创作）**，建模、重拓扑与完整次世代资产资产制作严禁反客为主。
2. **支撑知识定位**：UV 展开、高低模映射与贴图烘焙（Baking）属于材质前置支撑知识，教学深度以“满足材质制作与贴图映射需求”为边界。
3. **创作范式完整性**：涵盖“基于贴图的 PBR（Texture-based）”、“程序化/参数化（Procedural/Parametric）”与“图像转材质/采集（Material Acquisition）”三大范式。Procedural 范式保留为核心能力思维，不因 Designer 软件的选修性而被剔除。
4. **双出口应用导向**：实时游戏（Game Realtime）与影视动画（Animation / LookDev）作为材质成果的两个下游验证出口。
5. **标记客观性**：标记仅反映现有研究与教材事实，不作未经证实的精确百分比假设。

---

## 2. 知识与技能覆盖总矩阵 (Master Coverage Matrix)

### 图例说明
- **初步教学必要性 (Teaching Necessity)**：
  - `Likely Core`：高可信核心必修技能
  - `Likely Important`：高可信重要理解/排错能力
  - `Likely Optional`：进阶/选修扩展能力
  - `Supporting prerequisite`：材质前置支撑知识
  - `Unresolved`：教学深度待定
- **来源覆盖标记 (Source Coverage)**：
  - `Core coverage`：作为核心主线深入讲解
  - `Partial`：涉及部分概念或案例
  - `Supporting`：作为前置或支撑工具提及
  - `Advanced`：高阶深入专题
  - `Absent`：未覆盖该项内容
  - `Gap / Needs Research`：证据不足，待后续研究

---

### 2.1 模块一：Material Literacy (材质素养与物理光学基础)

| 知识 / 技能单元 (Unit) | 初步教学必要性 | Born Digital Painter 2025 | Adobe PBR Guide | Adobe 官方当前文档 | Born Digital 1日完成 2025 | Blender 程序化资源 | Born Digital Designer 2022 | 来阳 2026 | CGMA / Gnomon 课程先例 | Phase 1 基础报告结论 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **现实材质观察与参考分析** | `Likely Core` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Partial` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` |
| **PBR 物理可信性与能量守恒** | `Likely Core` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` |
| **Base Color 反射率与安全色阶** | `Likely Core` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` |
| **Roughness 微表面粗糙度模型** | `Likely Core` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` |
| **Metallic 金属度二值准则** | `Likely Core` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` |
| **Normal 切线空间法线原理** | `Likely Core` | `Core coverage` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` |
| **Height / Displacement 几何置换** | `Likely Important` | `Partial` | `Core coverage` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` |
| **Ambient Occlusion 环境遮挡作用** | `Likely Core` | `Core coverage` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` |
| **表面细节尺度与频率认知** | `Likely Important` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` |
| **sRGB 与 Linear 色彩空间规范** | `Likely Important` | `Core coverage` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` |

---

### 2.2 模块二：Texture-based Authoring (基于贴图的资产级材质创作)

| 知识 / 技能单元 (Unit) | 初步教学必要性 | Born Digital Painter 2025 | Adobe PBR Guide | Adobe 官方当前文档 | Born Digital 1日完成 2025 | Blender 程序化资源 | Born Digital Designer 2022 | 来阳 2026 | CGMA / Gnomon 课程先例 | Phase 1 基础报告结论 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Painter 工程设置与色彩管理** | `Likely Core` | `Core coverage` | `Supporting` | `Core coverage` | `Core coverage` | `Absent` | `Absent` | `Core coverage` | `Core coverage` | `Core coverage` |
| **图层结构与多通道同步管理** | `Likely Core` | `Core coverage` | `Supporting` | `Core coverage` | `Core coverage` | `Absent` | `Absent` | `Core coverage` | `Core coverage` | `Core coverage` |
| **遮罩体系与手绘特征细节** | `Likely Core` | `Core coverage` | `Supporting` | `Core coverage` | `Partial` | `Absent` | `Absent` | `Core coverage` | `Core coverage` | `Core coverage` |
| **智能材质 (Smart Materials) 组织** | `Likely Core` | `Core coverage` | `Supporting` | `Core coverage` | `Partial` | `Absent` | `Absent` | `Core coverage` | `Core coverage` | `Core coverage` |
| **智能生成器 (Generators) 驱动逻辑** | `Likely Core` | `Core coverage` | `Supporting` | `Core coverage` | `Partial` | `Absent` | `Absent` | `Core coverage` | `Core coverage` | `Core coverage` |
| **材质分层逻辑 (Base $\rightarrow$ Detail)** | `Likely Core` | `Core coverage` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` |
| **风化与磨损物理逻辑 (Weathering)** | `Likely Core` | `Core coverage` | `Partial` | `Core coverage` | `Partial` | `Partial` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` |
| **贴图导出模板与通道配置** | `Likely Core` | `Core coverage` | `Supporting` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` |

---

### 2.3 模块三：Supporting Pipeline Knowledge (材质支撑管线前置知识)

| 知识 / 技能单元 (Unit) | 初步教学必要性 | Born Digital Painter 2025 | Adobe PBR Guide | Adobe 官方当前文档 | Born Digital 1日完成 2025 | Blender 程序化资源 | Born Digital Designer 2022 | 来阳 2026 | CGMA / Gnomon 课程先例 | Phase 1 基础报告结论 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **UV 参数化展开与接缝 (Seams) 切分** | `Supporting prerequisite` | `Supporting` | `Supporting` | `Supporting` | `Absent` | `Supporting` | `Supporting` | `Core coverage` | `Supporting` | `Supporting` |
| **接缝与硬边对应原则 (Hard Edges)** | `Supporting prerequisite` | `Supporting` | `Supporting` | `Supporting` | `Absent` | `Supporting` | `Supporting` | `Partial` | `Supporting` | `Supporting` |
| **像素密度规划 (Texel Density)** | `Supporting prerequisite` | `Supporting` | `Core coverage` | `Supporting` | `Absent` | `Supporting` | `Supporting` | `Absent` | `Supporting` | `Supporting` |
| **高低模映射关系与拓扑准备** | `Supporting prerequisite` | `Supporting` | `Supporting` | `Supporting` | `Absent` | `Supporting` | `Supporting` | `Core coverage` | `Supporting` | `Supporting` |
| **关键贴图烘焙 (Baking: Normal/AO/Curv)** | `Supporting prerequisite` | `Core coverage` | `Supporting` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` | `Core coverage` | `Core coverage` | `Supporting` |

---

### 2.4 模块四：Procedural / Parametric Materials (程序化与参数化材质创作)

| 知识 / 技能单元 (Unit) | 初步教学必要性 | Born Digital Painter 2025 | Adobe PBR Guide | Adobe 官方当前文档 | Born Digital 1日完成 2025 | Blender 程序化资源 | Born Digital Designer 2022 | 来阳 2026 | CGMA / Gnomon 课程先例 | Phase 1 基础报告结论 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **节点着色器架构 (Shader Nodes)** | `Likely Important` | `Absent` | `Supporting` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` |
| **纹理坐标系 (Generated/Object/UV)** | `Likely Important` | `Partial` | `Supporting` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` |
| **算法纹理与噪声 (Noise/Voronoi)** | `Likely Important` | `Partial` | `Absent` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` |
| **数学运算与混合遮罩 (Math/Mix)** | `Likely Important` | `Partial` | `Absent` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` |
| **色彩映射与区间重映射 (ColorRamp)** | `Likely Important` | `Absent` | `Absent` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` |
| **映射缩放与平铺控制 (Mapping/Scale)** | `Likely Important` | `Partial` | `Supporting` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` |
| **随机化与多变异质感 (Randomization)** | `Likely Important` | `Partial` | `Absent` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` |
| **节点组封装与参数暴露 (Node Groups)** | `Likely Important` | `Absent` | `Absent` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Absent` | `Partial` | `Core coverage` |
| **独立程序化纹理与 `.sbsar` 母版生成** | `Likely Optional` | `Absent` | `Absent` | `Core coverage` | `Absent` | `Absent` | `Advanced` | `Absent` | `Partial` | `Likely Optional` |
| **程序化结果烘焙为 PBR 贴图包** | `Likely Important` | `Absent` | `Absent` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` | `Absent` | `Partial` | `Core coverage` |

---

### 2.5 模块五：Material Acquisition & Conversion (材质采集、图像转换与平铺)

| 知识 / 技能单元 (Unit) | 初步教学必要性 | Born Digital Painter 2025 | Adobe PBR Guide | Adobe 官方当前文档 | Born Digital 1日完成 2025 | Blender 程序化资源 | Born Digital Designer 2022 | 来阳 2026 | CGMA / Gnomon 课程先例 | Phase 1 基础报告结论 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **照片/扫描参考转 PBR 材质原理** | `Likely Important` | `Partial` | `Core coverage` | `Core coverage` | `Core coverage` | `Absent` | `Partial` | `Absent` | `Partial` | `Core coverage` |
| **Substance 3D Sampler 工具链工作流** | `Likely Important` | `Partial` | `Supporting` | `Core coverage` | `Core coverage` | `Absent` | `Partial` | `Absent` | `Partial` | `Likely Important` |
| **Image-to-Material 智能通道提取** | `Likely Important` | `Absent` | `Supporting` | `Core coverage` | `Core coverage` | `Absent` | `Absent` | `Absent` | `Partial` | `Likely Important` |
| **图像无缝平铺处理 (Seamless Tiling)** | `Likely Important` | `Partial` | `Supporting` | `Core coverage` | `Core coverage` | `Partial` | `Core coverage` | `Absent` | `Partial` | `Core coverage` |
| **真实物理尺寸校准 (Scale Calibration)** | `Likely Important` | `Partial` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Partial` | `Absent` | `Partial` | `Core coverage` |

---

### 2.6 模块六：LookDev & Multi-environment Validation (视觉开发与跨引擎验证)

| 知识 / 技能单元 (Unit) | 初步教学必要性 | Born Digital Painter 2025 | Adobe PBR Guide | Adobe 官方当前文档 | Born Digital 1日完成 2025 | Blender 程序化资源 | Born Digital Designer 2022 | 来阳 2026 | CGMA / Gnomon 课程先例 | Phase 1 基础报告结论 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Blender 材质视口与基础着色验证** | `Likely Important` | `Partial` | `Supporting` | `Core coverage` | `Absent` | `Core coverage` | `Partial` | `Core coverage` | `Partial` | `Core coverage` |
| **Unreal Engine 实时材质实例组装** | `Likely Core` | `Partial` | `Supporting` | `Core coverage` | `Absent` | `Absent` | `Partial` | `Partial` | `Core coverage` | `Core coverage` |
| **游戏运行时材质性能与约束 (ORM/BC7)** | `Likely Important` | `Partial` | `Core coverage` | `Core coverage` | `Absent` | `Partial` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` |
| **影视/动画高保真着色差异 (SSS/Coat)** | `Likely Optional` | `Partial` | `Core coverage` | `Core coverage` | `Absent` | `Core coverage` | `Partial` | `Absent` | `Partial` | `Likely Optional` |
| **跨渲染器着色表现差异对比** | `Likely Important` | `Core coverage` | `Core coverage` | `Core coverage` | `Absent` | `Partial` | `Core coverage` | `Absent` | `Core coverage` | `Core coverage` |
| **多环境 IBL 与极端光照压力测试** | `Likely Core` | `Core coverage` | `Core coverage` | `Core coverage` | `Partial` | `Partial` | `Core coverage` | `Partial` | `Core coverage` | `Core coverage` |

---

## 3. 六大能力模块覆盖深度解析

1. **Material Literacy（核心理论基石）**：
   - 处于各权威资料（Adobe PBR Guide, Born Digital, CGMA）交集核心，是决定材质是否物理合规、能否跨光照环境复用的不可动摇底座。
2. **Texture-based Authoring（核心实操生产力）**：
   - 以 Substance 3D Painter 为代表的资产级分层贴图工作流构成了当前游戏与影视资产制作的实操主力，具备最高教学优先级（`Likely Core`）。
3. **Supporting Pipeline（前置支撑知识）**：
   - UV 与 Baking 是连接三维几何与二维贴图的刚性前置纽带。教学策略应聚焦于“提供预制资产与标准 UV，重点攻坚贴图烘焙与接缝排错”，防止退化为建模课。
4. **Procedural / Parametric（程序化材质思维）**：
   - Blender 节点材质提供了零授权成本、直观可视的程序化教学入口，重点培养学生对噪波、数学混合、坐标映射及参数暴露的理解；而 Substance Designer 复杂的函数级 `.sbsar` 制作则定位于进阶选修（`Likely Optional`）。
5. **Material Acquisition（图像采集与转换）**：
   - Sampler / Image-to-Material 填补了由现实照片快速获取无缝 PBR 材质的工业空白，是传统材质与 AI 材质之间的重要技术过渡带。
6. **LookDev & Validation（闭环交付与验证）**：
   - 杜绝“视口美术”假象，通过 Unreal Engine / Marmoset 的材质实例组装与多环境 IBL 旋转验证，确保资产达到运行时交付标准。

---

## 4. 前置与支撑知识边界控制

```
                    ┌────────────────────────────────────────────────────────┐
                    │                      严禁越界领域                       │
                    │   - 复杂角色人体解剖雕刻 / 场景建筑从零白模搭建         │
                    │   - 手工多边形重拓扑 (Manual Retopology) 深入训练       │
                    │   - 骨骼绑定、权重刷取与角色动画制作                     │
                    └───────────────────────────▲────────────────────────────┘
                                                │ 严格剔除 / 仅提供成品
                    ┌───────────────────────────┴────────────────────────────┐
                    │                   受控支撑知识 (Prerequisites)          │
                    │   - UV 接缝与硬边匹配原则 (Seam vs Hard Edge)          │
                    │   - 像素密度 (Texel Density) 计算与对齐                 │
                    │   - 高低模烘焙算子 (Normal/AO/Curvature/ID) 提取与排错   │
                    └───────────────────────────▲────────────────────────────┘
                                                │ 向上支撑
                    ┌───────────────────────────┴────────────────────────────┐
                    │             课程核心主体：Material / Texture Authoring   │
                    │   - PBR 物理光学与通道分层控制                          │
                    │   - 程序化节点与纹理参数化合成                          │
                    │   - 图像转材质与无缝平铺                                │
                    │   - 实时引擎材质组装与 LookDev 多光照验证               │
                    └────────────────────────────────────────────────────────┘
```

---

## 5. 未决问题与证据缺口登记表 (Gap Register Before AI Phase 2)

在进入 Phase 2（AI 生产力工作流对材质管线的重塑评估）前，登记以下当前仍存的证据缺口与未决问题：

| 编号 | 未决议题 (Unresolved Issue) | 当前状态与缺口表现 (Status & Gap) | 对后续 Phase 2 的影响 |
| :--- | :--- | :--- | :--- |
| **GAP-01** | **程序化节点（Procedural Nodes）的实操考核深度** | 已确立 Blender Nodes 为主要入口，但本科生应独立完成多复杂的节点网络（如仅做基础噪波破损 vs. 完整砖墙程序化合成）尚缺量化评估。 | Phase 2 将评估 AI 节点生成（Text-to-Shader）对该门槛的冲击。 |
| **GAP-02** | **Substance 3D Sampler 的常规化程度** | Sampler 的 Image-to-Material 虽已成熟，但在本科教学中属于“必选核心模块”还是“快速体验选修”仍待课时权衡。 | Phase 2 需对比专业 AI 纹理工具与 Sampler 内置算法的精度差异。 |
| **GAP-03** | **Game Realtime 与 Animation LookDev 出口的分化边界** | 两大出口在着色复杂度（如 SSS / Coat / 置换）与优化约束（如 ORM 打包 / BC7 压缩）上的平衡机制仍待细化。 | 决定期末大作业是采用单一双重验证通道还是提供分流选项。 |
| **GAP-04** | **手工绘制微细节 vs. 智能生成器驱动的学时配比** | 传统手绘修贴图（如手工涂抹污垢划痕）在当前工业界中的必要性与被生成式工具压缩的程度尚缺一手案例证据。 | Phase 2 重点调研 AI 生成材质对微细节手绘环节的替代率。 |

---
*本矩阵归档于 `docs/research/curriculum-coverage-matrix.md`，由 Antigravity 自动化研究流水线生成并核查。*
