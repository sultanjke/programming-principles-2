import math

R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

a = dx * dx + dy * dy
b = 2 * (x1 * dx + y1 * dy)
c = x1 * x1 + y1 * y1 - R * R

if a < 1e-12:
    print(f"{0.0:.10f}")
else:
    disc = b * b - 4 * a * c
    if disc < 0:
        print(f"{0.0:.10f}")
    else:
        sqrt_disc = math.sqrt(disc)
        t1 = (-b - sqrt_disc) / (2 * a)
        t2 = (-b + sqrt_disc) / (2 * a)

        t1 = max(0.0, min(1.0, t1))
        t2 = max(0.0, min(1.0, t2))

        if t2 > t1:
            length = (t2 - t1) * math.sqrt(a)
            print(f"{length:.10f}")
        else:
            print(f"{0.0:.10f}")
