from vector import Vector

try:
    v1 = Vector([0.0, 1.0, 2.0, 3.0, 4.0])
    v2 = Vector((10, 15))
    v3 = v1 + v2
    print(v3)
    v4 = 2 * v3
    print(repr(v4))
    s = v4 * v1
    print(s)
except (TypeError, ValueError) as e:
    print("Error:", e)
