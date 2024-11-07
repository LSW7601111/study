# num1 = 31.2
# num2 = 22.3
# num3 = "안녕하세요"
# num4 = " 처음뵙겠습니다."
# num5 = "안녕하세요. \n처음뵙겠습니다. \n잘부탁드립니다."
# a1 = num1 + num2
# a2 = num1 * num2
# a3 = num1 / num2
# a4 = num3 + num4
# print(a1)
# print(a2)
# print(a3)
# print(a4)
# print(num5)
# # 컨트롤 슬러쉬 누르면 연산처리가 안된다.
# # 배열의 길이를 체크 많이 함 (자주 쓰임으로 알고 있으면 좋습니다.)
# str = "power good boy"
# len(str)
# # print(len(str))

# str[0]
# print(str[3])
# # print(str[-2])
# # print(str[0]+str[2]+str[4]) 비연속적으로 띄엄 띄엄 할때
# print(str[0:3]) 연속적으로 할때


# str = input("입력하세요 : ")
# print(str)

# num = int(input("입력하세요 : "))
# print(num)

# num1 = int(input("입력하세요 : "))
# num2 = int(input("입력하세요 : "))
# print(num1 + num2)


# num1, num2 = input("숫자 입력 2개 : "). split()
# re = int(num1) * int(num2)
# print("결과 =" , re)


# num1 = input("입력하세요 : ")
# num2 = input("입력하세요 : ")
# print(num1 + num2)


# sum1 = 3
# sum2 = 4
# print(sum1 ** sum2)

# 나눗셈 후 나머지를 리턴하는 % 연산자
# sum1 = 7 % 3
# print(sum1)

# sum2 = 3 % 7
# print(sum2)
# 나머지가 3인데 7로 나눠 지지 않기 때문에 3의 숫자가 다 들어간다


# sum1 =  7 / 4
# print(sum1)

# 나눗셈 후 몫을 리턴하는 // 연산자
# sum1 = 7 // 4
# print(sum1)

# money = True
# if money:
#    print("택시를 타고 가라")
# else:
#    print("걸어 가라")

# money = 0
# if money:
#     print("택시를 타고 가라")
# else:
#    print("걸어 가라")


# money = int(input("입력하세요 : "))
# if money:
#     print("택시를 타고 가라")
# else:
#    print("걸어 가라")

# num1 = 10
# num2 = 20
# money = int(input("입력하세요 : "))
# if money:
#     print(num1 + num2)
# else:
#    print(num1 * num2)   


# num1 = 10
# num2 = 20
# num3 = 25
# money = int(input("입력하세요 : "))
# if money:
#     print(num1 + num2)
# else:
#    print(num1 * num2)   
   

# 1일때 결과값이 나오고 1이 아닌 수가 나올때 프로그램 종료
# num1 = 10
# num2 = 20
# num3 = 25
# money = int(input("입력하세요 : "))
# if money == 1:
#     print(num1 + num2)
# else:
#    exit()



# score = int(input("입력하세요 : "))

# if score >=90:
#     print("A")
# elif score >=80:
#     print("B")
# elif score >=70:
#     print("C")
# elif score >=60:
#     print("D")
# else:
#     print("낙제 프로그램 종료")
#     ecit()

# 1. 콜라  2. 사이다 3. 환타 0. 프로그램 종료 합니다.

# num = int(input("입력하세요 : "))

# if num == 1:
#     print("콜라")
# elif num == 2:
#     print("사이다")
# elif num == 3:
#     print("환타")
# else:
#     print("프로그램 종료 합니다.")        
#     exit()

num = int(input("입력하세요 : "))
if (num%2) == 0:
    print("안녕")
elif (num%2) == 1:
    print("하세요")
elif (num%2) != 0:
    print("감사합니다.")
