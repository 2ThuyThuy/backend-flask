T = int(input())
for _ in range(T):
    z, a, b, x, y = list(map(int,input().split()))
    # check win
    if z >= a*x + b*y:
        print("WIN")
        continue
    if a > b: # swap if dame a large dame b
        a, b = b, a
        x, y = y, x
    if x*a >= z:
        print(int(z/a))
        continue
    z -= x*a
    if b*y >= z:
        print(int(z/b + x))












