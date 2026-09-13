# Lane G: Unreal Material & Substrate — Realtime Target Constraint Sample — Source-Native Research & Technical Index

> **Artifact Status**: Official Developer Documentation Direct Extraction & Bounded Target Sample  
> **Source Rule**: Strictly limited to first-party official sources per Issue #4 contract.  
> **Primary Sources**:
> 1. Epic Games Unreal Engine 5.8 Official Documentation (`dev.epicgames.com/documentation/en-us/unreal-engine/`)
>    - `physically-based-materials-in-unreal-engine`
>    - `substrate-materials-in-unreal-engine`
>    - `material-instances-in-unreal-engine`
>    - `interchange-framework-in-unreal-engine` & MaterialX Support Matrix
> **Artifact Placement**: `docs/research/source-native/unreal-substrate-target-sample.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane G: Unreal / Substrate** 进行严格受限的目标交付约束样本（Bounded Target Sample）提取，只回答一个核心问题：
$$\text{MaterialX / OpenPBR 标准表达进入实时游戏引擎后，还缺少什么？}$$
重点调查：
1. 实时引擎支持边界：UE 5.8 官方 MaterialX 1.39.4 节点支持矩阵与实际分类边界；
2. 明确区分：**OpenPBR 支持状态** 与 **Substrate 框架本身的 Beta 状态**；
3. 材质实例化（Material Instances）架构的真实机制与静态参数变体（Permutations）；
4. 目标管线优化模式（如 ORM 通道打包与纹理压缩）；
5. 严格区分**一手官方事实（SOURCE FACT）**与**教学研判假说（INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION）**。

---

## 2. 实时交付约束与引擎支持边界 (SOURCE FACT)

### 2.1 UE 5.8 官方 MaterialX 节点支持矩阵与 OpenPBR 状态 (Official Support Matrix)
根据 Unreal Engine 5.8 官方 Interchange Framework 与 MaterialX 技术支持文档：
1. **支持版本基线**：UE 5.8 官方支持的 MaterialX 规范版本为 **1.39.4**。
2. **OpenPBR Surface 支持与 Substrate 关系**：
   - **OpenPBR 具备官方支持**：在开启 Substrate 框架时，引擎提供对 OpenPBR Surface 的直接映射支持；
   - 当 Substrate 未开启时，导入器使用标准表面材质函数（StandardSurface material functions）进行替代映射；
   - **独立状态区分**：OpenPBR 导入映射支持本身是具备官方管线实现的；而 Substrate 框架整体在引擎中带有官方 Beta 标签（官方提示在商业发布时谨慎评估性能）。
3. **BSDF / EDF / VDF 节点支持矩阵官方真实分类**：
   - **MaterialX PBR BSDF 节点**：官方文档明确记录，所有 MaterialX PBR BSDF 节点在导入时**均实现为透传节点（pass-through nodes），且其输入不进行连接（inputs not connected）**；
   - **EDF (发光分布函数) 节点**：除 `uniform_edf` 获得支持外，其余 EDF 节点均作为透传节点处理且输入不连接；
   - **VDF (体积分布函数) 节点**：属于官方文档明确支持的节点集；
   - **Utility / PBR 节点**：仅 Epic 官方清单中明确列出的特定实用节点与数学节点获得导入转译支持。

### 2.2 材质实例化机制与参数控制 (Material Instances Architecture)
- **参数化派生架构**：
  - 虚幻引擎官方文档（`material-instances-in-unreal-engine`）指出，材质实例（Material Instances）是父级母材质（Parent Material）的参数化派生。
  - **动态参数修改优势**：在游戏运行或编辑时调整材质实例中的标量、向量或纹理参数，可以避免修改或重新编译整个底层基础材质图表。
- **静态参数与着色器变体 (Static Parameters & Permutations)**：
  - 官方文档明确说明：静态开关参数（Static Switch Parameters）或静态组件掩码的更改，由于改变对着色器分支的静态评估，**仍然会触发新的着色器变体编译（Shader Permutations）**。
  - **边界说明**：使用材质实例属于工程组织与参数化调优手段，官方文档未曾作出“赋予材质实例即可无条件合并 Draw Calls”的绝对承诺。

### 2.3 纹理通道打包与硬件压缩优化模式 (Texture Packing & Compression)
- **目标管线优化模式**：
  - 游戏实时渲染中广泛采用通道合并（Channel Packing）模式，最典型的为 **ORM 贴图**（将 Ambient Occlusion 放入 R 通道、Roughness 放入 G 通道、Metallic 放入 B 通道），用于减少纹理采样器占用与显存带宽消耗；
  - 配合 GPU 定长硬件压缩格式（如 DirectX 下的 BC7 针对带微变彩色的贴图、BC5 针对双通道法线 RG、BC1 针对基础 RGB）；
  - **性质归定**：这是游戏实时管线中经官方文档与工业实践证明的有效优化模式，属于目标交付端的管线工程规范，而非所有 3D 软件共同的强制性基础定义。

### 2.4 运行时动态材质实例 (Dynamic Material Instances)
- **游戏运行时的动态交互**：
  - 虚幻引擎支持通过蓝图（Blueprints）或 C++ 在游戏运行期间创建动态材质实例（`CreateDynamicMaterialInstance`）并动态改变参数（`SetScalarParameterValue`、`SetVectorParameterValue`）；
  - 用于实现角色受击变色、渐进式溶解、雨水潮湿等交互效果；
  - **特性说明**：动态材质参数可在需要时随游戏事件按需更新，或在特定动画插值下平滑变化，并不要求在每一帧无条件强制执行。

---

## 3. 解释性总结与教学研判假说 (INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION)

> [!NOTE]
> 本节内容为基于一手文档形成的教学设计假说，用于为后续 Gate 3 决策提供讨论基础，**不构成当前阶段的最终教学裁决**。

### 3.1 目标交付约束与防错教学假说
- **防错教学目标假说**：
  - 课程应坚决防止学生形成“在外部软件连好 MaterialX 或画好 PBR 贴图，导进游戏引擎就能直接用于商业出货”的简单化理解；
  - 引导学生认识到标准外观文件（MaterialX / OpenPBR）是**跨平台交换的起点**，进入实时游戏生产环境后，必须经过母材质适配、参数暴露、通道打包与性能调优等目标交付约束；
- **课程范围边界假说**：
  - 本课程的核心是 PBR 材质原理与多通道创作，不应偏离轨道扩展为深入的“虚幻引擎关卡制作与蓝图开发课程”；
  - 虚幻引擎在课程中应定位于**“实时目标交付约束与性能规范验证的典型样本（Bounded Realtime Sample）”**。

---

## 4. Evidence Register (Lane G)

| 证据条目 | 原始权威来源 | 证据类型 | 支撑事实 (SOURCE FACT) | 边界限定 (SOURCE FACT) |
| :--- | :--- | :--- | :--- | :--- |
| **UE Physically Based Materials** | Unreal Engine 5.8 Official Documentation | `Platform Documentation` | 确立 Base Color, Roughness, Metallic 的实时物理法则，定义电介质默认 Specular 0.5 对应 4% 反射率 | 仅定义引擎内 PBR 输入参数语义，不代表外部贴图免转译适配 |
| **Substrate Framework & OpenPBR Status** | Unreal Engine 5.8 Docs `substrate-materials-in-unreal-engine` | `Platform Documentation` | 证实开启 Substrate 时支持 OpenPBR Surface（未开启使用 StandardSurface 代替）；Substrate 框架自身标为 Beta 且警示商业发布性能风险 | 明确区分 OpenPBR 支持存在与 Substrate 框架自身的 Beta 属性 |
| **Material Instances & Permutations** | Unreal Engine 5.8 Docs `material-instances-in-unreal-engine` | `Platform Documentation` | 证实材质实例为参数化派生，动态修改免于重新编译父级材质，但静态参数变更仍会产生着色器变体（Permutations） | 属于参数继承与编译优化机制，不保证自动合并 Draw Calls |
| **UE 5.8 MaterialX Support Matrix** | UE 5.8 Documentation & Interchange Pipeline | `Platform Documentation` | 证实支持版本为 1.39.4；BSDF 节点作为透传处理且输入未连接；除 `uniform_edf` 外其余 EDF 节点为透传且输入未连接；VDF 节点获支持 | 依据官方准确分类记录支持矩阵，不推测未经证明的广泛节点失效 |

---
*Lane G Source-Native 提取校准完成，归档于 `docs/research/source-native/unreal-substrate-target-sample.md`。*
