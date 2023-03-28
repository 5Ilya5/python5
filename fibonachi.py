def nfib(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a + b
        a, b = b, a + b
        
res1 = list(x for x in nfib(20))
print(res1)
 
res2 = [x for x in nfib(20)]
print(res2)
 
res3 = []
for x in nfib(20):
    res3.append(x)
print(res3)
 
res4 = {x for x in nfib(20)}
print(res4)