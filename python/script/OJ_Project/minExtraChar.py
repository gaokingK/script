def minExtraChar(s: str, dictionary: list) -> int:
    n = len(s)
    # mapping = [-1] * n
    mapping = [[] for _ in range(n)]
    valid_map = []
    for word in dictionary:
        start = 0
        for _ in range(s.count(word)):
            valid_map.append(word)
            try:
                index = s.index(word, start) - 1 + len(word)
            except Exception as e:
                print(word)
                raise e
            start = index + 1
            # mapping[index] = max(len(word), mapping[index])
            mapping[index].append(len(word))
    def dfs(i):
        if i<0:
            return 0
        if mapping[i]:
            # return min(dfs(i-mapping[i]), dfs(i-1) + 1)
            return min(min([dfs(i-mapping[i][x]) for x in range(len(mapping[i]))]), dfs(i-1) + 1)
        else:
            return dfs(i-1)+1
    # print(valid_map)
    print(mapping)
    return dfs(n-1)
    # return mapping
# cc = ",".join(list(set([f"\"{x.strip()}\"" for x in bb.split("、") if x])))

if __name__ == "__main__":
        # s=["leetscode", "iamaboynot", "dwmodizxvvbosxxw", "ecolloycollotkvzqpdaumuqgs","sdosi"]
    dictionary = [["leet","code","leetcode"],["ama","ia","ot","yno"],["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"],["flbri","uaaz","numy","laper","ioqyt","tkvz","ndjb","gmg","gdpbo","x","collo","vuh","qhozp","iwk","paqgn","m","mhx","jgren","qqshd","qr","qpdau","oeeuq","c","qkot","uxqvx","lhgid","vchsk","drqx","keaua","yaru","mla","shz","lby","vdxlv","xyai","lxtgl","inz","brhi","iukt","f","lbjou","vb","sz","ilkra","izwk","muqgs","gom","je"],['d', 'dos', 't', 'fgyr', 'i', 'si', 'hhbz', 'ihg']]
    for s,d in zip(s,dictionary):
        if s == "sdosi":
            print(minExtraChar(s,d))
