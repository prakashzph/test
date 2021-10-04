coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print("Count for  number of possibilities to make 200p is", ways[target])
