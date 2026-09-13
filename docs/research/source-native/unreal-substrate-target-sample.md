# Lane G: Unreal Material & Substrate — Realtime Target Constraint Sample — Source-Native Research & Technical Index

> **Artifact Status**: Official Developer Documentation Direct Extraction & Bounded Target Sample  
> **Source Rule**: Strictly limited to first-party official sources per Issue #4 contract.  
> **Primary Sources**:
> 1. Epic Games Unreal Engine 5.8 Official Documentation (`dev.epicgames.com/documentation/en-us/unreal-engine/`)
>    - `physically-based-materials-in-unreal-engine`
>    - `substrate-materials-in-unreal-engine`
>    - `material-instances-in-unreal-engine`
>    - `interchange-framework-in-unreal-engine` & MaterialX Integration Notes
> **Artifact Placement**: `docs/research/source-native/unreal-substrate-target-sample.md`  

---

## 1. Executive Summary & Purpose

本研究针对 **Lane G: Unreal / Substrate** 进行严格受限的目标交付约束样本（Bounded Target Sample）提取，只回答一个核心问题：
$$\text{MaterialX / OpenPBR 标准表达进入实时游戏引擎后，还缺少什么？}$$
重点调查：
1. 实时引擎支持边界：UE 5.8 下对 MaterialX 1.39.4 与 Substrate OpenPBR 的支持现状与未支持/透传节点限制（Pass-through limitations）；
2. 材质实例化（Material Instances）架构与着色器编译变体（Permutations）；
3. 运行时动态材质行为（Dynamic Material Instances）与性能成本；
4. 目标管线优化模式（如 ORM 通道打包与纹理压缩）；
5. 严格区分**一手官方事实（SOURCE FACT）**与**教学研判假说（INTERPRETIVE SUMMARY / GATE 3 HYPOTHESIS — NOT A DECISION）**。

---

## 2. 实时交付约束与引擎支持边界 (SOURCE FACT)

### 2.1 UE 5.8 当前 MaterialX 与 OpenPBR 支持现状及限制
- **MaterialX 1.39.4 支持与版本断层**：
  - UE 5.8 的通用数据交换框架（Interchange Framework）中集成了对 MaterialX 的导入支持，其官方文档锁定的支持基线为 **MaterialX 1.39.4**（落后于开源最新稳定版 1.39.5）；
- **Substrate 下的 OpenPBR 支持与测试状态**：
  - 虚幻引擎在 Substrate 模块化材质框架下提供了对 OpenPBR 着色模型的实验性导入映射；
  - 官方文档对 Substrate 明确标注警告：“**Learn to use this Beta feature, but use caution when shipping with it.**”（学习该测试特性，但在商业发布出货时需保持谨慎）。
- **未支持/透传节点限制 (Unsupported / Pass-Through Limitations)**：
  - 官方技术文档与导入管线明确指出：MaterialX 网络中的某些高级程序化节点（如复杂自定义噪波、高阶数学函数或特定三向投射）在转译为虚幻原生材质图表（Unreal Material Graph）时，存在未被完全支持的情况；
  - 部分未支持节点会被自动回退为默认透传（Pass-through）或常量输出，导致跨平台导入后的材质在实时视口中出现外观丢失或局部失效。

### 2.2 材质实例化机制与着色器编译控制 (Material Instances Architecture)
- **母材质 (Master Material) 与实例化架构**：
  - 虚幻引擎官方文档（`material-instances-in-unreal-engine`）指出，材质系统的核心优化模式是将着色网络封装为包含参数（Scalar, Vector, Texture Parameters）的母材质，并在场景中广泛使用材质实例（Material Instance Constant, MIC）。
  - **核心技术原因**：
    1. **避免重复编译与着色器变体膨胀 (Shader Permutations)**：若为每个场景道具创建独立 Material Graph，将引发巨大的着色器编译开销并占用运行时着色器缓存；
    2. **轻量化参数调整**：材质实例共享同一个母材质编译好的 GPU 字节码，仅在常量数据上发生变更，从而大幅降低编辑与运行时的开销。
  - **边界说明**：使用材质实例有助于减少 GPU 状态切换和管线负担；但合批渲染（如 Instanced Static Mesh）还受到网格几何、光照状态及顶点格式等多种条件的严格限制，**并非单纯赋予材质实例就能自动无条件合并 Draw Calls**。

### 2.3 纹理通道打包与硬件压缩优化模式 (Texture Packing & Compression)
- **目标管线优化模式**：
  - 游戏实时渲染中广泛采用通道合并（Channel Packing）模式，最典型的为 **ORM 贴图**（将 Ambient Occlusion 放入 R 通道、Roughness 放入 G 通道、Metallic 放入 B 通道），用于减少纹理采样器占用与显存带宽消耗；
  - 配合 GPU 定长硬件压缩格式（如 DirectX 下的 BC7 针对带微变彩色的贴图、BC5 针对双通道法线 RG、BC1 针对基础 RGB）；
  - **性质归定**：这是游戏实时管线中经官方文档与工业实践证明的有效优化模式，属于目标交付端的管线工程规范，而非所有 3D 软件共同的强制性基础定义。

### 2.4 运行时动态材质实例 (Dynamic Material Instances)
- **游戏运行时的动态交互**：
  - 虚幻引擎支持通过蓝图（Blueprints）或 C++ 在游戏运行期间创建动态材质实例（`CreateDynamicMaterialInstance`）并动态改变参数（`SetScalarParameterValue`、`SetVectorParameterValue`）；
  - 用于实现角色受击变色、渐进式溶解、雨水潮湿等交互效果；
  - **特性说明**：动态材质参数可在需要时随游戏事件按需更新，或在特定动画插值下平滑变化，**不要求且通常并不在每一帧无条件强制更新**。

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
| **Substrate Framework & Beta Status** | Unreal Engine 5.8 Docs `substrate-materials-in-unreal-engine` | `Platform Documentation` | 证实 Substrate 引入模块化 Slab 架构并实验性支持 OpenPBR，但官方明确注明为 Beta 且警示商业发布性能风险 | 证明实时多层物理材质在游戏运行时具有严苛的性能开销 |
| **Material Instances & Permutations** | Unreal Engine 5.8 Docs `material-instances-in-unreal-engine` | `Platform Documentation` | 证实使用母材质与材质实例架构可避免着色器编译变体膨胀并实现轻量调参 | 降低编译与状态切换成本，不代表能无条件合并 Draw Calls |
| **MaterialX 1.39.4 Integration Boundary** | UE 5.8 Documentation & Interchange Pipeline | `Platform Documentation` | 证实 UE 5.8 Interchange 框架集成支持的是 MaterialX 1.39.4，且部分未支持节点存在透传回退限制 | 证明开源最新标准与商用引擎之间存在版本兼容滞后与未支持节点断层 |

---
*Lane G Source-Native 提取校准完成，归档于 `docs/research/source-native/unreal-substrate-target-sample.md`。*
