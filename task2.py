tri = []
n = int(input("Число рядов: "))
for i in range(n + 1):
    tri.append([])

tri[0].append(1)

for i in range(1, n + 1):
    tri[i].append(1)
    for j in range(1, i - 1):
            k = tri[i-1][j-1] + tri[i-1][j]
            tri[i].append(k)
    tri[i].append(1)
tri.__delitem__(1)
for i in tri:
        print(i)
