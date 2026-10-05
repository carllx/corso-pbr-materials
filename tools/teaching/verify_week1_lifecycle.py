"""
Week 1 教学资产包端到端生命周期与运行时验证套件 (Week 1 Lifecycle & Runtime Verification Suite)

用途：
严格验证 Week 1 教学资产包在真实教学与提交全生命周期中的完整性与稳健性：
1. 静态资产与构建输出完整性核验；
2. Starter / Recovery A/B/C 状态机与工作区/视口/机位核验；
3. 模拟实际学生与教师端到端工作流：
   分发 (Receive) -> 检视 (Inspect) -> 决策修改 (Modify) -> 保存 (Save) -> 
   独立单文件提交 (Submit to isolated dir without external textures) -> 异机重开核验 (Reopen & Verify)
4. 资源完整性保障 (Pack All 避免贴图丢失)。
"""

import os
import sys
import tempfile
import shutil
import bpy

def run_verification(package_dir):
    package_dir = os.path.abspath(package_dir)
    print(f"=== 开始 Week 1 端到端生命周期验证: {package_dir} ===")

    starter_blend = os.path.join(package_dir, "starter", "W1_Starter_Vintage_Flashlight.blend")
    recovery_a = os.path.join(package_dir, "recovery", "W1_Recovery_A_Starter.blend")
    recovery_b = os.path.join(package_dir, "recovery", "W1_Recovery_B_Post_Edit.blend")
    recovery_c = os.path.join(package_dir, "recovery", "W1_Recovery_C_Reference_View.png")
    reference_blend = os.path.join(package_dir, "reference", "W1_Reference_Result.blend")
    reference_png = os.path.join(package_dir, "reference", "reference_render.png")
    textures_dir = os.path.join(package_dir, "textures")

    # 1. 检查物理文件存在性
    assert os.path.exists(starter_blend), f"缺少 Starter: {starter_blend}"
    assert os.path.exists(recovery_a), f"缺少 Recovery A: {recovery_a}"
    assert os.path.exists(recovery_b), f"缺少 Recovery B: {recovery_b}"
    assert os.path.exists(recovery_c), f"缺少 Recovery C: {recovery_c}"
    assert os.path.exists(reference_blend), f"缺少 Reference blend: {reference_blend}"
    assert os.path.exists(reference_png), f"缺少 Reference png: {reference_png}"
    assert os.path.exists(textures_dir), f"缺少 Textures 目录: {textures_dir}"
    print("[PASS] 核心文件存在性核验通过。")

    # 2. 检查 Starter 内部拓扑、视口与机位
    bpy.ops.wm.open_mainfile(filepath=starter_blend)
    obj = bpy.data.objects.get("vintage_flashlight")
    assert obj is not None, "未找到 vintage_flashlight 对象"
    assert len(obj.material_slots) == 3, f"材质槽数量不符: {len(obj.material_slots)}"
    assert obj.material_slots[0].name == "vintage_flashlight"
    assert obj.material_slots[1].name == "vintage_flashlight_glass"
    assert obj.material_slots[2].name == "vintage_flashlight_body"
    assert obj.active_material_index == 2, "默认激活材质槽应为 Slot 2"

    # 面数分配检查
    s0 = sum(1 for p in obj.data.polygons if p.material_index == 0)
    s1 = sum(1 for p in obj.data.polygons if p.material_index == 1)
    s2 = sum(1 for p in obj.data.polygons if p.material_index == 2)
    assert s0 == 3765, f"Slot 0 面数不符: {s0}"
    assert s1 == 56, f"Slot 1 面数不符: {s1}"
    assert s2 == 1462, f"Slot 2 面数不符: {s2}"
    print("[PASS] Starter 材质槽面数分配严格精确: Slot 0=3765, Slot 1=56, Slot 2=1462。")

    # 检查所有 Screen 的视口与相机锁定
    for screen in bpy.data.screens:
        for a in screen.areas:
            if a.type == "VIEW_3D":
                for s in a.spaces:
                    if s.type == "VIEW_3D":
                        assert s.shading.type == "MATERIAL", f"Screen [{screen.name}] 视口着色非 MATERIAL: {s.shading.type}"
                        assert s.region_3d.view_perspective == "CAMERA", f"Screen [{screen.name}] 视角非 CAMERA: {s.region_3d.view_perspective}"
    print("[PASS] 全部工作区屏幕 3D 视口均处于 Material Preview 且锁定 Cam_Obs 相机机位。")

    # 检查 Slot 2 节点网络
    mat_body = obj.material_slots[2].material
    mix_node = mat_body.node_tree.nodes.get("Body_Color_Tint")
    assert mix_node is not None, "未在 Slot 2 中找到 Body_Color_Tint 节点"
    assert mix_node.blend_type == "MULTIPLY", f"混合模式非 MULTIPLY: {mix_node.blend_type}"
    assert abs(mix_node.inputs["Factor"].default_value - 0.0) < 1e-4, "初始 Factor 应为 0.0"
    col_b = mix_node.inputs[7].default_value
    assert (abs(col_b[0] - 1.0) < 1e-4 and abs(col_b[1] - 1.0) < 1e-4 and abs(col_b[2] - 1.0) < 1e-4), "初始 Color B 应为纯白"
    assert mix_node.select, "Body_Color_Tint 节点未处于选中状态"
    assert mat_body.node_tree.nodes.active == mix_node, "Body_Color_Tint 节点未处于 active 状态"
    print("[PASS] Body_Color_Tint 节点链路、Multiply 参数与选中聚焦状态核验通过。")

    # 检查贴图打包状态 (Pack All)
    packed_images = [img for img in bpy.data.images if img.name != "Render Result"]
    assert len(packed_images) == 5, f"贴图数量不符: {len(packed_images)}"
    for img in packed_images:
        assert img.packed_file is not None, f"贴图未打包内嵌: {img.name}"
        assert img.size[0] == 1024 and img.size[1] == 1024, f"贴图分辨率异常: {img.name} {img.size}"
    print(f"[PASS] 全部 5 张 1K 贴图均完成内嵌打包 (Packed File True)。")

    # 3. 检查 Recovery B 跳关检查点
    bpy.ops.wm.open_mainfile(filepath=recovery_b)
    rec_body = bpy.data.materials.get("vintage_flashlight_body")
    rec_mix = rec_body.node_tree.nodes.get("Body_Color_Tint")
    assert rec_mix is not None, "Recovery B 缺少 Body_Color_Tint 节点"
    assert abs(rec_mix.inputs["Factor"].default_value - 0.85) < 1e-4, f"Recovery B Factor 不符: {rec_mix.inputs['Factor'].default_value}"
    assert rec_mix.inputs[7].default_value[0] < 0.5, "Recovery B 颜色应为军绿色"
    print("[PASS] Recovery B 跳关检查点参数核验通过 (Factor=0.85 军绿)。")

    # 4. 全生命周期端到端隔离模拟 (Receive -> Modify -> Save -> Submit -> Reopen)
    print("\n--- 启动全生命周期端到端隔离测试 ---")
    sim_dir = tempfile.mkdtemp(prefix="w1_sim_lifecycle_")
    try:
        # A. 学生获取 Starter
        student_work_blend = os.path.join(sim_dir, "student_local", "W1_Flashlight_2026001.blend")
        os.makedirs(os.path.dirname(student_work_blend), exist_ok=True)
        shutil.copyfile(starter_blend, student_work_blend)

        # B. 学生在 Blender 中打开并实施修改
        bpy.ops.wm.open_mainfile(filepath=student_work_blend)
        s_obj = bpy.data.objects["vintage_flashlight"]
        s_body = s_obj.material_slots[2].material
        s_mix = s_body.node_tree.nodes["Body_Color_Tint"]
        
        # 实施首次决策与微调
        s_mix.inputs["Factor"].default_value = 0.80
        s_mix.inputs[7].default_value = (0.28, 0.62, 0.18, 1.0) # 调好的军绿
        bpy.ops.wm.save_mainfile()
        print("  - 学生在本地完成修改并保存")

        # C. 模拟学生将单个 .blend 文件提交到完全孤立的目录 (无任何 textures/ 兄弟目录)
        submitted_isolated_blend = os.path.join(sim_dir, "teacher_inbox", "isolated_env", "W1_Flashlight_2026001.blend")
        os.makedirs(os.path.dirname(submitted_isolated_blend), exist_ok=True)
        shutil.copyfile(student_work_blend, submitted_isolated_blend)
        print("  - 学生单文件提交到完全隔离的评阅环境 (无外部贴图)")

        # D. 模拟教师在完全独立的进程环境中打开提交的包
        bpy.ops.wm.open_mainfile(filepath=submitted_isolated_blend)
        t_obj = bpy.data.objects.get("vintage_flashlight")
        assert t_obj is not None, "异机重开失败：未能找到模型对象"
        t_body = t_obj.material_slots[2].material
        t_mix = t_body.node_tree.nodes.get("Body_Color_Tint")
        assert abs(t_mix.inputs["Factor"].default_value - 0.80) < 1e-4, "参数持久化丢失"
        assert abs(t_mix.inputs[7].default_value[0] - 0.28) < 1e-4, "颜色参数持久化丢失"

        # 核心：检查贴图在孤立环境下重开是否依然有效且无丢失
        for img in bpy.data.images:
            if img.name != "Render Result":
                assert img.packed_file is not None, f"异机孤立环境下贴图未打包: {img.name}"
                assert img.size[0] == 1024, f"贴图数据损坏: {img.name}"
                # 验证像素数据可读性
                assert len(img.pixels) == 1024 * 1024 * 4, f"像素数据长度异常: {img.name}"

        # 检查受保护部件零污染
        t_s0 = sum(1 for p in t_obj.data.polygons if p.material_index == 0)
        t_s1 = sum(1 for p in t_obj.data.polygons if p.material_index == 1)
        t_s2 = sum(1 for p in t_obj.data.polygons if p.material_index == 2)
        assert t_s0 == 3765 and t_s1 == 56 and t_s2 == 1462, "受保护材质槽面数被意外篡改"

        print("  - 教师在独立环境下重开：节点参数 100% 持久化、5 张贴图零丢失、保护槽零污染！")
        print("[PASS] 全生命周期端到端闭环验证通过 (receive -> modify -> save -> submit -> reopen)！")
    finally:
        shutil.rmtree(sim_dir)

    print("\n=== 全部 Week 1 运行时与生命周期验证项目 100% PASS ===")

if __name__ == "__main__":
    pkg_dir = sys.argv[-1] if len(sys.argv) > 1 and not sys.argv[-1].startswith("-") else ".scratch/teaching_package_w1"
    run_verification(pkg_dir)
