class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = []
        dic = {}

        for string in strs:
            sorted_string = ''.join(sorted(string))

            if sorted_string not in dic:
                dic[sorted_string] = []

            dic[sorted_string].append(string)

        for key, value in dic.items():
            anagrams.append(value)
        return anagrams



        