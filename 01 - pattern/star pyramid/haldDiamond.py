n=5
for i in range(1, (2*n-1)+1):
    stars = i
    if i > n:
        stars = 2*n-i

    for j in range(stars):
        print("*", end=" ")
    print()
