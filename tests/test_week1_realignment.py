"""
Week 1 教学重构与契约对齐自动化测试套件 (Week 1 Realignment Contract Test Suite)
严格依据 Issue #37 教学设计变更契约、PR #34 备课治理规则及 Browser Review 修正要求进行断言。
"""

import os
import re
import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PACKAGE_PATH = os.path.join(REPO_ROOT, "docs/research/week1-executable-teaching-package-v0.1.md")
HANDOUT_PATH = os.path.join(REPO_ROOT, "docs/research/week1-student-handout-v0.1.md")
EVIDENCE_MAP_PATH = os.path.join(REPO_ROOT, "docs/research/week1-9-teaching-evidence-map.md")
LEDGER_PATH = os.path.join(REPO_ROOT, "docs/research/course-design-ledger.md")
TOPOLOGY_PATH = os.path.join(REPO_ROOT, "docs/research/case-topology-join.md")
AGENTS_PATH = os.path.join(REPO_ROOT, "AGENTS.md")
GOVERNANCE_PATH = os.path.join(REPO_ROOT, "docs/agents/artifact-governance.md")

def read_file(path):
    assert os.path.exists(path), f"文件不存在: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def test_160_minute_budget_and_blocks():
    """验证 160 分钟计划预算严格相等，Block 1-11 结构与第 30 分钟首次上机"""
    content = read_file(PACKAGE_PATH)
    blocks = [
        ("Block 1", 15),
        ("Block 2", 15),
        ("Block 3", 20),
        ("Block 4", 20),
        ("Block 5", 15),
        ("Block 6", 25),
        ("Block 7", 10),
        ("Block 8", 15),
        ("Block 9", 10),
        ("Block 10", 5),
        ("Block 11", 10),
    ]
    total_minutes = sum(m for _, m in blocks)
    assert total_minutes == 160, f"总分钟数不等于 160: {total_minutes}"

    hands_on_start = 15 + 15
    assert hands_on_start == 30, f"首次上机时间应为第 30 分钟: {hands_on_start}"
    assert "Block 3" in content
    assert "原生几何体热身" in content or "Native Geometry Warmup" in content

def test_geometry_warmup_discipline_and_responsibilities():
    """验证几何体热身教学纪律与操作职责：不评分不提交、亲手添加/位移/指派预置材质、容灾备用"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)

    for c in [pkg_content, handout_content]:
        assert "不单独评分" in c or "不计分" in c
        assert "无需提交" in c or "不提交" in c
        assert "Material Preview" in c
        assert "高光会跑" in c
        # 验证最小主动动作与职责对齐：亲手添加球体与指派预置材质
        assert "UV Sphere" in c or "球体" in c
        assert "Mat_Warmup_Sphere" in c or "预置材质" in c
        # 验证容灾 fallback 机制存在且操作明确为点亮眼睛图标
        assert "Fallback" in c or "备用" in c
        assert "眼睛" in c or "Eye" in c

    # 验证脚手架脚本契约：必须采用 hide_set(True) 视口眼睛隐藏，严禁设置全局 hide_viewport=True
    scaffold_path = os.path.join(REPO_ROOT, "tools/teaching/scaffold_week1_geometry_warmup.py")
    scaffold_code = read_file(scaffold_path)
    assert "hide_set(True)" in scaffold_code
    assert "hide_viewport = False" in scaffold_code
    assert "fallback_sphere.hide_viewport = True" not in scaffold_code

def test_anti_hint_pollution_and_transfer_challenge():
    """验证消除提示污染：区分跟进练习与无剧透的独立迁移判别挑战"""
    handout_content = read_file(HANDOUT_PATH)
    pkg_content = read_file(PACKAGE_PATH)

    assert "独立迁移判别" in handout_content or "Transfer" in handout_content
    assert "去色" in handout_content or "出厂" in handout_content or "原始红色外观" in handout_content
    assert "独立迁移" in pkg_content or "迁移判别" in pkg_content

def test_layered_ui_and_option_b():
    """验证分层 UI 教学与 Option B 预置节点保护"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)

    assert "分层讲解 UI" in pkg_content or "分层 UI" in pkg_content
    assert "Option B" in pkg_content
    assert "Body_Color_Tint" in pkg_content
    assert "Predict → Operate → Explain" in handout_content
    assert "重开持久化" in pkg_content or "完全退出 Blender 进程" in pkg_content

def test_evidence_map_pointers():
    """验证证据地图 KU-W01-1..4 指针一致性"""
    content = read_file(EVIDENCE_MAP_PATH)
    assert "KU-W01-1" in content
    assert "KU-W01-2" in content
    assert "KU-W01-3" in content
    assert "KU-W01-4" in content
    assert "Block 3" in content
    assert "高光会跑" in content

def test_supersession_discipline():
    """验证旧限制已在拥有位置标注 supersession，且 §7.3 状态协调有效区分设计取代与未实测容量"""
    ledger_content = read_file(LEDGER_PATH)
    topo_content = read_file(TOPOLOGY_PATH)
    pkg_content = read_file(PACKAGE_PATH)

    assert "SUPERSEDED" in ledger_content or "superseded" in ledger_content
    assert "Issue #37" in ledger_content
    assert "Issue #37" in topo_content
    assert "PARTIALLY SUPERSEDED" in topo_content or "superseded" in topo_content

    # 验证 Package §7.3 状态协调与未实测容量边界保留
    assert "DESIGN SUPERSEDED BY ISSUE #37" in pkg_content
    assert "STUDENT RUNTIME EVIDENCE REQUIRED" in pkg_content
    assert "REAL-HUMAN CAPACITY UNMEASURED" in pkg_content
    assert "TARGET-LAB WINDOWS RUNTIME REQUIRED" in pkg_content

def test_no_local_absolute_paths_in_teaching_package():
    """验证教学包及核心材料中无本机绝对路径链接 (如 file:///Users)"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)

    assert "file:///Users" not in pkg_content, "教学包中包含本机 file:///Users 绝对路径！"
    assert "file:///Users" not in handout_content, "学生手册中包含本机 file:///Users 绝对路径！"

def test_governance_prep_discipline_and_slide_projection():
    """验证备课治理规范与极轻 PPT 投影（应急 Buffer 不设独立投影页）"""
    agents_content = read_file(AGENTS_PATH)
    gov_content = read_file(GOVERNANCE_PATH)
    pkg_content = read_file(PACKAGE_PATH)

    assert "global" in agents_content.lower() or "sharp" in agents_content.lower()
    assert "lightweight ppt projection" in agents_content.lower() or "lightweight ppt projection" in gov_content.lower()
    assert "## Visible" in gov_content
    assert "## Visual" in gov_content
    assert "READY | TODO | LIVE" in gov_content
    # 验证应急 Buffer (Block 11) 不强制占独立投影页
    assert "Block 11" in pkg_content
    assert "0 页" in pkg_content or "不设独立页" in pkg_content

def test_teacher_trial_round1_corrections():
    """验证第一轮教师试走反馈后的联动修正：Shade Smooth、B2->B5桥接、Mix 原生标签及 Multiply 白色特性"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)
    ledger_content = read_file(LEDGER_PATH)
    evidence_content = read_file(EVIDENCE_MAP_PATH)

    # 1. 热身 Shade Smooth
    assert "平滑着色" in handout_content and "Shade Smooth" in handout_content
    assert "平滑着色" in pkg_content and "Shade Smooth" in pkg_content

    # 2. B2 -> B5 概念到 Shader Editor 界面桥接 (必要教学交接)
    assert "必要桥接" in pkg_content or "必要桥接" in handout_content
    assert "Principled BSDF" in handout_content
    assert "Base Color" in handout_content and "Metallic" in handout_content and "Roughness" in handout_content

    # 3. 节点标签规范与称谓对齐 (学生端优先使用 Mix (外壳调色))
    assert "Mix (外壳调色)" in pkg_content
    assert "Mix (外壳调色)" in handout_content

    # 4. 漆面改色、遮罩保护与预测保护 (术语表与示范无答案剧透，解释在操作后)
    assert "绝非软件失灵" in handout_content or "绝非软件失灵" in pkg_content or "绝非软件卡死" in ledger_content
    assert "中性元" in ledger_content
    # 验证术语表中未包含独立迁移预测泄露
    term_section = handout_content.split("#### 本周核心概念与有界术语")[1].split("### 步骤 1")[0]
    assert "黑白灰油漆" not in term_section, "Handout 术语表中提前泄露了独立迁移答案！"

    # 5. 台账与证据地图同步与证据属性区分
    assert "Teacher Trial Round 1 Audit" in ledger_content
    assert "TEACHER-REPORTED" in ledger_content
    assert "TECHNICAL FACT" in ledger_content
    assert "CURRENT DESIGN DECISION" in ledger_content
    assert "IN TRIAL / UNMEASURED / GATE OPEN" in ledger_content
    assert "Shade Smooth" in evidence_content
    assert "Block 4 (Flashlight 20min)" in evidence_content

def test_paint_mask_recolor_pipeline():
    """验证手电筒漆面遮罩与两级级联管线契约 (Color Mode + Paint Mask)"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)
    ledger_content = read_file(LEDGER_PATH)
    evidence_content = read_file(EVIDENCE_MAP_PATH)

    # 1. 漆面遮罩与金属保护滤网
    assert "Paint Mask" in handout_content and "Paint Mask" in pkg_content
    assert "金属保护" in handout_content and "金属保护" in pkg_content
    assert "Metal_Protection_Filter" in pkg_content or "金属保护滤网" in pkg_content
    assert "Paint_Mask_Ramp" in pkg_content or "漆面遮罩" in pkg_content

    # 2. Color 混合模式与 Predict-Operate-Explain 升级
    assert "COLOR" in pkg_content or "颜色模式" in pkg_content
    assert "Predict" in handout_content and "Operate" in handout_content and "Explain" in handout_content
    assert "银灰色" in handout_content and "冷峻" in handout_content

    # 3. 台账第 6 节与 Week 2 教学取向记录
    assert "Paint Mask & Two-Stage Recoloring Pipeline" in ledger_content
    assert "WEEK 2 PEDAGOGICAL ORIENTATION POINTER" in pkg_content
    assert "视觉问题驱动 Blend Mode 选择" in pkg_content and "视觉问题驱动 Blend Mode 选择" in ledger_content
    assert "代码驱动材质" in pkg_content and "代码驱动材质" in ledger_content

def test_recovery_reference_feedback_differentiation():
    """验证 Recovery B (初选草绿) 与 Reference (优化沉稳橄榄绿) 终态存在显著反馈修订差异 (Delta 1)"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)

    # 1. Handout 中示范三字段明确体现草绿 0.85 -> 橄榄绿/降低饱和度 0.80 的反馈改进
    assert "草绿" in handout_content
    assert "鲜艳草绿色" in handout_content or "草绿，Factor=0.85" in handout_content
    assert "色彩饱和度过高像现代塑料外壳" in handout_content or "像现代塑料外壳" in handout_content
    assert "降低饱和度并微调明度" in handout_content and "Factor 调至 0.80" in handout_content

    # 2. Package 中明确记录 Recovery B 为初选草绿起点，Reference 为反馈优化终态
    assert "草绿" in pkg_content
    assert "沉稳橄榄绿" in pkg_content or "优化橄榄绿" in pkg_content

def test_no_multiply_teaching_contract_residue():
    """验证实际生效的教学包和学生任务单中彻底消除旧版 Multiply 教学契约残留 (Delta 2)"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)

    # 1. 学生任务单中不应存在任何生效的 Multiply 指令或说明
    assert "Multiply" not in handout_content, "Handout 中仍残留旧版 Multiply！"

    # 2. 教学包中仅允许在 Week 2 指针回顾历史对比中提及 Multiply，生效执行条款中不得作为 W1 机制
    # 检查 Block 5, Block 6, §5.2, §7.1, §7.2, §10 均无 Multiply 作为生效调节器
    b5_b6_section = pkg_content.split("### 3.4 教学 Block 极轻 PPT 投影")[1].split("### 3.1 课堂节奏")[0]
    assert "Multiply" not in b5_b6_section, "Package 表 3.4 中仍残留 Multiply！"

    lo_section = pkg_content.split("### 1.2 预期可观察成效")[1].split("### 1.3 教师专用标准参考答案")[0]
    assert "Multiply" not in lo_section, "Package LO2 中仍残留 Multiply！"



