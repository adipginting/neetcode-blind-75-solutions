class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        # write your code here
        output = ""
        for i in range(len(strs)):
            if i != len(strs) - 1 and strs[i] != ":":
                output = output + strs[i] + ":;"
            elif strs[i] == ":" and i != len(strs) - 1:
                output = output + ":" + strs[i] + ":;"
            elif i == len(strs) - 1:
                output = output + strs[i]
        return output

    """
    @param: str: A string
    @return: decodes a single string to a list of strings
    """
    def decode(self, str):
        # write your code here
        colon = 0
        word = ""
        strs = []
        for i in range (len(str)):
            if str[i] != ":" and str[i] != ";":
                word = word + str[i]
            elif str[i] == ":":
                colon += 1
            elif str[i] == ";":
                colon = 0
            
            if colon == 1 and word != "":
                strs.append(word)
                word = ""
            elif colon == 2:
                strs.append(":")
                colon = 0
        strs.append(word)

        return strs
