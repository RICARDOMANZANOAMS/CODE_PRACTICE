from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom=Counter(ransomNote)
        count_maga=Counter(magazine)
        print(count_ransom)
        print(count_maga)
        
        flag=0
        for i in count_ransom:
            for j in count_maga:
                if i==j:
                    print("here")
                    print(count_maga[j])
                    print(count_ransom[i])
                    if count_maga[j]>=count_ransom[i]:
                        flag+=1
                        break
        print("flag")
        print(flag)
        length_ransom=len(count_ransom)
        if length_ransom==flag:
            return True
        else:
            return False
                    
                