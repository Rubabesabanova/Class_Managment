def staircase(n):
    for i in range(n):
        pattern=""
        for k in range(n):
            if i+1<n-i+1:
                pattern+="#"
            else:
                pattern +=" "
        print(pattern)
n = int(input())

staircase(n)