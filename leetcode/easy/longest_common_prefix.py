class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        strs = strs[1:]
        match_count = 0
        for idx, char in enumerate(first_word):
            count = 0
            for word in strs:
                if len(word) - 1 >= idx :
                    if word[idx] == char:
                        count += 1
                    else:
                        if count == len(strs):
                            match_count+= 1            
                        return first_word[0:match_count]
            
            if count == len(strs):
                match_count += 1
                
        return first_word[0:match_count]
