def longestSemiRepetitiveSubstring(s: str):
    if len(s)<3:
        return len(s)
    ans=1
    same_num=0
    i = 0
    for j in range(1, len(s)):
        if s[j] == s[j-1]:
            same_num +=1
            if same_num >1:
                i = l
                same_num = 1
                l = j
            else:
                l = j
            ans = max(j - i + 1, ans)

        else:
            ans = max(j - i + 1, ans)
            j += 1
    return ans


if __name__ == "__main__":
    s = "5332212345678922"
    print(longestSemiRepetitiveSubstring(s))
