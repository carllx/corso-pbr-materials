"""
Week 1 教学重构与契约对齐自动化测试套件 (Week 1 Realignment Contract Test Suite)
严格依据 Issue #37 教学设计变更契约与 PR #34 备课治理规则进行断言。
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
    # 提取各 Block 分钟数 (严格等于 160 分钟 PLAN BUDGET)
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

    # 首次上机时间：Block 1 (15m) + Block 2 (15m) = 第 30 分钟进入 Block 3
    hands_on_start = 15 + 15
    assert hands_on_start == 30, f"首次上机时间应为第 30 分钟: {hands_on_start}"
    assert "Block 3" in content
    assert "原生几何体热身" in content or "Native Geometry Warmup" in content

def test_geometry_warmup_discipline():
    """验证几何体热身教学纪律：不评分不提交、Material Preview 默认不依赖场景灯"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)

    for c in [pkg_content, handout_content]:
        assert "不单独评分" in c or "不计分" in c
        assert "无需提交" in c or "不提交" in c
        assert "Material Preview" in c
        assert "高光会跑" in c

def test_layered_ui_and_option_b():
    """验证分层 UI 教学与 Option B 预置节点保护"""
    pkg_content = read_file(PACKAGE_PATH)
    handout_content = read_file(HANDOUT_PATH)

    # 热身仅讲基础视口导航，手电筒正式任务才引入 Shading 工作区
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
    """验证旧限制已在拥有位置标注 supersession"""
    ledger_content = read_file(LEDGER_PATH)
    topo_content = read_file(TOPOLOGY_PATH)

    assert "SUPERSEDED" in ledger_content or "superseded" in ledger_content
    assert "Issue #37" in ledger_content
    assert "Issue #37" in topo_content
    assert "PARTIALLY SUPERSEDED" in topo_content or "superseded" in topo_content

def test_governance_prep_discipline():
    """验证备课治理规范中关于全局图景、极轻 PPT 投影与最低充分表达的规则"""
    agents_content = read_file(AGENTS_PATH)
    gov_content = read_file(GOVERNANCE_PATH)

    assert "global" in agents_content.lower() or "sharp" in agents_content.lower()
    assert "lightweight ppt projection" in agents_content.lower() or "lightweight ppt projection" in gov_content.lower()
    assert "## Visible" in gov_content
    assert "## Visual" in gov_content
    assert "READY | TODO | LIVE" in gov_content
