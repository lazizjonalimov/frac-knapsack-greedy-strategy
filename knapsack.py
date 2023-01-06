# Returns the maximum value – Greedy Strategy
def frac_knapSack(W, weight, benefit, set_size_n):
    if set_size_n == 0 or W == 0:
        return 0
    if weight[set_size_n - 1] > W:
        return frac_knapSack(W, weight, benefit, set_size_n - 1)
    else:
        value = max(benefit[set_size_n - 1] + frac_knapSack(W - weight[set_size_n - 1],
                                                        weight, benefit, set_size_n - 1),
                    frac_knapSack(W, weight, benefit, set_size_n - 1))

        return value


# To test above function
# benefits = [100, 50, 56]
# weights = [2, 5, 8]
S = [(11, 5), (10, 7), (7, 5), (10, 6), (14, 3), (7, 1), (9, 6)]
benefits = [y[0] for y in S]
weights = [y[1] for y in S]

W = 17
n = len(benefits)
print(frac_knapSack(W, weights, benefits, n))
# 156
