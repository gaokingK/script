def combinationSum4(nums, target: int) -> int:
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
    i=len(nums)
    return dfs(target, i)


if __name__ == "__main__":
    nums = [1,2,3]
    target = 4
    print(combinationSum4(nums, target))