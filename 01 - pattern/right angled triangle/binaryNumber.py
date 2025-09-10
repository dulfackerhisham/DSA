n=5
start = 0
for i in range(1, n+1):
    if i % 2 == 0:
        start = 0
    else:
        start = 1

    for j in range(1,i+1):
        print(start, end=" ")
        if start == 0:
            start = 1
        else:
            start = 0
    print()