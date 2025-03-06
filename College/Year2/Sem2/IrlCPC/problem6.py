n = int(input())
logs = [input().split(" ") for _ in range(n)]

q = int(input())
reqs = [input().split(" ") for _ in range(q)]

outputs = {}
for req in reqs:
    for log in logs:
        if req[2] == log[2]:
            if log[2] not in outputs.keys():
                outputs[log[2]] = []

            if ((req[0] <= log[0]) and (req[1] >- log[0])):
                outputs[req[2]].append(log[1])

for k, v in outputs.items():
    if len(v) > 0:
        print(" ".join(sorted(v)))
    else:
        print("NONE")

10
2023-10-01T12:34:56 192.168.1.1 GET
2023-10-01T12:41:10 192.168.1.8 PUT
2023-10-01T12:39:50 192.168.1.6 POST
2023-10-01T12:35:10 192.168.1.2 POST
2023-10-01T12:37:30 192.168.1.4 PUT
2023-10-01T12:36:20 192.168.1.3 DELETE
2023-10-01T12:40:00 192.168.1.7 DELETE
2023-10-01T12:38:40 192.168.1.5 GET
2023-10-01T12:42:20 192.168.1.9 GET
2023-10-01T12:43:30 192.168.1.10 POST
3
2023-10-01T12:34:56 2023-11-02T12:40:00 GET



