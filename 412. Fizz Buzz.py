class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result=[]
        for i in range(1,n+1):
            if ((i%3)!=0) and ((i%5)!=0):
                result.append(str(i))
            else:
                if ((i%3)==0) and ((i%5)==0):
                    result.append("FizzBuzz")
                else:
                    if (i%3)==0:
                        result.append("Fizz")
                    if (i%5)==0:
                        result.append("Buzz")
        return result
            