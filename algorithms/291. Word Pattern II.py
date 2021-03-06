class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
#         return self.dfs(pattern, str, {})

#     def dfs(self, pattern, str, dict):
#         if len(pattern) == 0 and len(str) > 0:
#             return False
#         if len(pattern) == len(str) == 0:
#             return True
#         for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
#             if pattern[0] not in dict and str[:end] not in dict.values():
#                 dict[pattern[0]] = str[:end]
#                 if self.dfs(pattern[1:], str[end:], dict):
#                     return True
#                 del dict[pattern[0]]
#             elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
#                 if self.dfs(pattern[1:], str[end:], dict):
#                     return True
#         return False



        dic = {}
        def dfs(pattern,str):
            if not pattern and not str:
                return True
            if not pattern and str:
                return False
            for i in range(1,len(str)-len(pattern)+2):
                if pattern[0] not in dic and str[:i] not in dic.values():
                    dic[pattern[0]] = str[:i]
                    if dfs(pattern[1:],str[i:]):
                        return True
                    del dic[pattern[0]]
                elif pattern[0] in dic and dic[pattern[0]] == str[:i]:
                    if dfs(pattern[1:],str[i:]):
                        return True
            return False
        return dfs(pattern,str)
