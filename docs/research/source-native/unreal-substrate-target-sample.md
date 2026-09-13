# Lane G: Unreal Material & Substrate — Realtime Target Constraint Sample — Source-Native Research & Technical Index

> **Artifact Status**: Official Developer Documentation Direct Extraction & Bounded Target Sample  
> **Primary Sources**:
> 1. Epic Games Unreal Engine 5.8 Official Documentation (`dev.epicgames.com/documentation/en-us/unreal-engine/`)
>    - `physically-based-materials-in-unreal-engine`
>    - `substrate-materials-in-unreal-engine`
>    - `material-instances-in-unreal-engine`
> 2. Brian Karis (Epic Games), "Real Shading in Unreal Engine 4" (SIGGRAPH 2013 Course Notes)
> **Artifact Placement**: `docs/research/source-native/unreal-substrate-target-sample.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane G: Unreal / Substrate** 进行严格受限的目标交付约束样本（Bounded Target Sample）提取，只回答一个核心问题：
$$\text{MaterialX / OpenPBR 表达进入游戏实时引擎（Realtime Engine）后，还缺少什么？}$$
重点调查：
1. 材质导入与标准支持边界（Import/Support Boundary）；
2. 材质实例化（Material Instances）架构；
3. 运行时材质行为与性能开销（Runtime Material Behavior & Performance）；
4. 平台硬件与渲染管线约束（Platform & Pipeline Constraints）；
5. 引擎原生着色器图表行为（Engine-native Graph Behavior）。

**核心防错目的**：坚决防止学生和课程团队形成“能够用 MaterialX 描述 / 能够在 DCC 中导入 = 能够直接用于游戏实时生产”的严重错误推论。

---

## 2. 实时交付约束与标准格式的鸿沟 (The Delivery Gap)

标准材质描述（MaterialX / OpenPBR）与工业级实时游戏引擎（Unreal Engine）之间存在以下 5 大核心现实鸿沟：

### 2.1 材质实例化与参数继承 (Material Instances vs. Source Graphs)
- **游戏引擎的渲染批处理瓶颈**：
  - 在实时渲染中，如果每个物体都使用一个独立的 Material Graph（母材质），每个材质都会被单独编译为一个独立的 Shader 变体，引发剧烈的 **Draw Call 激增、着色器编译膨胀（Shader Permutation Explosion）与 GPU 状态切换开销**。
- **Unreal 的生产标准工作流**：
  - 游戏管线强制要求使用 **Master Material（母材质）$\to$ Material Instance Constant (MIC / 材质实例)** 继承架构。
  - 母材质预先编写好通用的着色计算逻辑，并将贴图采样槽（Texture Parameters）与调参滑块（Scalar / Vector Parameters）暴露为参数；
  - 运行时成百上千个场景道具仅仅是母材质的实例（Instances），共享同一个编译好的 GPU 着色器代码段，仅在常量缓冲（Constant Buffer）中更新贴图指针与参数，从而实现高效的 GPU 实例化合批（Instanced Draw Calls）。
- **与 MaterialX 的鸿沟**：
  - MaterialX 描述的是平铺展开的单一材质网络，不包含 Unreal 专有的母材质/子实例继承层次树与编译优化管线。

### 2.2 纹理通道打包与显存带宽约束 (Texture Channel Packing / ORM & BC7)
- **显存带宽（Bandwidth）是实时渲染的第一生命线**：
  - 离线渲染或 DCC（Arnold / Cycles）习惯使用散装贴图（单独的 Roughness.png, Metallic.png, AO.png 散装文件）。
  - 在实时游戏引擎中，散装贴图会导致多倍的显卡纹理采样器（Texture Sampler）占用与显存带宽浪费。
- **工业刚性规范：ORM 打包**：
  - 将三个独立的单通道数据合并为单张 8-bit RGB 贴图：
    - **R 通道**：Ambient Occlusion (AO)
    - **G 通道**：Roughness (粗糙度)
    - **B 通道**：Metallic (金属度)
  - 配合 GPU 硬件级定长分块压缩格式（DirectX 平台采用 **BC7** 针对复杂颜色，采用 **BC5** 针对双通道法线 RG，**BC1/BC3** 针对线性数据）；
  - 这种硬件级内存与通道约束在标准 OpenPBR / MaterialX XML 语法中并不直接体现。

### 2.3 运行时动态材质行为 (Runtime Behavior & Dynamic Material Instances)
- **游戏特有的动态交互**：
  - 角色受击发红、物体表面动态雨水浸湿（动态调整 Roughness）、积雪融化、溶解特效（Dissolve Masking）、受光照驱动的顶点风力摆动（World Position Offset, WPO）。
- **动态控制机制**：
  - 游戏逻辑（C++ / Blueprints）需要在每一帧动态更新材质参数（`CreateDynamicMaterialInstance`, `SetScalarParameterValue`）；
  - 这些运行时时间轴逻辑、物理交互接口和粒子系统碰撞数据，完全超出静态外观描述格式的范畴。

### 2.4 Substrate 现代框架带来的演进与边界 (Substrate Overview & Constraints)
Unreal Engine 5 推出了 **Substrate**（下一代模块化材质框架，旨在取代旧有的固定 Default Lit / Clear Coat 着色模型模式）：
- **Substrate 架构演进**：
  - 引入类似于 OpenPBR 的模块化 BSDF Slab 概念；
  - 支持复杂的多层介质混合（Substrate Slab, Substrate Add, Substrate Horizontal/Vertical Layer）；
  - 具备更精确的光学参数支持（F0 / F90、Mean Free Path、薄膜干涉、Fuzz）。
- **官方技术警示与工业约束**：
  - **性能成本极其敏感**：Substrate 是通过更复杂的 GBuffer 格式（Multi-layer GBuffer）和按需着色代码分支实现的。层级越复杂（如在一个材质上叠加 3 层 Slab），其片元着色器执行时间（PS Cost）成倍增加，极易在移动端或低配主机上发生性能崩溃；
  - 官方文档明确注明：“**Learn to use this Beta feature, but use caution when shipping with it.**”（学习该测试特性，但在商业发布出货时需保持谨慎）。

---

## 3. 教学价值研判支撑：拒绝“能导入 = 能出货”的推论

通过对 Unreal / Substrate 官方约束的提取，为后续 Gate 3 提供了极其关键的教学边界：

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                   实时目标引擎交付约束对照模型                                   │
├───────────────────────────────┬──────────────────────────────────────────────────┤
│ 1. 错误认知                   │ “在 DCC 里连好 MaterialX / OpenPBR，导进虚幻     │
│    (Naive Assumption)         │  引擎就能直接用来做游戏。”                       │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 2. 工业事实                   │ - 引擎支持导入 MaterialX 仅解决了初始网络转译；   │
│    (Production Reality)       │ - 生产中必须重构为 Master Material + Instance； │
│                               │ - 必须执行 ORM 通道合并与 GPU 压缩格式匹配；     │
│                               │ - 必须严格管控 Substrate Slab 层数以防掉帧；     │
│                               │ - 必须保留运行时蓝图交互与动态材质参数接口。     │
├───────────────────────────────┼──────────────────────────────────────────────────┤
│ 3. 课程边界结论               │ 本课程绝不办成“虚幻引擎材质综合教程”，仅将虚幻   │
│    (Curriculum Bounded Scope) │ 引擎作为**【实时目标交付约束与性能红线】的验证   │
│                               │ 样本**，用于闭环检验贴图在游戏环境下的落地合规性│
└───────────────────────────────┴──────────────────────────────────────────────────┘
```

---

## 4. Evidence Register (Lane G)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 | 边界限定 |
| :--- | :--- | :--- | :--- | :--- |
| **UE Physically Based Materials** | Unreal Engine 5.8 Official Documentation | `Platform Documentation` | 确立 Base Color, Roughness, Metallic 的实时物理法则，电介质 Specular 0.5 对应 4% 反射率 | 仅定义标准 PBR 输入语义，不证明外部贴图免适配 |
| **Substrate Materials Framework** | Unreal Engine 5.8 Docs `substrate-materials-in-unreal-engine` | `Platform Documentation` | 证实 Substrate 引入模块化 Slab 与多层架构，但官方明确标为 Beta 并警示商用发布性能开销 | 证明实时多层材质有严苛的 GPU 运行时性能代价 |
| **Material Instances Architecture** | Unreal Engine 5.8 Docs `material-instances-in-unreal-engine` | `Platform Documentation` | 证实游戏生产强制要求母材质与参数化实例体系以避免着色器编译膨胀与 Draw Call 激增 | 证明 MaterialX 等扁平表达不可直接替代引擎原生层级 |

---
*Lane G Source-Native 提取完成，归档于 `docs/research/source-native/unreal-substrate-target-sample.md`。*
