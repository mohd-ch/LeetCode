class Solution:
    def fizzBuzz(self,n):
        aList = []
        i = 1
        while i<=n:
            if i%3==0 and i%5==0:
                aList.append("FizzBuzz")
            elif i%5==0:
                aList.append("Buzz")
            elif i%3==0:
                aList.append("Fizz")
            else:
                aList.append(str(i))
            i+=1
        return aList
            