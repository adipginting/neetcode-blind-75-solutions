class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s2) < len(s1):
            return False
        
        s1_dict = {}
        for i in range(len(s1)):
            if s1[i] not in s1_dict:
                s1_dict[s1[i]] = 1
            else:
                s1_dict[s1[i]] = s1_dict[s1[i]] + 1
        print(s1_dict)
            
        l = 0
        r = len(s1)
        permutation = True
        
        while r <= len(s2):
            permutation = True
            s2_dict = {}
            for i in range(l, r):
                if s2[i] not in s2_dict:
                    s2_dict[s2[i]] = 1
                else:
                    s2_dict[s2[i]] = s2_dict[s2[i]] + 1
            print(s2_dict)
            
            for i in range(len(s1)):
                if s1[i] not in s2_dict:
                    permutation = False
                    l = l + 1
                    r = r + 1
                    break
                
                if s1_dict[s1[i]] != s2_dict[s1[i]]:
                    permutation = False
                    l = l + 1
                    r = r + 1
                    break
                    
            if permutation == True:
                break
                
        return permutation
