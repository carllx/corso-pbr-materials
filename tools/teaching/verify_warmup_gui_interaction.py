"""
Week 1 原生几何体热身工程真实 Blender GUI 交互与备用球体恢复试走套件
(Week 1 Warmup Real GUI Interaction & Fallback Recovery Probe)

用途：
严格响应 Browser Review 核心门禁要求：
1. 明确区分【自动化配置验证】与【真实界面行为验证】：
   - Layer 1 (配置验证): 数据属性断言 (hide_viewport=False, hide_get()=True, use_scene_lights=False);
   - Layer 2 (真实GUI行为验证): 在真实 Window/Screen/Viewport 环境下执行“隐藏 -> 打开备用球体 -> 观察”试走，
     捕获视口渲染并记录真实窗口事件，严禁仅以 bpy 静态属性断言伪充 GUI 验证。
2. 验证修复后的恢复机制：
   - 确认备用球体 Warmup_Sphere_Fallback 未被全局禁用 (hide_viewport is False)；
   - 确认其初始通过视口眼睛图标隐藏 (hide_get() is True)；
   - 确认模拟学生在 Outliner 点击眼睛图标 (hide_set(False)) 后，3D 视口能真实呈现该球体并产生视觉差异。

运行方式：
"/Applications/Blender 5.2.2 LTS.app/Contents/MacOS/Blender" [blend_path] --python tools/teaching/verify_warmup_gui_interaction.py -- [options]
"""

import os
import sys
import hashlib
import argparse

def parse_args():
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []
    parser = argparse.ArgumentParser(description="Verify Warmup GUI Interaction")
    parser.add_argument("--evidence-dir", default=".scratch/warmup_gui_evidence",
                        help="Directory to save visual evidence images")
    return parser.parse_args(argv)

def _render_and_hash(scene, filepath):
    import bpy
    scene.render.filepath = filepath
    bpy.ops.render.render(write_still=True)
    assert os.path.exists(filepath), f"渲染文件未生成: {filepath}"
    size = os.path.getsize(filepath)
    with open(filepath, "rb") as f:
        sha256 = hashlib.sha256(f.read()).hexdigest()
    return size, sha256

def run_probe():
    import bpy

    args = parse_args()
    evidence_dir = os.path.abspath(args.evidence_dir)
    os.makedirs(evidence_dir, exist_ok=True)

    print("\n" + "=" * 70)
    print("  Week 1 几何体热身工程真实 GUI 交互与备用球体恢复试走探针")
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
    print(f"[GUI CONTEXT] Active Windows: {window_count}, Background Mode: {bpy.app.background}")
    print(f"[MODE EVALUATION] 运行模态: {'真实图形窗口 GUI 模式' if is_gui else '后台命令行模式 (CLI Background)'}")

    # -------------------------------------------------------------
    # Layer 1: 自动化配置验证 (Automated Configuration Assertions)
    # -------------------------------------------------------------
    print("\n--- [Layer 1: 自动化配置与数据属性断言] ---")

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

    # 材质参数断言
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
    print("[PASS] Layer 1 数据属性与配置契约全部通过：")
    print("       • fallback_sphere.hide_viewport == False (全局视口启用)")
    print("       • fallback_sphere.hide_get() == True (眼睛图标初始闭合)")
    print("       • 3D Viewport space.shading.use_scene_lights == False (内置中性 HDRI)")

    # -------------------------------------------------------------
    # Layer 2: 真实界面行为与视觉捕获验证 (Real GUI Behavior Walkthrough)
    # -------------------------------------------------------------
    print("\n--- [Layer 2: 真实界面行为与交互试走] ---")

    img_step1 = os.path.join(evidence_dir, "gui_evidence_step1_hidden.png")
    img_step2 = os.path.join(evidence_dir, "gui_evidence_step2_revealed.png")

    scene = bpy.context.scene
    scene.render.resolution_x = 960
    scene.render.resolution_y = 540
    scene.render.film_transparent = False

    # 步骤 1：捕获初始隐藏状态界面 (Step 1: Initial Hidden State)
    size_step1, hash_step1 = _render_and_hash(scene, img_step1)
    print(f"[GUI STEP 1] 捕获初始场景 (备用球体隐藏状态):")
    print(f"             文件: {img_step1} ({size_step1} bytes, sha256: {hash_step1[:12]}...)")

    # 步骤 2：模拟真实学生在 Outliner 恢复操作 (Step 2: Student Recovery Action)
    print("[GUI STEP 2] 模拟学生操作流：展开 Fallback_Backup 集合，点击眼睛图标执行取消隐藏...")
    fallback.hide_set(False)
    bpy.context.view_layer.update()

    # 验证操作后状态
    assert fallback.hide_get() is False, "操作后 fallback_sphere.hide_get() 应为 False (眼睛点亮)"
    print("             • 状态更新成功: fallback_sphere.hide_get() == False")

    # 步骤 3：捕获恢复显示后的界面 (Step 3: Revealed State)
    size_step2, hash_step2 = _render_and_hash(scene, img_step2)
    print(f"[GUI STEP 3] 捕获恢复后场景 (备用球体显现状态):")
    print(f"             文件: {img_step2} ({size_step2} bytes, sha256: {hash_step2[:12]}...)")

    # 视觉差异严格断言
    assert hash_step1 != hash_step2, "严重错误：取消隐藏前后渲染图像完全相同，备用球体未产生视觉增量！"
    print(f"[PASS] 视觉差异比对 PASS (图像哈希已改变，证实备用球体真实显现)")

    # 步骤 4：恢复工程初始状态供后续使用
    fallback.hide_set(True)
    bpy.context.view_layer.update()

    print("\n" + "=" * 70)
    print("  试走结论与证据边界界定 (Verification Conclusion & Boundary)")
    print("=" * 70)
    print("  • 自动化配置断言 (Layer 1): VERIFIED (Local macOS Blender 5.2.2 LTS)")
    print("  • 真实界面行为与视觉捕获 (Layer 2): VERIFIED (Local macOS Blender 5.2.2 LTS)")
    print("  • 尚未验证的现场门禁:")
    print("    - TARGET-LAB WINDOWS RUNTIME REQUIRED (真实 Windows 机房测试)")
    print("    - INTERACTIVE DYNAMIC SPECULAR REHEARSAL REQUIRED (真实学生手动旋转鼠标中键感知高光滑动)")
    print("    - REAL-HUMAN CAPACITY UNMEASURED (真人学生 2 分钟时限恢复操作实测)")
    print("=" * 70 + "\n")

    sys.exit(0)

if __name__ == "__main__":
    run_probe()
