def best_total_price(prices, k):
    if len(prices) < k:
        return 0
    total = sum(prices[:k])
    maxtotal = total
    for i in range(len(prices) - k):
        total -= prices[i]
        total += prices[i + k]
        maxtotal = max(maxtotal, total)

    return maxtotal

# Sliding Window Iterations:

# First Iteration (i = 0):
# total -= prices[0] => total = 11 - 7 = 4
# total += prices[3] => total = 4 + 5 = 9
# maxtotal = max(11, 9) = 11
# Second Iteration (i = 1):
# total -= prices[1] => total = 9 - 3 = 6
# total += prices[4] => total = 6 + 8 = 14
# maxtotal = max(11, 14) = 14
# Third Iteration (i = 2):
# total -= prices[2] => total = 14 - 1 = 13
# total += prices[5] => total = 13 + 9 = 22
# maxtotal = max(14, 22) = 22
# Fourth Iteration (i = 3):
# total -= prices[3] => total = 22 - 5 = 17
# total += prices[6] => total = 17 + 10 = 27
# maxtotal = max(22, 27) = 27
# Fifth Iteration (i = 4):
# total -= prices[4] => total = 27 - 8 = 19
# total += prices[7] => total = 19 + 22 = 41
# maxtotal = max(27, 41) = 41
# Sixth Iteration (i = 5):
# total -= prices[5] => total = 41 - 9 = 32
# total += prices[8] => total = 32 + 33 = 65
# maxtotal = max(41, 65) = 65