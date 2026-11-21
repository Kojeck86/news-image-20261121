#!/usr/bin/env python3
"""Draw the front page of 21 November 2026 as entry.png (1024x1024).

Stories (all reported on Saturday 21 November 2026):
 1. Russia's biggest attack on Ukraine: 400+ drones, 110 missiles; two
    missiles land in Poland; PM Tusk calls it a deliberate provocation.
 2. AI stock sell-off: S&P 500 -3.7% into correction, Nasdaq -5.3%,
    wiping out all of 2026's gains.
 3. ICJ finds Myanmar responsible for genocide against the Rohingya -
    the first time the court has held a state responsible.
 4. UK and EU sign their biggest post-Brexit agreements (food trade,
    carbon markets, youth mobility for 100,000 young Britons).
 5. COP31 climate talks in Antalya run past deadline, deadlocked over
    fossil fuels.
Ticker: Houthi missiles at Riyadh intercepted; daraxonrasib cancer pill
hope (tumours undetectable in 1 in 12); Peru 6.9 quake.
"""

import math
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 233)
INK = (17, 17, 17)
RED = (185, 28, 28)
BLUE = (30, 58, 95)
GOLD = (180, 131, 9)
GREY = (90, 90, 86)
LIGHT = (239, 243, 248)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(text, fnt, max_w, draw):
    """Greedy word wrap; returns list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, x, y, lines, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y


def draw_kyiv(draw, x, y, w, h):
    """Night sky over a city skyline, explosions, missile trails."""
    draw.rectangle([x, y, x + w, y + h], fill=(22, 35, 61))
    stars = [(18, 22), (60, 48), (120, 18), (180, 40), (240, 16), (300, 52),
             (360, 24), (420, 44), (90, 80), (210, 66), (330, 78), (30, 110),
             (150, 96), (270, 108), (390, 92), (450, 30), (45, 150), (400, 130)]
    for sx, sy in stars:
        draw.ellipse([x + sx - 1, y + sy - 1, x + sx + 1, y + sy + 1], fill=(255, 255, 255))
    draw.ellipse([x + w - 78, y + 22, x + w - 38, y + 62], fill=(238, 232, 205))
    # skyline
    base = y + h
    buildings = [(0, 150), (46, 120), (92, 168), (140, 108), (186, 150),
                 (232, 96), (280, 140), (326, 112), (372, 156), (418, 128)]
    for bx, bh in buildings:
        draw.rectangle([x + bx, base - bh, x + bx + 46, base], fill=(11, 18, 32))
    windows = [(12, 60), (30, 90), (58, 40), (76, 70), (104, 52), (122, 88),
               (152, 46), (170, 78), (198, 58), (216, 92), (244, 36), (262, 66),
               (292, 50), (310, 84), (338, 44), (356, 72), (384, 56), (402, 86),
               (430, 48), (448, 80)]
    for wx, wy in windows:
        draw.rectangle([x + wx, base - wy, x + wx + 5, base - wy + 7], fill=(253, 224, 71))
    # explosions
    for ex, ey, r in [(150, 120, 34), (330, 92, 26)]:
        for rr, col in [(r, (220, 38, 38)), (int(r * 0.7), (249, 115, 22)),
                        (int(r * 0.42), (253, 224, 71))]:
            draw.ellipse([x + ex - rr, y + ey - rr, x + ex + rr, y + ey + rr], fill=col)
        for ang in range(0, 360, 45):
            a = math.radians(ang)
            x1 = x + ex + int(math.cos(a) * r)
            y1 = y + ey + int(math.sin(a) * r)
            x2 = x + ex + int(math.cos(a) * (r + 16))
            y2 = y + ey + int(math.sin(a) * (r + 16))
            draw.line([x1, y1, x2, y2], fill=(249, 115, 22), width=3)
    # missile trails
    draw.line([(x + 60, y + 20), (x + 110, y + 90), (x + 138, y + 128)],
              fill=(255, 255, 255), width=3)
    draw.line([(x + 420, y + 12), (x + 370, y + 70), (x + 342, y + 100)],
              fill=(255, 255, 255), width=3)
    draw.ellipse([x + 134, y + 124, x + 142, y + 132], fill=(255, 255, 255))
    draw.ellipse([x + 338, y + 96, x + 346, y + 104], fill=(255, 255, 255))
    # smoke
    for sx, sy, sr in [(90, 236, 34), (300, 244, 40), (200, 250, 30)]:
        draw.ellipse([x + sx - sr, y + sy - sr // 2, x + sx + sr, y + sy + sr // 2],
                     fill=(100, 100, 110))


def draw_chart(draw, x, y, w, h):
    """Falling market chart."""
    draw.rectangle([x, y, x + w, y + h], fill=(255, 255, 255), outline=(200, 200, 196))
    for gy in range(1, 4):
        yy = y + h * gy // 4
        draw.line([(x + 8, yy), (x + w - 8, yy)], fill=(225, 225, 220), width=1)
    pts = [(x + 16, y + 18), (x + 70, y + 30), (x + 120, y + 26), (x + 170, y + 48),
           (x + 220, y + 44), (x + 270, y + 66), (x + 320, y + 62), (x + 370, y + 88),
           (x + 420, y + 84), (x + w - 16, y + h - 14)]
    draw.line(pts, fill=RED, width=4)
    draw.polygon([(x + w - 16, y + h - 14), (x + w - 34, y + h - 30), (x + w - 34, y + h - 12)],
                 fill=RED)
    draw.text((x + 14, y + h - 26), "S&P 500 -3.7%", font=font(SANS_B, 18), fill=RED)


def draw_scales(draw, x, y, w, h):
    """Scales of justice."""
    draw.rectangle([x, y, x + w, y + h], fill=LIGHT, outline=(200, 200, 196))
    cx = x + w // 2
    top = y + 14
    draw.rectangle([cx - 3, top, cx + 3, y + h - 22], fill=BLUE)
    draw.line([(cx - 78, top + 8), (cx + 78, top + 8)], fill=BLUE, width=4)
    draw.ellipse([cx - 7, top - 6, cx + 7, top + 8], fill=GOLD)
    for side in (-1, 1):
        px = cx + side * 78
        draw.line([(px, top + 8), (px - 22, y + h - 52)], fill=BLUE, width=2)
        draw.line([(px, top + 8), (px + 22, y + h - 52)], fill=BLUE, width=2)
        draw.line([(px, top + 8), (px, y + h - 52)], fill=BLUE, width=2)
        draw.arc([px - 26, y + h - 56, px + 26, y + h - 24], 0, 180, fill=GOLD, width=4)
    draw.rectangle([cx - 52, y + h - 22, cx + 52, y + h - 14], fill=BLUE)


def draw_flags(draw, x, y, w, h):
    """Simplified UK and EU flags side by side."""
    draw.rectangle([x, y, x + w, y + h], fill=LIGHT, outline=(200, 200, 196))
    # UK flag (schematic)
    fx, fy, fw, fh = x + 24, y + 26, 180, 68
    draw.rectangle([fx, fy, fx + fw, fy + fh], fill=(1, 33, 105))
    draw.polygon([(fx, fy), (fx + 26, fy), (fx + fw, fy + fh), (fx + fw - 26, fy + fh)], fill=(255, 255, 255))
    draw.polygon([(fx + fw, fy), (fx + fw - 26, fy), (fx, fy + fh), (fx + 26, fy + fh)], fill=(255, 255, 255))
    draw.rectangle([fx + fw // 2 - 13, fy, fx + fw // 2 + 13, fy + fh], fill=(255, 255, 255))
    draw.rectangle([fx, fy + fh // 2 - 13, fx + fw, fy + fh // 2 + 13], fill=(255, 255, 255))
    draw.rectangle([fx + fw // 2 - 8, fy, fx + fw // 2 + 8, fy + fh], fill=(200, 16, 46))
    draw.rectangle([fx, fy + fh // 2 - 8, fx + fw, fy + fh // 2 + 8], fill=(200, 16, 46))
    # EU flag
    ex, ey, ew, eh = x + w - 204, y + 26, 180, 68
    draw.rectangle([ex, ey, ex + ew, ey + eh], fill=(0, 51, 153))
    for i in range(12):
        a = math.radians(i * 30 - 90)
        sx = ex + ew // 2 + int(math.cos(a) * 26)
        sy = ey + eh // 2 + int(math.sin(a) * 22)
        draw.ellipse([sx - 3, sy - 3, sx + 3, sy + 3], fill=(255, 209, 0))


def draw_globe(draw, x, y, w, h):
    """Earth with a rising thermometer."""
    draw.rectangle([x, y, x + w, y + h], fill=LIGHT, outline=(200, 200, 196))
    cx, cy, r = x + 96, y + h // 2 + 4, 46
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(37, 99, 235))
    draw.ellipse([cx - 30, cy - 26, cx - 2, cy - 4], fill=(22, 163, 74))
    draw.ellipse([cx + 4, cy + 6, cx + 32, cy + 30], fill=(22, 163, 74))
    draw.ellipse([cx - 12, cy + 18, cx + 10, cy + 38], fill=(22, 163, 74))
    # thermometer
    tx = x + w - 96
    draw.rounded_rectangle([tx, y + 14, tx + 22, y + h - 34], radius=11,
                           fill=(255, 255, 255), outline=RED, width=3)
    draw.ellipse([tx - 8, y + h - 40, tx + 30, y + h - 18], fill=RED)
    draw.rectangle([tx + 5, y + 34, tx + 17, y + h - 28], fill=RED)
    draw.text((tx + 32, y + 18), "1.5C", font=font(SANS_B, 17), fill=RED)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- masthead ---
    title_f = font(SERIF_B, 96)
    d.text((W // 2, 14), "THE WORLD", font=title_f, fill=INK, anchor="ma")
    date_f = font(SANS_B, 27)
    d.text((W // 2, 118), "SATURDAY  •  21 NOVEMBER 2026", font=date_f, fill=INK, anchor="ma")
    d.line([(32, 152), (W - 32, 152)], fill=INK, width=3)
    d.line([(32, 158), (W - 32, 158)], fill=INK, width=1)

    # --- lead story: Russia / Poland ---
    draw_kyiv(d, 32, 170, 468, 258)
    tx = 524
    kick_f = font(SANS_B, 20)
    d.text((tx, 178), "UKRAINE  •  POLAND", font=kick_f, fill=RED)
    head_f = font(SERIF_B, 50)
    lines = wrap("MISSILES FALL ON POLAND", head_f, 468, d)
    y = draw_lines(d, tx, 206, lines, head_f, INK, 56)
    sum_f = font(SANS, 21)
    summary = ("Russia fires 400+ drones and 110 missiles at Ukraine "
               "overnight. At least 8 killed in Kyiv; two missiles land "
               "in Poland — PM Tusk calls it a deliberate provocation.")
    lines = wrap(summary, sum_f, 468, d)[:4]
    draw_lines(d, tx, y + 8, lines, sum_f, INK, 27)

    d.line([(32, 440), (W - 32, 440)], fill=INK, width=2)

    # --- row 2: markets + ICJ ---
    row2_y = 452
    draw_chart(d, 32, row2_y, 464, 112)
    draw_scales(d, 528, row2_y, 464, 112)
    for cx, kicker, head, summ in [
        (32, "MARKETS", "AI ROUT DRAGS MARKETS INTO CORRECTION",
         "S&P 500 -3.7%, Nasdaq -5.3% — wiping out all of 2026's gains."),
        (528, "JUSTICE  •  THE HAGUE", "MYANMAR GUILTY OF GENOCIDE",
         "World Court: Myanmar must let Rohingya return and pay "
         "reparations — a first."),
    ]:
        y = row2_y + 120
        d.text((cx, y), kicker, font=kick_f, fill=RED)
        hf = font(SERIF_B, 29)
        lines = wrap(head, hf, 464, d)
        y = draw_lines(d, cx, y + 26, lines, hf, INK, 33)
        sf = font(SANS, 19)
        lines = wrap(summ, sf, 464, d)[:2]
        draw_lines(d, cx, y + 6, lines, sf, INK, 24)

    d.line([(32, 722), (W - 32, 722)], fill=INK, width=2)

    # --- row 3: UK-EU + COP31 ---
    row3_y = 734
    draw_flags(d, 32, row3_y, 464, 112)
    draw_globe(d, 528, row3_y, 464, 112)
    for cx, kicker, head, summ in [
        (32, "BRUSSELS", "BIGGEST UK–EU DEAL SINCE BREXIT",
         "Three pacts: food trade, carbon markets, youth mobility "
         "for 100,000 young Britons."),
        (528, "CLIMATE  •  ANTALYA", "CLIMATE TALKS RUN PAST DEADLINE",
         "COP31 in overtime as ~200 nations fail to agree "
         "on fossil fuels."),
    ]:
        y = row3_y + 120
        d.text((cx, y), kicker, font=kick_f, fill=RED)
        hf = font(SERIF_B, 29)
        lines = wrap(head, hf, 464, d)
        y = draw_lines(d, cx, y + 26, lines, hf, INK, 33)
        sf = font(SANS, 19)
        lines = wrap(summ, sf, 464, d)[:2]
        draw_lines(d, cx, y + 6, lines, sf, INK, 24)

    # --- ticker ---
    d.line([(32, 1000), (W - 32, 1000)], fill=INK, width=2)
    tick = ("ALSO: Riyadh intercepts Houthi missiles  •  Cancer pill hope: "
            "tumours vanish in 1 in 12  •  Peru quake 6.9")
    tf_size = 17
    while tf_size > 13:
        tf = font(SANS_B, tf_size)
        if d.textlength(tick, font=tf) <= 960:
            break
        tf_size -= 1
    d.text((W // 2, 1005), tick, font=tf, fill=INK, anchor="ma")

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG")
    print("wrote", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
