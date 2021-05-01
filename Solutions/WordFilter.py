# NAME : Prefix and Suffix Search
# LINK : https://leetcode.com/explore/challenge/card/may-leetcoding-challenge-2021/598/week-1-may-1st-may-7th/3728/
# DATE : 01/05/2021

class WordFilter:

    def __init__(self, words: List[str]):
        self.dict = {}

        for i in range(len(words)):
            for j in range(len(words[i])):
                for k in range(len(words[i])):
                    self.dict[words[i][:j + 1] + "#" + words[i][k:]] = i

    def f(self, prefix: str, suffix: str) -> int:
        return self.dict[prefix + "#" + suffix] if prefix + "#" + suffix in self.dict else -1


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)

class WordFilterTLE:

    def __init__(self, words: List[str]):
        self.prefix = {}
        self.suffix = {}

        for i in range(len(words)):
            for j in range(len(words[i]) + 1):
                if j > 0:  # Prefix
                    if words[i][:j] in self.prefix:
                        self.prefix[words[i][:j]] .append(i)
                    else:
                        self.prefix[words[i][:j]] = [i]

                if j < len(words[i]):  # Suffix
                    if words[i][j:] in self.suffix:
                        self.suffix[words[i][j:]].append(i)
                    else:
                        self.suffix[words[i][j:]] = [i]

    def f(self, prefix: str, suffix: str) -> int:
        result = []

        if prefix in self.prefix and suffix in self.suffix:
            for i in range(len(self.prefix[prefix])):
                if self.prefix[prefix][i] in self.suffix[suffix]:
                    result.append(self.prefix[prefix][i])

        return -1 if result == [] else max(result)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
