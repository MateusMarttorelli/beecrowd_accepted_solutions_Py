def clamp(v, lo, hi):
    return max(lo, min(v, hi))

damage = {
    "fire": 200,
    "water": 300,
    "earth": 400,
    "air": 100
}

radius = {
    "fire":  [20, 30, 50],
    "water": [10, 25, 40],
    "earth": [25, 55, 70],
    "air":   [18, 38, 60]
}

T = int(input())

for _ in range(T):
    w, h, x0, y0 = map(int, input().split())
    spell, level, cx, cy = input().split()
    level = int(level)
    cx = int(cx)
    cy = int(cy)

    r = radius[spell][level - 1]

    closest_x = clamp(cx, x0, x0 + w)
    closest_y = clamp(cy, y0, y0 + h)

    dist2 = (closest_x - cx)**2 + (closest_y - cy)**2

    if dist2 <= r*r:
        print(damage[spell])
    else:
        print(0)
