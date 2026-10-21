# 第 1 讲：Substance 3D Painter / MeetMat 教师 GUI 试走操作卡与反馈模板 (Minimal Walkthrough Guide)

> **治理定位与执行门禁 (Governance & Status)**：  
> - **承载工单**：[Issue #40](https://github.com/carllx/corso-pbr-materials/issues/40)（关联父工单 [Roadmap #1](https://github.com/carllx/corso-pbr-materials/issues/1)；[Draft PR #41](https://github.com/carllx/corso-pbr-materials/pull/41)）  
> - **输入依据**：广州软件学院第 1 讲既有 PPT/PDF 课件（`1-初识Substance 3D Painter.pdf`）；第一讲教学草案 [painter-week1-meetmat-teaching-draft-v0.1.md](painter-week1-meetmat-teaching-draft-v0.1.md)；郑琳《Substance 3D Painter游戏贴图绘制与材质制作》(2024) 章节与图表指针；[legacy-courseware-source-pedagogical-audit.md](legacy-courseware-source-pedagogical-audit.md)  
> - **核心使命**：为授课教师提供一份**可在实机（或目标机房 PC）独立快速试走的最小交互操作卡**，以最短路径闭环验证 MeetMat 核心交互与工程生命周期；**不等待 160 分钟大班真人课堂容量测量**，先在教师端确认可操作性与截图抓取。  
> - **端侧宿主边界说明 (Host Boundary Notice)**：  
>   - 经 IDE 端侧环境系统核查，当前执行环境未配置 Whimsical 或 Notion 的 API Token、专用 CLI 或 MCP 插件，无法从端侧直接程序化读取私有云端白板或备课工作台；  
>   - 该边界**不构成对本次 GUI 试走交付的阻塞**；项目严格遵循 `AGENTS.md` 规范，以 **GitHub 仓库为唯一教学决策真实数据源 (Single Source of Truth, SSOT)**，不新建外部替代库，不私自复制代码与受限原件。  
> - **门禁定界**：当前操作卡内未在目标机房实操 PC 端到端核实的按钮文字、弹窗层级与系统快捷键统一标记为 **`RUNTIME REQUIRED`**；教师完成试走并回填反馈表后，方可升级为 `VERIFIED ON TARGET PC`。

---

## 1. 教师最小 GUI 试走操作卡 (Step-by-Step Walkthrough Card)

本操作卡围绕教师已接受的保底核心任务设计：**MeetMat Head 纹理集、底层黄色电介质塑料、第二层深色覆盖面罩、黑色遮罩画笔开窗与纠错、单通道视口核验、另存为 `.spp` 并彻底退出重启核验**。全流程预计耗时约 **15–20 分钟**。

```
┌──────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 第 1 讲教师最小 GUI 试走 8 步全景                            │
├─────────┬──────────────────────┬─────────────────────────────────────────────────────────────┤
│ 步骤    │ 操作核心             │ 验证目标与交付物                                            │
├─────────┼──────────────────────┼─────────────────────────────────────────────────────────────┤
│ Step 1  │ 启动与载入示例       │ 打开官方原生 MeetMat Sample，确认视口与网格贴图完备         │
│ Step 2  │ 视口与光照交互       │ 验证 Alt 导航三键客、F 键聚焦与 Shift+右键 HDRI 天光旋转   │
│ Step 3  │ 纹理集聚焦           │ 在 Texture Set List 中锁定 Head 部位，规避 Body/Base 分心   │
│ Step 4  │ 底层黄色塑料填充层   │ 添加 Fill Layer，固定光照视角，调节 Roughness 观察光斑聚散  │
│ Step 5  │ 第二层深色覆盖层     │ 新建深蓝黑 Fill Layer，核验全头覆盖状态                     │
│ Step 6  │ 黑色遮罩与开窗涂抹   │ 挂载 Black Mask，用 1 键白画笔面部开窗，用 X 键黑画笔擦除   │
│ Step 7  │ 视口通道检查与快照   │ 用 C 键通道核验 Metallic=0 与 Roughness；按 Tab 截取视口    │
│ Step 8  │ 工程保存退出重开闭环 │ 规范命名存为 .spp，彻底退出进程并双击重开，核验数据持久化   │
└─────────┴──────────────────────┴─────────────────────────────────────────────────────────────┘
```

---

### Step 1：软件启动与载入官方 MeetMat 示例 (Open Sample)

- **【操作动作 (Action)】**：
  1. 启动目标电脑上的 Substance 3D Painter 软件；
  2. 若弹出初始欢迎弹窗，点击右上角关闭或点击 `Open Sample...`；若已进入主界面，点击顶部菜单栏：`File (文件) -> Open Sample... (打开样本...)`；
  3. 在弹出的官方内置示例列表窗口中，找到并双击选中 **`MeetMat`**（或 `MeetMat.spp`）。
- **【预期画面 (Expected Screen)】**：
  - 视口正中出现灰白色（或带初始棋盘格/基础材质）的 MeetMat 球人完整模型；
  - 右侧面板展开，右上角显示纹理集列表，右下角显示图层堆栈；视口光照正常渲染，无着色器编译报错红字。
- **【常见操作卡点 (Gotchas)】**：
  - **卡点 1-A**：个别绿色版或精简版机房安装可能删除了 `samples` 文件夹，导致 `Open Sample...` 对话框空白；
  - **卡点 1-B**：误点击 `File -> Open...`，在本地文件夹寻找文件导致卡住。
- **【最小恢复办法 (Recovery Steps)】**：
  - 若 `Open Sample...` 为空，在文件资源管理器中全局搜索 `MeetMat.spp`，通常位于 `C:\Program Files\Adobe\Adobe Substance 3D Painter\resources\samples\` 或文档目录下；若确实缺失，启动备用 U 盘中的干净 `MeetMat_Starter.spp` 救急。
- **【实机门禁标记】**：`RUNTIME REQUIRED`（确认目标机房版本是否原生自带样本）。
- **【教材证据指针】**：`zheng-2024-painter` §2.1.2 打开工程与样本（印刷页 17 / 物理页 27；图 2.6）。

---

### Step 2：3D 视口核心导航与环境光照旋转 (Viewport & HDRI)

- **【操作动作 (Action)】**：
  1. **视口导航三键客**：
     - 按住键盘 `Alt + 鼠标左键拖动`：围绕球人进行 360 度多角度旋转观察；
     - 按住键盘 `Alt + 鼠标中键拖动`：上下左右平移视口视野；
     - 按住键盘 `Alt + 鼠标右键水平拖动`（或滚轮滚动）：推拉缩放视角；
     - 按键盘单键 **`F`**（Frame / 聚焦）：将当前选中模型部件（Head）自动居中聚焦于 3D 视口中央（**注意**：`F` 键仅重置相机对准中心与观察距离，**绝不重置环境光照旋转角度 (HDRI)，也不恢复特定默认视角方向或着色模式**）；
  2. **旋转环境光照（独立观察活动）**：
     - 固定当前观察角度，按住键盘 **`Shift + 鼠标右键水平左右拖动`**。
- **【预期画面 (Expected Screen)】**：
  - 观察球人头部与底座，天光环境贴图（球形全景）随鼠标拖动实时旋转，模型表面的明暗交界线与环境反光自然平滑转动，视口无撕裂或卡死。
- **【常见操作卡点 (Gotchas)】**：
  - **卡点 2-A**：误把 `Shift+右键` 记为 `Alt+右键`，导致模型视角被推拉而非旋转光照；
  - **卡点 2-B**：视口被无意推拉到极远或穿模进入模型内部，视野一片漆黑；
  - **卡点 2-C**：误以为按 `F` 键能还原被旋转过的天光角度（纠正：天光旋转独立于相机聚焦）。
- **【最小恢复办法 (Recovery Steps)】**：
  - 视角飞离丢失时，按键盘字母 **`F`** 键将模型居中召回视口中心；天光若需重置可观察环境球方位或继续用 `Shift+右键` 调整到合适受光面。
- **【实机门禁标记】**：`RUNTIME REQUIRED`（核验机房 Windows 机械键盘与三键鼠标中键灵敏度）。
- **【教材证据指针】**：`zheng-2024-painter` §2.2 视图操作（印刷页 17~18 / 物理页 27~28）。

---

### Step 3：纹理集列表确认与 Head 部位聚焦 (Texture Set Focus)

- **【操作动作 (Action)】**：
  1. 将视线移至软件界面右上方的 **`Texture Set List (纹理集列表)`** 调板；
  2. 观察列表中存在的 3 个纹理集项：`Head`、`Body`、`Base`；
  3. 用鼠标单击选中 **`Head`**（确保该行呈现高亮选中状态）；
  4. 检查下方的 **`Layers (图层)`** 调板，确认当前显示的图层归属于 `Head`。
- **【预期画面 (Expected Screen)】**：
  - `Head` 保持高亮激活；3D 视口中若有其他部位存在图层，不会混杂到当前的图层堆栈中；第一讲全员任务严格锁定在头部。
- **【常见操作卡点 (Gotchas)】**：
  - **卡点 3-A**：误留在 `Base` 或 `Body`，在后续建层时画了半天发现头部没有任何变化；
  - **卡点 3-B**：误点击了纹理集旁边的眼睛图标，导致头部在视口中被直接隐藏。
- **【最小恢复办法 (Recovery Steps)】**：
  - 若头部在视口中消失，重新点击 `Texture Set List` 中 `Head` 旁边的眼睛图标恢复可见；确认当前蓝色/灰色高亮条停在 `Head` 上。
- **【实机门禁标记】**：`VERIFIED (概念规范)` / `RUNTIME REQUIRED (UI 语言高亮表现)`。
- **【教材证据指针】**：`zheng-2024-painter` §2.10 纹理集列表（印刷页 62~65 / 物理页 72~75；图 2.115）。

---

### Step 4：建立底层黄色塑料填充层与粗糙度参数微调 (Plastic Base & Roughness)

- **【操作动作 (Action)】**：
  1. 在 `Layers (图层)` 调板上方工具条中，定位并点击 **油漆桶图标（`Add fill layer / 添加填充图层`）**；
  2. 在新生成的图层上双击文本，重命名为 **`Plastic_Base`**；
  3. 查看下方 **`Properties: Fill (属性: 填充)`** 调板：
     - 在通道开关按钮区（`color`, `metal`, `rough`, `nrm`, `height`），鼠标点击取消激活 **`nrm`** 与 **`height`** 按钮（仅保留 `color`, `metal`, `rough` 三大通道亮起）；
     - 点击 **`baseColor`** 色块，在弹出的拾色器中选择一个明亮柠檬黄（例如 Hue 约 50°，高饱和）；
     - 确认 **`Metallic`** 滑块数值严格保持为 **`0.0`**（电介质绝缘体）；
     - **执行单一变量 Roughness 因果实验（严格固定视口视角与照明不动）**：
       - 将视角调整到一个能清晰看到天光高光斑点的固定角度，**松开鼠标并不再旋转光照与视角**；
       - 先拖动 **`Roughness`** 滑块到 **`0.10`**：观察固定视角下黄色球头表面光斑，高光极其锐利紧凑、边界清晰；
       - 再逐渐拖动 **`Roughness`** 滑块到 **`0.85`**：在同一固定视角下观察，原锐利高光光斑迅速扩散开散为大面积柔和微弱的哑光漫晕（验证微表面粗糙度对光斑展宽的单一因果影响）；
       - 最终将 `Roughness` 设定在 **`0.15`** 作为底层光洁塑料底漆质感。
- **【预期画面 (Expected Screen)】**：
  - 3D 视口中 MeetMat 的整个头部呈现明亮黄色；
  - 固定视角下，Roughness 滑块左右拖动能即时看到高光光斑“聚拢 $\leftrightarrow$ 扩散”的明显反差，且无金属彩色反光。
- **【常见操作卡点 (Gotchas)】**：
  - **卡点 4-A**：误点击了毛笔图标（`Add layer`，添加了普通手绘图层），导致属性调板中没有颜色色块与 Roughness 滑块；
  - **卡点 4-B**：手滑拉动了 `Metallic` 滑块变成 0.5 灰度，导致黄色塑料呈现诡异的灰暗脏感。
- **【最小恢复办法 (Recovery Steps)】**：
  - 若建错图层，直接选中该图层按键盘 `Delete` 键删除，重新认准带“油漆桶”图标的填充层新建；
  - 若 `Metallic` 偏离 0，直接双击输入框手动键入数字 `0` 并回车。
- **【实机门禁标记】**：`RUNTIME REQUIRED`（核验属性面板中通道按钮的即时开关响应）。
- **【教材证据指针】**：`zheng-2024-painter` §2.9.3 填充图层（印刷页 48 / 物理页 58；图 2.81）。

---

### Step 5：建立第二层深色覆盖填充层 (Face Mask Fill Layer)

- **【操作动作 (Action)】**：
  1. 再次点击 `Layers` 调板上方的油漆桶图标，新建第二个填充图层；
  2. 双击图层名重命名为 **`Face_Mask`**；
  3. 在下方属性面板中：
     - 同样关闭 `nrm` 与 `height` 通道；
     - 点击 `baseColor`，将颜色设置为深蓝黑色（接近黑夜，如 RGB: 0.05, 0.08, 0.12）；
     - 将 `Metallic` 保持为 **`0.0`**；
     - 将 `Roughness` 设为 **`0.05`**（比底层更加镜面光亮）。
- **【预期画面 (Expected Screen)】**：
  - 视口中整个 MeetMat 头部被完全覆盖为深蓝黑色，刚才的黄色底层全部被遮挡住；
  - 图层堆栈中 `Face_Mask` 位于 `Plastic_Base` 之上。
- **【常见操作卡点 (Gotchas)】**：
  - **卡点 5-A**：新图层被拖到了 `Plastic_Base` 下方，导致视口看不到任何变化。
- **【最小恢复办法 (Recovery Steps)】**：
  - 鼠标按住 `Face_Mask` 图层向上拖拽，确保其层级位于 `Plastic_Base` 顶层。
- **【实机门禁标记】**：`VERIFIED (图层层叠原理)`。
- **【教材证据指针】**：`zheng-2024-painter` §2.9 图层调板概述（印刷页 46~47 / 物理页 56~57）。

---

### Step 6：挂载黑色遮罩与画笔局部开窗涂抹纠错 (Black Mask & Painting)

- **【操作动作 (Action)】**：
  1. **挂载黑色遮罩**：
     - 在 `Layers` 面板中，用鼠标右键单击 `Face_Mask` 图层；
     - 在弹出的右键上下文菜单中，点击选择 **`Add black mask (添加黑色遮罩)`**；
  2. **画笔开窗涂抹 (白色显现)**：
     - 观察 `Face_Mask` 图层右侧出现一个黑色矩形小方块（且有白色高亮细边框）；
     - 按键盘单键 **`1`**（激活左侧工具栏的 Paint 画笔工具）；
     - 视线移到左下方的属性/画笔面板，确认当前 Grayscale 灰度颜色为 **`1.0 (纯白色)`**；
     - 在 3D 视口中，按住 `Ctrl + 鼠标右键水平拖动` 调节画笔大小至适中（约硬币大小）；
     - 用鼠标左键在 MeetMat 面部平整区域由内向外涂抹出一个平整的面罩轮廓；
  3. **画笔擦除纠错 (黑色遮蔽)**：
     - 故意在面颊边缘多画出一笔造成穿帮；
     - 按键盘单键 **`X`**（切换前景色与背景色，画笔颜色瞬间从白 1.0 变为黑 0.0）；
     - 用黑色画笔涂抹刚才多画的多余边缘，面罩边缘立刻被擦除，重新露出底层的明黄色；
     - 再次按 **`X`** 切回白色画笔，修整面罩轮廓完成。
- **【预期画面 (Expected Screen)】**：
  - 挂载黑遮罩的瞬间，整个头部恢复为黄色；
  - 白色画笔涂抹处，深蓝黑色面罩清晰显现；
  - 按 X 切换黑色画笔后可无损擦除多余笔触，体现出遮罩的“黑透白不透”与可逆纠错特性。
- **【常见操作卡点 (Gotchas)】**：
  - **卡点 6-A**：鼠标选错了图层左侧的材质球本体方块，画笔画在本体上无效或报错；
  - **卡点 6-B**：画笔颜色误设为 0.5 灰度，导致画出来的面罩半透明发灰。
- **【最小恢复办法 (Recovery Steps)】**：
  - 鼠标明确点击图层右侧的**黑色遮罩方块**，确认白边框框在遮罩方块上；
  - 检查属性面板最下方颜色，确保只在纯白 (1.0) 与纯黑 (0.0) 之间切换。
- **【实机门禁标记】**：`RUNTIME REQUIRED`（核验 `Ctrl+右键拖动` 调节笔刷大小与 `X` 键黑白切换在不同系统下的快捷键响应）。
- **【教材证据指针】**：`zheng-2024-painter` §2.9.3 遮罩效果（印刷页 51~54 / 物理页 61~64；图 2.88~2.90）。

---

### Step 7：视口单通道检查与纯净截图保存 (Channel Inspection & Screenshot)

- **【操作动作 (Action)】**：
  1. **单通道物理核验 (快捷键 C / B / M 语义区分)**：
     - 将鼠标指针悬停在 3D 视口上，连续按键盘单键 **`C`**（Channel / 材质通道切换），观察视口左上角显示的通道名称在循环切换：
       - 切到 `BaseColor`：看到黄色底色与深色面罩固有色，表面无任何虚假绘制的高光或阴影；
       - 切到 `Roughness`：看到微观粗糙度灰度图（底层 0.15 偏深灰，面罩 0.05 接近纯黑）；
       - 切到 `Metallic`：看到**完全纯黑的画面 (0.0)**，确认绝无灰度杂质；
     - **特别注意快捷键语义区分**：
       - 单键 **`C`**：循环查看**材质属性通道** (Material Channels: Base Color, Roughness, Metallic, Normal, Height...)；
       - 单键 **`B`**：循环查看**网格烘焙贴图** (Mesh Maps: AO, Curvature, Normal, World Space Normal...)；
       - 单键 **`M`**：返回完整的**复合材质渲染模式** (Material Mode)；
     - 核验完成后，按键盘单键 **`M`**，将视口恢复为完整的 `Material` 渲染视图；
  2. **沉浸式视口切换与截图**：
     - 按键盘单键 **`F2`**：将视口锁定为纯 3D 视口（隐藏可能并排的 2D UV 视口；注：非截图快捷键）；
     - 按键盘 **`Tab`** 键：临时隐藏界面所有侧边调板与工具栏，进入全屏纯净模型视口；
     - 使用键盘截图快捷键（Windows: `Win + Shift + S` 或 `PrintScreen`；macOS: `Cmd + Shift + 4`）截取一张 16:9 高清视口图，保存为 `Slide18_SaveAs_Dialog_And_CleanTab.png`；
     - 再次按 **`Tab`** 键恢复所有操作面板。
- **【预期画面 (Expected Screen)】**：
  - 按 `C` 键通道切换自如，物理通道数值纯净规范；
  - `Tab` 键能迅速一键隐藏全界面杂乱控件，留下清晰展示黄色塑料与深色面罩反光对比的成果图。
- **【常见操作卡点 (Gotchas)】**：
  - **卡点 7-A**：误把快捷键 `F2` 当成截图按钮，等待软件出图无果；
  - **卡点 7-B**：误按 `B` 键切换到了 Mesh Maps 网格贴图视图（如 Curvature/AO），导致画面显示异常；
  - **卡点 7-C**：不知道按 `M` 可以从单通道视口切换回正常材质，卡在黑白通道视图。
- **【最小恢复办法 (Recovery Steps)】**：
  - 误按 `B` 或 `C` 切到单通道时，牢记按字母 **`M`**（Material 缩写），即可瞬间回到正常彩色复合光照材质视口。
- **【实机门禁标记】**：`RUNTIME REQUIRED`（验证目标机房 Windows 系统自带截图快捷键与软件 Tab 全屏交互）。
- **【教材证据指针】**：`zheng-2024-painter` §2.2.1 视图显示模式（印刷页 19 / 物理页 29；图 2.11）。

---

### Step 8：工程规范另存为、彻底退出 Painter 与重启打开核验 (Persistence Lifecycle)

- **【操作动作 (Action)】**：
  1. **规范另存为工程**：
     - 点击菜单 `File -> Save As... (另存为...)`（或按快捷键 `Ctrl + Shift + S`）；
     - 在弹出的文件保存对话框中，定位至测试工作盘（例如 `D:\GR2102_Test\`）；
     - 将工程命名为规范格式：`GR2102_W1_TeacherTest_MeetMat.spp`，点击保存；
     - 观察软件右下角进度条跑完，顶部标题栏显示当前文件名；
  2. **彻底退出 Painter 进程**：
     - 点击右上角红叉 `X` 或点击菜单 `File -> Exit (退出)`；
     - 打开任务管理器（`Ctrl + Shift + Esc`），快速核验 `Adobe Substance 3D Painter.exe` 进程是否已彻底退出，杜绝后台僵尸进程占用显存；
  3. **重启打开核验持久化**：
     - 在文件资源管理器中找到刚才保存的 `GR2102_W1_TeacherTest_MeetMat.spp`；
     - 鼠标双击该文件重新启动 Painter；
     - 核验打开后的工程：
       - ① 3D 视口是否保持刚才绘制的黄色塑料与深色面罩？
       - ② 右上角切换到 `Head`，图层面板中 `Plastic_Base` 与 `Face_Mask`（含黑遮罩）是否完整保留、参数未丢失？
- **【预期画面 (Expected Screen)】**：
  - 工程顺利重开，图层结构、遮罩绘制与物理通道参数 100% 完整复原，没有丢失任何笔触或产生材质损坏。
- **【常见操作卡点 (Gotchas)】**：
  - **卡点 8-A**：保存时未等待进度条走完就强行关机或断电，导致 `.spp` 文件头损坏；
  - **卡点 8-B**：误点击“保存”覆写了软件默认 sample 原文件（若权限不足会报错拒绝访问）。
- **【最小恢复办法 (Recovery Steps)】**：
  - 必须使用 `Save As... (另存为)` 保存到学生专用作业盘，绝不直接覆盖 Sample 目录；若重开弹窗报错或文件大小显示为 0KB 则属保存异常中断；以**成功重新打开工程、图层调板中 `Plastic_Base` 与 `Face_Mask`（含黑遮罩）层级结构及参数完整保留**作为有效验证依据（绝不以文件是否超过 50MB 作为判断标准）。
- **【实机门禁标记】**：`RUNTIME REQUIRED`（机房实机端到端退出与重开持久化探针）。
- **【教材证据指针】**：`zheng-2024-painter` §2.1.3 保存工程（印刷页 17 / 物理页 27）。

---

## 2. 教师试走最小反馈模板 (Minimal Walkthrough Feedback Form)

> **使用说明**：教师完成上述 8 步试走后，仅需花 **3 分钟** 勾选以下简明表格并记录卡点，回传给 Course Owner 或填入 GitHub Issue #40，即可闭环第一讲实操门禁。**无需测满 160 分钟！**

```markdown
### GR2102 第 1 讲教师 GUI 试走反馈报告

1. **测试环境与宿主硬件**：
   - 测试日期：2026-____-____
   - 软件确切版本：Substance 3D Painter 版本号 __________（如 8.3.0 / 9.1.2 / 10.0 等）
   - 操作系统：Windows 10 / 11 / macOS __________
   - 显卡与驱动：NVIDIA RTX __________ (驱动版本：__________)

2. **8 步流程通断核查表**：
| 步骤编号与测试项 | 是否走通 (PASS / CONDITIONAL / FAIL) | 约略耗时 | 现场发现卡点或操作异常说明 |
| :--- | :---: | :---: | :--- |
| Step 1: 载入官方 MeetMat 示例 | [ ] PASS  [ ] COND  [ ] FAIL | ___ min | |
| Step 2: 视口导航与 Shift+右键光照 | [ ] PASS  [ ] COND  [ ] FAIL | ___ min | |
| Step 3: Texture Set 锁定 Head | [ ] PASS  [ ] COND  [ ] FAIL | ___ min | |
| Step 4: 黄色底层塑料与 Roughness | [ ] PASS  [ ] COND  [ ] FAIL | ___ min | |
| Step 5: 第二层深色覆盖填充层 | [ ] PASS  [ ] COND  [ ] FAIL | ___ min | |
| Step 6: 黑色遮罩画笔开窗与 X 纠错 | [ ] PASS  [ ] COND  [ ] FAIL | ___ min | |
| Step 7: C 键通道检查与 Tab 截图 | [ ] PASS  [ ] COND  [ ] FAIL | ___ min | |
| Step 8: 存为 .spp 退出并重开核验 | [ ] PASS  [ ] COND  [ ] FAIL | ___ min | |
| **试走总耗时** | **总计：约 ______ 分钟** | | (仅记录个人操作耗时，不测大班容量) |

3. **需补拍实机高清截图就绪清单 (统一 Shot 01~10 规范编号)**：
   - [ ] Shot 01 (Slide 05 / Step 1: MeetMat 全貌并框出 Head 区域 / `Slide05_MeetMat_Overview.png`)
   - [ ] Shot 02 (Slide 06 / Step 2: Painter 4 大面板界面全览 / `Slide06_Essential_UI_4Panels.png`)
   - [ ] Shot 03 (Slide 07 / Step 2: Shift+右键光照旋转高光位移连拍 / `Slide07_HDRI_Rotation_Demo.jpg`)
   - [ ] Shot 04 (Step 3: Texture Set 锁定 Head 高亮图 / `Step03_TextureSet_Head_Highlight.png`)
   - [ ] Shot 05 (Slide 08 / Step 4: Plastic_Base 填充层黄色属性 / `Slide08_Plastic_Base_FillLayer.png`)
   - [ ] Shot 06 (Slide 09 / Step 4: 固定光照视角下 Roughness 0.1 vs 0.8 对比 / `Slide09_Roughness_HandsOn_SideBySide.png`)
   - [ ] Shot 07 (Slide 10 / Step 6: Black Mask 挂载与白画笔开窗涂抹 / `Slide10_BlackMask_Painting_Demo.png`)
   - [ ] Shot 08 (Slide 11 / Step 6: 遮罩绘制与 X 键修边缘连拍 / `Slide11_Mask_Painting_StepByStep.png`)
   - [ ] Shot 09 (Slide 17 / Step 7: C 键单通道核验 Metallic 纯黑与 BaseColor 对比 / `Slide17_Channel_Inspection_C_Key.png`)
   - [ ] Shot 10 (Slide 18 / Step 7~8: Tab 纯净视口图与 Save As 规范命名弹窗 / `Slide18_SaveAs_Dialog_And_CleanTab.png`)

4. **核心教学决策建议（教师勾选）**：
   - 关于学生开局路径：[ ] 赞成官方原生 MeetMat Sample 从零建层   [ ] 建议教师预置 Starter.spp
   - 关于第 30 分钟动手时机：[ ] 节奏合适，尽早上手体验好   [ ] 觉得仍需前置更多理论
   - 其他现场反馈：________________________________________________________
```

---
*操作卡编制完成，归档于 `docs/research/painter-week1-teacher-gui-walkthrough-guide.md`。*
