class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        mappings1 = {}
        mappings2 = {}
        
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sch = s[i]
            tch = t[i]

            if sch == tch and sch not in mappings1 and tch not in mappings2:
                mappings1[sch] = tch
                mappings2[tch] = sch
                continue
            else:
                if sch in mappings1:
                    if mappings1[sch] == tch and (tch not in mappings2 or mappings2[tch] == sch):
                        continue
                    else:
                        return False

                elif tch in mappings2:
                    if mappings2[tch] == sch and (sch not in mappings1 or mappings1[sch] == tch):
                        continue
                    else:
                        return False
                else:
                    mappings1[sch] = tch
                    mappings2[tch] = sch

        return True
    
