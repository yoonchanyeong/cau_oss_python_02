def arithmetic_ops(op):
    num1 = int(input("첫번째 정수를 입력하세요. : "))
    num2 = int(input("두번째 정수를 입력하세요. : "))
    return op(num1, num2), num1, num2
    
def plus(num1, num2):
    return num1+num2

def minus(num1, num2):
    return num1-num2
    

while True:
    yeonsan = input("연산기호를 입력하세요. 끝내려면 end를 입력하세요. : ")
    if(yeonsan == "end"):   #end입력되면 종료
        break
    elif(yeonsan == "+"):
        ret, num1, num2 = arithmetic_ops(plus)
    elif(yeonsan == "-"):
        ret, num1, num2 = arithmetic_ops(minus)
    elif(yeonsan == "*"):
        ret, num1, num2 = arithmetic_ops(lambda x,y : x*y)
    elif(yeonsan == "/"):
        ret, num1, num2 = arithmetic_ops(lambda x,y : x/y)
    elif(yeonsan == "%"):
        ret, num1, num2 = arithmetic_ops(lambda x,y : x%y)
    else:
        print("Invalid operation")  #이외의 문자열이 입력된 경우 다시 입력받기
        continue
    print(f"{num1}{yeonsan}{num2} = {ret}") #연산 결과를 출력
    
print("Exit program")
