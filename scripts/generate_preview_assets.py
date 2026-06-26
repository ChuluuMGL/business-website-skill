#!/usr/bin/env python3
"""Generate visual preview assets for style and interaction presets."""

from __future__ import annotations

import json
import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
PREVIEW_DIR = ROOT / "assets" / "previews"
STYLE_DIR = PREVIEW_DIR / "styles"
INTERACTION_DIR = PREVIEW_DIR / "interactions"

FONT_REGULAR_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
]
FONT_BOLD_CANDIDATES = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/Helvetica.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf",
]


STYLE_PALETTES = {
    "executive-b2b-trust": {
        "bg": "#F7FAF8",
        "surface": "#FFFFFF",
        "text": "#10211C",
        "muted": "#69766F",
        "accent": "#0E5E43",
        "accent2": "#C9A35D",
        "line": "#DCE5DF",
    },
    "industrial-precision": {
        "bg": "#F3F6F5",
        "surface": "#FFFFFF",
        "text": "#17211D",
        "muted": "#60706A",
        "accent": "#185A6A",
        "accent2": "#6C7A86",
        "line": "#D6E0DD",
    },
    "ai-saas-data-cloud": {
        "bg": "#F6F8FF",
        "surface": "#FFFFFF",
        "text": "#141A2E",
        "muted": "#657089",
        "accent": "#2F6BFF",
        "accent2": "#14B8A6",
        "line": "#D9E2FF",
    },
    "premium-editorial-brand": {
        "bg": "#FAF8F4",
        "surface": "#FFFFFF",
        "text": "#191714",
        "muted": "#746D63",
        "accent": "#8E4D2D",
        "accent2": "#1F2933",
        "line": "#E7DED2",
    },
    "minimal-luxury": {
        "bg": "#F9F7F2",
        "surface": "#FFFFFC",
        "text": "#15130F",
        "muted": "#80796D",
        "accent": "#756145",
        "accent2": "#B99F6B",
        "line": "#E8E0D3",
    },
    "dark-data-command-center": {
        "bg": "#071117",
        "surface": "#0D1B24",
        "text": "#EAF4F1",
        "muted": "#8EA5A0",
        "accent": "#36D399",
        "accent2": "#4EA3FF",
        "line": "#1D343F",
    },
    "sustainable-green-tech": {
        "bg": "#F4FAF6",
        "surface": "#FFFFFF",
        "text": "#10241C",
        "muted": "#61756B",
        "accent": "#198754",
        "accent2": "#2BA8A0",
        "line": "#D8E9DF",
    },
    "bold-creative-agency": {
        "bg": "#FFF7EB",
        "surface": "#FFFFFF",
        "text": "#15110D",
        "muted": "#6F6356",
        "accent": "#EF5B2A",
        "accent2": "#101828",
        "line": "#EBD9C2",
    },
    "public-sector-civic": {
        "bg": "#F7FAFC",
        "surface": "#FFFFFF",
        "text": "#162333",
        "muted": "#667085",
        "accent": "#2563A8",
        "accent2": "#3B7A57",
        "line": "#DDE7F0",
    },
    "fintech-secure": {
        "bg": "#F5F8FA",
        "surface": "#FFFFFF",
        "text": "#101B2D",
        "muted": "#64748B",
        "accent": "#0F766E",
        "accent2": "#1E3A8A",
        "line": "#D9E4EA",
    },
}


def find_font_path(bold: bool = False) -> str | None:
    candidates = FONT_BOLD_CANDIDATES if bold else FONT_REGULAR_CANDIDATES
    for candidate in candidates:
        if Path(candidate).exists():
            return candidate
    return None


def font(size: int, bold: bool = False):
    path = find_font_path(bold)
    if path:
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def hex_rgb(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def blend(a: str, b: str, t: float) -> tuple[int, int, int]:
    ar, ag, ab = hex_rgb(a)
    br, bg, bb = hex_rgb(b)
    return (
        round(ar + (br - ar) * t),
        round(ag + (bg - ag) * t),
        round(ab + (bb - ab) * t),
    )


def rounded(draw: ImageDraw.ImageDraw, box, radius: int, fill, outline=None, width: int = 1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def text(draw: ImageDraw.ImageDraw, xy, value: str, size: int, color, bold: bool = False, anchor=None):
    draw.text(xy, value, font=font(size, bold), fill=color, anchor=anchor)


def line_text(draw, x: int, y: int, width: int, height: int, color, count: int = 3):
    for i in range(count):
        w = int(width * (0.82 - i * 0.16))
        draw.rounded_rectangle((x, y + i * (height + 8), x + w, y + height + i * (height + 8)), 4, fill=color)


def gradient_rect(img: Image.Image, box, c1: str, c2: str, horizontal: bool = True):
    x1, y1, x2, y2 = box
    w = x2 - x1
    h = y2 - y1
    grad = Image.new("RGB", (w, h))
    pixels = grad.load()
    for y in range(h):
        for x in range(w):
            t = x / max(1, w - 1) if horizontal else y / max(1, h - 1)
            pixels[x, y] = blend(c1, c2, t)
    img.paste(grad, (x1, y1))


def draw_browser(draw, img, box, palette):
    x1, y1, x2, y2 = box
    rounded(draw, box, 26, palette["surface"], palette["line"], 2)
    rounded(draw, (x1 + 24, y1 + 22, x1 + 52, y1 + 50), 14, palette["accent"])
    for i, w in enumerate([68, 54, 76]):
        draw.rounded_rectangle((x1 + 74 + i * 98, y1 + 31, x1 + 74 + i * 98 + w, y1 + 41), 5, fill=palette["line"])
    rounded(draw, (x2 - 174, y1 + 21, x2 - 28, y1 + 51), 15, palette["accent"], None)
    text(draw, (x2 - 101, y1 + 36), "CTA", 14, "#FFFFFF", True, "mm")
    draw.line((x1, y1 + 70, x2, y1 + 70), fill=palette["line"], width=2)


def draw_style_preview(style, size=(1280, 820)) -> Image.Image:
    palette = STYLE_PALETTES[style["id"]]
    img = Image.new("RGB", size, palette["bg"])
    draw = ImageDraw.Draw(img)
    w, h = size
    dark = style["id"] == "dark-data-command-center"
    text_color = palette["text"]
    muted = palette["muted"]
    surface = palette["surface"]
    line = palette["line"]
    accent = palette["accent"]
    accent2 = palette["accent2"]

    draw_browser(draw, img, (56, 54, w - 56, h - 54), palette)
    content = (96, 154, w - 96, h - 96)
    x1, y1, x2, y2 = content

    if style["id"] == "executive-b2b-trust":
        text(draw, (x1, y1 + 44), style["name"], 38, text_color, True)
        line_text(draw, x1, y1 + 108, 410, 13, line, 4)
        rounded(draw, (x1, y1 + 232, x1 + 172, y1 + 274), 21, accent)
        rounded(draw, (x1 + 196, y1 + 232, x1 + 370, y1 + 274), 21, "#FFFFFF", accent, 2)
        rounded(draw, (x1 + 500, y1 + 40, x2, y1 + 330), 24, "#FFFFFF", line, 2)
        for i, label in enumerate(["Proof", "Capability", "Process"]):
            bx = x1 + 534 + i * 186
            rounded(draw, (bx, y1 + 78, bx + 150, y1 + 156), 16, "#F7FAF8", line, 2)
            text(draw, (bx + 20, y1 + 106), label, 18, text_color, True)
            draw.rounded_rectangle((bx + 20, y1 + 128, bx + 110, y1 + 138), 5, fill=line)
        for i in range(4):
            by = y1 + 196 + i * 28
            draw.rounded_rectangle((x1 + 538, by, x2 - 42 - i * 34, by + 12), 6, fill="#DCE5DF")
        for i in range(3):
            rounded(draw, (x1 + i * 250, y2 - 130, x1 + 220 + i * 250, y2 - 54), 14, "#FFFFFF", line, 2)
            text(draw, (x1 + 26 + i * 250, y2 - 102), f"Service {i + 1}", 18, text_color, True)
            draw.rounded_rectangle((x1 + 26 + i * 250, y2 - 72, x1 + 160 + i * 250, y2 - 60), 6, fill=line)
    elif style["id"] in {"dark-data-command-center", "ai-saas-data-cloud"}:
        rounded(draw, (x1, y1, x2, y2), 24, surface, line, 2)
        for i in range(0, 8):
            yy = y1 + 36 + i * 58
            draw.line((x1 + 28, yy, x2 - 28, yy), fill=line, width=1)
        text(draw, (x1 + 44, y1 + 52), style["name"], 30, text_color, True)
        line_text(draw, x1 + 46, y1 + 104, 310, 13, line, 3)
        rounded(draw, (x1 + 46, y1 + 218, x1 + 210, y1 + 258), 20, accent)
        rounded(draw, (x1 + 232, y1 + 218, x1 + 390, y1 + 258), 20, blend(surface, accent, 0.18), accent, 1)
        for i in range(4):
            bx = x1 + 460 + (i % 2) * 270
            by = y1 + 62 + (i // 2) * 198
            rounded(draw, (bx, by, bx + 230, by + 158), 18, blend(surface, "#FFFFFF", 0.08), line, 2)
            draw.rounded_rectangle((bx + 22, by + 24, bx + 98, by + 36), 6, fill=accent if i % 2 == 0 else accent2)
            for j in range(5):
                bar_h = 26 + j * 10 + i * 3
                draw.rounded_rectangle((bx + 24 + j * 34, by + 120 - bar_h, bx + 46 + j * 34, by + 120), 6, fill=blend(accent, accent2, j / 4))
        for i in range(3):
            rounded(draw, (x1 + 46 + i * 132, y2 - 120, x1 + 150 + i * 132, y2 - 54), 14, blend(surface, accent, 0.12), line, 1)
            text(draw, (x1 + 70 + i * 132, y2 - 92), f"0{i + 1}", 22, accent, True)
    elif style["id"] in {"industrial-precision", "sustainable-green-tech"}:
        text(draw, (x1, y1 + 26), style["name"], 38, text_color, True)
        line_text(draw, x1, y1 + 84, 390, 13, muted if dark else line, 3)
        rounded(draw, (x1, y1 + 196, x1 + 176, y1 + 238), 21, accent)
        diagram = (x1 + 470, y1 + 34, x2, y1 + 364)
        rounded(draw, diagram, 24, surface, line, 2)
        for i in range(4):
            cx = diagram[0] + 72 + i * 140
            cy = diagram[1] + 160 + int(math.sin(i) * 18)
            draw.ellipse((cx - 28, cy - 28, cx + 28, cy + 28), fill=blend(accent, accent2, i / 4), outline=surface, width=4)
            if i:
                px = diagram[0] + 72 + (i - 1) * 140
                py = diagram[1] + 160 + int(math.sin(i - 1) * 18)
                draw.line((px + 28, py, cx - 28, cy), fill=accent, width=5)
        for i in range(3):
            rounded(draw, (x1 + i * 250, y2 - 130, x1 + 220 + i * 250, y2 - 54), 14, surface, line, 2)
            text(draw, (x1 + 26 + i * 250, y2 - 104), f"Capability {i + 1}", 18, text_color, True)
            draw.rounded_rectangle((x1 + 26 + i * 250, y2 - 72, x1 + 160 + i * 250, y2 - 60), 6, fill=line)
    elif style["id"] in {"premium-editorial-brand", "minimal-luxury"}:
        rounded(draw, (x1, y1, x1 + 440, y2), 24, surface, line, 1)
        gradient_rect(img, (x1 + 470, y1, x2, y2), palette["line"], palette["bg"], False)
        title = "Premium Editorial" if style["id"] == "premium-editorial-brand" else style["name"]
        text(draw, (x1 + 42, y1 + 76), title, 36, text_color, True)
        line_text(draw, x1 + 44, y1 + 168, 320, 12, line, 4)
        rounded(draw, (x1 + 44, y2 - 128, x1 + 218, y2 - 86), 21, accent)
        for i in range(4):
            bx = x1 + 520 + (i % 2) * 260
            by = y1 + 58 + (i // 2) * 228
            rounded(draw, (bx, by, bx + 210, by + 176), 18, blend("#FFFFFF", palette["bg"], 0.28), None)
            draw.rectangle((bx + 22, by + 22, bx + 188, by + 116), fill=blend(accent, accent2, i / 4))
            draw.line((bx + 22, by + 138, bx + 164, by + 138), fill=text_color, width=2)
    elif style["id"] == "bold-creative-agency":
        text(draw, (x1, y1 + 66), "MAKE THE CASE VISIBLE", 52, text_color, True)
        line_text(draw, x1 + 4, y1 + 148, 420, 13, muted, 3)
        rounded(draw, (x1 + 4, y1 + 260, x1 + 192, y1 + 306), 23, accent)
        for i in range(5):
            bx = x1 + 500 + (i % 2) * 230
            by = y1 + 12 + (i // 2) * 145
            rounded(draw, (bx, by, bx + 190, by + 112), 18, blend("#FFFFFF", accent, 0.12 + i * 0.03), accent2 if i == 0 else line, 2)
            draw.rectangle((bx + 20, by + 20, bx + 170, by + 62), fill=accent if i % 2 == 0 else accent2)
    elif style["id"] == "public-sector-civic":
        text(draw, (x1, y1 + 42), style["name"], 40, text_color, True)
        line_text(draw, x1, y1 + 106, 430, 13, line, 4)
        for i in range(6):
            bx = x1 + (i % 3) * 250
            by = y1 + 238 + (i // 3) * 140
            rounded(draw, (bx, by, bx + 214, by + 98), 14, surface, line, 2)
            draw.ellipse((bx + 24, by + 26, bx + 56, by + 58), fill=accent if i % 2 == 0 else accent2)
            line_text(draw, bx + 74, by + 30, 100, 9, line, 2)
        rounded(draw, (x1 + 820, y1 + 38, x2, y2 - 58), 22, blend("#FFFFFF", accent, 0.08), line, 1)
        for i in range(5):
            draw.rounded_rectangle((x1 + 854, y1 + 90 + i * 54, x2 - 40, y1 + 118 + i * 54), 8, fill=blend("#FFFFFF", accent, 0.11))
    elif style["id"] == "fintech-secure":
        text(draw, (x1, y1 + 44), style["name"], 40, text_color, True)
        line_text(draw, x1, y1 + 108, 380, 13, line, 3)
        rounded(draw, (x1, y1 + 228, x1 + 170, y1 + 270), 21, accent)
        rounded(draw, (x1 + 470, y1 + 36, x2, y2 - 42), 24, surface, line, 2)
        for i in range(4):
            bx = x1 + 512 + (i % 2) * 280
            by = y1 + 82 + (i // 2) * 176
            rounded(draw, (bx, by, bx + 238, by + 120), 18, "#FFFFFF", line, 2)
            draw.rounded_rectangle((bx + 22, by + 24, bx + 90, by + 38), 7, fill=accent if i < 2 else accent2)
            draw.arc((bx + 124, by + 24, bx + 202, by + 102), 20, 330, fill=accent, width=9)
            draw.arc((bx + 124, by + 24, bx + 202, by + 102), 330, 380, fill=line, width=9)
    else:
        text(draw, (x1, y1 + 42), style["name"], 40, text_color, True)

    rounded(draw, (x1, y2 - 28, x1 + 14, y2 - 14), 7, accent)
    text(draw, (x1 + 26, y2 - 30), style["tone"], 18, muted)
    return img


def generate_style_assets(styles):
    STYLE_DIR.mkdir(parents=True, exist_ok=True)
    thumbs = []
    for style in styles:
        img = draw_style_preview(style)
        out = STYLE_DIR / f"{style['id']}.png"
        img.save(out, quality=95)
        thumb = img.resize((640, 410), Image.Resampling.LANCZOS)
        thumbs.append((style, thumb))

    overview = Image.new("RGB", (1480, 2520), "#F2F5F4")
    draw = ImageDraw.Draw(overview)
    text(draw, (70, 58), "Business Website Style Presets", 48, "#10211C", True)
    text(draw, (70, 116), "10 practical, premium directions for proposal-grade websites", 24, "#5E6B66")
    col_w = 670
    row_h = 455
    for idx, (style, thumb) in enumerate(thumbs):
        col = idx % 2
        row = idx // 2
        x = 70 + col * col_w
        y = 178 + row * row_h
        rounded(draw, (x, y, x + 630, y + 410), 22, "#FFFFFF", "#DDE5E1", 2)
        overview.paste(thumb.resize((604, 386), Image.Resampling.LANCZOS), (x + 13, y + 12))
        text(draw, (x + 22, y + 354), style["name"], 22, "#101828", True)
        text(draw, (x + 22, y + 382), style["id"], 15, "#667085")
    overview.save(PREVIEW_DIR / "style-overview.png", quality=95)


def make_frame(title: str, subtitle: str = "", size=(640, 360), bg="#F6F8FB"):
    img = Image.new("RGB", size, bg)
    draw = ImageDraw.Draw(img)
    rounded(draw, (18, 18, size[0] - 18, size[1] - 18), 20, "#FFFFFF", "#D8E0E7", 2)
    draw.rounded_rectangle((38, 38, 60, 60), 11, fill="#0E5E43")
    text(draw, (78, 36), title, 22, "#101828", True)
    if subtitle:
        text(draw, (78, 64), subtitle, 14, "#667085")
    draw.line((38, 88, size[0] - 38, 88), fill="#E5EAF0", width=2)
    return img


def make_showcase_frame(title: str, subtitle: str = "", size=(640, 360), bg="#071117"):
    img = Image.new("RGB", size, bg)
    draw = ImageDraw.Draw(img)
    for i in range(0, size[0], 32):
        draw.line((i, 0, i - 80, size[1]), fill="#0C1F28", width=1)
    rounded(draw, (18, 18, size[0] - 18, size[1] - 18), 22, "#0B1720", "#1C3440", 2)
    draw.rounded_rectangle((38, 38, 60, 60), 11, fill="#36D399")
    text(draw, (78, 36), title, 21, "#EAF4F1", True)
    if subtitle:
        text(draw, (78, 64), subtitle, 14, "#8EA5A0")
    draw.line((38, 88, size[0] - 38, 88), fill="#1D343F", width=2)
    return img


def save_gif(frames, path: Path, duration=72):
    path.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(path, save_all=True, append_images=frames[1:], duration=duration, loop=0, optimize=True, disposal=2)


def gif_staggered_reveal():
    frames = []
    for f in range(24):
        img = make_frame("Anime.js staggered reveal", "Cards enter in a readable sequence")
        draw = ImageDraw.Draw(img)
        for i in range(6):
            delay = i * 2
            p = max(0, min(1, (f - delay) / 10))
            yoff = int((1 - p) * 26)
            color = blend("#E8F2EE", "#0E5E43", 0.1 + p * 0.22)
            x = 58 + (i % 3) * 178
            y = 124 + (i // 3) * 96 + yoff
            rounded(draw, (x, y, x + 144, y + 66), 14, color, "#D2E4DC", 1)
            draw.rounded_rectangle((x + 18, y + 18, x + 74, y + 28), 5, fill="#0E5E43")
            draw.rounded_rectangle((x + 18, y + 40, x + 112, y + 48), 4, fill="#B8CEC5")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "animejs-staggered-reveal.gif")


def gif_svg_line_draw():
    frames = []
    points = [(92, 238), (188, 160), (304, 222), (420, 142), (540, 208)]
    for f in range(24):
        img = make_frame("Anime.js SVG line draw", "Process path appears as the section enters")
        draw = ImageDraw.Draw(img)
        total_segments = len(points) - 1
        progress = f / 23 * total_segments
        for i in range(total_segments):
            start = points[i]
            end = points[i + 1]
            if progress >= i + 1:
                draw.line((start, end), fill="#185A6A", width=6)
            elif progress > i:
                t = progress - i
                mid = (round(start[0] + (end[0] - start[0]) * t), round(start[1] + (end[1] - start[1]) * t))
                draw.line((start, mid), fill="#185A6A", width=6)
        for i, p in enumerate(points):
            active = progress >= max(0, i - 0.2)
            draw.ellipse((p[0] - 19, p[1] - 19, p[0] + 19, p[1] + 19), fill="#2BA8A0" if active else "#E5EAF0", outline="#FFFFFF", width=4)
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "animejs-svg-line-draw.gif")


def gif_metric_count_up():
    frames = []
    for f in range(24):
        img = make_frame("Metric count-up", "Use only for confirmed numbers")
        draw = ImageDraw.Draw(img)
        value = round(18 + (86 - 18) * (1 - math.cos(f / 23 * math.pi)) / 2)
        for i, label in enumerate(["Coverage", "Efficiency", "Response"]):
            x = 70 + i * 174
            rounded(draw, (x, 132, x + 136, 236), 18, "#F7FAF8", "#D8E6DF", 2)
            text(draw, (x + 24, 152), f"{max(0, value - i * 8)}%", 32, "#0E5E43", True)
            text(draw, (x + 24, 196), label, 14, "#667085")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "metric-count-up.gif")


def gif_case_filter():
    frames = []
    labels = ["All", "Energy", "SaaS"]
    for f in range(30):
        img = make_frame("Case filter transition", "Filter without breaking the grid")
        draw = ImageDraw.Draw(img)
        active = 0 if f < 10 else 1 if f < 20 else 2
        for i, label in enumerate(labels):
            fill = "#0E5E43" if i == active else "#EFF4F2"
            fg = "#FFFFFF" if i == active else "#31413B"
            rounded(draw, (64 + i * 118, 112, 154 + i * 118, 146), 17, fill)
            text(draw, (109 + i * 118, 129), label, 13, fg, True, "mm")
        for i in range(8):
            visible = active == 0 or i % 3 == active - 1
            shade = "#E7F3EE" if visible else "#F1F3F5"
            outline = "#0E5E43" if visible else "#DDE3E8"
            x = 66 + (i % 4) * 130
            y = 174 + (i // 4) * 68
            rounded(draw, (x, y, x + 104, y + 46), 12, shade, outline, 1)
            draw.rounded_rectangle((x + 14, y + 14, x + 66, y + 22), 4, fill=outline)
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "case-filter-transition.gif")


def gif_sticky_cta():
    frames = []
    for f in range(24):
        img = make_frame("Sticky CTA rail", "Useful on long proposal pages")
        draw = ImageDraw.Draw(img)
        scroll = int(f / 23 * 78)
        for i in range(8):
            y = 112 + i * 48 - scroll
            draw.rounded_rectangle((72, y, 408, y + 24), 7, fill="#EEF2F6")
        rounded(draw, (456, 128, 572, 250), 18, "#0E5E43")
        text(draw, (514, 162), "Talk", 22, "#FFFFFF", True, "mm")
        text(draw, (514, 198), "Plan", 16, "#D7F3E8", True, "mm")
        draw.rounded_rectangle((480, 222, 548, 234), 6, fill="#FFFFFF")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "sticky-cta-rail.gif")


def gif_roi_calculator():
    frames = []
    for f in range(26):
        img = make_frame("ROI calculator feedback", "Inputs update transparent estimates")
        draw = ImageDraw.Draw(img)
        p = f / 25
        knob = 102 + int(320 * p)
        draw.rounded_rectangle((92, 154, 432, 164), 5, fill="#DCE7E2")
        draw.rounded_rectangle((92, 154, knob, 164), 5, fill="#0E5E43")
        draw.ellipse((knob - 13, 148, knob + 13, 174), fill="#0E5E43", outline="#FFFFFF", width=3)
        value = int(120 + p * 460)
        rounded(draw, (458, 126, 572, 214), 16, "#F2F9F6", "#CFE4DA", 2)
        text(draw, (515, 156), f"{value}k", 28, "#0E5E43", True, "mm")
        text(draw, (515, 190), "estimate", 13, "#667085", anchor="mm")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "roi-calculator-feedback.gif")


def gif_image_mask():
    frames = []
    for f in range(24):
        img = make_frame("Premium image mask reveal", "Editorial reveal for real visuals")
        draw = ImageDraw.Draw(img)
        x1, y1, x2, y2 = 78, 126, 356, 260
        rounded(draw, (x1, y1, x2, y2), 18, "#E9E2D6")
        reveal = x1 + int((x2 - x1) * f / 23)
        draw.rectangle((x1, y1, reveal, y2), fill="#8E4D2D")
        for i in range(4):
            draw.rounded_rectangle((406, 140 + i * 26, 552 - i * 22, 152 + i * 26), 6, fill="#E7DED2")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "premium-image-mask-reveal.gif")


def gif_dashboard_sequence():
    frames = []
    for f in range(28):
        img = make_frame("Dashboard panel sequence", "Panels follow product logic")
        draw = ImageDraw.Draw(img)
        panels = [(70, 122, 236, 204), (258, 122, 570, 204), (70, 224, 312, 300), (334, 224, 570, 300)]
        for i, box in enumerate(panels):
            p = max(0, min(1, (f - i * 4) / 9))
            fill = blend("#F3F6F8", "#DDEBFF", p)
            rounded(draw, box, 16, fill, "#CAD7E4", 2)
            bx1, by1, bx2, by2 = box
            for j in range(4):
                h = int((20 + j * 10) * p)
                draw.rounded_rectangle((bx1 + 24 + j * 28, by2 - 20 - h, bx1 + 42 + j * 28, by2 - 20), 5, fill="#2F6BFF")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "dashboard-panel-sequence.gif")


def gif_process_stepper():
    frames = []
    for f in range(30):
        img = make_frame("Process stepper", "Clickable workflow with active states")
        draw = ImageDraw.Draw(img)
        active = min(4, f // 6)
        points = [(96 + i * 112, 176) for i in range(5)]
        draw.line((points[0], points[-1]), fill="#D8E3DE", width=6)
        draw.line((points[0], points[active]), fill="#0E5E43", width=6)
        for i, p in enumerate(points):
            fill = "#0E5E43" if i <= active else "#EFF4F2"
            fg = "#FFFFFF" if i <= active else "#667085"
            draw.ellipse((p[0] - 24, p[1] - 24, p[0] + 24, p[1] + 24), fill=fill, outline="#FFFFFF", width=4)
            text(draw, p, str(i + 1), 16, fg, True, "mm")
        rounded(draw, (180, 228, 460, 278), 14, "#F7FAF8", "#D8E6DF", 2)
        text(draw, (320, 253), f"Step {active + 1} details", 18, "#10211C", True, "mm")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "process-stepper.gif")


def gif_gsap_scroll_storyline():
    frames = []
    for f in range(30):
        img = make_frame("GSAP scroll storyline", "Reserved for complex story pages")
        draw = ImageDraw.Draw(img)
        p = f / 29
        draw.rounded_rectangle((78, 120, 120, 292), 20, fill="#E7ECEF")
        draw.rounded_rectangle((78, 120, 120, 120 + int(172 * p)), 20, fill="#EF5B2A")
        slide = int(80 * math.sin(p * math.pi))
        rounded(draw, (172 + slide, 122, 526 + slide, 274), 22, "#FFF7EB", "#EBD9C2", 2)
        text(draw, (204 + slide, 166), f"Scene {1 + int(p * 3)}", 30, "#15110D", True)
        draw.rounded_rectangle((204 + slide, 212, 420 + slide, 226), 7, fill="#EF5B2A")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "gsap-scroll-storyline.gif")


def gif_product_hotspot():
    frames = []
    dots = [(210, 158), (324, 212), (450, 162)]
    for f in range(30):
        img = make_frame("Product hotspot tour", "Explain real features, not decoration")
        draw = ImageDraw.Draw(img)
        rounded(draw, (88, 120, 504, 270), 20, "#F4F7FA", "#CFDAE6", 2)
        draw.rounded_rectangle((118, 148, 260, 170), 7, fill="#2F6BFF")
        draw.rounded_rectangle((118, 190, 448, 204), 7, fill="#DDE6F2")
        draw.rounded_rectangle((118, 224, 380, 238), 7, fill="#DDE6F2")
        active = (f // 10) % 3
        for i, p in enumerate(dots):
            r = 12 + (6 if i == active and f % 10 < 5 else 0)
            draw.ellipse((p[0] - r, p[1] - r, p[0] + r, p[1] + r), fill="#14B8A6", outline="#FFFFFF", width=3)
        tx, ty = dots[active]
        rounded(draw, (tx + 20, ty - 30, tx + 140, ty + 12), 12, "#101828")
        text(draw, (tx + 80, ty - 9), f"Feature {active + 1}", 13, "#FFFFFF", True, "mm")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "product-hotspot-tour.gif")


def gif_comparison_before_after():
    frames = []
    for f in range(28):
        img = make_frame("Before / after comparison", "Useful only with supported claims")
        draw = ImageDraw.Draw(img)
        x1, y1, x2, y2 = 88, 120, 552, 278
        rounded(draw, (x1, y1, x2, y2), 18, "#D8E3DE")
        split = x1 + int((x2 - x1) * (0.22 + 0.56 * (1 - math.cos(f / 27 * math.pi)) / 2))
        draw.rectangle((x1, y1, split, y2), fill="#8FA39A")
        draw.rectangle((split, y1, x2, y2), fill="#198754")
        draw.line((split, y1, split, y2), fill="#FFFFFF", width=5)
        draw.ellipse((split - 17, 182 - 17, split + 17, 182 + 17), fill="#FFFFFF", outline="#198754", width=3)
        text(draw, (142, 146), "Before", 16, "#FFFFFF", True)
        text(draw, (470, 146), "After", 16, "#FFFFFF", True)
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "comparison-before-after.gif")


def gif_pinned_scroll_storytelling():
    frames = []
    scenes = [
        ("Problem", "#EF5B2A"),
        ("System", "#2F6BFF"),
        ("Proof", "#36D399"),
        ("CTA", "#C9A35D"),
    ]
    for f in range(36):
        img = make_showcase_frame("Pinned scroll storytelling", "GSAP pin + scrub for proposal narratives")
        draw = ImageDraw.Draw(img)
        p = f / 35
        active = min(3, int(p * 4))
        draw.rounded_rectangle((70, 118, 112, 300), 21, fill="#132B35")
        draw.rounded_rectangle((70, 118, 112, 118 + int(182 * p)), 21, fill="#36D399")
        for i, (label, color) in enumerate(scenes):
            y = 122 + i * 43
            fill = color if i <= active else "#203842"
            draw.ellipse((77, y, 105, y + 28), fill=fill, outline="#0B1720", width=3)
            text(draw, (126, y + 4), label, 16, "#EAF4F1" if i == active else "#8EA5A0", i == active)
        card_x = 252 + int(math.sin(p * math.pi * 2) * 38)
        card_y = 126 + int(math.cos(p * math.pi * 2) * 8)
        rounded(draw, (card_x, card_y, card_x + 272, card_y + 148), 24, "#102632", "#2F4D5A", 2)
        text(draw, (card_x + 28, card_y + 42), scenes[active][0], 34, scenes[active][1], True)
        draw.rounded_rectangle((card_x + 30, card_y + 88, card_x + 212, card_y + 102), 7, fill="#24434D")
        draw.rounded_rectangle((card_x + 30, card_y + 118, card_x + 168, card_y + 130), 6, fill="#24434D")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "pinned-scroll-storytelling.gif")


def gif_scroll_scrub_dashboard_morph():
    frames = []
    for f in range(34):
        img = make_showcase_frame("Scroll-scrub dashboard morph", "Metrics transform with scroll position")
        draw = ImageDraw.Draw(img)
        p = f / 33
        rounded(draw, (62, 116, 578, 292), 24, "#0E202B", "#203D49", 2)
        for i in range(5):
            x = 94 + i * 80
            h = int(32 + 90 * (0.35 + 0.65 * math.sin(p * math.pi + i * 0.65) ** 2))
            color = blend("#36D399", "#4EA3FF", i / 4)
            draw.rounded_rectangle((x, 248 - h, x + 36, 248), 8, fill=color)
        cx = 486
        cy = 196
        r = 48
        draw.arc((cx - r, cy - r, cx + r, cy + r), 0, 360, fill="#1E3A44", width=14)
        draw.arc((cx - r, cy - r, cx + r, cy + r), -90, -90 + int(320 * p), fill="#36D399", width=14)
        for i in range(3):
            y = 126 + i * 34
            w = int(84 + 72 * abs(math.sin(p * math.pi + i)))
            draw.rounded_rectangle((94, y, 94 + w, y + 10), 5, fill="#2F6BFF")
        text(draw, (486, 198), f"{int(42 + p * 48)}", 26, "#EAF4F1", True, "mm")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "scroll-scrub-dashboard-morph.gif")


def gif_horizontal_case_wall():
    frames = []
    colors = ["#EF5B2A", "#2F6BFF", "#36D399", "#C9A35D", "#8E4D2D", "#14B8A6"]
    for f in range(34):
        img = make_showcase_frame("Horizontal case wall", "Pinned horizontal work/case browsing")
        draw = ImageDraw.Draw(img)
        p = f / 33
        offset = int(-260 * p)
        for i in range(6):
            x = 72 + i * 128 + offset
            y = 122 + int(math.sin((p + i) * math.pi) * 10)
            rounded(draw, (x, y, x + 106, y + 142), 18, "#102632", "#2A4652", 2)
            draw.rectangle((x + 14, y + 16, x + 92, y + 76), fill=colors[i])
            draw.rounded_rectangle((x + 14, y + 96, x + 82, y + 106), 5, fill="#294650")
            draw.rounded_rectangle((x + 14, y + 118, x + 62, y + 126), 4, fill="#294650")
        draw.rounded_rectangle((74, 300, 566, 306), 3, fill="#1D343F")
        draw.rounded_rectangle((74, 300, 74 + int(492 * p), 306), 3, fill="#36D399")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "horizontal-case-wall.gif")


def gif_shared_layout_transition():
    frames = []
    for f in range(30):
        img = make_frame("Shared layout transition", "Motion layoutId / shared element handoff", bg="#F6F8FF")
        draw = ImageDraw.Draw(img)
        p = (1 - math.cos((f / 29) * math.pi)) / 2
        cards = [(72, 128, 172, 202), (204, 128, 304, 202), (336, 128, 436, 202)]
        for box in cards:
            rounded(draw, box, 14, "#FFFFFF", "#D9E2FF", 2)
        x1 = int(72 + (306 - 72) * p)
        y1 = int(128 + (198 - 128) * p)
        x2 = int(172 + (548 - 172) * p)
        y2 = int(202 + (288 - 202) * p)
        rounded(draw, (x1, y1, x2, y2), 18, "#2F6BFF", "#FFFFFF", 2)
        draw.rounded_rectangle((x1 + 22, y1 + 24, min(x2 - 22, x1 + 146), y1 + 36), 6, fill="#FFFFFF")
        draw.rounded_rectangle((x1 + 22, y1 + 52, min(x2 - 36, x1 + 212), y1 + 62), 5, fill="#BFD1FF")
        if p > 0.42:
            text(draw, (330, 156), "detail view", 17, "#667085")
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "shared-layout-transition.gif")


def gif_threejs_product_orbit():
    frames = []
    for f in range(36):
        img = make_showcase_frame("3D product orbit hero", "Three.js/WebGL only when product or spatial value is real")
        draw = ImageDraw.Draw(img)
        cx, cy = 330, 198
        angle = f / 36 * math.tau
        draw.ellipse((cx - 160, cy - 44, cx + 160, cy + 44), outline="#1D5660", width=3)
        for i in range(3):
            a = angle + i * math.tau / 3
            x = cx + int(math.cos(a) * 154)
            y = cy + int(math.sin(a) * 40)
            size = 18 + int((math.sin(a) + 1) * 7)
            draw.ellipse((x - size, y - size, x + size, y + size), fill=blend("#36D399", "#4EA3FF", i / 2), outline="#EAF4F1", width=2)
        for i in range(3):
            offset = i * 16
            pts = [(cx, cy - 76 + offset), (cx + 72, cy - 34 + offset), (cx, cy + 8 + offset), (cx - 72, cy - 34 + offset)]
            draw.polygon(pts, fill=blend("#102632", "#2F6BFF", 0.25 + i * 0.18), outline="#4EA3FF")
        draw.line((cx, cy - 76, cx, cy + 40), fill="#36D399", width=2)
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "threejs-product-orbit-hero.gif")


def gif_shader_liquid_reveal():
    frames = []
    for f in range(34):
        img = make_showcase_frame("Shader / liquid reveal", "WebGL-style reveal for brand and creative pages")
        draw = ImageDraw.Draw(img)
        p = f / 33
        x1, y1, x2, y2 = 72, 116, 568, 292
        rounded(draw, (x1, y1, x2, y2), 24, "#101828", "#2A4652", 2)
        points = []
        for i in range(34):
            x = x1 + int((x2 - x1) * i / 33)
            wave = math.sin(i * 0.52 + p * math.tau * 2) * 22
            y = int(y1 + (y2 - y1) * p + wave)
            points.append((x, y))
        poly = [(x1, y2)] + points + [(x2, y2)]
        draw.polygon(poly, fill="#EF5B2A")
        for i in range(4):
            draw.arc((154 + i * 74, 134, 254 + i * 74, 234), 20 + f * 8, 220 + f * 8, fill=blend("#36D399", "#4EA3FF", i / 3), width=4)
        text(draw, (104, 150), "Reveal", 34, "#FFFFFF", True)
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "shader-liquid-reveal.gif")


def gif_magnetic_media_hover():
    frames = []
    for f in range(32):
        img = make_frame("Magnetic media hover", "Premium portfolio and case preview behavior", bg="#FFF7EB")
        draw = ImageDraw.Draw(img)
        p = f / 31
        cursor_x = int(102 + 398 * p)
        cursor_y = int(136 + 98 * math.sin(p * math.pi))
        for i in range(4):
            x = 84 + i * 112
            y = 150 + int(math.sin(p * math.pi + i) * 16)
            scale = 1 + 0.18 * max(0, 1 - abs(cursor_x - (x + 44)) / 100)
            w = int(78 * scale)
            h = int(96 * scale)
            rounded(draw, (x, y, x + w, y + h), 16, "#FFFFFF", "#EBD9C2", 2)
            draw.rectangle((x + 14, y + 14, x + w - 14, y + 58), fill="#EF5B2A" if i % 2 == 0 else "#101828")
        draw.ellipse((cursor_x - 11, cursor_y - 11, cursor_x + 11, cursor_y + 11), fill="#101828", outline="#FFFFFF", width=3)
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "magnetic-media-hover.gif")


def gif_orbit_network_map():
    frames = []
    nodes = [(320, 190), (198, 144), (442, 142), (206, 250), (456, 248), (320, 108)]
    for f in range(36):
        img = make_showcase_frame("Interactive orbit network", "Platform ecosystem, AI agents, integrations, or coverage maps")
        draw = ImageDraw.Draw(img)
        p = f / 35
        center = nodes[0]
        for i, n in enumerate(nodes[1:], start=1):
            phase = (p + i / 5) % 1
            alpha_color = blend("#1D343F", "#36D399", 0.35 + 0.65 * math.sin(phase * math.pi) ** 2)
            draw.line((center, n), fill=alpha_color, width=3)
        draw.ellipse((center[0] - 44, center[1] - 44, center[0] + 44, center[1] + 44), fill="#102632", outline="#36D399", width=4)
        text(draw, center, "AI", 26, "#EAF4F1", True, "mm")
        for i, (x, y) in enumerate(nodes[1:], start=1):
            pulse = 8 + int(6 * math.sin((p + i * 0.17) * math.tau) ** 2)
            draw.ellipse((x - pulse, y - pulse, x + pulse, y + pulse), fill=blend("#2F6BFF", "#36D399", i / 5), outline="#EAF4F1", width=2)
        frames.append(img)
    save_gif(frames, INTERACTION_DIR / "interactive-orbit-network.gif")


def generate_interaction_assets():
    INTERACTION_DIR.mkdir(parents=True, exist_ok=True)
    gif_staggered_reveal()
    gif_svg_line_draw()
    gif_metric_count_up()
    gif_case_filter()
    gif_sticky_cta()
    gif_roi_calculator()
    gif_image_mask()
    gif_dashboard_sequence()
    gif_process_stepper()
    gif_gsap_scroll_storyline()
    gif_product_hotspot()
    gif_comparison_before_after()
    gif_pinned_scroll_storytelling()
    gif_scroll_scrub_dashboard_morph()
    gif_horizontal_case_wall()
    gif_shared_layout_transition()
    gif_threejs_product_orbit()
    gif_shader_liquid_reveal()
    gif_magnetic_media_hover()
    gif_orbit_network_map()


def main():
    PREVIEW_DIR.mkdir(parents=True, exist_ok=True)
    styles = json.loads((ROOT / "assets" / "presets" / "design-styles.json").read_text())["presets"]
    generate_style_assets(styles)
    generate_interaction_assets()
    print(f"Generated previews in {PREVIEW_DIR}")


if __name__ == "__main__":
    main()
