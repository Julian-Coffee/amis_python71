
N = int(input("Введіть кількість кеглей - "))
mass = ["I"]*N
K = int(input("Введіть кількість кидків - "))
for i in range (K):
    li = int(input("введіть номер першої збитої кеглі - "))
    ri = int(input("введіть номер останньої збитої кеглі - "))
    for k in range(li, ri+1):
        mass[k-1] = "."
for m in range(len(mass)):
    print(mass[m], end = "")
input()