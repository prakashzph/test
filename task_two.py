from math import factorial

def total_route(n,k):
    return factorial(n)/(factorial(k)*factorial(n-k))

print ('Hence, the total routes for 20*20 grid is '+str(total_route(40,20))) # n=20+20(since the grid is 20*20) and k = 20

