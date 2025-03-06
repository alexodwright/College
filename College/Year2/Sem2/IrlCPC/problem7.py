# our solution
# for _ in range(20):
#     n = int(input())
#     c = 0
#     exceptions = [ "1", "4", "5", "6", "8", "9"]
#     for num in range(0, 3*int("3"*n)+1, 3):
#         valid = True
#         if (num % 3) == 0:
#             for e in exceptions:
#                 if e in str(num):
#                     valid = False
#                     break
#             if valid and len(str(num)) == n:
#                 c += 1
#     print(c)

# actual solution
n = int(input())
res = 2 if n == 1 else 4**(n-1)
print(res)
