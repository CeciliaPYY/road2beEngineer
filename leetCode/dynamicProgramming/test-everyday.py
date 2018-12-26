rods = [1,1,2]
dp = [False for i in range(len(rods)+1)]
dp[0] = [(0,0)]
for i in range(1, len(rods)+1):
    h = rods[i]
    for h1, h2 in dp[i-1]:
        dp += (h1, h2) 
        dp += (h1, h2+h) 
        if h1 + h < h2:
            dp += (h1+h, h2) 
        else:
            dp += (h2, h1+h) 