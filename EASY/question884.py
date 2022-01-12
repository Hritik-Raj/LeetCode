class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        dictVal = {}
        returnList = []
        for x in s1.split():
            if x not in dictVal:
                dictVal[x] = 1
            else:
                dictVal[x] += 1
        for x in s2.split():
            if x not in dictVal:
                dictVal[x] = 1
            else:
                dictVal[x] += 1
        for item in dictVal:
            if dictVal[item] == 1:
                returnList.append(item)
        return returnList
            