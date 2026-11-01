# 第 1 讲 MeetMat 18 页幻灯片图像映射、公开仓库合规审查与审校台账

> 版本：v1.1 ｜ 基线关联：Commit `6b12de0` ｜ 对应 Issue #40 / Draft PR #41  
> 输入基准：2026-11-01 Notion 教师交互备课工作台最新版审校稿及 `Skill｜PPT 编写规范 v0.3`。

---

## 1. 15 个 Notion 原始图片块逐项核对表 (100% 真实嵌入)

| Slide | 嵌入文件（存放在 `assets/w1_meetmat/`） | 来源类型与分辨率 | 对应知识点与教学功能 | 审校与同步状态 |
| :--- | :--- | :--- | :--- | :--- |
| **Slide 01** | `img_01_three_classical_busts_three_materials.png` | 外部渲染参考 (1672×941) | 三材质古典雕像对比，引出从经验盲调到 PBR 物理约束与分层思维 | 已有图块 · 教师待审 |
| **Slide 04** | `img_02_1793170130533.png` | 教师 Painter 截图 (380×370) | MeetMat Head 光洁黄色塑料实操外观（Specular Highlight 集中锐利） | 真实截图 · 待审 |
| **Slide 04** | `img_03_1793170142855.png` | 教师 Painter 截图 (392×384) | MeetMat Head 粗糙暗哑陶土实操外观（Specular Highlight 弥散柔和） | 真实截图 · 待审 |
| **Slide 05** | `img_04_image.png` | 外部参考拼图 (800×450) | 官方标杆资产 MeetMat 与潮玩角色换肤（POP MART Molly）类比图 | 示例图待审（保留出处与许可声明） |
| **Slide 06** | `img_05_Slide06_Painter_UI_annotated.png` | 教师 Painter 截图 (1909×1150) | Painter 四核心面板与视口导航高精度分区标注图 | 真实截图 · 待审 |
| **Slide 07** | `img_06_Screenshot_2026-10-28_155822.png` | 教师 Painter 截图 (665×864) | 环境光照观察：天光方向 A（正面受光、背面偏暗） | 真实截图 · 待审 |
| **Slide 07** | `img_07_Screenshot_2026-10-28_155837.png` | 教师 Painter 截图 (674×909) | 环境光照观察：Shift+右键旋转天光后方向 B（正面偏暗、背面受光，高光显著位移） | 真实截图 · 待审 |
| **Slide 07** | `img_08_Screenshot_2026-10-28_160247.png` | 教师 Painter 截图 (711×754) | **Display Settings → Environment Map（更换 HDRI 环境图的入口）** | 真实截图 · 待审 |
| **Slide 08** | `img_09_image.png` | 教师 Painter 截图 (1312×1199) | Yellow Plastic 底漆填充层与 Properties - Fill 参数面板截图 | **已制作 · 已入页（教师已确认完成）** |
| **Slide 09** | `img_10_Slide09_roughness_fixed_light.png` (由原 SVG 渲染) | 原创矢量概念图 (2200×1000) | Roughness 0.10 vs 0.85 固定视角与光照单变量受控实验示意图 | 概念矢量图待审 · 真实实操截图待制作 |
| **Slide 10** | `img_11_image.png` | 教师 Painter 截图 (1448×1086) | 展示如何添加 Black Mask（黑色遮罩隐藏深色上层，露出黄色底漆） | **已制作 · 已入页（教师已确认完成）** |
| **Slide 10** | `img_12_image.png` | 教师 Painter 截图 (1448×1086) | 展示遮罩实际效果（白色画笔开窗显现深色层，黑色画笔修边纠错） | **已制作 · 已入页（教师已确认完成）** |
| **Slide 12** | `img_13_image.png` | 外部教学图表 (1672×941) | Microfacet 微表面方向分布与镜面反射集中／模糊机制示意图 | **待同步旧图**（新候选待同步入页，保留差量记录） |
| **Slide 13** | `img_14_image.png` | 外部渲染参考 (1618×770) | 黄色塑料 (Metallic=0) 与黄金球体 (Metallic=1) 漫反射/镜面反射光学差异参考图 | 参考图已插入 · 教师确认本轮不再调整 |
| **Slide 14** | `img_15_image.png` | 整合示意图 (1672×941) | Layer A（底层）+ Layer B（上层）+ Mask（遮罩）= Result 空间显隐四格合成图 | 整合图已插入 · 教师确认本轮不再调整 |

---

## 2. 图像核查专项：Slide 07 第三张截图（Display Settings）核定

经过像素级 OCR 与 Substance 3D Painter 官方 UI 对照核实：
- **截图真实内容**：该图为 Painter 视口右侧的 `DISPLAY SETTINGS`（显示设置）面板，其中在 `Environment settings` 下点击 `Environment Map` 缩略图后，弹出了环境光资源预设架（包含 `Panorama`、`Soft front`、`Soft low`、`Studio 02` 等不同 HDRI 缩略图）。
- **核实结论**：
  1. 该截图**明确展示的是“更换 Environment Map 的入口与预设库”**；
  2. 它**绝非单纯的曝光度（Environment Exposure）或背景可见性（Environment Opacity）微调**，也不是旋转天光的操作；
  3. PPT 正文与图注已严格对齐 Notion 教师稿：“03 更换 HDRI 是另一件事：Display Settings → Environment Map”与“图 07-3: Display Settings → Environment Map（更换 HDRI 入口）”，消除了把曝光设置误当成换环境的表述风险。

---

## 3. 公开仓库第三方素材合规审查与授权风控

针对保存在 `assets/w1_meetmat/` 及嵌入 PPTX 中的图片，按知识产权与公开仓库传播范围进行分级定界：

### ① 教师/课程团队自有资产（无合规风险，适合公开保存）
- **覆盖文件**：`img_02`、`img_03`、`img_05`、`img_06`、`img_07`、`img_08`、`img_09`、`img_11`、`img_12`（真实软件界面截图）及 `img_10`（原创矢量概念图）、`img_15`（遮罩合成图）。
- **性质认定**：属于授课教师在官方正版软件中结合教学案例生成的原创示范素材，且用于高校课堂教学与学术交流，符合合理使用与开源规范。

### ② 第三方商业 IP 与外部版权素材（须控制传播范围，设置授权/替换门禁）
1. **Slide 05 潮玩换肤类比图 (`img_04_image.png`)**：
   - **风险点**：包含 POP MART（泡泡玛特）Molly 盲盒公仔官方商品摄影图，以及 Adobe 社区 Meet MAT 大赛外部艺术家作品。
   - **合规边界**：
     - 当前仅作为高校非商业性闭环教学辅助类比，PPT 正文与 Notes 中已完整标明出处与免责声明（不声称二者直接关联，不冒充自有版权）；
     - **传播门禁**：若仓库或课程套件未来计划公开发行或商业化出版，**严禁扩大该图片传播**，必须在公开前替换为团队拥有完整版权的原创潮玩 IP 资产或 CC0 共有资产。
2. **Slide 01 封面三材质雕像 (`img_01_...`)**：
   - **风险点**：来源于外部三维渲染教材/学术演示语料。
   - **处置策略**：目前标注为“已有图块 · 教师待审”，后续若公开出版，建议教师在 Painter 中以同一 MeetMat 资产的玉石、石膏与金属预设自行截取原生高清图替换。
3. **Slide 12 微表面朝向图 (`img_13_...`)**：
   - **风险点**：来自经典外文教材/技术报告图表，有潜在版权边界。
   - **处置策略**：当前 Notion 教师稿已明确记录“新修订候选图已制作完成，待入页同步”；新版图为课程团队依据物理原理自主重绘，同步后即可彻底消除外部版权风险。
4. **Slide 13 塑料与黄金对比参考图 (`img_14_...`)**：
   - **风险点**：外部学术参考渲染图。
   - **处置策略**：图注与 Notes 已明确为“两类反射的视觉启发，不代表同条件实验”。后续迭代中优先替换为同环境、同一 MeetMat Head 真实材质截图。

---

## 4. 剩余待教师裁决事项 (Pending Teacher Decisions)

1. **Slide 12 新版候选图同步入页**：
   - 教师稿记载新图已由外部生成，但尚未回传至仓库。待教师或 Browser Lead 在 Notion 确认新图文件后，IDE 即可完成单图热替换。
2. **Slide 09 真实 Painter 实操截图补拍**：
   - 当前采用高清晰度矢量概念图作为教学过渡；后续是否需要补拍真实 Painter 视口截图（固定机位与光照下的 Roughness 0.10 与 0.85 对比），由教师视课堂试讲效果决定。
3. **Slide 05 商业 IP 替换时机**：
   - 在高校校内授课期间，保留 Molly 潮流玩具类比具备极高教学吸引力；是否需要在开源前制作自有基模潮玩替代图，待课程开源阶段统筹决策。
