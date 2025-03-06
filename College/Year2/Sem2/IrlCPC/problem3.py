w, h = map(int, input().split(" "))
n = int(input())
components = [tuple(map(int, input().split(" "))) for _ in range(n)]

def colliding(c1, c2):
    ax, ay, w1, h1 = c1
    bx, by, w2, h2 = c2

    if ((by < ay + h1) and (by > ay)) and ((bx > ax) and (bx < ax + w1)):
        return True
    return False

collided = False
for c1 in components:
    for c2 in components:
        if c1 != c2:
            if colliding(c1, c2) or colliding(c2, c1):
                collided = True
                break

if collided:
    print("-1")
else:
    areas = [c[2]*c[3] for c in components]
    e = round(((sum(areas)*100)/(w*h)), 2)
    print(e)
