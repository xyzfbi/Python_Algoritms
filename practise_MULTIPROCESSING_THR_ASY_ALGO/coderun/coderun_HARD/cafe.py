import sys


def main():
    n = int(input())
    prices = [int(input()) for _ in range(n)]

    max_coupons = n +2
    dp = [[float('inf')] * max_coupons for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        current = prices[i -1]
        for j in range(max_coupons):
            if dp[i - 1][j]  == float('inf'):
                continue
            new_j = j
            cost = current
            if cost > 100:
                new_j += 1
            if new_j < max_coupons:
                if dp[i][new_j] > dp[i-1][j] + cost:
                    dp[i][new_j] = dp[i-1][j] + cost

            if j > 0:
                new_j -= 1
                if dp[i][new_j] > dp[i-1][j]:
                    dp[i][new_j] = dp[i-1][j]

    min_cost = min(dp[n])
    best_j = 0
    for j in range(max_coupons):
        if dp[n][j] == min_cost:
            best_j = j

    remain_c = best_j
    used_coupons = 0
    days_used = []
    curr_j = best_j

    for i in range(n, 0, -1):
        flag = False
        for j in range(max_coupons):
            if curr_j == j - 1  and (j - 1) >= 0 and dp[i][curr_j] == dp[i-1][j]:
                used_coupons += 1
                days_used.append(i)
                curr_j = j
                flag = True
                break
        if flag:
            continue
        price = prices[i - 1]
        if price > 100:
            curr_j -= 1
    days_used.sort()
    print(min_cost)
    print(remain_c, used_coupons)
    for d in days_used:
        print(d)



if __name__ == '__main__':
    main()