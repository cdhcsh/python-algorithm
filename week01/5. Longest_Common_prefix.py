def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    count = 0
    while True:
        if len(strs[0]) < (count + 1):
            return strs[0][:count]
        tmp = strs[0][count]
        for s in strs[1:]:
            if len(s) <= (count+1) or tmp != s[count]:
                return strs[0][:count]
        count += 1
