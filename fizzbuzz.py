def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        arr=[]
        thirdStep=0
        fifthStep=0
        for i in range(1,n+1):
            thirdStep+=1
            fifthStep+=1
            
            if thirdStep==3 and fifthStep==5:
                
                arr.append("fizzBuzz")
                thirdStep=0
                fifthStep=0
                
            elif thirdStep==3:
                arr.append("Fizz")
                thirdStep=0
            elif fifthStep==5:
                arr.append("Buzz")
                fifthStep=0
            else:
                arr.append(str(i))
        print(arr)
fizzBuzz(20)