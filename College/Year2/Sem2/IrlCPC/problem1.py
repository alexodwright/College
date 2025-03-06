n = int(input())

products = [map(int, input().split(" ")) for _ in range(n)]

total = 0
for p in products:
    eff_w = p[0] * max(0, (1-((p[1])/200)))
    tot_rev = eff_w * p[2] * (p[1]/100)
    total += tot_rev
print(round(total, 2))
