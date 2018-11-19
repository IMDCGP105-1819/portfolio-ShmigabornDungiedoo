def fib(n):
    if n==0 or n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("number: "))
print(fib(n))

for n in range (1, 21):
    print(fib(n))
