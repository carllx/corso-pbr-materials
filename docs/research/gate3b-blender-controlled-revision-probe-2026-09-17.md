# Gate 3B Blender 5.2 LTS 受控修订充分性实测探针报告

> **探针阶段**：Stage 2 Gate 3B — Practice Implementation Re-baselining & Sufficiency Probe  
> **审查基准与依据**：GitHub Issue #5 (Comment ID: `5706879947`)、Owner Approved Directives (2026-09-17)  
> **核心探针问题**：在工具中立（Tool-neutral）的受控修订要求下，Blender 5.2 LTS 是否已经足够形成清楚、可恢复、可解释的本科教学实现？

---

## 1. 证据状态与事实标签体系 (Fact Labels)

本报告严格区分客观事实、实测观察与教学推论：
- **`[VERIFIED LOCAL FACT]`**：本机实际执行命令、路径检查、版本输出与哈希校验确证的物理事实；
- **`[OBSERVED PROBE RESULT]`**：在 Blender 5.2.2 LTS 运行环境下实际执行受控修订干跑所记录的操作与视觉数据；
- **`[TEACHING INTERPRETATION]`**：基于实测事实对本科教学认知负荷、学生心智模型与备课成本的专业推论；
- **`[UNKNOWN / NOT TESTED]`**：本次有界探针未涉及或当前仍未掌握的外部事实。

---

## 2. 运行环境与基线资产事实 (Environment & Assets)

### 2.1 运行环境双版本并存核验
- `[VERIFIED LOCAL FACT]`: 本机原有 `/Applications/Blender.app` 保持完全未动，经 app 内可执行文件核验为 `Blender 4.5.1 LTS` (Hash: `b0a72b245dcf`, Built: 2025-07-29)；
- `[VERIFIED LOCAL FACT]`: 依据官方发布源 `https://download.blender.org/release/Blender5.2/` 下载官方 `blender-5.2.2-macos-arm64.dmg`；
- `[VERIFIED LOCAL FACT]`: DMG SHA256 校验值为 `dc4125399b8bfefe283cc1624d6cfc7809d1cac20ace51072127eb371f31f210`，与官方发布的 `blender-5.2.2.sha256` 100% 严格一致；
- `[VERIFIED LOCAL FACT]`: 部署为 `/Applications/Blender 5.2.2 LTS.app`，经 app 内可执行文件核验为 `Blender 5.2.2 LTS` (Hash: `d13f752e3b9c`, Built: 2026-09-14 15:14 / Release 2026-09-15)；
- `[VERIFIED LOCAL FACT]`: Substance 3D Painter 独立应用在本机未安装，本轮未执行任何 Painter 安装或探测。

### 2.2 教师预置测试资产说明
- `[VERIFIED LOCAL FACT]`: 依据教学规范（建模与 UV 仅为支撑知识），由教师端预置极简、中性且规范展开 UV 的硬表面零件（倒角机械盖板 `BevelPlate`，尺寸 $2.0 \times 1.4 \times 0.3\,\text{m}$，边缘平滑倒角，Smart UV 投影展开，搭配三点面光源与摄像机）。
- 标记声明：`Teacher-provided setup / not part of tested student authoring workload`。
- 本地工程路径：`/Users/yamlam/.gemini/antigravity/brain/7be0ae4e-b9e2-409d-8be4-5d858898125e/scratch/gate3b/controlled_revision_base.blend`。

---

## 3. 受控修订探针干跑流程 (Controlled Revision Probe Execution)

干跑严格对应真实 Blender 5.2 GUI Shader Editor 教学操作流程：

### 阶段 1：初始材质搭建 (Initial Material Setup)
- **因果分层关系**：
  - 底层基底 (Base Metal)：`Principled BSDF`，工业铸钢色 (`RGB: 0.24, 0.25, 0.27`)，金属度 `Metallic = 1.0`，粗糙度 `Roughness = 0.25`；
  - 表层涂装 (Coating Paint)：`Principled BSDF`，安全橙面漆 (`RGB: 0.82, 0.40, 0.05`)，非金属 `Metallic = 0.0`，粗糙度 `Roughness = 0.45`；
- **空间遮罩控制**：`Texture Coordinate (Object)` $\to$ `Noise Texture (Scale 4.5, Detail 4.0)` $\to$ `ColorRamp`（黑位 `0.42`，白位 `0.48`）；
- **混合输出**：`Mix Shader`（`Fac = ColorRamp`，`Shader1 = Coating`，`Shader2 = Base Metal`）$\to$ `Material Output`；
- `[OBSERVED PROBE RESULT]`: 成功生成 `controlled_revision_initial.blend` (SHA256: `64749ee7fdc34504...`) 并渲染验证图 `probe_initial_render.png`。视口清晰呈现橙色涂装剥落露出高光金属基底。

### 阶段 2：第一次受控修订 (Revision #1 — 局部磨损扩大与表面粗化)
- **修订要求**：指定接触磨损区域扩大约 35%，且暴露金属因机械刮擦发生物理粗糙度上升；非目标区域（橙漆表面）保持原样。
- **GUI 操作执行**：
  - 空间范围调整：选中 `ColorRamp`，将滑动色标位置调整为 `0.35` 与 `0.42`；
  - 属性物理联动：选中 `Base_Metal` 节点，将 `Roughness` 从 `0.25` 滑动调整为 `0.40`；
- `[OBSERVED PROBE RESULT]`: 
  - 橙漆涂层 Base Color 保持 `(0.82, 0.40, 0.05)`，Roughness 保持 `0.45`，Metallic 保持 `0.0`，非目标区域 100% 严格未受污染；
  - 成功保存 `controlled_revision_r1.blend` (SHA256: `af2a6d89c6abb598...`) 并渲染 `probe_revision1_render.png`。

### 阶段 3：保存、关闭进程与重新加载恢复 (Save / Close / Reopen Verification)
- **操作**：完全退出 Blender 进程，释放内存，重新启动 `Blender 5.2.2 LTS` 并打开 `controlled_revision_r1.blend`。
- `[OBSERVED PROBE RESULT]`:
  - 材质 `M_Coated_Plate` 完整恢复；
  - 节点网络中 `Mask_ColorRamp`、`Base_Metal`、`Coating_Enamel`、`Mix_Shader` 节点标识与位置完好；
  - `ColorRamp` 色标值 (`0.35/0.42`) 与 `Base_Metal` 粗糙度 (`0.40`) 读数精确一致，控制入口直观立等可寻。

### 阶段 4：第二次受控修订 (Revision #2 — 二次范围微调与属性独立解耦调整)
- **修订要求**：在重开工程中微调磨损边缘（进一步扩展至 `0.30/0.38`），并在该局部区域内**独立**调整金属氧化变暗（Base Color 调深至 `0.13, 0.14, 0.15`），验证与涂层及粗糙度的解耦独立性。
- `[OBSERVED PROBE RESULT]`:
  - 空间滑块与颜色属性独立调整顺利完成；
  - 涂层非目标通道数据再次核验证明保持 `0.45` 粗糙度与 `0.0` 金属度不变；
  - 成功保存 `controlled_revision_r2.blend` (SHA256: `f5dac7f30c66654d...`) 并渲染 `probe_revision2_render.png`。

---

## 4. 观察字段实测记录 (Ten Observation Fields)

依据不搞打分量表、不设伪精确及格线的原则，真实记录以下 10 项观察字段：

| 观察字段 | 探针实测记录 (Probe Observation) | 教学定性解释 (Teaching Interpretation) |
| :--- | :--- | :--- |
| **1. 教师准备负担 (Teacher Prep)** | 准备标准倒角几何与基础布光仅需数分钟，无需任何外部资产包或付费插件。 | 教师无需提前打包高复杂度 Python 资产或维护庞大模板库，年度备课与资产维护负担极低。 |
| **2. 学生直面概念量 (Student Concepts)** | 直面概念为：`Principled BSDF`、`Mix Shader`、`ColorRamp` 标量映射与物理因果分层（底漆/表漆）。 | 概念直接对应 PBR 物理模型与色彩/遮罩基础，无“工具私有黑话”（如智能材质/锚点/通道填充）。 |
| **3. 需心智跟踪的表示形式 (Mental Representations)** | 2 个直观的材质块（涂装 BSDF、金属 BSDF）与 1 个遮罩流。共 3 个核心组块。 | 认知负荷低，学生可清晰在脑海中建立“底层是什么、表层是什么、谁在控制露出”的心智模型。 |
| **4. 编辑局部性 (Edit Locality)** | 修改范围仅需定位到 `ColorRamp`；修改金属质感仅需调整 `Base_Metal`。未出现通道间相互污染。 | 局部性极高。由于节点分立，调整露底物理参数绝不会破坏未露底漆面参数。 |
| **5. 显式意图依赖 (Intentional Dependencies)** | 空间遮罩同时且显式地驱动了 Base Color、Roughness、Metallic 三个通道在边界处的自然物理切换。 | 依赖关系完全符合现实物理腐蚀/磨损因果，且在节点连线上肉眼可见（一根线连接 Mix Fac）。 |
| **6. 隐蔽/黑箱依赖 (Hidden Dependencies)** | 无任何隐藏的 Layer Blend Mode、隐藏 Pass-through 通道或跨图层锚点引用。 | 故障排查（Debug）直观，没有“不知道哪个图层改了粗糙度”的图层栈黑箱困扰。 |
| **7. 二次修订摩擦度 (Second-revision Friction)** | 极低。面对二次追加需求，直接拖动已有 `ColorRamp` 色标或取色器即可实时生效。 | 教学迭代顺畅，修改单响应敏捷，无需重新烘焙或重画像素。 |
| **8. 保存与重新打开恢复度 (Save/Reopen Recovery)** | 100% 恢复。Blender `.blend` 文件自包含，节点别名与布局完好如初。 | 教学交作业与课后恢复零丢失风险。 |
| **9. 排错与查阅文档需求 (Troubleshooting & Docs)** | 5.2.2 LTS 运行期间无崩溃、无 shader 报错。唯一的 Deprecation 提示为 `mat.use_nodes` 预计在 6.0 移除（当前 5.2 LTS 完全支持）。 | 软件稳定性高，学生无需频繁查阅边缘功能说明书。 |
| **10. 导出影响与第二工具动机 (Export & Second-tool Motivation)** | `Mix Shader` 在 Blender 视口中表现极佳，但若直接导出为 glTF/Game Engine 需要烘焙或转为单 BSDF 混合。 | **这是唯一的潜在张力点**；但在 LO3 材质分层与受控修订能力培养上，并不需要引入第二软件 Painter。 |

---

## 5. 未决事实清单 (Unknown / Not Tested)

以下事项本次探针明确未予测试，保持客观边界：
- `[UNKNOWN 01]`: 在 Blender 5.2 中执行全流程贴图烘焙（Bake to PBR Textures for ORM/glTF）的学生直面操作摩擦；
- `[UNKNOWN 02]`: 多图块 UV (UDIM) 或复杂有机生物体手绘纹理在 Blender 5.2 下的教学体验；
- `[UNKNOWN 03]`: 标准高校机房在全班并发运行 EEVEE Next 时的 GPU 算力瓶颈。

---

## 6. 决策门禁裁决 (Decision Gate Finding)

基于客观实测证据，本次探针裁决为：

### **`BLENDER_CONTROLLED_REVISION_SUFFICIENCY_POSITIVE`**

#### 裁决依据：
1. **受控修订两次修改完整且顺畅达成**：在 Blender 5.2.2 LTS 原生环境下，无论是磨损范围扩大、物理粗糙度耦合调整，还是二次独立色彩调整，均可在极低操作步骤下精准完成；
2. **控制入口清晰、依赖显式可查**：学生直面的节点网络干净紧凑，非目标区域保全性达到 100%；
3. **保存重开完全可恢复**：数据块自包含，无外部材质库断链风险；
4. **无引入第二工具的保留教学刚需**：在 LO3“多通道分层创作与空间局部受控修订”教学中，Blender 5.2 已经完全自足（Sufficient），未观察到必须引入 Substance 3D Painter 才能解决的保留能力阻碍；
5. **结论意涵**：**本轮严禁安装 Substance 3D Painter**。实践主线保持 Blender-only 为首要候选。下一步 Gate 3B 行动应聚焦于受限下游交付验证（Downstream Delivery Probe）。

---

## 7. 资产归档与哈希记录 (Artifact Ledger)

依据代码仓库治理规范，二进制 `.blend` 与渲染 PNG 归档于本地会话暂存区，不强制作为大体积二进制推送到 Git 仓库：
- **基线几何**：`controlled_revision_base.blend`
- **初始工程**：`controlled_revision_initial.blend` (SHA256: `64749ee7fdc3450410ff10a8c2f1f5166299b8ea0ea1d8ea83446bf4fc911f93`)
- **修订 1 工程**：`controlled_revision_r1.blend` (SHA256: `af2a6d89c6abb5985dc7321e25e9d9972bc58a0b0d6118aa95c0245bca532a82`)
- **修订 2 工程**：`controlled_revision_r2.blend` (SHA256: `f5dac7f30c66654df6bf532677ceb264e16ff7284da828fe539b56f2ec550785`)
- **验证图像**：`probe_initial_render.png`, `probe_revision1_render.png`, `probe_revision2_render.png` (均已在报告中视觉核验通过)。
