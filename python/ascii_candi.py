"""
Candi ASCII Generator
Jalankan: python ascii_candi.py --steps 6 --tiers 4 --width 61 --height 22
"""

import argparse

def candi_ascii(width=61, height=22, steps=6, tiers=4):
    canvas = [[" "]*width for _ in range(height)]
    mid = width//2

    def fill_row(y, x1, x2, ch):
        x1 = max(0, min(width-1, x1))
        x2 = max(0, min(width-1, x2))
        if 0 <= y < height and x1 <= x2:
            for x in range(x1, x2+1):
                canvas[y][x] = ch

    y = 1
    w = width-8

    # undakan (steps)
    for s in range(steps):
        x1 = mid - w//2; x2 = mid + w//2
        fill_row(y,   x1, x2, "#")
        fill_row(y+1, x1, x2, "#")
        y += 2
        w = int(w*0.90)

    # tier (bagian atas)
    for t in range(tiers):
        x1 = mid - w//2; x2 = mid + w//2
        fill_row(y,   x1, x2, "=")
        fill_row(y+1, x1, x2, "=")
        y += 2
        w = int(w*0.82)

    # stupa utama
    fill_row(y, mid-1, mid+1, "O"); y += 1
    fill_row(y, mid, mid, "^")

    # garis tanah
    for x in range(width):
        canvas[0][x] = "-"

    lines = ["".join(row) for row in canvas[::-1]]
    return "\n".join(lines)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--steps", type=int, default=6)
    p.add_argument("--tiers", type=int, default=4)
    p.add_argument("--width", type=int, default=61)
    p.add_argument("--height", type=int, default=22)
    args = p.parse_args()
    print(candi_ascii(args.width, args.height, args.steps, args.tiers))
