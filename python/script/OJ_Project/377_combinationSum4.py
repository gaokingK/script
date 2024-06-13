def combinationSum4(nums, target: int) -> int:
    n = []
    r = 0

    def dfs(t,i):
        nonlocal r
        if t < 0 or i < 0:
            # print(t,i, 0)
            return 0
        if t == 0:
            # print(t,i, 1)
            return 1
        # a = dfs(t-nums[i], i)
        # if a == 1:
        #     n.append(nums[i])
        #     if t == target:
        #         print(n)
        #         n = []
        # b = dfs(t, i-1)
        # return a + b
        # return dfs(t-nums[i], i) + dfs(t, i-1)
        for j in range(i):
            print(f"调用dfs({t-nums[j]}, {i})")
            r += dfs(t-nums[j], i)
            print(f"调用dfs({t-nums[j]}, {i}), 结果为{r}, r为{r}")
            
        return r
    i = len(nums)
    print(f"调用dfs({target}, {i})")
    return dfs(target, i)
    

if __name__ == "__main__":
    nums = [2,3]
    target = 5
    print(combinationSum4(nums, target))
"""
1 1 1 
2 1


"""
