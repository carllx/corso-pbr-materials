"""
Week 1 教学资产包确定性构建脚本 (Week 1 Teaching Package Deterministic Rebuild Script)

用途：
从 Poly Haven 官方原版 Vintage Flashlight 资产（1K 分辨率）出发，
确定性重构出符合 Week 1 教学要求的完整资产包 (Option B Scaffolded Shader Editor 方案)：
- Starter: 预置 Slot 2 (vintage_flashlight_body, 1,462面)，预连 Body Color Tint 节点并保持视觉中性开局状态 (Factor=0.0, Color B=(1,1,1,1))，锁定机位与 Material Preview；
- Recovery A: 预连节点的纯净中性开局备份；
- Recovery B: 内置已完成首次材质决策（Multiply 0.85 军绿）的跳关检查点；
- Recovery C & Reference: 统一光照源下的参考工程与效果截图。

使用方式 (在 Blender 5.2 LTS 环境下运行)：
blender -b --python tools/teaching/build_week1_teaching_package.py -- [可选参数]
参数：
--source-dir <path> : 包含官方 vintage_flashlight_1k.blend 与贴图的目录 (默认: .scratch/prototype/vintage_flashlight_1k)
--output-dir <path> : 教学包输出目录 (默认: .scratch/teaching_package_w1)
"""

import sys
import os
import shutil
import argparse
import bpy
import bmesh

def parse_args():
    # 解析 Blender 命令行传递给 Python 的参数（位于 '--' 之后）
    argv = sys.argv
    if "--" in argv:
        argv = argv[argv.index("--") + 1:]
    else:
        argv = []
    
    parser = argparse.ArgumentParser(description="Build Week 1 Teaching Package")
    parser.add_argument("--source-dir", default=".scratch/prototype/vintage_flashlight_1k",
                        help="Path to directory containing official vintage_flashlight_1k.blend and textures")
    parser.add_argument("--output-dir", default=".scratch/teaching_package_w1",
                        help="Path to output teaching package directory")
    return parser.parse_args(argv)

def build_package(source_dir, output_dir):
    source_dir = os.path.abspath(source_dir)
    output_dir = os.path.abspath(output_dir)
    official_blend = os.path.join(source_dir, "vintage_flashlight_1k.blend")
    source_textures = os.path.join(source_dir, "textures")
    if not os.path.exists(source_textures):
        # 兼容贴图直接存放在 source_dir 的情况
        source_textures = source_dir

    assert os.path.exists(official_blend), f"官方原版工程未找到: {official_blend}"

    starter_dir = os.path.join(output_dir, "starter")
    recovery_dir = os.path.join(output_dir, "recovery")
    reference_dir = os.path.join(output_dir, "reference")
    textures_dir = os.path.join(output_dir, "textures")

    for d in [starter_dir, recovery_dir, reference_dir, textures_dir]:
        os.makedirs(d, exist_ok=True)

    starter_blend = os.path.join(starter_dir, "W1_Starter_Vintage_Flashlight.blend")
    recovery_a_blend = os.path.join(recovery_dir, "W1_Recovery_A_Starter.blend")
    recovery_b_blend = os.path.join(recovery_dir, "W1_Recovery_B_Post_Edit.blend")
    reference_blend = os.path.join(reference_dir, "W1_Reference_Result.blend")
    reference_img = os.path.join(reference_dir, "reference_render.png")
    recovery_c_img = os.path.join(recovery_dir, "W1_Recovery_C_Reference_View.png")

    print("=== 开始构建 Week 1 教学资产包 ===")
    print(f"官方输入源: {official_blend}")
    print(f"输出目标目录: {output_dir}")

    # 1. 复制贴图到本地教学包 textures 目录
    expected_textures = [
        "vintage_flashlight_diff_1k.jpg",
        "vintage_flashlight_rough_1k.exr",
        "vintage_flashlight_metal_1k.exr",
        "vintage_flashlight_nor_gl_1k.exr",
        "vintage_flashlight_alpha_1k.png"
    ]
    for tex in expected_textures:
        src_tex = os.path.join(source_textures, tex)
        dst_tex = os.path.join(textures_dir, tex)
        if os.path.exists(src_tex) and not os.path.exists(dst_tex):
            shutil.copyfile(src_tex, dst_tex)
            print(f"复制贴图: {tex}")

    # 2. 打开官方原版工程
    bpy.ops.wm.open_mainfile(filepath=official_blend)
    obj = bpy.data.objects.get('vintage_flashlight')
    assert obj is not None, "未在官方工程中找到 vintage_flashlight 网格对象"

    # 3. 使用 BMesh 确定性识别连通拓扑分量 (Loose Parts)
    bm = bmesh.new()
    bm.from_mesh(obj.data)
    bm.faces.ensure_lookup_table()

    visited_faces = set()
    components = []
    for face in bm.faces:
        if face.index in visited_faces:
            continue
        comp = []
        queue = [face]
        visited_faces.add(face.index)
        while queue:
            curr = queue.pop(0)
            comp.append(curr.index)
            for edge in curr.edges:
                for linked_face in edge.link_faces:
                    if linked_face.index not in visited_faces:
                        visited_faces.add(linked_face.index)
                        queue.append(linked_face)
        components.append(comp)
    bm.free()

    # 提取下底壳 (812面) 与顶盖 (650面)，合计 1,462 面
    shell_comps = [c for c in components if len(c) in (812, 650)]
    assert len(shell_comps) == 2, f"主体外壳部件数量不符: 期望 2 个 (812/650面)，实测 {len(shell_comps)}"
    body_face_indices = set(shell_comps[0] + shell_comps[1])
    assert len(body_face_indices) == 1462, f"主体外壳面数异常: {len(body_face_indices)}"
    print("主体外壳 1,462 面确定性定位成功。")

    # 4. 创建 Slot 2: vintage_flashlight_body
    mat_orig = obj.material_slots[0].material
    mat_body = mat_orig.copy()
    mat_body.name = "vintage_flashlight_body"
    obj.data.materials.append(mat_body)

    for p in obj.data.polygons:
        if p.index in body_face_indices:
            p.material_index = 2

    # 核验面分配
    s0 = sum(1 for p in obj.data.polygons if p.material_index == 0)
    s1 = sum(1 for p in obj.data.polygons if p.material_index == 1)
    s2 = sum(1 for p in obj.data.polygons if p.material_index == 2)
    assert s0 == 3765 and s1 == 56 and s2 == 1462, "材质槽面分配不匹配"
    print(f"材质槽面分配核验 PASS: Slot 0={s0}(受保护机械), Slot 1={s1}(受保护玻璃), Slot 2={s2}(学生编辑区)")

    # 5. 规范观察环境设置 (固定相机与 Material Preview)
    if 'Cam_Obs' not in bpy.data.objects:
        cam_data = bpy.data.cameras.new("Cam_Obs")
        cam_data.lens = 75
        cam_obj = bpy.data.objects.new("Cam_Obs", cam_data)
        bpy.context.scene.collection.objects.link(cam_obj)
        cam_obj.location = (0.28, -0.32, 0.22)
        cam_obj.rotation_euler = (1.15, 0.0, 0.72)
    bpy.context.scene.camera = bpy.data.objects['Cam_Obs']

    # 辅助备用场景阳光 (非规范观察主基准)
    if 'Light_Obs' not in bpy.data.objects:
        light_data = bpy.data.lights.new("Light_Obs", type='SUN')
        light_data.energy = 2.5
        light_obj = bpy.data.objects.new("Light_Obs", light_data)
        bpy.context.scene.collection.objects.link(light_obj)
        light_obj.rotation_euler = (0.8, 0.2, 0.5)

    obj.active_material_index = 2
    bpy.context.scene.render.engine = 'BLENDER_EEVEE'

    def configure_viewport_and_textures():
        # 设置视口首屏默认使用 Material Preview 且锁定相机视角
        for a in bpy.context.screen.areas:
            if a.type == 'VIEW_3D':
                for s in a.spaces:
                    if s.type == 'VIEW_3D':
                        s.shading.type = 'MATERIAL'
                        s.region_3d.view_perspective = 'CAMERA'
        # 修正相对路径
        for img in bpy.data.images:
            if not img.name or img.name == 'Render Result':
                continue
            base = os.path.basename(img.filepath)
            img.filepath = f"//../textures/{base}"
            abs_p = bpy.path.abspath(img.filepath)
            assert os.path.exists(abs_p), f"贴图未找到: {abs_p}"
        bpy.ops.wm.save_mainfile()

    # --- 在 Slot 2 (vintage_flashlight_body) 中预置并连好 Mix Color 调色节点 ---
    nodes = mat_body.node_tree.nodes
    links = mat_body.node_tree.links

    diff_img = [n for n in nodes if n.type == 'TEX_IMAGE' and 'diff' in n.image.name.lower()][0]
    bsdf = [n for n in nodes if n.type == 'BSDF_PRINCIPLED'][0]

    mix_node = nodes.new(type='ShaderNodeMix')
    mix_node.name = "Body_Color_Tint"
    mix_node.label = "Body Color Tint"
    mix_node.data_type = 'RGBA'
    mix_node.blend_type = 'MULTIPLY'
    mix_node.inputs['Factor'].default_value = 0.0
    mix_node.inputs[7].default_value = (1.0, 1.0, 1.0, 1.0) # 中性纯白，初始状态像素级零偏差
    mix_node.location = (bsdf.location.x - 300, bsdf.location.y + 100)

    links.new(diff_img.outputs['Color'], mix_node.inputs[6])
    links.new(mix_node.outputs['Result'], bsdf.inputs['Base Color'])

    # --- 生成 Starter 与 Recovery A (预连节点、中性开局状态) ---
    bpy.ops.wm.save_as_mainfile(filepath=starter_blend)
    configure_viewport_and_textures()
    print(f"已生成 Starter (预连中性节点): {starter_blend}")
    shutil.copyfile(starter_blend, recovery_a_blend)
    print(f"已生成 Recovery A: {recovery_a_blend}")

    # --- 生成 Recovery B (已完成首个材质决策检查点: Multiply 0.85 军绿色) ---
    mix_node.inputs['Factor'].default_value = 0.85
    mix_node.inputs[7].default_value = (0.32, 0.58, 0.22, 1.0) # 军绿色

    bpy.ops.wm.save_as_mainfile(filepath=recovery_b_blend)
    configure_viewport_and_textures()
    print(f"已生成 Recovery B (完成初次决策检查点): {recovery_b_blend}")

    # --- 生成 Reference Result (优化微调后终态: Factor 0.80) ---
    mix_node.inputs['Factor'].default_value = 0.80
    mix_node.inputs[7].default_value = (0.28, 0.62, 0.18, 1.0)

    bpy.ops.wm.save_as_mainfile(filepath=reference_blend)
    configure_viewport_and_textures()
    print(f"已生成 Reference Result: {reference_blend}")

    # --- 渲染生成参考图与 Recovery C 降级图 ---
    # 利用与 Material Preview 相同的 studio/forest 环境 HDRI 提供视觉一致的参考图
    forest_exr = None
    candidates = [
        "/Applications/Blender 5.2.2 LTS.app/Contents/Resources/5.2/datafiles/studiolights/world/forest.exr",
        "/Applications/Blender.app/Contents/Resources/5.2/datafiles/studiolights/world/forest.exr"
    ]
    for c in candidates:
        if os.path.exists(c):
            forest_exr = c
            break

    if forest_exr:
        if 'Light_Obs' in bpy.data.objects:
            bpy.data.objects['Light_Obs'].hide_render = True
        scene = bpy.context.scene
        scene.world.use_nodes = True
        wnodes = scene.world.node_tree.nodes
        wlinks = scene.world.node_tree.links
        wnodes.clear()
        bg = wnodes.new(type='ShaderNodeBackground')
        env = wnodes.new(type='ShaderNodeTexEnvironment')
        env.image = bpy.data.images.load(forest_exr)
        out = wnodes.new(type='ShaderNodeOutputWorld')
        wlinks.new(env.outputs['Color'], bg.inputs['Color'])
        wlinks.new(bg.outputs['Background'], out.inputs['Surface'])

        scene.render.image_settings.file_format = 'PNG'
        scene.render.filepath = reference_img
        bpy.ops.render.render(write_still=True)
        print(f"已渲染参考图: {reference_img}")
        shutil.copyfile(reference_img, recovery_c_img)
        print(f"已生成 Recovery C 降级图: {recovery_c_img}")
    else:
        print("未检测到内置 studio HDRI，跳过离线参考图渲染。")

    print("=== Week 1 教学资产包确定性重构完成 ===")

if __name__ == "__main__":
    args = parse_args()
    build_package(args.source_dir, args.output_dir)
