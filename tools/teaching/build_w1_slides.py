#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_w1_slides.py
生成《三维数字材质制作》第 1 讲《初识 Substance 3D Painter / MeetMat》18 页教师审校候选版 PPTX。
严格遵循：
- 16:9 宽屏大学课堂投影规范
- Notion 备课稿 v0.3 双层父子结构与 01/02/03 编号锚点
- 15 个 Notion 真实原图完整嵌入与版式适配
- 完整 Presenter Notes 教师口播讲稿与知识解释
- 教学边界：不扩充学生任务，不写未经学院核准的具体考核比例，保留专业英文术语
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
    # 顶部微型面包屑与 Block 药丸徽章
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

    # 页码
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
    parts = re.split(r"(<b>.*?</b>)", text)
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

    caption_h = Inches(0.45) if caption else Inches(0.1)
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
        stat_w = Inches(1.8)
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
    clean_notes = notes_raw.replace("<b>", "").replace("</b>", "").strip()
    notes_slide = slide.notes_slide
    tf = notes_slide.notes_text_frame
    tf.text = clean_notes

# ==============================================================================
# 18 页个性化幻灯片排版渲染器
# ==============================================================================
def render_slide_content(slide, s, slide_num, total_slides):
    """根据页码与内容形态分发专属排版"""
    add_header(slide, slide_num, total_slides, s["short_title"], s["block"])
    add_footer(slide, slide_num, total_slides)
    set_slide_notes(slide, s["notes_raw"])

    embedded_imgs = s.get("embedded_images", [])

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

        add_bullet_item(tf, "<b>01 本课从已有材质经验走向 PBR</b>：从三维基础经验出发，回答“为什么表面看起来像这种材质”。", Pt(13), Pt(12))
        add_bullet_item(tf, "<b>02 用物理规律观察，用分层思维创作</b>：PBR 提供光与表面的可控约束，分层让材质组织可修改。", Pt(13), Pt(12))
        add_bullet_item(tf, "<b>03 今日任务：认识 Painter，动手制作 MeetMat</b>：在 Head 上完成底层、粗糙度与面罩开窗，并保存工程。", Pt(13), Pt(18))
        add_bullet_item(tf, "<b>授课信息</b>：授课教师：林昕 ｜ 2026–2027 学年第一学期", Pt(11), Pt(0))

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

        c1 = create_card(slide, Inches(0.8), Inches(4.2), Inches(5.7), Inches(2.6))
        tb1 = slide.shapes.add_textbox(Inches(1.0), Inches(4.35), Inches(5.3), Inches(2.3))
        tf1 = tb1.text_frame
        tf1.word_wrap = True
        add_bullet_item(tf1, "<b>01 九周路线不是重复更换九种预设</b>", Pt(14), Pt(8))
        add_bullet_item(tf1, "这是能力的逐步积累：从首讲认识工具与现象，到后续不同材质掌握新的观察、控制和制作方法，最终落地到作品交付质量。", Pt(12), Pt(6))
        add_bullet_item(tf1, "图示为全学期能力路线概览，不意味着后八讲细节已被机械冻结。", Pt(11), Pt(0))

        c2 = create_card(slide, Inches(6.8), Inches(4.2), Inches(5.733), Inches(2.6))
        tb2 = slide.shapes.add_textbox(Inches(7.0), Inches(4.35), Inches(5.3), Inches(2.3))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        add_bullet_item(tf2, "<b>02 本课程的主体是材质制作</b>", Pt(14), Pt(8))
        add_bullet_item(tf2, "核心解决的问题：模型已有后，如何让表面看起来可信、符合艺术意图、且具备持续可修改性。", Pt(12), Pt(6))
        add_bullet_item(tf2, "使用标准基模是为了把宝贵课堂时间留给 PBR 参数、图层与贴图表现；建模和 UV 仅在需要支撑材质任务时补充。", Pt(11), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 03: 考核评价导向与第一讲声明
    # --------------------------------------------------------------------------
    elif slide_num == 3:
        col_w = Inches(3.75)
        caps = [
            ("01 材质规律理解", "理解光与表面相互作用的物理约束与表现机制，能清楚解释参数设置原因，而非仅凭感觉盲调或背诵数值。"),
            ("02 图层组织规范", "建立清晰的图层命名、职责分离与非破坏性遮罩习惯，使资产具备工程可维护性与团队协作修改可能。"),
            ("03 分析与解决问题", "遇到黑屏、参数失真、通道混乱或保存异常时，具备单通道诊断与自查能力，能理性定位故障节点。")
        ]
        for i, (c_title, c_desc) in enumerate(caps):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), col_w, Inches(3.0))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), col_w - Inches(0.4), Inches(2.6))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, f"<b>{c_title}</b>", Pt(15), Pt(10))
            add_bullet_item(tf, c_desc, Pt(12), Pt(0))

        bottom_card = create_card(slide, Inches(0.8), Inches(4.7), Inches(11.733), Inches(2.1), bg_color=COLOR_ORANGE_BG, border_color=COLOR_ORANGE_BORDER)
        tb_bot = slide.shapes.add_textbox(Inches(1.1), Inches(4.85), Inches(11.133), Inches(1.8))
        tf_bot = tb_bot.text_frame
        tf_bot.word_wrap = True
        add_bullet_item(tf_bot, "<b>02 看重制作过程与最终质量（学校正式考核为准）</b>：本讲介绍的是课程重视的学习方向，不是擅自宣布成绩比例。考勤、平时作业与期末权重以教务处正式核定文件为准，未核准数字不出现在课堂承诺中。", Pt(12.5), Pt(8))
        add_bullet_item(tf_bot, "<b>03 第一讲不另外布置课后作业</b>：本讲希望学生在 160 分钟课堂内完成首次动手操作、观察对比与文件持久化保存，不增加一份长篇课后报告负担；这不代表改动学校正式考核制度。", Pt(12.5), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 04: 视觉观察前置悬念：单组材质身份对比
    # --------------------------------------------------------------------------
    elif slide_num == 4:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.6), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.2), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        add_bullet_item(tf, "<b>为什么高光表现完全不同？</b>", Pt(16), Pt(12))
        add_bullet_item(tf, "<b>01 同一个 MeetMat Head，两种材料外观</b>：光洁塑料 vs 粗糙陶土（均在 Painter 相同几何与灯光下截取）。", Pt(12.5), Pt(10))
        add_bullet_item(tf, "<b>02 观察高光 (Specular Highlight)</b>：哪一边更清晰集中？哪一边更宽柔模糊？", Pt(12.5), Pt(10))
        add_bullet_item(tf, "<b>03 思考本质原因</b>：为什么真实高光会随照明与观察角度自然移动，而画在 Base Color 里的白斑不会？", Pt(12.5), Pt(14))
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
        
        add_bullet_item(tf, "<b>认识官方标杆资产 MeetMat</b>", Pt(16), Pt(12))
        add_bullet_item(tf, "<b>01 MeetMat 资产结构</b>：包含 Head、Body、Base 三个核心 Texture Set（纹理集）；本讲所有示范与实操集中于 <b>Head</b>。", Pt(13), Pt(12))
        add_bullet_item(tf, "<b>02 潮玩盲盒与换肤类比</b>：类比 POP MART Molly 等潮流玩具——同一个标准基模，通过不同的材质属性与涂装设计，获得截然不同的角色生命力与材质身份。", Pt(13), Pt(12))
        add_bullet_item(tf, "<b>03 专注表面材质设计</b>：省去复杂角色建模，把全部精力集中在颜色、粗糙度、金属感与分层遮罩上。", Pt(13), Pt(14))
        add_bullet_item(tf, "<b>版权与出处声明</b>：官方 MeetMat 资产归属于 Adobe Substance 3D；潮玩作品出处保留，仅作教学类比，不声称二者直接关联。", Pt(10), Pt(0))

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
        
        add_bullet_item(tf, "<b>四大核心面板职责</b>", Pt(16), Pt(10))
        add_bullet_item(tf, "<b>01 四个面板负责不同操作</b>：\n• <b>3D Viewport</b>：实时光照视口观察\n• <b>Texture Set List</b>：选择 Head 纹理集\n• <b>Layers</b>：图层堆叠与组织管理\n• <b>Properties</b>：图层参数与材质通道控制", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>02 视口导航操作</b>：\n• Alt + 鼠标左键：旋转视口观察\n• Alt + 鼠标中键：平移视口\n• Alt + 鼠标右键：缩放视图", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>03 快捷键 F</b>：将视角快速重新居中聚焦到当前模型，避免视口迷失（非重置材质状态）。", Pt(12), Pt(0))

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
        
        add_bullet_item(tf, "<b>光照观察三要素</b>", Pt(16), Pt(10))
        add_bullet_item(tf, "<b>01 Shift + 鼠标右键</b>：水平拖拽旋转环境天光 (Environment Map)，亲眼观察高光光斑与倒影在曲面上的移动。", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>02 旋转光照 vs 更换环境</b>：旋转是改变光照角度，更换 HDRI 是改变整体色彩气氛与反射细节；本讲重点通过旋转观察高光位移。", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>03 Display Settings</b>：环境光不透明度与曝光度控制窗口，便于将背光旋转到正面或调整背景可见性。", Pt(12), Pt(0))

        if len(embedded_imgs) >= 3:
            img1, img2, img3 = embedded_imgs[0], embedded_imgs[1], embedded_imgs[2]
            add_image_fitted(slide, img1["path"], Inches(5.0), Inches(1.5), Inches(3.8), Inches(3.2),
                             caption=img1["caption"], status=img1["status"])
            add_image_fitted(slide, img2["path"], Inches(9.0), Inches(1.5), Inches(3.533), Inches(3.2),
                             caption=img2["caption"], status=img2["status"])
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
        
        add_bullet_item(tf, "<b>教师示范：黄色底漆填充层</b>", Pt(16), Pt(10))
        add_bullet_item(tf, "<b>01 建立黄色底漆 Fill Layer</b>：命名为 Plastic_Base，选择纯正高饱和黄色。", Pt(12.5), Pt(10))
        add_bullet_item(tf, "<b>02 通道是材质的不同属性</b>：\n• <b>Base Color</b>：控制表面反射的固有颜色\n• <b>Roughness</b>：控制微表面的粗糙与高光聚散\n• <b>Metallic</b>：控制绝缘体(=0)与导体(=1)\n• <b>Normal / Height</b>：本讲指认名称，暂不展开实操", Pt(11.5), Pt(10))
        add_bullet_item(tf, "<b>03 调整 Roughness 观察高光变化</b>：拖动滑块从 0.10 调整至 0.85，高光从锐利紧聚变为柔和弥散。", Pt(12), Pt(0))

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
        
        add_bullet_item(tf, "<b>【实操 1】开课第 30 分钟动手</b>", Pt(16), Pt(10))
        add_bullet_item(tf, "<b>01 固定视角与光线</b>：保持相同机位与灯光条件，不旋转视口，排除环境干扰。", Pt(12.5), Pt(10))
        add_bullet_item(tf, "<b>02 Roughness 单变量对比实验</b>：\n• 设置 <b>Roughness = 0.10</b>：观察光泽塑料表面紧聚、锐利的高光亮点\n• 设置 <b>Roughness = 0.85</b>：观察表面高光扩散、边缘柔和暗哑", Pt(12), Pt(12))
        add_bullet_item(tf, "<b>完成检查清单</b>：\n✔ 成功建立 Fill Layer 并重命名为 Plastic_Base\n✔ 确认 Metallic = 0，仅改动 Roughness\n✔ 亲眼观察到高光轮廓从锐利到模糊的平滑变化", Pt(11.5), Pt(0))

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
        
        add_bullet_item(tf, "<b>教师示范：分层与遮罩</b>", Pt(16), Pt(10))
        add_bullet_item(tf, "<b>01 新建深色 Fill Layer 覆盖底层</b>：建立命名为 Face_Mask 的深灰色高粗糙度图层，直接完全覆盖黄色底层。", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>02 添加黑色遮罩 (Add black mask)</b>：图层瞬间被完全隐藏，露出底层的黄色塑料。", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>03 白色画笔开窗与 X 键可逆纠错</b>：\n• 在遮罩层用<b>纯白画笔</b>涂绘，让上层深色显现\n• 按 <b>X 键</b>快速切换为纯黑画笔，擦除画错区域\n• 非破坏性修改，底层参数完好无损", Pt(11.5), Pt(0))

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
        steps_data = [
            ("步骤一：遮罩开窗", "在 Head 纹理集上建立第二层深色 Fill Layer，添加 Black Mask；选中遮罩，使用白色画笔绘制个性化眼眶或面罩轮廓。", "White 显现当前图层"),
            ("步骤二：X 键无损纠错", "当边缘画出界或形状不满意时，立即按键盘 X 键切换为黑色笔刷涂抹纠错。不使用 Eraser 橡皮擦，保证图层参数完整。", "Black 隐藏当前图层"),
            ("步骤三：笔刷快捷控制", "熟练使用快捷控制提高效率：Ctrl + 鼠标右键水平拖拽调节笔刷尺寸大小，垂直拖拽调节边缘羽化硬度 (Hardness)。", "高效手势控制规范")
        ]
        for i, (title_s, desc_s, tag_s) in enumerate(steps_data):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), step_w, Inches(3.3))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), step_w - Inches(0.4), Inches(2.9))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, f"<b>{title_s}</b>", Pt(15), Pt(8))
            add_bullet_item(tf, desc_s, Pt(12), Pt(10))
            add_bullet_item(tf, f"<b>要点提示</b>：{tag_s}", Pt(11), Pt(0))

        check_card = create_card(slide, Inches(0.8), Inches(5.0), Inches(11.733), Inches(1.8), bg_color=COLOR_GREEN_BG, border_color=COLOR_GREEN_BORDER)
        tb_chk = slide.shapes.add_textbox(Inches(1.1), Inches(5.15), Inches(11.133), Inches(1.5))
        tf_chk = tb_chk.text_frame
        tf_chk.word_wrap = True
        add_bullet_item(tf_chk, "<b>完成检查标准 (Observable Standards)</b>：", Pt(13), Pt(6))
        add_bullet_item(tf_chk, "✔ 面罩边缘清晰干净，无大面积误涂或飞白；\n✔ 能够自如使用 X 键进行黑白反向擦除，深刻理解遮罩的无损可逆属性；\n✔ 教师巡视重点：检查是否误将笔刷画在 Layer 颜色通道上，确保选中并处于 Mask 图标上绘制。", Pt(11.5), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 12: 理论升华一：微表面为什么改变反射？
    # --------------------------------------------------------------------------
    elif slide_num == 12:
        left_card = create_card(slide, Inches(0.8), Inches(1.5), Inches(4.8), Inches(5.3))
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(1.7), Inches(4.4), Inches(4.9))
        tf = tb.text_frame
        tf.word_wrap = True
        
        add_bullet_item(tf, "<b>微表面模型 (Microfacet Model)</b>", Pt(16), Pt(10))
        add_bullet_item(tf, "<b>01 微表面朝向分布 → 镜面反射形态</b>：\n• <b>Smooth (光滑)</b>：微表面法线朝向高度一致，镜面反射集中在狭窄角度内，倒影与高光清晰锐利。\n• <b>Rough (粗糙)</b>：微表面朝向分散杂乱，反射光线被散射到极宽范围，倒影模糊甚至无法辨认边界。", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>02 解释 Slide 09 实操因果</b>：反射变暗或模糊，是因为光能被散射到更多方向，而非光线凭空消失（反射分散 ≠ 没有反射）。", Pt(12), Pt(12))
        add_bullet_item(tf, "<b>理论降负界限</b>：示意图只表达朝向分布模型，非显微物理照片；Roughness 不改变宏观几何，不加入 BRDF 复杂公式。", Pt(10.5), Pt(0))

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
        
        add_bullet_item(tf, "<b>漫反射与镜面反射 (Diffuse vs Specular)</b>", Pt(16), Pt(10))
        add_bullet_item(tf, "<b>01 材质颜色来自完全不同的物理路径</b>：\n• <b>黄色塑料 (Metallic = 0)</b>：进入表层发生次表面散射形成黄色的漫反射 (Diffuse Reflection)；白光照射下的高光几乎全白。\n• <b>黄金球体 (Metallic = 1)</b>：纯金属内部自由电子直接吸收折射光，无漫反射；其金黄色完全来自有色的镜面反射 (Specular Reflection)！", Pt(11.5), Pt(10))
        add_bullet_item(tf, "<b>02 Base Color 的用途随 Metallic 动态切换</b>：\n• 绝缘体 (非金属)：Base Color 定义漫反射颜色；\n• 纯金属：Base Color 直接定义高光镜面反射颜色。", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>实用工程判断</b>：黄色油漆涂抹的铁盒，按可见的表面塑料层设 Metallic = 0；真正露出的金属划痕才设 Metallic = 1。", Pt(11), Pt(0))

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
        
        add_bullet_item(tf, "<b>图层与遮罩职责分离</b>", Pt(16), Pt(10))
        add_bullet_item(tf, "<b>01 职责清晰划分</b>：\n• <b>Layer (图层)</b>：负责定义材质材质属性 (颜色、粗糙度、金属感)\n• <b>Mask (遮罩)</b>：专门负责控制该图层在空间中哪里显现、哪里隐藏", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>02 黑白灰基础法则</b>：\n• <b>Black</b>：完全隐藏当前层，露出底层\n• <b>White</b>：完全显现当前层，覆盖底层\n• <b>Grey</b>：产生半透明或平滑过渡显现", Pt(12), Pt(10))
        add_bullet_item(tf, "<b>03 非破坏性工作流 (Non-destructive)</b>：任何时候修改遮罩，图层内所有材质参数完好保留，随时可回溯调整。", Pt(12), Pt(0))

        if embedded_imgs:
            img = embedded_imgs[0]
            add_image_fitted(slide, img["path"], Inches(5.8), Inches(1.5), Inches(6.733), Inches(5.3),
                             caption=img["caption"], status=img["status"])

    # --------------------------------------------------------------------------
    # Slide 15: 【独立创作】MeetMat Head 个性化材质定制
    # --------------------------------------------------------------------------
    elif slide_num == 15:
        card_w = Inches(3.75)
        roles = [
            ("角色方向 A：机甲英雄", "参考经典红金或黑金视觉语言，形成高明度反差的面罩特征。学有余力者可选做面罩 Metallic = 1 或金属性边缘。", "重点：高饱和红黄撞色"),
            ("角色方向 B：工业防护机器人", "以警示橙、哑光黑或军绿工程涂层为主，底漆保持高粗糙度耐磨质感。必做 Metallic = 0 双层塑料质感。", "重点：哑光工业防护语汇"),
            ("角色方向 C：复古设计师潮玩", "波普艺术或撞色现代玩具风格，面罩设计波点、条纹或几何开窗，突出纯净的光泽与鲜明个性表达。", "重点：几何图腾趣味表达")
        ]
        for i, (r_title, r_desc, r_tag) in enumerate(roles):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), card_w, Inches(3.2))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), card_w - Inches(0.4), Inches(2.8))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, f"<b>{r_title}</b>", Pt(15), Pt(8))
            add_bullet_item(tf, r_desc, Pt(11.5), Pt(10))
            add_bullet_item(tf, f"<b>设计焦点</b>：{r_tag}", Pt(10.5), Pt(0))

        bottom_req = create_card(slide, Inches(0.8), Inches(4.9), Inches(11.733), Inches(1.9), bg_color=COLOR_GREEN_BG, border_color=COLOR_GREEN_BORDER)
        tb_req = slide.shapes.add_textbox(Inches(1.1), Inches(5.05), Inches(11.133), Inches(1.6))
        tf_req = tb_req.text_frame
        tf_req.word_wrap = True
        add_bullet_item(tf_req, "<b>独立创作要求与完成检查标准 (35 分钟总预算闭环)</b>：", Pt(13), Pt(6))
        add_bullet_item(tf_req, "• <b>必做基准</b>：全员以两层非金属 Fill Layer (Metallic = 0)、鲜明 Roughness 反差、Black Mask 干净修边为必做；\n• <b>选做拓展</b>：进度较快学生可尝试面罩 Metallic = 1，不作为强制计分要求；\n• <b>完成检查</b>：能向同桌或老师清晰讲出角色意图，图层保持规范命名与非破坏性结构。", Pt(11.5), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 16: 轻量前后观察对比与免课后作业卡
    # --------------------------------------------------------------------------
    elif slide_num == 16:
        card_l = create_card(slide, Inches(0.8), Inches(1.5), Inches(5.7), Inches(5.3))
        tb_l = slide.shapes.add_textbox(Inches(1.1), Inches(1.7), Inches(5.1), Inches(4.9))
        tf_l = tb_l.text_frame
        tf_l.word_wrap = True
        add_bullet_item(tf_l, "<b>随堂 3 行观察记录模板</b>", Pt(17), Pt(12))
        add_bullet_item(tf_l, "用简单的三行文字记录自己的材质判断，随工程一同保存：", Pt(12.5), Pt(14))
        
        add_bullet_item(tf_l, "<b>Before (设计意图)</b>：\n「我想表现怎样的材质身份？（如：复古光泽设计师玩具）」", Pt(12), Pt(10))
        add_bullet_item(tf_l, "<b>Action (制作行为)</b>：\n「我改变了哪些 Layer、Roughness 或 Metallic 参数？（如：底层黄色 Roughness 0.15，面罩黑色 0.85）」", Pt(12), Pt(10))
        add_bullet_item(tf_l, "<b>After (观察结果)</b>：\n「我观察到了什么具体的反射变化？（如：黄色部分倒影鲜明集中，黑色面罩呈现哑光扩散）」", Pt(12), Pt(0))

        card_r = create_card(slide, Inches(6.8), Inches(1.5), Inches(5.733), Inches(5.3), bg_color=COLOR_ORANGE_BG, border_color=COLOR_ORANGE_BORDER)
        tb_r = slide.shapes.add_textbox(Inches(7.1), Inches(1.7), Inches(5.133), Inches(4.9))
        tf_r = tb_r.text_frame
        tf_r.word_wrap = True
        add_bullet_item(tf_r, "<b>【免作业声明】课堂闭环交付</b>", Pt(17), Pt(12))
        add_bullet_item(tf_r, "<b>01 课堂随堂完成，不留长篇作业</b>：\n三行记录旨在引导学生理清创作思考，直接保存在工程旁或随堂备忘录中，不转化为课后冗长报告。", Pt(12.5), Pt(12))
        add_bullet_item(tf_r, "<b>02 时间紧迫时的剪裁原则</b>：\n若课堂创作时间紧张，优先确保 Slide 18 的工程安全保存，可口头回答三行要点，不把未写完的文字变成隐藏课后作业。", Pt(12.5), Pt(12))
        add_bullet_item(tf_r, "<b>03 教学边界声明</b>：\n轻量收束仅服务于本讲教学节奏，不违背或替代学院教务处的正式课程考核要求。", Pt(11), Pt(0))

    # --------------------------------------------------------------------------
    # Slide 17: 四级反馈漏斗与同桌 30 秒互查
    # --------------------------------------------------------------------------
    elif slide_num == 17:
        card_w = Inches(3.75)
        funnels = [
            ("01 同桌 30 秒互查", "两人并排观察彼此屏幕，快速指出一个做得清楚的亮点、一个需要检查的细节（例如面罩边缘是否有误涂溢出、底层是否误开 Metallic）。\n\n口头反馈，不替对方修改设备。", "同伴诊断 · 30 秒闭环"),
            ("02 快捷键 C 单通道诊断", "当外观异常或金属感不对时，按键盘 C 键循环查看各 Material Channel：\n• Base Color：检查固有色是否纯正\n• Metallic：重点检查是否全黑(=0)\n• Roughness：检查明暗参数分布", "单通道透视诊断"),
            ("03 快捷键 M 返回材质视图", "诊断完成后，按键盘 M 键立即返回完整的 Material 材质光照视图。\n\n警示提醒：按 B 键是进入 Mesh Maps (烘焙网格贴图) 模式，切勿与材质视图混淆！", "返回完整视口 · 辨析 B/M 键")
        ]
        for i, (f_title, f_desc, f_tag) in enumerate(funnels):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), card_w, Inches(4.0))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), card_w - Inches(0.4), Inches(3.6))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, f"<b>{f_title}</b>", Pt(15), Pt(10))
            add_bullet_item(tf, f_desc, Pt(12), Pt(12))
            add_bullet_item(tf, f"<b>核心原则</b>：{f_tag}", Pt(11), Pt(0))

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
        steps_18 = [
            ("第一步：规范另存为工程", "在菜单栏点击 File → Save As，保存为独立的 Painter 工程文件 (.spp)。\n\n使用简短、英文字母且具备识别度的命名（如 MeetMat_Head_W1.spp），保存在个人固定目录。", "关键：保存可编辑 .spp 工程"),
            ("第二步：关闭软件重开验证", "在课堂内彻底关闭 Substance 3D Painter 软件，重新启动并打开刚才保存的 .spp 工程。\n\n亲眼确认：Head 纹理集、两个 Fill Layer、黑白遮罩均完整恢复且仍可编辑！", "关键：打破“保存成功提示假象”"),
            ("第三步：截图存档与下讲预告", "调整满意角度，截取高清晰度材质效果图。工程与截图按课堂指导提交备份。\n\n下讲预告：第 2 讲《塑料材质进阶与 ID 分区制作》（从双层走向复杂零件结构）。", "关键：交付可追溯工程作品")
        ]
        for i, (t18, d18, tag18) in enumerate(steps_18):
            x = Inches(0.8) + i * Inches(4.0)
            create_card(slide, x, Inches(1.5), step_w, Inches(3.8))
            tb = slide.shapes.add_textbox(x + Inches(0.2), Inches(1.7), step_w - Inches(0.4), Inches(3.4))
            tf = tb.text_frame
            tf.word_wrap = True
            add_bullet_item(tf, f"<b>{t18}</b>", Pt(15), Pt(10))
            add_bullet_item(tf, d18, Pt(12), Pt(12))
            add_bullet_item(tf, f"<b>执行标准</b>：{tag18}", Pt(11), Pt(0))

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
