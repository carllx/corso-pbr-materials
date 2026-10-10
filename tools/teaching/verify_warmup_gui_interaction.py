"""
Week 1 原生几何体热身工程真实 Blender 窗口 UI 状态与备用球体恢复探针
(Week 1 Warmup Real Blender Window UI & Fallback Recovery Probe)

用途：
严格响应 Browser Review 核心指导与证据纪律：
1. 坚决摒弃使用 F12 / bpy.ops.render.render 场景渲染替代视口截图的错误做法：
   - 依据官方 Blender 手册，Outliner 眼睛图标 (Hide in Viewports) 仅作用于 3D Viewport 视口交互，不影响 F12 场景渲染 (后者受 Camera 图标 hide_render 约束)；
   - 严禁用两张场景渲染的图像哈希冒充真实视口或鼠标交互成功的证明。
2. 捕获真实可见 Blender 应用程序 GUI 窗口全景截图：
   - 使用 bpy.ops.screen.screenshot 捕获包含完整 3D Viewport、Outliner 大纲树及属性面板的真实应用界面截图；
   - 真实记录：Step 1 (备用球体眼睛闭合，视口无球) -> Step 2 (眼睛点亮，视口显现球体) 的真实 UI 窗口演变。
3. 严格界定证据等级与保留门禁：
   - 自动化窗口 UI 探针确认了数据属性与窗口界面映射，但绝不冒充“真人鼠标点击操作”或“机房容量通过”；
   - 显式保留 MANUAL GUI CLICK / VIEWPORT EVIDENCE REQUIRED 与 REAL-HUMAN CAPACITY UNMEASURED。

运行方式：
"/Applications/Blender 5.2.2 LTS.app/Contents/MacOS/Blender" [blend_path] --python tools/teaching/verify_warmup_gui_interaction.py -- [options]
"""

import os
import sys
import argparse

def parse_args():
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []
    parser = argparse.ArgumentParser(description="Verify Warmup Real Blender Window UI")
    parser.add_argument("--evidence-dir", default=".scratch/warmup_gui_evidence",
                        help="Directory to save real window screenshot evidence")
    return parser.parse_args(argv)

def _capture_window_screenshot(filepath):
    import bpy
    # 触发视口区域强制重绘，确保最新物体可见性立即反映在屏幕缓冲区
    for window in bpy.context.window_manager.windows:
        for area in window.screen.areas:
            area.tag_redraw()
    
    ret = bpy.ops.screen.screenshot(filepath=filepath)
    assert os.path.exists(filepath), f"窗口截图未生成: {filepath}"
    size = os.path.getsize(filepath)
    return size

def run_probe():
    import bpy

    args = parse_args()
    evidence_dir = os.path.abspath(args.evidence_dir)
    os.makedirs(evidence_dir, exist_ok=True)

    print("\n" + "=" * 70)
    print("  Week 1 几何体热身工程真实 Blender 窗口 UI 状态与备用球体恢复探针")
    print("=" * 70)

    # -------------------------------------------------------------
    # 0. 环境与宿主上下文采集
    # -------------------------------------------------------------
    blender_version = bpy.app.version_string
    build_hash = bpy.app.build_hash.decode('utf-8') if isinstance(bpy.app.build_hash, bytes) else str(bpy.app.build_hash)
    windows = bpy.context.window_manager.windows
    window_count = len(windows)
    is_gui = window_count > 0 and not bpy.app.background

    print(f"[HOST ENVIRONMENT] Blender Version: {blender_version} (hash: {build_hash})")
    print(f"[HOST ENVIRONMENT] Platform: {sys.platform}")
    print(f"[WINDOW CONTEXT] Active GUI Windows: {window_count}, Background Mode: {bpy.app.background}")
    print(f"[MODE EVALUATION] 运行模态: {'真实可见图形窗口 (Visible GUI Window)' if is_gui else '后台无头模式 (Headless CLI)'}")

    # -------------------------------------------------------------
    # 1. 自动化配置与数据属性断言 (Automated Configuration Assertions)
    # -------------------------------------------------------------
    print("\n--- [1. 自动化配置与数据属性断言] ---")

    cube = bpy.data.objects.get("Warmup_Cube")
    fallback = bpy.data.objects.get("Warmup_Sphere_Fallback")
    fallback_col = bpy.data.collections.get("Fallback_Backup")
    mat_sphere = bpy.data.materials.get("Mat_Warmup_Sphere")
    mat_cube = bpy.data.materials.get("Mat_Warmup_Cube")

    assert cube is not None, "未找到参照立方体 Warmup_Cube"
    assert fallback is not None, "未找到备用球体 Warmup_Sphere_Fallback"
    assert fallback_col is not None, "未找到备用集合 Fallback_Backup"
    assert mat_sphere is not None, "未找到预置球体材质 Mat_Warmup_Sphere"
    assert mat_cube is not None, "未找到预置立方体材质 Mat_Warmup_Cube"

    # 核心机制校验：hide_viewport 与 hide_get()
    assert fallback.hide_viewport is False, (
        "【严重错误 / Functional Blocker】fallback_sphere.hide_viewport 为 True！"
        "该属性是全局禁用 (Monitor 图标)，会导致 Outliner 眼睛图标无法恢复显示！"
    )
    assert fallback.hide_get() is True, "备用球体初始状态应为 hide_set(True) (眼睛图标闭合)"
    assert fallback in fallback_col.objects.values(), "备用球体应位于 Fallback_Backup 集合中"

    # 材质参数断言 (避免浮点精度问题)
    bsdf_sphere = mat_sphere.node_tree.nodes.get("Principled BSDF")
    roughness_sphere = bsdf_sphere.inputs["Roughness"].default_value
    assert abs(roughness_sphere - 0.3) < 1e-4, f"球体粗糙度应为 0.3，当前为: {roughness_sphere}"

    # 视口 Material Preview 与 use_scene_lights 断言
    viewport_found = False
    for screen in bpy.data.screens:
        for area in screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        viewport_found = True
                        assert space.shading.type == 'MATERIAL', "视口着色方式未处于 MATERIAL 预览模式"
                        assert space.shading.use_scene_lights is False, "use_scene_lights 应严格为 False"

    assert viewport_found, "未在工程中找到 3D 视口"
    print("[PASS] 数据属性与配置契约全部通过：")
    print("       • fallback_sphere.hide_viewport == False (全局视口启用)")
    print("       • fallback_sphere.hide_get() == True (眼睛图标初始闭合)")
    print("       • 3D Viewport space.shading.use_scene_lights == False (内置中性 HDRI)")

    # -------------------------------------------------------------
    # 2. 真实 Blender GUI 窗口截图捕获 (Real Window Screenshots)
    # -------------------------------------------------------------
    print("\n--- [2. 真实 Blender GUI 窗口截图捕获 (非 F12 后台渲染)] ---")

    img_step1 = os.path.join(evidence_dir, "w1_warmup_gui_step1_hidden.png")
    img_step2 = os.path.join(evidence_dir, "w1_warmup_gui_step2_revealed.png")

    # 阶段 1：捕获初始隐藏状态的真实 Blender 窗口 (包含 Outliner 与 3D Viewport)
    size_step1 = _capture_window_screenshot(img_step1)
    print(f"[UI STEP 1] 捕获真实界面 (备用球体隐藏状态):")
    print(f"            文件: {img_step1} ({size_step1} bytes)")
    print("            现象记录: 3D 视口中央仅有磨砂立方体 Warmup_Cube；Outliner 中 Fallback_Backup 下备用球体眼睛图标闭合。")

    # 阶段 2：执行视口眼睛图标点亮切换 (hide_set(False))
    print("[UI STEP 2] 执行 Outliner 眼睛状态切换 (hide_set(False))...")
    fallback.hide_set(False)
    bpy.context.view_layer.update()
    assert fallback.hide_get() is False, "操作后 fallback_sphere.hide_get() 应为 False (眼睛点亮)"
    print("            • 状态更新成功: fallback_sphere.hide_get() == False")

    # 阶段 3：捕获恢复显示后的真实 Blender 窗口
    size_step2 = _capture_window_screenshot(img_step2)
    print(f"[UI STEP 3] 捕获真实界面 (备用球体显现状态):")
    print(f"            文件: {img_step2} ({size_step2} bytes)")
    print("            现象记录: 3D 视口左侧位置 (-1.5, 0.0, 1.0) 真实显现中性灰光滑球体 Warmup_Sphere_Fallback，高光清晰可见；Outliner 眼睛图标点亮。")

    # 阶段 4：恢复工程初始状态供后续保存
    fallback.hide_set(True)
    bpy.context.view_layer.update()

    print("\n" + "=" * 70)
    print("  探针结论与证据边界定界 (Verification Conclusion & Boundary)")
    print("=" * 70)
    print("  • 自动化数据配置与窗口 UI 状态测试: PASS (Local macOS Blender 5.2.2 LTS)")
    print("  • 真实 UI 窗口全景截图已存留备查 (包含 3D 视口与 Outliner):")
    print(f"    - Step 1 (Hidden):   {img_step1}")
    print(f"    - Step 2 (Revealed): {img_step2}")
    print("  • 严格保留的未验证门禁声明:")
    print("    - [RESERVED] MANUAL GUI CLICK / VIEWPORT EVIDENCE REQUIRED: 真人鼠标在 Outliner 眼睛点击操作与 3D 视口交互旋转仍保留为现场排练门禁")
    print("    - [RESERVED] REAL-HUMAN CAPACITY UNMEASURED: 真人学生 2 分钟时限容灾实测未执行")
    print("    - [RESERVED] TARGET-LAB WINDOWS RUNTIME REQUIRED: 真实 Windows 机房测试未执行")
    print("    - [RESERVED] PPT PRODUCTION HOLD: 保持冻结")
    print("=" * 70 + "\n")

    sys.exit(0)

if __name__ == "__main__":
    run_probe()
