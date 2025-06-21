n=5

for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")

    for j in range(2*i+1):
        print("*", end="")

    for j in range(n-i-1):
        print(" ", end="")
    print()

#Pyramid
# n = 6
# for i in range(1, n+1):
#     for j in range(1, n - i +1):  #nth(n=6) iteration is happening which is not needed thats the reason we are getting at last a empty line
#         print(" ", end=" ")
#         if j == (n - i):
#             print("* " * (2*i-1))