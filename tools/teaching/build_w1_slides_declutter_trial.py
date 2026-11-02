#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_w1_slides_declutter_trial.py
《三维数字材质制作》第 1 讲 MeetMat 幻灯片视觉减负试验（Slide 04、08、12、15 重设计）。

遵循原则：
1. "PPT 让学生看懂，Presenter Notes 让教师讲清"；
2. 不改变教学知识点、课堂任务和 160 分钟节奏；
3. 100% 完整保留 Notion v0.3 原版 Presenter Notes；
4. 瑞士/杂志风高反差暗色主题（深夜蓝黑底色，专为暗室视口投影优化，无眩光）；
5. 突出大图、材料对比、真实操作截图与核心观察/原理提问，消除密集文字卡片；
6. 严格执行 English-first 术语规范与科学边界（Roughness ≠ 几何凹凸，Specular ≠ Diffuse）；
7. 产出：
   - W1_MeetMat_4slides_declutter_trial.pptx
   - W1_MeetMat_4slides_declutter_trial.pdf
   - 逐页 PNG 渲染
   - 新旧版并排对照总览图 W1_MeetMat_4slides_side_by_side_overview.png
"""

import os
import sys
import json
import re
import subprocess
from PIL import Image, ImageDraw, ImageFont

import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

# ==============================================================================
# 画布全局规范与暗色 PBR 调色盘
# ==============================================================================
SLIDE_WIDTH = Inches(13.333333)
SLIDE_HEIGHT = Inches(7.5)

FONT_HEADING = "Microsoft YaHei"
FONT_BODY = "Microsoft YaHei"
FONT_MONO = "Consolas"

# 调色盘：Dark Industrial PBR Blueprint
COLOR_BG = RGBColor(10, 18, 30)              # #0A121E 深邃夜蓝黑
COLOR_CARD_BG = RGBColor(17, 28, 45)         # #111C2D 容器底色
COLOR_CARD_BG_ALT = RGBColor(23, 38, 60)     # #17263C 高亮容器底色
COLOR_CARD_BORDER = RGBColor(34, 56, 84)     # #223854 发丝边框
COLOR_CARD_BORDER_HI = RGBColor(56, 92, 133) # #385C85 强调边框

COLOR_TEXT_MAIN = RGBColor(241, 245, 249)    # #F1F5F9 纯净冰白（高反差）
COLOR_TEXT_BODY = RGBColor(203, 213, 225)    # #CBD5E1 浅灰白正文
COLOR_TEXT_MUTED = RGBColor(148, 163, 184)   # #94A3B8 辅助中灰
COLOR_TEXT_HINT = RGBColor(100, 116, 139)    # #64748B 次要提示灰

COLOR_ACCENT_CYAN = RGBColor(56, 189, 248)   # #38BDF8 电气蓝/青色（观察与路径焦点）
COLOR_ACCENT_AMBER = RGBColor(245, 158, 11)  # #F59E0B 琥珀金（关键提问与参数强调）
COLOR_ACCENT_GREEN = RGBColor(16, 185, 129)  # #10B981 完成检查绿
COLOR_ACCENT_ROSE = RGBColor(244, 63, 94)    # #F43F5E 警示粉红

COLOR_PILL_BG = RGBColor(24, 44, 66)         # #182C42 章节标签底色
COLOR_PILL_BORDER = RGBColor(40, 70, 105)    # #284669 章节标签描边
COLOR_DIVIDER = RGBColor(27, 45, 68)         # #1B2D44 底部细分割线

# ==============================================================================
# 基础组件辅助函数
# ==============================================================================
def setup_slide(prs):
    """创建幻灯片并建立深色夜蓝黑背景（底层矩形保险）"""
    slide = prs.slides.add_slide(prs.slide_layouts[6]) # blank layout
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = COLOR_BG

    bg_rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_WIDTH, SLIDE_HEIGHT)
    bg_rect.fill.solid()
    bg_rect.fill.fore_color.rgb = COLOR_BG
    bg_rect.line.fill.background()
    return slide

def create_card(slide, left, top, width, height,
                bg_color=COLOR_CARD_BG,
                border_color=COLOR_CARD_BORDER,
                border_width=Pt(1)):
    """绘制圆角矩形卡片容器"""
    card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left, top, width, height)
    card.fill.solid()
    card.fill.fore_color.rgb = bg_color
    if border_color:
        card.line.color.rgb = border_color
        card.line.width = border_width
    else:
        card.line.fill.background()
    return card

def add_header(slide, slide_num, short_title, pill_label, block_label="Block 1"):
    """绘制标准化幻灯片顶部导航、Pill 徽章与主标题"""
    # 顶部面包屑
    crumb_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.24), Inches(7.5), Inches(0.26))
    tf_c = crumb_box.text_frame
    tf_c.word_wrap = True
    tf_c.margin_left = tf_c.margin_top = tf_c.margin_right = tf_c.margin_bottom = 0
    p_c = tf_c.paragraphs[0]
    p_c.text = "GR2102  /  三维数字材质制作  /  第 1 讲"
    p_c.font.name = FONT_HEADING
    p_c.font.size = Pt(10.5)
    p_c.font.color.rgb = COLOR_TEXT_MUTED

    # 顶部右侧周次标识
    badge_box = slide.shapes.add_textbox(Inches(9.0), Inches(0.24), Inches(3.533), Inches(0.26))
    tf_b = badge_box.text_frame
    tf_b.word_wrap = True
    tf_b.margin_left = tf_b.margin_top = tf_b.margin_right = tf_b.margin_bottom = 0
    p_b = tf_b.paragraphs[0]
    p_b.alignment = PP_ALIGN.RIGHT
    p_b.text = f"W1 · MEETMAT  ｜  {block_label}"
    p_b.font.name = FONT_HEADING
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_TEXT_MUTED

    # 章节 Pill 徽章
    if pill_label:
        pill_w = Inches(1.15)
        pill_h = Inches(0.30)
        pill_shape = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.58), pill_w, pill_h)
        pill_shape.fill.solid()
        pill_shape.fill.fore_color.rgb = COLOR_PILL_BG
        pill_shape.line.color.rgb = COLOR_PILL_BORDER
        pill_shape.line.width = Pt(1)
        
        tf_pill = pill_shape.text_frame
        tf_pill.word_wrap = False
        tf_pill.margin_left = tf_pill.margin_top = tf_pill.margin_right = tf_pill.margin_bottom = 0
        p_pill = tf_pill.paragraphs[0]
        p_pill.alignment = PP_ALIGN.CENTER
        p_pill.text = pill_label
        p_pill.font.name = FONT_HEADING
        p_pill.font.size = Pt(10)
        p_pill.font.bold = True
        p_pill.font.color.rgb = COLOR_ACCENT_CYAN

    # 主标题
    title_box = slide.shapes.add_textbox(Inches(2.2), Inches(0.54), Inches(10.333), Inches(0.42))
    tf_t = title_box.text_frame
    tf_t.word_wrap = True
    tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0
    p_t = tf_t.paragraphs[0]
    p_t.text = short_title
    p_t.font.name = FONT_HEADING
    p_t.font.size = Pt(20)
    p_t.font.bold = True
    p_t.font.color.rgb = COLOR_TEXT_MAIN

def add_footer(slide, slide_num, total_slides=18):
    """绘制标准化底部细线、审校标识与页码"""
    line_y = Inches(6.92)
    divider = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), line_y, Inches(11.733), Pt(1))
    divider.fill.solid()
    divider.fill.fore_color.rgb = COLOR_DIVIDER
    divider.line.fill.background()

    notice_box = slide.shapes.add_textbox(Inches(0.8), Inches(7.02), Inches(9.0), Inches(0.24))
    tf_n = notice_box.text_frame
    tf_n.word_wrap = True
    tf_n.margin_left = tf_n.margin_top = tf_n.margin_right = tf_n.margin_bottom = 0
    p_n = tf_n.paragraphs[0]
    p_n.text = "视觉减负试验版 · 聚焦大图对比与核心认知 · Presenter Notes 完整保留"
    p_n.font.name = FONT_BODY
    p_n.font.size = Pt(9.5)
    p_n.font.color.rgb = COLOR_TEXT_MUTED

    page_box = slide.shapes.add_textbox(Inches(10.5), Inches(7.02), Inches(2.033), Inches(0.24))
    tf_p = page_box.text_frame
    tf_p.word_wrap = False
    tf_p.margin_left = tf_p.margin_top = tf_p.margin_right = tf_p.margin_bottom = 0
    p_p = tf_p.paragraphs[0]
    p_p.alignment = PP_ALIGN.RIGHT
    p_p.text = f"Slide {slide_num:02d}  /  {total_slides:02d}"
    p_p.font.name = FONT_HEADING
    p_p.font.size = Pt(11)
    p_p.font.bold = True
    p_p.font.color.rgb = COLOR_ACCENT_AMBER

def fit_image_in_box(image_path, max_left, max_top, max_width, max_height):
    """计算图像等比保持最大填充范围的坐标与尺寸，杜绝拉伸"""
    with Image.open(image_path) as img:
        img_w, img_h = img.size
    aspect = img_w / img_h
    box_aspect = max_width / max_height

    if aspect > box_aspect:
        render_w = max_width
        render_h = render_w / aspect
        render_left = max_left
        render_top = max_top + (max_height - render_h) / 2
    else:
        render_h = max_height
        render_w = render_h * aspect
        render_top = max_top
        render_left = max_left + (max_width - render_w) / 2

    return render_left, render_top, render_w, render_h

def set_presenter_notes(slide, notes_raw):
    """将 Notion 权威 Presenter Notes 完整存入幻灯片备注区"""
    clean_notes = re.sub(r'<[^>]+>', '', notes_raw).strip()
    notes_slide = slide.notes_slide
    notes_tf = notes_slide.notes_text_frame
    notes_tf.text = clean_notes

# ==============================================================================
# Slide 04: 材质观察（大图 Duo Compare + 极简观察提问）
# ==============================================================================
def build_slide_04(prs, data_item):
    """
    Slide 04: 视觉观察前置悬念：单组材质身份对比
    重设计重点：
    1. 两张真实 MeetMat Head 截图作为绝对视觉主体，大幅拉伸铺展；
    2. 投影文字聚焦一个核心观察问题：“两种材料的反射有什么不同？”；
    3. 清理三栏密集文字卡，仅保留直观高光对比观察点；
    4. 底部保留关键思考：“为什么真实高光会跑，画在 Base Color 里的白斑不会？”
    """
    slide = setup_slide(prs)
    add_header(slide, 4, "同一个 Head，两种材质外观", "材质观察", "Block 1 · 约 5 分钟")
    add_footer(slide, 4, 18)

    # 1. 核心提问横幅（极度醒目，引发全班聚焦）
    q_card = create_card(slide, Inches(0.8), Inches(1.08), Inches(11.733), Inches(0.66),
                         bg_color=COLOR_CARD_BG_ALT, border_color=COLOR_CARD_BORDER_HI)
    tb_q = slide.shapes.add_textbox(Inches(1.0), Inches(1.16), Inches(11.333), Inches(0.50))
    tf_q = tb_q.text_frame
    tf_q.word_wrap = True
    tf_q.margin_left = tf_q.margin_top = tf_q.margin_right = tf_q.margin_bottom = 0
    p_q = tf_q.paragraphs[0]
    p_q.text = "核心观察提问：两种材料的反射有什么不同？"
    p_q.font.name = FONT_HEADING
    p_q.font.size = Pt(20)
    p_q.font.bold = True
    p_q.font.color.rgb = COLOR_ACCENT_AMBER

    # 2. 左右并排大图容器 (Duo Compare)
    card_w = Inches(5.72)
    card_h = Inches(4.35)
    card_top = Inches(1.88)

    img_items = data_item["embedded_images"]

    # --- 左侧卡片：光洁塑料 ---
    left_c = Inches(0.8)
    create_card(slide, left_c, card_top, card_w, card_h, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)

    # 标签条
    tb_l_tag = slide.shapes.add_textbox(left_c + Inches(0.2), card_top + Inches(0.12), card_w - Inches(0.4), Inches(0.32))
    tf_lt = tb_l_tag.text_frame
    p_lt = tf_lt.paragraphs[0]
    p_lt.text = "A. 光洁黄色塑料 (Glossy Plastic)"
    p_lt.font.name = FONT_HEADING
    p_lt.font.size = Pt(14)
    p_lt.font.bold = True
    p_lt.font.color.rgb = COLOR_TEXT_MAIN

    # 图片嵌入
    img_l_path = img_items[0]["path"]
    rl, rt, rw, rh = fit_image_in_box(img_l_path, left_c + Inches(0.2), card_top + Inches(0.48), card_w - Inches(0.4), Inches(3.30))
    slide.shapes.add_picture(img_l_path, rl, rt, rw, rh)

    # 底部观察结论要点
    tb_l_sub = slide.shapes.add_textbox(left_c + Inches(0.2), card_top + Inches(3.85), card_w - Inches(0.4), Inches(0.38))
    tf_ls = tb_l_sub.text_frame
    p_ls = tf_ls.paragraphs[0]
    p_ls.text = "▶ 观察焦点：高光边界锐利集中 · 能辨认清晰的环境倒影"
    p_ls.font.name = FONT_BODY
    p_ls.font.size = Pt(11)
    p_ls.font.bold = True
    p_ls.font.color.rgb = COLOR_ACCENT_CYAN

    # --- 右侧卡片：粗糙陶土 ---
    right_c = Inches(6.813)
    create_card(slide, right_c, card_top, card_w, card_h, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)

    tb_r_tag = slide.shapes.add_textbox(right_c + Inches(0.2), card_top + Inches(0.12), card_w - Inches(0.4), Inches(0.32))
    tf_rt = tb_r_tag.text_frame
    p_rt = tf_rt.paragraphs[0]
    p_rt.text = "B. 粗糙暗哑陶土 (Rough Clay)"
    p_rt.font.name = FONT_HEADING
    p_rt.font.size = Pt(14)
    p_rt.font.bold = True
    p_rt.font.color.rgb = COLOR_TEXT_MAIN

    img_r_path = img_items[1]["path"]
    rl, rt, rw, rh = fit_image_in_box(img_r_path, right_c + Inches(0.2), card_top + Inches(0.48), card_w - Inches(0.4), Inches(3.30))
    slide.shapes.add_picture(img_r_path, rl, rt, rw, rh)

    tb_r_sub = slide.shapes.add_textbox(right_c + Inches(0.2), card_top + Inches(3.85), card_w - Inches(0.4), Inches(0.38))
    tf_rs = tb_r_sub.text_frame
    p_rs = tf_rs.paragraphs[0]
    p_rs.text = "▶ 观察焦点：高光宽柔模糊 · 镜面反射弥散开来、倒影边界消融"
    p_rs.font.name = FONT_BODY
    p_rs.font.size = Pt(11)
    p_rs.font.bold = True
    p_rs.font.color.rgb = COLOR_ACCENT_CYAN

    # 3. 底部思考条（悬念收束）
    bottom_card = create_card(slide, Inches(0.8), Inches(6.32), Inches(11.733), Inches(0.48),
                              bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)
    tb_b = slide.shapes.add_textbox(Inches(1.0), Inches(6.38), Inches(11.333), Inches(0.36))
    tf_b = tb_b.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "03 核心思考：为什么真实高光会随照明与观察角度自然位移，而画在 Base Color 里的白斑永远是一块死图？"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.color.rgb = COLOR_TEXT_MUTED

    set_presenter_notes(slide, data_item["notes_raw"])

# ==============================================================================
# Slide 08: Painter 操作示范（Hero Screenshot + 少量编号操作流）
# ==============================================================================
def build_slide_08(prs, data_item):
    """
    Slide 08: 教师示范一：底漆填充层与 Roughness
    重设计重点：
    1. 截图大幅放大至中央主视觉（Hero Screenshot），让后排看清 Head、Layers、Properties；
    2. 侧边采用高反差 3 步操作徽标（01 选 Head → 02 建 Fill Layer → 03 调参数）；
    3. 保留学生跟练关键路径，排错细节与原理保留在 Presenter Notes。
    """
    slide = setup_slide(prs)
    add_header(slide, 8, "教师示范：新建底漆填充层与 Roughness", "教师示范", "Block 2 · 约 5 分钟")
    add_footer(slide, 8, 18)

    # 1. 顶部操作目标条
    sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.08), Inches(11.733), Inches(0.34))
    tf_s = sub_box.text_frame
    p_s = tf_s.paragraphs[0]
    p_s.text = "操作目标：在 Head 上建立第一个规范填充层 Plastic_Base，并比较 Roughness 0.10 与 0.85"
    p_s.font.name = FONT_HEADING
    p_s.font.size = Pt(13)
    p_s.font.bold = True
    p_s.font.color.rgb = COLOR_ACCENT_CYAN

    # 2. 左侧紧凑编号操作流 (3 步徽标卡片，宽 3.5 英寸)
    left_x = Inches(0.8)
    left_w = Inches(3.5)
    steps = [
        ("01", "选中对象", "Texture Set List", "确认当前激活的是 Head 纹理集，避免误画到 Body/Base。"),
        ("02", "新建图层", "Layers 面板", "点击油漆桶图标创建 Fill Layer，双击重命名为 Plastic_Base。"),
        ("03", "通道参数", "Properties - Fill", "Base Color = 明黄色；Metallic = 0；对比 Roughness 0.10 vs 0.85。")
    ]

    card_y = Inches(1.50)
    card_h = Inches(1.45)
    gap_y = Inches(0.18)

    for i, (num, action_title, panel_name, desc) in enumerate(steps):
        top_y = card_y + i * (card_h + gap_y)
        card = create_card(slide, left_x, top_y, left_w, card_h, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)

        tb = slide.shapes.add_textbox(left_x + Inches(0.16), top_y + Inches(0.12), left_w - Inches(0.32), card_h - Inches(0.24))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0

        p1 = tf.paragraphs[0]
        p1.text = f"[{num}]  {action_title}"
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(13)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_ACCENT_AMBER if i == 2 else COLOR_ACCENT_CYAN

        p2 = tf.add_paragraph()
        p2.text = f"面板：{panel_name}"
        p2.font.name = FONT_MONO
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_TEXT_MUTED

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.name = FONT_BODY
        p3.font.size = Pt(10.5)
        p3.font.color.rgb = COLOR_TEXT_BODY

    # 3. 右侧大幅放大 Painter GUI 截图 (Hero Screenshot, 宽 8.0 英寸)
    right_x = Inches(4.5)
    right_w = Inches(8.033)
    right_h = Inches(4.71)

    create_card(slide, right_x, Inches(1.50), right_w, right_h, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)

    img_item = data_item["embedded_images"][0]
    img_path = img_item["path"]
    rl, rt, rw, rh = fit_image_in_box(img_path, right_x + Inches(0.12), Inches(1.50) + Inches(0.12), right_w - Inches(0.24), right_h - Inches(0.24))
    slide.shapes.add_picture(img_path, rl, rt, rw, rh)

    # 4. 底部贴士与恢复条
    bottom_card = create_card(slide, Inches(0.8), Inches(6.32), Inches(11.733), Inches(0.48),
                              bg_color=COLOR_CARD_BG_ALT, border_color=COLOR_CARD_BORDER_HI)
    tb_b = slide.shapes.add_textbox(Inches(1.0), Inches(6.38), Inches(11.333), Inches(0.36))
    tf_b = tb_b.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "★ 示范收尾值：设回 Roughness = 0.15 ｜ 排错提醒：若未看到黄色变化，先检查 Texture Set 选中项与图层显隐"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_ACCENT_GREEN

    set_presenter_notes(slide, data_item["notes_raw"])

# ==============================================================================
# Slide 12: Roughness 原理（Microfacet Hero + 核心因果提问）
# ==============================================================================
def build_slide_12(prs, data_item):
    """
    Slide 12: 理论升华一：微表面为什么改变反射？
    重设计重点：
    1. 现有经典 Microfacet 原理图作为视觉主体铺展；
    2. 顶部突出核心因果提问：“为什么黄色没有改变，高光的清晰度却变了？”；
    3. 侧边放置极简的 Smooth vs Rough 光学反射分布因果链；
    4. 严格恪守科学边界：Roughness ≠ 几何凹凸，Roughness ≠ Normal Map。
    """
    slide = setup_slide(prs)
    add_header(slide, 12, "微表面为什么改变反射？", "理论升华", "Block 4 · 约 5 分钟")
    add_footer(slide, 12, 18)

    # 1. 核心理论提问横幅
    q_card = create_card(slide, Inches(0.8), Inches(1.08), Inches(11.733), Inches(0.66),
                         bg_color=COLOR_CARD_BG_ALT, border_color=COLOR_CARD_BORDER_HI)
    tb_q = slide.shapes.add_textbox(Inches(1.0), Inches(1.16), Inches(11.333), Inches(0.50))
    tf_q = tb_q.text_frame
    p_q = tf_q.paragraphs[0]
    p_q.text = "核心思考：为什么 Base Color 黄色没有变，高光的清晰度却变了？"
    p_q.font.name = FONT_HEADING
    p_q.font.size = Pt(19)
    p_q.font.bold = True
    p_q.font.color.rgb = COLOR_ACCENT_AMBER

    # 2. 左侧大幅 Microfacet 原理图容器 (Hero Image, 宽 7.6 英寸)
    left_x = Inches(0.8)
    left_w = Inches(7.6)
    main_h = Inches(4.35)
    main_y = Inches(1.88)

    create_card(slide, left_x, main_y, left_w, main_h, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)

    img_item = data_item["embedded_images"][0]
    img_path = img_item["path"]
    rl, rt, rw, rh = fit_image_in_box(img_path, left_x + Inches(0.15), main_y + Inches(0.15), left_w - Inches(0.3), main_h - Inches(0.5))
    slide.shapes.add_picture(img_path, rl, rt, rw, rh)

    # 图片审校状态题注（严格合规）
    tb_cap = slide.shapes.add_textbox(left_x + Inches(0.2), main_y + main_h - Inches(0.36), left_w - Inches(0.4), Inches(0.30))
    tf_cap = tb_cap.text_frame
    p_cap = tf_cap.paragraphs[0]
    p_cap.text = "【经典教学图表 · Microfacet 微表面方向分布与镜面反射散射示意】"
    p_cap.font.name = FONT_BODY
    p_cap.font.size = Pt(9.5)
    p_cap.font.color.rgb = COLOR_TEXT_MUTED

    # 3. 右侧因果逻辑卡片（两栏对比，宽 3.88 英寸）
    right_x = Inches(8.65)
    right_w = Inches(3.883)
    card_half_h = Inches(2.08)

    # --- 上卡：Smooth ---
    create_card(slide, right_x, main_y, right_w, card_half_h, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)
    tb_s = slide.shapes.add_textbox(right_x + Inches(0.18), main_y + Inches(0.14), right_w - Inches(0.36), card_half_h - Inches(0.28))
    tf_s = tb_s.text_frame
    tf_s.word_wrap = True
    p_s1 = tf_s.paragraphs[0]
    p_s1.text = "光滑表面 (Smooth / Low Roughness)"
    p_s1.font.name = FONT_HEADING
    p_s1.font.size = Pt(13)
    p_s1.font.bold = True
    p_s1.font.color.rgb = COLOR_ACCENT_CYAN

    p_s2 = tf_s.add_paragraph()
    p_s2.text = "• 微平面法线 (Microfacet Normal) 朝向一致\n• 镜面反射 (Specular Reflection) 集中在窄角度\n• 视口表现：锐利高光、清晰倒影"
    p_s2.font.name = FONT_BODY
    p_s2.font.size = Pt(10.5)
    p_s2.font.color.rgb = COLOR_TEXT_BODY

    # --- 下卡：Rough ---
    card_r_top = main_y + Inches(2.27)
    create_card(slide, right_x, card_r_top, right_w, card_half_h, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)
    tb_r = slide.shapes.add_textbox(right_x + Inches(0.18), card_r_top + Inches(0.14), right_w - Inches(0.36), card_half_h - Inches(0.28))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p_r1 = tf_r.paragraphs[0]
    p_r1.text = "粗糙表面 (Rough / High Roughness)"
    p_r1.font.name = FONT_HEADING
    p_r1.font.size = Pt(13)
    p_r1.font.bold = True
    p_r1.font.color.rgb = COLOR_ACCENT_AMBER

    p_r2 = tf_r.add_paragraph()
    p_r2.text = "• 微平面法线朝向随机杂乱偏转\n• 镜面反射光线向各方向弥散开来\n• 视口表现：宽柔模糊白晕、倒影消融"
    p_r2.font.name = FONT_BODY
    p_r2.font.size = Pt(10.5)
    p_r2.font.color.rgb = COLOR_TEXT_BODY

    # 4. 底部科学边界提醒条（守护学术严谨性）
    bottom_card = create_card(slide, Inches(0.8), Inches(6.32), Inches(11.733), Inches(0.48),
                              bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)
    tb_b = slide.shapes.add_textbox(Inches(1.0), Inches(6.38), Inches(11.333), Inches(0.36))
    tf_b = tb_b.text_frame
    p_b = tf_b.paragraphs[0]
    p_b.text = "严正科学边界：Roughness 控制的是微平面法线朝向分布，不是宏观几何凹凸，也不等于 Normal Map。"
    p_b.font.name = FONT_BODY
    p_b.font.size = Pt(10.5)
    p_b.font.bold = True
    p_b.font.color.rgb = COLOR_TEXT_MUTED

    set_presenter_notes(slide, data_item["notes_raw"])

# ==============================================================================
# Slide 15: 角色材质创作（视觉参考卡片 + 达标与选做边界）
# ==============================================================================
def build_slide_15(prs, data_item):
    """
    Slide 15: 【独立创作】MeetMat Head 个性化材质定制
    重设计重点：
    1. 彻底淘汰三栏纯文字卡片，采用带有视觉图示的角色身份参考卡（复用合法已有素材）；
    2. 呈现 3 种鲜明材质身份（机甲英雄、工业防护机器人、复古设计师玩具）；
    3. 底部明确标注全员最低必做达标线与进阶选做边界，保障课堂可执行性。
    """
    slide = setup_slide(prs)
    add_header(slide, 15, "【独立创作】MeetMat Head 个性化材质定制", "独立创作", "Block 7 · 约 32 分钟")
    add_footer(slide, 15, 18)

    # 1. 顶部创作导引
    sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.08), Inches(11.733), Inches(0.34))
    tf_s = sub_box.text_frame
    p_s = tf_s.paragraphs[0]
    p_s.text = "创作指导：先构思角色材质身份，再用 Base Color、Roughness 反差与 Black Mask 图案表达意图（限定 Head）"
    p_s.font.name = FONT_HEADING
    p_s.font.size = Pt(12.5)
    p_s.font.bold = True
    p_s.font.color.rgb = COLOR_ACCENT_CYAN

    # 2. 三个角色身份视觉参考卡片 (宽 3.73 英寸, 高 4.30 英寸)
    cards_data = [
        {
            "tag": "身份 01 · 科技感",
            "title": "机甲英雄 (Hero)",
            "img_path": "assets/w1_meetmat/trial_crops/hero_mask_ref.png",
            "mat_trait": "底漆光洁 (Roughness 0.10) ＋ 锐利科技面罩开窗",
            "palette": "配色参考：红黄 / 黑金高对比"
        },
        {
            "tag": "身份 02 · 工业感",
            "title": "工业防护机器人 (Hazard)",
            "img_path": "assets/w1_meetmat/img_03_1793170142855.png",
            "mat_trait": "底漆哑光耐磨 (Roughness 0.85) ＋ 警示分区与橡胶感",
            "palette": "配色参考：工程警示黄黑 / 哑光灰"
        },
        {
            "tag": "身份 03 · 潮玩感",
            "title": "复古设计师玩具 (Art Toy)",
            "img_path": "assets/w1_meetmat/trial_crops/art_toy_ref.png",
            "mat_trait": "微哑光软胶或陶瓷质感 (Roughness 0.35) ＋ 趣味几何遮罩",
            "palette": "配色参考：低饱和莫兰迪色系 / 柔和几何"
        }
    ]

    card_y = Inches(1.50)
    card_w = Inches(3.733)
    card_h = Inches(4.30)
    gap_x = Inches(0.266)

    for i, c in enumerate(cards_data):
        c_left = Inches(0.8) + i * (card_w + gap_x)
        create_card(slide, c_left, card_y, card_w, card_h, bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)

        # 身份标签与标题
        tb_t = slide.shapes.add_textbox(c_left + Inches(0.18), card_y + Inches(0.12), card_w - Inches(0.36), Inches(0.50))
        tf_t = tb_t.text_frame
        tf_t.word_wrap = True
        tf_t.margin_left = tf_t.margin_top = tf_t.margin_right = tf_t.margin_bottom = 0

        p1 = tf_t.paragraphs[0]
        p1.text = c["tag"]
        p1.font.name = FONT_HEADING
        p1.font.size = Pt(10)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_ACCENT_AMBER if i == 0 else (COLOR_ACCENT_CYAN if i == 1 else COLOR_ACCENT_GREEN)

        p2 = tf_t.add_paragraph()
        p2.text = c["title"]
        p2.font.name = FONT_HEADING
        p2.font.size = Pt(15)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_TEXT_MAIN

        # 视觉参考图片（居中等比）
        img_box_y = card_y + Inches(0.68)
        img_box_h = Inches(2.20)
        rl, rt, rw, rh = fit_image_in_box(c["img_path"], c_left + Inches(0.18), img_box_y, card_w - Inches(0.36), img_box_h)
        slide.shapes.add_picture(c["img_path"], rl, rt, rw, rh)

        # 材质特征说明
        tb_m = slide.shapes.add_textbox(c_left + Inches(0.18), card_y + Inches(2.98), card_w - Inches(0.36), Inches(1.15))
        tf_m = tb_m.text_frame
        tf_m.word_wrap = True
        tf_m.margin_left = tf_m.margin_top = tf_m.margin_right = tf_m.margin_bottom = 0

        pm1 = tf_m.paragraphs[0]
        pm1.text = c["mat_trait"]
        pm1.font.name = FONT_BODY
        pm1.font.size = Pt(10.5)
        pm1.font.color.rgb = COLOR_TEXT_BODY

        pm2 = tf_m.add_paragraph()
        pm2.text = c["palette"]
        pm2.font.name = FONT_BODY
        pm2.font.size = Pt(10)
        pm2.font.color.rgb = COLOR_TEXT_MUTED

    # 3. 底部达标检查与选做边界条（双区明确，保护学生节奏）
    bottom_y = Inches(5.92)
    # 左边：全员达标线（宽 8.6 英寸）
    req_w = Inches(8.6)
    create_card(slide, Inches(0.8), bottom_y, req_w, Inches(0.88), bg_color=COLOR_CARD_BG_ALT, border_color=COLOR_ACCENT_GREEN)

    tb_req = slide.shapes.add_textbox(Inches(0.96), bottom_y + Inches(0.08), req_w - Inches(0.32), Inches(0.72))
    tf_req = tb_req.text_frame
    tf_req.word_wrap = True
    p_r1 = tf_req.paragraphs[0]
    p_r1.text = "✓ 【全员必做达标线】限 Head 区域 ｜ 约 32 分钟"
    p_r1.font.name = FONT_HEADING
    p_r1.font.size = Pt(11)
    p_r1.font.bold = True
    p_r1.font.color.rgb = COLOR_ACCENT_GREEN

    p_r2 = tf_req.add_paragraph()
    p_r2.text = "1. 能陈述设计意图  2. 两层非金属 Fill Layer (Metallic=0)  3. 显著 Roughness 反差  4. 遮罩边缘干净  5. 完整保存工程"
    p_r2.font.name = FONT_BODY
    p_r2.font.size = Pt(10)
    p_r2.font.color.rgb = COLOR_TEXT_MAIN

    # 右边：选做边界（宽 2.9 英寸）
    opt_w = Inches(2.933)
    opt_x = Inches(9.6)
    create_card(slide, opt_x, bottom_y, opt_w, Inches(0.88), bg_color=COLOR_CARD_BG, border_color=COLOR_CARD_BORDER)

    tb_opt = slide.shapes.add_textbox(opt_x + Inches(0.14), bottom_y + Inches(0.08), opt_w - Inches(0.28), Inches(0.72))
    tf_opt = tb_opt.text_frame
    tf_opt.word_wrap = True
    p_o1 = tf_opt.paragraphs[0]
    p_o1.text = "+ 【进阶选做】（不设评分优势）"
    p_o1.font.name = FONT_HEADING
    p_o1.font.size = Pt(10.5)
    p_o1.font.bold = True
    p_o1.font.color.rgb = COLOR_ACCENT_CYAN

    p_o2 = tf_opt.add_paragraph()
    p_o2.text = "快速完成者可选做面罩 Metallic = 1 或绘制印章；不增加课时。"
    p_o2.font.name = FONT_BODY
    p_o2.font.size = Pt(9.5)
    p_o2.font.color.rgb = COLOR_TEXT_MUTED

    set_presenter_notes(slide, data_item["notes_raw"])

def ensure_trial_crops():
    """从既有合法素材中程序化截取角色参考图，保持自包含与零外部依赖"""
    crop_dir = "assets/w1_meetmat/trial_crops"
    os.makedirs(crop_dir, exist_ok=True)
    hero_crop_path = os.path.join(crop_dir, "hero_mask_ref.png")
    toy_crop_path = os.path.join(crop_dir, "art_toy_ref.png")
    
    # 截取机甲面罩参考 (来自 img_12)
    im12 = Image.open("assets/w1_meetmat/img_12_image.png")
    crop_head = im12.crop((200, 260, 680, 740))
    crop_head.save(hero_crop_path)

    # 截取潮玩设计参考 (来自 img_04 官方 MeetMat)
    im4 = Image.open("assets/w1_meetmat/img_04_image.png")
    crop_toy = im4.crop((30, 30, 260, 435))
    crop_toy.save(toy_crop_path)

# ==============================================================================
# 主执行入口
# ==============================================================================
def main():
    print("=== 开始生成 W1 PPT 视觉减负试验（Slide 04、08、12、15） ===")
    ensure_trial_crops()

    # 1. 读取基础数据源 slides_data.json
    data_path = "assets/w1_meetmat/slides_data.json"
    with open(data_path, "r", encoding="utf-8") as f:
        slides_data = json.load(f)

    data_map = {item["number"]: item for item in slides_data}

    # 2. 初始化 Presentation
    prs = Presentation()
    prs.slide_width = SLIDE_WIDTH
    prs.slide_height = SLIDE_HEIGHT

    # 3. 逐页构建 4 页试验幻灯片
    print("-> 构建 Slide 04: 视觉观察前置悬念（Duo Compare 大图并排）...")
    build_slide_04(prs, data_map[4])

    print("-> 构建 Slide 08: 教师示范一（Hero 截图 + 3 步操作流）...")
    build_slide_08(prs, data_map[8])

    print("-> 构建 Slide 12: 理论升华一（Microfacet 大图 + 因果链）...")
    build_slide_12(prs, data_map[12])

    print("-> 构建 Slide 15: 【独立创作】（角色身份视觉参考卡 + 达标线）...")
    build_slide_15(prs, data_map[15])

    # 4. 保存 PPTX
    out_pptx = "W1_MeetMat_4slides_declutter_trial.pptx"
    prs.save(out_pptx)
    print(f"✓ PPTX 保存成功: {out_pptx}")

    # 5. 导出 PDF
    out_pdf = "W1_MeetMat_4slides_declutter_trial.pdf"
    print("-> 正在调用 LibreOffice 导出 PDF 预览...")
    cmd_pdf = ["/opt/homebrew/bin/soffice", "--headless", "--convert-to", "pdf", out_pptx]
    subprocess.run(cmd_pdf, check=True)
    print(f"✓ PDF 导出成功: {out_pdf}")

    # 6. 使用 pdftoppm 渲染高清单页图片 (150 DPI)
    print("-> 正在渲染 4 页高清预览 PNG...")
    trial_png_dir = "assets/w1_meetmat/trial_slides"
    os.makedirs(trial_png_dir, exist_ok=True)
    cmd_ppm = ["/opt/homebrew/bin/pdftoppm", "-png", "-r", "150", out_pdf, f"{trial_png_dir}/slide"]
    subprocess.run(cmd_ppm, check=True)
    print(f"✓ 页面 PNG 渲染完成，保存在 {trial_png_dir}/")

    # 7. 提取原版 18 页对应 4 页并制作新旧并排对照总览图
    print("-> 正在合成新旧版并排对照总览图...")
    build_side_by_side_overview(trial_png_dir)
    print("=== 全部构建与对比总览生成完成！ ===")

def build_side_by_side_overview(trial_png_dir):
    """提取原版 18 页 PDF 中的对应页，与新版试验页拼接成高分辨率并排对比长图"""
    old_pdf = "W1_MeetMat_18slides_preview.pdf"
    old_png_dir = "assets/w1_meetmat/old_slides_ref"
    os.makedirs(old_png_dir, exist_ok=True)

    # 提取旧版的 Slide 04, 08, 12, 15
    for target in [4, 8, 12, 15]:
        cmd = ["/opt/homebrew/bin/pdftoppm", "-png", "-r", "150", "-f", str(target), "-l", str(target),
               old_pdf, f"{old_png_dir}/old_{target:02d}"]
        subprocess.run(cmd, check=True)

    # 组装 4 行对比图
    # 每行：[旧版图 900宽] + [间距] + [新版图 900宽]，上方带有说明栏
    # 新版图片在 trial_png_dir: slide-1.png, slide-2.png, slide-3.png, slide-4.png
    slide_pairs = [
        (4, f"{old_png_dir}/old_04-04.png", f"{trial_png_dir}/slide-1.png",
         "Slide 04 材质观察", "原版：小图居中、文字卡片拥挤、焦点分散", "新版：大图 Duo Compare 铺展、聚焦核心问题「反射有什么不同？」"),
        (8, f"{old_png_dir}/old_08-08.png", f"{trial_png_dir}/slide-2.png",
         "Slide 08 Painter 示范", "原版：三栏文字挤压右侧截图、UI细节看不清", "新版：大幅放大 Hero 截图、3步操作徽标流、排错细节进 Notes"),
        (12, f"{old_png_dir}/old_12-12.png", f"{trial_png_dir}/slide-3.png",
         "Slide 12 Roughness 原理", "原版：密集理论文字堆叠、Microfacet示意图局促", "新版：Microfacet 大图为主体、核心提问引出 Smooth vs Rough 反射因果"),
        (15, f"{old_png_dir}/old_15-15.png", f"{trial_png_dir}/slide-4.png",
         "Slide 15 角色材质创作", "原版：纯文字三栏、零视觉参考、学生缺乏感官启发", "新版：3组角色身份视觉参考卡、全员必做达标线与进阶选做边界分明")
    ]

    target_w = 900
    target_h = int(target_w * 9 / 16) # 506
    gap_x = 40
    row_header_h = 70
    margin = 40

    total_w = margin * 2 + target_w * 2 + gap_x
    row_total_h = row_header_h + target_h + 30
    total_h = margin * 2 + 100 + len(slide_pairs) * row_total_h

    canvas = Image.new("RGB", (total_w, total_h), (10, 18, 30))
    draw = ImageDraw.Draw(canvas)

    # 尝试加载中文字体
    font_paths = [
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/Library/Fonts/Arial Unicode.ttf"
    ]
    font_title = None
    font_sub = None
    font_card = None
    font_desc = None
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                font_title = ImageFont.truetype(fp, 36)
                font_sub = ImageFont.truetype(fp, 18)
                font_card = ImageFont.truetype(fp, 20)
                font_desc = ImageFont.truetype(fp, 15)
                break
            except Exception:
                pass
    if font_title is None:
        font_title = font_sub = font_card = font_desc = ImageFont.load_default()

    # 绘制大标题
    draw.text((margin, margin), "W1 MeetMat 幻灯片视觉减负试验 · 新旧版并排对照总览", fill=(241, 245, 249), font=font_title)
    draw.text((margin, margin + 48), "核心设计原则：PPT 让学生看懂（大图/操作/提问），Presenter Notes 让教师讲清（因果/排错/原理）", fill=(56, 189, 248), font=font_sub)

    # 循环绘制每一行
    curr_y = margin + 100
    for s_num, old_p, new_p, title_str, old_desc, new_desc in slide_pairs:
        # 行标题背景
        draw.rectangle([(margin, curr_y), (total_w - margin, curr_y + row_header_h - 10)], fill=(17, 28, 45), outline=(34, 56, 84))
        draw.text((margin + 20, curr_y + 10), title_str, fill=(245, 158, 11), font=font_card)
        draw.text((margin + 20, curr_y + 38), f"旧版诊断: {old_desc}", fill=(244, 63, 94), font=font_desc)
        draw.text((margin + target_w + gap_x + 20, curr_y + 38), f"新版改进: {new_desc}", fill=(16, 185, 129), font=font_desc)

        img_y = curr_y + row_header_h

        # 旧版图
        if os.path.exists(old_p):
            im_old = Image.open(old_p).resize((target_w, target_h), Image.Resampling.LANCZOS)
            canvas.paste(im_old, (margin, img_y))
            draw.rectangle([(margin, img_y), (margin + target_w, img_y + target_h)], outline=(244, 63, 94), width=2)

        # 新版图
        if os.path.exists(new_p):
            im_new = Image.open(new_p).resize((target_w, target_h), Image.Resampling.LANCZOS)
            canvas.paste(im_new, (margin + target_w + gap_x, img_y))
            draw.rectangle([(margin + target_w + gap_x, img_y), (margin + target_w * 2 + gap_x, img_y + target_h)], outline=(16, 185, 129), width=2)

        curr_y += row_total_h

    overview_out = "W1_MeetMat_4slides_side_by_side_overview.png"
    canvas.save(overview_out)
    print(f"✓ 并排对照总览图生成成功: {overview_out} ({total_w}x{total_h})")

if __name__ == "__main__":
    main()
