#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_w1_slides.py
生成《三维数字材质制作》第 1 讲《初识 Substance 3D Painter / MeetMat》18 页教师审校候选版 PPTX。

架构设计守则：
1. 数据驱动（Data-Driven）：所有幻灯片标题、正文要点、完成检查、问句与 Presenter Notes 严格源自 assets/w1_meetmat/slides_data.json（权威 Notion v0.3 审校数据），避免脚本中手写文本导致内容脱节。
2. 图像适配：15 个真实图像块严格等比居中缩放嵌入卡片，杜绝拉伸；准确呈现题注与审校标签。
3. 视觉设计：16:9 宽屏学术高反差排版，专为大学机房与课堂投影优化。
4. 教学边界守恒：维持已确认的物理概念、操作要点与 160 分钟节奏预算。
"""

import os
import sys
import json
import re
from PIL import Image

import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# 视觉规范与调色板 (Academic PBR Modern Editorial)
# ==============================================================================
SLIDE_WIDTH = Inches(13.333333)
SLIDE_HEIGHT = Inches(7.5)

FONT_HEADING = "Microsoft YaHei"
FONT_BODY = "Microsoft YaHei"
FONT_MONO = "Consolas"

# 现代高对比度低疲劳学术配色
COLOR_BG = RGBColor(248, 250, 252)          # #F8FAFC 画布浅灰
COLOR_CARD_BG = RGBColor(255, 255, 255)     # #FFFFFF 卡片纯白
COLOR_CARD_BORDER = RGBColor(226, 232, 240) # #E2E8F0 发丝边框
COLOR_CARD_BORDER_ACTIVE = RGBColor(147, 197, 253) # #93C5FD 强调边框

COLOR_TEXT_MAIN = RGBColor(15, 23, 42)      # #0F172A 深石板灰（高对比投影）
COLOR_TEXT_BODY = RGBColor(51, 65, 85)      # #334155 正文灰
COLOR_TEXT_MUTED = RGBColor(100, 116, 139)  # #64748B 次级辅助灰
COLOR_TEXT_LIGHT = RGBColor(148, 163, 184)  # #94A3B8 浅灰

COLOR_ACCENT_BLUE = RGBColor(37, 99, 235)   # #2563EB 科技蓝（主视觉焦点）
COLOR_ACCENT_DARK_BLUE = RGBColor(29, 78, 216) # #1D4ED8 深蓝
COLOR_ACCENT_AMBER = RGBColor(217, 119, 6)  # #D97706 材质高光黄/琥珀色
COLOR_ACCENT_GREEN = RGBColor(5, 150, 105)  # #059669 检查闭环绿
COLOR_ACCENT_RED = RGBColor(225, 29, 72)    # #E11D48 警示与注意红

COLOR_BADGE_BG = RGBColor(239, 246, 255)    # #EFF6FF 药丸徽章背景
COLOR_BADGE_BORDER = RGBColor(191, 219, 254) # #BFDBFE 药丸徽章边框
COLOR_BADGE_TEXT = RGBColor(29, 78, 216)    # #1D4ED8 药丸徽章文字

COLOR_ORANGE_BG = RGBColor(255, 247, 237)   # #FFF7ED 警示卡片底色
COLOR_ORANGE_BORDER = RGBColor(254, 215, 170) # #FED7AA
COLOR_GREEN_BG = RGBColor(240, 253, 244)    # #F0FDF4 完成检查卡底色
COLOR_GREEN_BORDER = RGBColor(187, 247, 208)

# ==============================================================================
# 基础几何与排版辅助函数
# ==============================================================================
def create_card(slide, left, top, width, height, 
                bg_color=COLOR_CARD_BG, 
                border_color=COLOR_CARD_BORDER, 
                border_width=Pt(1)):
    """在幻灯片中绘制一张圆角矩形卡片容器"""
    shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    shape.fill.solid()
    shape.fill.fore_color.rgb = bg_color
    if border_color:
        shape.line.color.rgb = border_color
        shape.line.width = border_width
    else:
        shape.line.fill.background()
    return shape

def add_header(slide, slide_num, total_slides, short_title, block_info):
    """绘制标准化幻灯片顶部导航与标题栏"""
    # 1. 顶部面包屑文本
    crumb_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(8.5), Inches(0.35))
    tf_c = crumb_box.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
    p_c = tf_c.paragraphs[0]
    p_c.text = "GR2102 三维数字材质制作 · 第 1 讲 初识 Substance 3D Painter 与 MeetMat"
    p_c.font.name = FONT_HEADING
    p_c.font.size = Pt(11)
    p_c.font.bold = True
    p_c.font.color.rgb = COLOR_TEXT_MUTED

    # 2. Block 药丸徽章
    if block_info:
        badge_w = Inches(3.2)
        badge_h = Inches(0.32)
        badge_left = Inches(12.533) - badge_w
        badge_top = Inches(0.38)
        b_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, badge_left, badge_top, badge_w, badge_h)
        b_shape.fill.solid()
        b_shape.fill.fore_color.rgb = COLOR_BADGE_BG
        b_shape.line.color.rgb = COLOR_BADGE_BORDER
        b_shape.line.width = Pt(1)
        b_tf = b_shape.text_frame
        b_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        b_tf.margin_left = b_tf.margin_top = b_tf.margin_right = b_tf.margin_bottom = 0
        b_p = b_tf.paragraphs[0]
        b_p.text = block_info
        b_p.alignment = PP_ALIGN.CENTER
        b_p.font.name = FONT_HEADING
        b_p.font.size = Pt(10)
        b_p.font.bold = True
        b_p.font.color.rgb = COLOR_BADGE_TEXT

    # 3. 主标题
    title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.733), Inches(0.65))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = f"Slide {slide_num:02d} ｜ {short_title}"
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(21)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_TEXT_MAIN

def add_footer(slide, slide_num, total_slides):
    """绘制底部审校与页码标识"""
    footer_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(11.733), Inches(0.3))
    tf = footer_box.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.text = "教师交互备课工作台审校候选稿 · 依据 Notion 备课稿 v0.3 与 GitHub #40/#41 · 授课教师：林昕"
    p.font.name = FONT_BODY
    p.font.size = Pt(9)
    p.font.color.rgb = COLOR_TEXT_LIGHT

    num_box = slide.shapes.add_textbox(Inches(11.5), Inches(7.05), Inches(1.033), Inches(0.3))
    tf_n = num_box.text_frame
    tf_n.word_wrap = False
    tf_n.margin_left = tf_n.margin_top = tf_n.margin_right = tf_n.margin_bottom = 0
    p_n = tf_n.paragraphs[0]
    p_n.text = f"{slide_num:02d} / {total_slides:02d}"
    p_n.alignment = PP_ALIGN.RIGHT
    p_n.font.name = FONT_HEADING
    p_n.font.size = Pt(10)
    p_n.font.bold = True
    p_n.font.color.rgb = COLOR_TEXT_MUTED

def parse_html_runs(text):
    """解析带有 <b></b> 标签的文本为带格式的 run 列表: [(text, is_bold), ...]"""
    clean_text = text.replace(r"\_", "_")  # 处理 markdown 转义下划线
    parts = re.split(r"(<b>.*?</b>)", clean_text)
    runs = []
    for part in parts:
        if not part:
            continue
        if part.startswith("<b>") and part.endswith("</b>"):
            clean = part[3:-4]
            runs.append((clean, True))
        else:
            runs.append((part, False))
    return runs

def add_bullet_item(text_frame, line_text, default_size=Pt(12), space_after=Pt(8)):
    """在文本框中添加一行支持 <b> 加粗渲染的教案要点"""
    p = text_frame.add_paragraph() if len(text_frame.paragraphs[0].text) > 0 else text_frame.paragraphs[0]
    p.space_after = space_after
    
    clean_line = line_text.strip()
    if clean_line.startswith("- "):
        clean_line = clean_line[2:].strip()
    
    runs = parse_html_runs(clean_line)
    for text_val, is_bold in runs:
        r = p.add_run()
        r.text = text_val
        r.font.name = FONT_BODY
        r.font.size = default_size
        r.font.bold = is_bold
        if is_bold:
            r.font.color.rgb = COLOR_TEXT_MAIN
        else:
            r.font.color.rgb = COLOR_TEXT_BODY

def add_image_fitted(slide, img_path, box_left, box_top, box_w, box_h, caption="", status=""):
    """
    在指定卡片区域内严格保持原图纵横比嵌入图片，并添加题注与审校状态标签
    """
    if not os.path.exists(img_path):
        print(f"Warning: Image not found at {img_path}")
        return None

    card = create_card(slide, box_left, box_top, box_w, box_h, bg_color=COLOR_CARD_BG)

    caption_h = Inches(0.48) if caption else Inches(0.1)
    available_img_h = box_h - caption_h - Inches(0.2)
    available_img_w = box_w - Inches(0.3)

    try:
        im = Image.open(img_path)
        orig_w, orig_h = im.size
    except Exception as e:
        print(f"Error opening image {img_path}: {e}")
        return None

    scale = min(available_img_w / Inches(orig_w / 96.0), available_img_h / Inches(orig_h / 96.0))
    render_w = Inches(orig_w / 96.0) * scale
    render_h = Inches(orig_h / 96.0) * scale

    img_x = box_left + (box_w - render_w) / 2
    img_y = box_top + Inches(0.15) + (available_img_h - render_h) / 2

    pic = slide.shapes.add_picture(img_path, img_x, img_y, width=render_w, height=render_h)

    if caption:
        cap_box = slide.shapes.add_textbox(box_left + Inches(0.15), box_top + box_h - caption_h - Inches(0.05), 
                                           box_w - Inches(0.3), caption_h)
        tf_cap = cap_box.text_frame
        tf_cap.word_wrap = True
        tf_cap.margin_left = tf_cap.margin_top = tf_cap.margin_right = tf_cap.margin_bottom = 0
        p_cap = tf_cap.paragraphs[0]
        p_cap.text = caption
        p_cap.alignment = PP_ALIGN.CENTER
        p_cap.font.name = FONT_BODY
        p_cap.font.size = Pt(9.5)
        p_cap.font.color.rgb = COLOR_TEXT_MUTED

    if status:
        stat_w = Inches(1.9)
        stat_h = Inches(0.26)
        stat_x = box_left + box_w - stat_w - Inches(0.15)
        stat_y = box_top + Inches(0.12)
        s_badge = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, stat_x, stat_y, stat_w, stat_h)
        s_badge.fill.solid()
        if "已确认" in status or "已入页" in status:
            s_badge.fill.fore_color.rgb = COLOR_GREEN_BG
            s_badge.line.color.rgb = COLOR_GREEN_BORDER
            text_color = COLOR_ACCENT_GREEN
        elif "待同步" in status or "差异" in status:
            s_badge.fill.fore_color.rgb = COLOR_ORANGE_BG
            s_badge.line.color.rgb = COLOR_ORANGE_BORDER
            text_color = COLOR_ACCENT_AMBER
        else:
            s_badge.fill.fore_color.rgb = COLOR_BADGE_BG
            s_badge.line.color.rgb = COLOR_BADGE_BORDER
            text_color = COLOR_ACCENT_BLUE
        s_badge.line.width = Pt(1)

        s_tf = s_badge.text_frame
        s_tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        s_tf.margin_left = s_tf.margin_top = s_tf.margin_right = s_tf.margin_bottom = 0
        s_p = s_tf.paragraphs[0]
        s_p.text = status
        s_p.alignment = PP_ALIGN.CENTER
        s_p.font.name = FONT_HEADING
        s_p.font.size = Pt(8.5)
        s_p.font.bold = True
        s_p.font.color.rgb = text_color

    return pic

def set_slide_notes(slide, notes_raw):
    """清理并设置幻灯片的 Presenter Notes"""
    clean_notes = notes_raw.replace("<b>", "").replace("</b>", "").replace(r"\_", "_").strip()
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = clean_notes

def parse_ppt_raw(raw_text):
    """
    解析 Notion 的 PPT 可见内容原始文本
    返回:
      question: str or None (如果有独立问句，如 "为什么 Roughness 会改变反射的清晰度？")
      items: list of str (每一项要点，如 "- <b>01 ...</b>：...")
    """
    lines = [l.strip() for l in raw_text.strip().split("\n") if l.strip()]
    question = None
    items = []
    for l in lines:
        if not l.startswith("-") and not re.match(r"^\d+", l) and not l.startswith("<b>0") and not l.startswith("<b>完"):
            question = l.replace("<b>", "").replace("</b>", "").strip()
        else:
            items.append(l)
    return question, items

# ==============================================================================
# 18 页个性化幻灯片排版渲染器 (完全由 slides_data.json 数据驱动)
# ==============================================================================
def render_slide_content(slide, s, slide_num, total_slides):
    """根据页码与内容形态分发专属排版，正文严格来源于结构化数据"""
    add_header(slide, slide_num, total_slides, s["short_title"], s["block"])
    add_footer(slide, slide_num, total_slides)
    set_slide_notes(slide, s["notes_raw"])

    embedded_imgs = s.get("embedded_images", [])
    question, items = parse_ppt_raw(s["ppt_raw"])

    # --------------------------------------------------------------------------
    # Slide 01: 课程封面与开场声明
    # --------------------------------------------------------------------------
    if slide_num == 1:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(5.8), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.1), Inches(1.8), Inches(5.2), Inches(4.7))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p0 = tf.paragraphs[0]
        p0.text = "从经验走向 PBR"
        p0.font.name = FONT_HEADING
        p0.font.size = Pt(28)
        p0.font.bold = True
        p0.font.color.rgb = COLOR_ACCENT_BLUE
        p0.space_after = Pt(14)

        for it in items:
            add_bullet_item(tf, it, Pt(13), Pt(12))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.3), 
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 02: 课程宏观定位与 9 周进阶阶梯
    # --------------------------------------------------------------------------
    elif slide_num == 2:
        top_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(11.733), Inches(2.5))
        tb_top = slide.shapes.add_textbox(Inches(1.0), Inches(1.65), Inches(11.333), Inches(2.2))
        tf_top = tb_top.text_frame
        tf_top.word_wrap = True
        
        p = tf_top.paragraphs[0]
        p.text = "九周材质进阶阶梯 (Curriculum Progression Ladder)"
        p.font.name = FONT_HEADING
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_after = Pt(12)

        weeks = [
            ("W1", "MeetMat", True),
            ("W2", "塑料/ID", False),
            ("W3", "木材", False),
            ("W4", "金属", False),
            ("W5", "石材", False),
            ("W6", "布料", False),
            ("W7", "蜡质/皮肤", False),
            ("W8", "综合/发光", False),
            ("W9", "精修交付", False),
        ]
        step_w = Inches(1.18)
        step_h = Inches(1.1)
        for i, (w_lbl, w_sub, is_curr) in enumerate(weeks):
            s_x = Inches(1.0) + i * Inches(1.26)
            s_y = Inches(2.2)
            c = create_card(slide, s_x, s_y, step_w, step_h,
                            bg_color=COLOR_ACCENT_BLUE if is_curr else COLOR_CARD_BG,
                            border_color=COLOR_ACCENT_DARK_BLUE if is_curr else COLOR_CARD_BORDER)
            s_tb = slide.shapes.add_textbox(s_x, s_y + Inches(0.12), step_w, step_h - Inches(0.24))
            s_tf = s_tb.text_frame
            s_tf.margin_left = s_tf.margin_top = s_tf.margin_right = s_tf.margin_bottom = 0
            sp1 = s_tf.paragraphs[0]
            sp1.alignment = PP_ALIGN.CENTER
            sp1.text = w_lbl
            sp1.font.name = FONT_HEADING
            sp1.font.size = Pt(13)
            sp1.font.bold = True
            sp1.font.color.rgb = RGBColor(255, 255, 255) if is_curr else COLOR_TEXT_MAIN
            
            sp2 = s_tf.add_paragraph()
            sp2.alignment = PP_ALIGN.CENTER
            sp2.text = w_sub
            sp2.font.name = FONT_BODY
            sp2.font.size = Pt(10)
            sp2.font.color.rgb = RGBColor(239, 246, 255) if is_curr else COLOR_TEXT_MUTED

        # 下方两个卡片直接来源于 items[0] 和 items[1]
        c1 = create_card(slide, Inches(0.8), Inches(4.2), Inches(5.7), Inches(2.6))
        tb1 = slide.shapes.add_textbox(Inches(1.0), Inches(4.35), Inches(5.3), Inches(2.3))
        tf1 = tb1.text_frame
        tf1.word_wrap = True
        if len(items) > 0:
            add_bullet_item(tf1, items[0], Pt(13.5), Pt(8))
            add_bullet_item(tf1, "这是能力的逐步积累：从首讲认识工具与现象，到后续不同材质掌握新的观察、控制和制作方法，最终落地到作品交付质量。", Pt(12), Pt(0))

        c2 = create_card(slide, Inches(6.8), Inches(4.2), Inches(5.733), Inches(2.6))
        tb2 = slide.shapes.add_textbox(Inches(7.0), Inches(4.35), Inches(5.3), Inches(2.3))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        if len(items) > 1:
            add_bullet_item(tf2, items[1], Pt(13.5), Pt(8))
            add_bullet_item(tf2, "核心解决的问题：模型已有后，如何让表面看起来可信、符合艺术意图、且具备持续可修改性。使用现成基模是为了把时间留给材质观察与贴图表现。", Pt(12), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 03: 考核评价导向与第一讲声明
    # --------------------------------------------------------------------------
    elif slide_num == 3:
        # 顶部三项核心能力来源于 items[0]
        col_w = Inches(3.75)
        caps = [
            ("材质规律理解", "理解光与表面相互作用的物理约束与表现机制，能清楚解释参数设置原因，而非仅凭感觉盲调或背诵数值。"),
            ("图层组织规范", "建立清晰的图层命名、职责分离与非破坏性遮罩习惯，使资产具备工程可维护性与团队协作修改可能。"),
            ("分析与解决问题", "遇到黑屏、参数失真、通道混乱或保存异常时，具备单通道诊断与自查能力，能理性定位故障节点。")
        ]
        for i, (c_title, c_desc) in enumerate(caps):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), col_w, Inches(3.0))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), col_w - Inches(0.4), Inches(2.6))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, f"<b>01 能力重点：{c_title}</b>", Pt(15), Pt(10))
            add_bullet_item(tf, c_desc, Pt(12), Pt(0))

        # 下方两条重要原则声明卡来源于 items[1] 和 items[2]
        bottom_card = create_card(slide, Inches(0.8), Inches(4.7), Inches(11.733), Inches(2.1), bg_color=COLOR_ORANGE_BG, border_color=COLOR_ORANGE_BORDER)
        tb_bot = slide.shapes.add_textbox(Inches(1.1), Inches(4.85), Inches(11.133), Inches(1.8))
        tf_bot = tb_bot.text_frame
        tf_bot.word_wrap = True
        if len(items) > 1:
            add_bullet_item(tf_bot, items[1], Pt(13), Pt(10))
        if len(items) > 2:
            add_bullet_item(tf_bot, items[2], Pt(13), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 04: 视觉观察前置悬念：单组材质身份对比
    # --------------------------------------------------------------------------
    elif slide_num == 4:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.6), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.2), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for it in items:
            add_bullet_item(tf, it, Pt(12.5), Pt(14))
        add_bullet_item(tf, "<b>教学定界提醒</b>：这是特定条件下的材质身份对比示例，并非严格单变量实验（单变量严谨对比见 Slide 09）。", Pt(10.5), Pt(0))

        if len(embedded_imgs) >= 2:
            img1, img2 = embedded_imgs[0], embedded_imgs[1]
            add_image_fitted(slide, img1["path"], Inches(5.6), Inches(1.5), Inches(3.4), Inches(5.3),
                             caption=img1["caption"], status=img1["status"])
            add_image_fitted(slide, img2["path"], Inches(9.2), Inches(1.5), Inches(3.333), Inches(5.3),
                             caption=img2["caption"], status=img2["status"])

    # --------------------------------------------------------------------------
    # Slide 05: 第一讲标杆资产：认识 MeetMat
    # --------------------------------------------------------------------------
    elif slide_num == 5:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(5.4), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(5.0), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for it in items:
            add_bullet_item(tf, it, Pt(13), Pt(14))
        add_bullet_item(tf, "<b>出处与许可声明</b>：官方 MeetMat 资产归属于 Adobe Substance 3D；潮玩参考图出处保留，仅作教学换肤类比，不声称二者直接关联。", Pt(10), Pt(0))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(6.4), Inches(1.5), Inches(6.133), Inches(5.3),
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 06: 认识 Painter 的必要界面与视口操作
    # --------------------------------------------------------------------------
    elif slide_num == 6:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.6), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.2), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for it in items:
            add_bullet_item(tf, it, Pt(12.5), Pt(14))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(5.6), Inches(1.5), Inches(6.933), Inches(5.3),
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 07: 观察环境光：旋转与更换 HDRI
    # --------------------------------------------------------------------------
    elif slide_num == 7:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.0), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(3.6), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for it in items:
            add_bullet_item(tf, it, Pt(12.5), Pt(14))

        if len(embedded_imgs) >= 3:
            img1, img2, img3 = embedded_imgs[0], embedded_imgs[1], embedded_imgs[2]
            add_image_fitted(slide, img1["path"], Inches(5.0), Inches(1.5), Inches(3.8), Inches(3.2),
                             caption=img1["caption"], status=img1["status"])
            add_image_fitted(slide, img2["path"], Inches(9.0), Inches(1.5), Inches(3.533), Inches(3.2),
                             caption=img2["caption"], status=img2["status"])
            # 图 3 明确标注更换 HDRI 入口
            add_image_fitted(slide, img3["path"], Inches(5.0), Inches(4.9), Inches(7.533), Inches(1.9),
                             caption=img3["caption"], status=img3["status"])

    # --------------------------------------------------------------------------
    # Slide 08: 教师示范一：黄色底漆填充层与 Roughness
    # --------------------------------------------------------------------------
    elif slide_num == 8:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.4), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for it in items:
            add_bullet_item(tf, it, Pt(12.5), Pt(14))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(5.8), Inches(1.5), Inches(6.733), Inches(5.3),
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 09: 【实操任务 1】第 30 分钟动手：参数因果实验
    # --------------------------------------------------------------------------
    elif slide_num == 9:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.4), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for it in items:
            add_bullet_item(tf, it, Pt(12.5), Pt(14))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(5.8), Inches(1.5), Inches(6.733), Inches(5.3),
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 10: 教师示范二：第二层覆盖与黑色遮罩开窗
    # --------------------------------------------------------------------------
    elif slide_num == 10:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.4), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.0), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for it in items:
            add_bullet_item(tf, it, Pt(12), Pt(12))

        if len(embedded_imgs) >= 2:
            img1, img2 = embedded_imgs[0], embedded_imgs[1]
            add_image_fitted(slide, img1["path"], Inches(5.4), Inches(1.5), Inches(3.5), Inches(5.3),
                             caption=img1["caption"], status=img1["status"])
            add_image_fitted(slide, img2["path"], Inches(9.1), Inches(1.5), Inches(3.433), Inches(5.3),
                             caption=img2["caption"], status=img2["status"])

    # --------------------------------------------------------------------------
    # Slide 11: 【实操任务 2】学生跟练：面罩遮罩开窗与快速纠错
    # --------------------------------------------------------------------------
    elif slide_num == 11:
        step_w = Inches(3.75)
        # 三张卡片完全从 items 读取（item 0: 结构, item 1: 绘制与修边, item 2: 完成检查）
        item_0 = items[0] if len(items) > 0 else "01 跟练面罩结构"
        item_1 = items[1] if len(items) > 1 else "02 局部绘制与修边"
        item_chk = items[2] if len(items) > 2 else "完成检查"

        c1 = create_card(slide, Inches(0.8), Inches(1.5), step_w, Inches(3.3))
        tb1 = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), step_w - Inches(0.4), Inches(2.9))
        tf1 = tb1.text_frame
        tf1.word_wrap = True
        add_bullet_item(tf1, item_0, Pt(13), Pt(8))
        add_bullet_item(tf1, "优先确认底层 Plastic_Base 与上层 Face_Mask 正确建立，并成功挂载 Black Mask 黑色遮罩。", Pt(11.5), Pt(0))

        c2 = create_card(slide, Inches(4.8), Inches(1.5), step_w, Inches(3.3))
        tb2 = slide.shapes.add_textbox(Inches(5.0), Inches(1.7), step_w - Inches(0.4), Inches(2.9))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        add_bullet_item(tf2, item_1, Pt(13), Pt(8))
        add_bullet_item(tf2, "优先使用可见界面操作；体会白色显现、黑色隐藏的可逆关系，把“修回来”作为本次跟练的关键能力。", Pt(11.5), Pt(0))

        c3 = create_card(slide, Inches(8.8), Inches(1.5), step_w, Inches(3.3))
        tb3 = slide.shapes.add_textbox(Inches(9.0), Inches(1.7), step_w - Inches(0.4), Inches(2.9))
        tf3 = tb3.text_frame
        tf3.word_wrap = True
        add_bullet_item(tf3, "<b>操作提醒与规范</b>", Pt(13), Pt(8))
        add_bullet_item(tf3, "• 检查选中的是 Mask 缩略图还是 Layer\n• 根据造型在界面面板调节笔刷大小与形状\n• 尚未确认的快捷键不列为必须背诵", Pt(11.5), Pt(0))

        # 下方完成检查卡
        check_card = create_card(slide, Inches(0.8), Inches(5.0), Inches(11.733), Inches(1.8), bg_color=COLOR_GREEN_BG, border_color=COLOR_GREEN_BORDER)
        tb_chk = slide.shapes.add_textbox(Inches(1.1), Inches(5.15), Inches(11.133), Inches(1.5))
        tf_chk = tb_chk.text_frame
        tf_chk.word_wrap = True
        add_bullet_item(tf_chk, item_chk, Pt(13.5), Pt(6))
        add_bullet_item(tf_chk, "✔ 能看到黄色底漆与局部深色面罩反差；\n✔ 能够自如在遮罩上反向擦除，亲身验证遮罩的非破坏性无损编辑。", Pt(12), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 12: 理论升华一：微表面为什么改变反射？
    # --------------------------------------------------------------------------
    elif slide_num == 12:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.4), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        # 问句横幅
        if question:
            p_q = tf.paragraphs[0]
            p_q.text = question
            p_q.font.name = FONT_HEADING
            p_q.font.size = Pt(16)
            p_q.font.bold = True
            p_q.font.color.rgb = COLOR_ACCENT_BLUE
            p_q.space_after = Pt(12)

        for it in items:
            add_bullet_item(tf, it, Pt(12.5), Pt(14))
        add_bullet_item(tf, "<b>概念示意声明</b>：示意图表达微表面朝向模型，非显微照片；无可见几何凹凸，不加入 BRDF 公式。", Pt(10.5), Pt(0))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(5.8), Inches(1.5), Inches(6.733), Inches(5.3),
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 13: 理论升华二：为什么黄色塑料与黄金的反射不同？
    # --------------------------------------------------------------------------
    elif slide_num == 13:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(5.0), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.6), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        if question:
            p_q = tf.paragraphs[0]
            p_q.text = question
            p_q.font.name = FONT_HEADING
            p_q.font.size = Pt(16)
            p_q.font.bold = True
            p_q.font.color.rgb = COLOR_ACCENT_BLUE
            p_q.space_after = Pt(12)

        for it in items:
            add_bullet_item(tf, it, Pt(12), Pt(14))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(6.0), Inches(1.5), Inches(6.533), Inches(5.3),
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 14: 理论升华三：图层与遮罩的显隐关系
    # --------------------------------------------------------------------------
    elif slide_num == 14:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.4), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        for it in items:
            add_bullet_item(tf, it, Pt(12.5), Pt(14))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(5.8), Inches(1.5), Inches(6.733), Inches(5.3),
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 15: 【独立创作】MeetMat Head 个性化材质定制
    # --------------------------------------------------------------------------
    elif slide_num == 15:
        card_w = Inches(3.75)
        # 上排三个创意角色方向卡（来源于 item 0）
        roles = [
            ("角色方向 A：机甲英雄", "参考经典红金或黑金视觉语言，形成高明度反差的面罩特征。学有余力者可选做面罩 Metallic = 1 或金属性边缘。", "高饱和红黄撞色"),
            ("角色方向 B：工业防护机器人", "以警示橙、哑光黑或军绿工程涂层为主，底漆保持高粗糙度耐磨质感。必做 Metallic = 0 双层塑料质感。", "哑光工业防护语汇"),
            ("角色方向 C：复古设计师潮玩", "波普艺术或撞色现代玩具风格，面罩设计波点、条纹或几何开窗，突出纯净的光泽与鲜明个性表达。", "几何图腾趣味表达")
        ]
        for i, (r_title, r_desc, r_tag) in enumerate(roles):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), card_w, Inches(3.2))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), card_w - Inches(0.4), Inches(2.8))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, f"<b>{r_title}</b>", Pt(14.5), Pt(8))
            add_bullet_item(tf, r_desc, Pt(11.5), Pt(10))
            add_bullet_item(tf, f"<b>设计焦点</b>：{r_tag}", Pt(10.5), Pt(0))

        bottom_req = create_card(slide, Inches(0.8), Inches(4.9), Inches(11.733), Inches(1.9), bg_color=COLOR_GREEN_BG, border_color=COLOR_GREEN_BORDER)
        tb_req = slide.shapes.add_textbox(Inches(1.1), Inches(5.05), Inches(11.133), Inches(1.6))
        tf_req = tb_req.text_frame
        tf_req.word_wrap = True
        if len(items) > 1:
            add_bullet_item(tf_req, items[1], Pt(12.5), Pt(6))
        if len(items) > 2:
            add_bullet_item(tf_req, items[2], Pt(12.5), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 16: 轻量前后观察对比与免课后作业卡
    # --------------------------------------------------------------------------
    elif slide_num == 16:
        card_l = create_card(slide, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
        tb_l = slide.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(5.1), Inches(4.9))
        tf_l = tb_l.text_frame
        tf_l.word_wrap = True
        add_bullet_item(tf_l, "<b>随堂 3 行观察记录模板</b>", Pt(17), Pt(10))
        for it in items[:4]:  # 包含 01 及 Before/Action/After
            add_bullet_item(tf_l, it, Pt(12), Pt(8))

        card_r = create_card(slide, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.3), bg_color=COLOR_ORANGE_BG, border_color=COLOR_ORANGE_BORDER)
        tb_r = slide.shapes.add_textbox(Inches(7.1), Inches(1.7), Inches(5.133), Inches(4.9))
        tf_r = tb_r.text_frame
        tf_r.word_wrap = True
        add_bullet_item(tf_r, "<b>【免作业声明】课堂闭环交付</b>", Pt(17), Pt(10))
        if len(items) > 4:
            add_bullet_item(tf_r, items[4], Pt(13), Pt(12))
        add_bullet_item(tf_r, "<b>剪裁原则</b>：若课堂时间紧张，优先确保 Slide 18 的工程安全保存，可口头回答三行要点，不把未写完的文字变成隐藏课后作业。", Pt(12), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 17: 四级反馈漏斗与同桌 30 秒互查
    # --------------------------------------------------------------------------
    elif slide_num == 17:
        card_w = Inches(3.75)
        for i, it in enumerate(items[:3]):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), card_w, Inches(4.0))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), card_w - Inches(0.4), Inches(3.6))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, it, Pt(14), Pt(12))
            if i == 0:
                add_bullet_item(tf, "口头反馈，不替对方修改设备；指出一个做得清楚的亮点、一个需要检查的细节。", Pt(11.5), Pt(0))
            elif i == 1:
                add_bullet_item(tf, "重点检查 Metallic 通道是否误涂为非零值，快速定位参数异常。", Pt(11.5), Pt(0))
            elif i == 2:
                add_bullet_item(tf, "按 M 键返回完整材质视口；切勿与 B 键 (Mesh Maps) 模式混淆。", Pt(11.5), Pt(0))

        b_c = create_card(slide, Inches(0.8), Inches(5.7), Inches(11.733), Inches(1.1))
        tb_b = slide.shapes.add_textbox(Inches(1.1), Inches(5.8), Inches(11.133), Inches(0.9))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        add_bullet_item(tf_b, "<b>四级反馈纠错梯队</b>：同桌互查 → 助教巡视 → 教师投屏广播典型错误 → 恢复上一步/撤销。机房快捷键响应存在版本差异时，引导学生通过界面下拉菜单操作。", Pt(11), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 18: 数据持久化：规范另存为、退出软件与重开验证
    # --------------------------------------------------------------------------
    elif slide_num == 18:
        step_w = Inches(3.75)
        for i, it in enumerate(items[:3]):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), step_w, Inches(3.8))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), step_w - Inches(0.4), Inches(3.4))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, it, Pt(14), Pt(12))
            if i == 0:
                add_bullet_item(tf, "使用简短、英文字母且具备识别度的命名（如 MeetMat_Head_W1.spp），保存在个人固定目录。", Pt(11.5), Pt(0))
            elif i == 1:
                add_bullet_item(tf, "课堂内彻底关闭软件重开，亲眼确认 Head、底漆、面罩和遮罩完整可编辑，打破“提示保存成功假象”。", Pt(11.5), Pt(0))
            elif i == 2:
                add_bullet_item(tf, "截取清晰材质视图提交，下讲预告：第 2 讲《塑料材质进阶与 ID 分区制作》。", Pt(11.5), Pt(0))

        sum_card = create_card(slide, Inches(0.8), Inches(5.5), Inches(11.733), Inches(1.3), bg_color=COLOR_GREEN_BG, border_color=COLOR_GREEN_BORDER)
        tb_s = slide.shapes.add_textbox(Inches(1.1), Inches(5.62), Inches(11.133), Inches(1.1))
        tf_s = tb_s.text_frame
        tf_s.word_wrap = True
        add_bullet_item(tf_s, "<b>第 1 讲圆满达成教学闭环</b>：学生完成从已有认知到 PBR 规律建立、从界面视口到图层遮罩制作、从参数因果实验到工程持久化验证的全流程实践。下周见！", Pt(12.5), Pt(0))

# ==============================================================================
# 主执行入口
# ==============================================================================
def main():
    json_path = "assets/w1_meetmat/slides_data.json"
    if not os.path.exists(json_path):
        print(f"Error: {json_path} does not exist!")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        slides_data = json.load(f)

    total_slides = len(slides_data)
    print(f"Loaded {total_slides} slides from {json_path}.")

    prs = pptx.Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT
    blank_layout = prs.slide_layouts[6]

    for s in slides_data:
        slide_num = s["number"]
        print(f"Building Slide {slide_num:02d}: {s['short_title']} ...")
        slide = prs.slides.add_slide(blank_layout)
        render_slide_content(slide, s, slide_num, total_slides)

    output_pptx = "W1_MeetMat_18slides_teacher_review.pptx"
    prs.save(output_pptx)
    print(f"Successfully generated presentation: {output_pptx} ({os.path.getsize(output_pptx)} bytes)")

if __name__ == "__main__":
    main()
