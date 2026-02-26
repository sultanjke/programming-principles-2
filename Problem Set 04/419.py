import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1
seg_len = math.sqrt(dx ** 2 + dy ** 2)

a = dx ** 2 + dy ** 2
b = 2 * (x1 * dx + y1 * dy)
c = x1 ** 2 + y1 ** 2 - R ** 2

intersects = False
if a > 1e-12:
    disc = b ** 2 - 4 * a * c
    if disc > 0:
        sqrt_disc = math.sqrt(disc)
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)
        t1c = max(0, min(1, t1))
        t2c = max(0, min(1, t2))
        if t2c > t1c + 1e-12:
            intersects = True

if not intersects:
    print(f"{seg_len:.10f}")
else:
    dA = math.sqrt(x1 ** 2 + y1 ** 2)
    dB = math.sqrt(x2 ** 2 + y2 ** 2)

    tangent_A = math.sqrt(max(0, dA ** 2 - R ** 2))
    tangent_B = math.sqrt(max(0, dB ** 2 - R ** 2))

    angle_A = math.atan2(y1, x1)
    angle_B = math.atan2(y2, x2)

    alpha_A = math.acos(min(1, R / dA))
    alpha_B = math.acos(min(1, R / dB))

    best = float('inf')
    for sA in [-1, 1]:
        for sB in [-1, 1]:
            tA_angle = angle_A + sA * alpha_A
            tB_angle = angle_B + sB * alpha_B

            arc_angle = abs(tA_angle - tB_angle)
            arc_angle = arc_angle % (2 * math.pi)
            if arc_angle > math.pi:
                arc_angle = 2 * math.pi - arc_angle

            arc_len = R * arc_angle
            total = tangent_A + arc_len + tangent_B
            best = min(best, total)

    print(f"{best:.10f}")
