def combinationSum4(nums, target: int) -> int:
    n = []
    r = 0
    step=[]
    # @cache
    def dfs(n,i):
        # nonlocal r
        r=0

        if n==0:
            return 1
        for j in range(i):
            #step.append(nums[j
            if nums[j]<= n:
                r+=dfs(n-nums[j],i)
                continue
        # r = sum(dfs(n-nums[j],i) for j in range(i) if nums[j] <= n)
        return r


    def dfs2(t,i):
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
            print(f"调用dfs({t-nums[j]}, {i}), r={r}")
            r += dfs(t-nums[j], i)
            print(f"调用dfs({t-nums[j]}, {i})后, r={r}")
            

        for j in range(i):
            print(f"dfs{t,i}内使用{nums[j]}调用dfs{t-nums[j], i}, r={r}")
            # r += dfs(t-nums[j], i)
            # _r=0
            _r = dfs(t-nums[j], i)
            r+=_r
            print(f"dfs{t,i}内使用{nums[j]}调用dfs{t-nums[j], i}的结果为{_r}, r={r}")
            
        return r
    i = len(nums)
    print(f"调用dfs({target}, {i})")
    return dfs(target, i)
    



if __name__ == "__main__":
    nums = [1]
    target = 5
    print(combinationSum4(nums, target))
"""
1 1 1 
2 1


"""


