from math import inf
def coinChange(coins, amount: int) -> int:
    n = len(coins) - 1
    f = [[-1] * n]
    # def dfs(i, c):
    #     if i<0:
    #         return 0 if c == 0 else inf
    #     if c < coins[i]:
    #         return dfs(i-1, c)
    #     return min(dfs(i, c-coins[i]) + 1, dfs(i-1, c))
    # ans = dfs(n, amount)
    # return ans if ans < inf else -1

itm_nginx_accesslog_source
if __name__ == "__main__":
    coins = [1, 2, 5]
    amount = 8
    print(coinChange(coins, amount))
