# 숫자형
# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))
# 문자형
# print('풍선')
# print('나비')
# print('ㅋㅋㅋㅋㅋㅋㅋㅋㅋ')
# print('ㅋ'*9)
# 참 / 거짓
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not (5 > 10))
#변수
# animal = "강아지"
# name = "연탄이"
# age = 4
# hobby = "산책"
# is_adult = age > 3

# print("우리집 " + animal + "의 이름은 " + name +"예요")
# # hobby ="공놀이"
# # print(name +"는 " + str(age) +"살이며, " + hobby+ "을 좋아해요.")
# print(name, "는 ", age, "살이며, ",  hobby,"을 좋아해요.")
# print(name +"는 어른 일까요? " + str(is_adult))

# station = "사당"
# # station = "신도림"
# # station = "인천공항"
# print(station+ "행 열차가 들어오고 있습니다.")

# print (1+1) # 2
# print(3-2) # 1
# print (5*2) # 10
# print(6/3) # 2

# print(2**3) # 2^3 = 8
# print(5%3) # 나머지 구하기 2
# print (10%3) # 1
# print (5//3) # 1
# print (10//3) # 3

# print(10 > 3) # True 
# print (4 >= 7) #False
# print(10 < 3) # False 
# print(5 <= 5) # True

# print(3 == 3) # True 
# print(4 == 2) # False
# print(3+ 4 ==7)# True

# print (1 != 3) # True 
# print(not (1 != 3)) # False

# print ( (3 > 0) and (3 < 5)) # True 
# print ((3 > 0) & (3 < 5)) # True

# print ((3 > 0) or (3 > 5)) # True 
# print ((3 > 0) | (3 > 5)) # True

# print (5 > 4 > 3) # True 
# print(5 > 4 > 7) # False

# print (2 + 3 * 4) #14
# print ((2 + 3) * 4) # 20
# number = 2 + 3 * 4 # 14
# print (number)
# number = number + 2 #16
# print (number)
# number += 2 # 18
# print (number)
# number *= 2 # 36
# print (number)
# number /= 2 # 18
# print (number)
# number -= 2 # 16
# print (number)
# number %=5 # 1
# print (number)

# print(abs(-5)) #5
# print(pow(4, 2)) # 4^2 =4*4 = 16
# print(max(5, 12)) #12
# print(min(5, 12)) #5
# print(round(3.14))#3
# print(round(4.99))#5

# from math import*
# print(floor(4.99)) # 내림. 4
# print(ceil(3.14)) # 올림. 4
# print(sqrt(16)) # 제곱근. 4

# from random import *
# print(random())
# print(random() * 10)
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10))
# print(int(random() * 10)+ 1)
# print(int(random() * 10)+ 1)
# print(int(random() * 10)+ 1)
# print(int(random() * 10)+ 1)
# print(int(random() * 10)+ 1)
# print(int(random() * 10)+ 1)
# print(int(random() * 45)+ 1)

# print(randrange(1, 46)) #1 ~ 46 미만의 임의 값

# date = randint(4, 28)
# print("오프라인 스터디 모임의 날짜는 매월 " + str(date) +"로 선정되었습니다.")

# sentence = '나는 소년 입니다.'
# print(sentence)

# sentence2 = '파이썬은 쉬워요'
# print(sentence2)

# sentence3 = """
# 나는 소년이고, 
# 파이썬은 쉬워요.
# """
# print(sentence3)

# jumin = "990120-1234567"
# print ("성별 : "+ jumin[7])

# print("연 :"+ jumin[0:2]) # 0 부터 2 직전까지 (0, 1)

# print("월 :"+ jumin[2:4])

# print("일 :"+ jumin[4:6])

# print("생년월일 :" + jumin[:6]) # 처음부터 6 직전까지

# print("뒤 7자리 :"+jumin[7:]) # 7 부터 끝까지
# print("뒤 7자리 (뒤에부터) :"+ jumin[-7:])# 맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python. lower ())
# print(python.upper ())
# print(python [0]. isupper ())
# print(len (python) )
# print(python.replace("Python", "Java"))
# index = python.index("n")
# print (index)
# index = python.index("n", index + 1)
# print(index)
# print (python. find ("Java"))
# #print(python.index("Java"))
# print("hi")
# print(python.count("n"))

# # 방법 1
# print("나는 %d살입니다."% 20)  # 정수 출력 (20)
# print("나는 %s을 좋아해요."% "파이썬")  # 문자열 출력 (파이썬)
# print("Apple 은 %c로 시작해요." % "A")  # 문자 출력 (A)
# print("나는 %d살입니다."% 20)
# print("나는 %s색과 %s색을 좋아해요."% ("파란", "빨간"))
# # 방법 2
# print("나는 {}살입니다.".format (20))  # 정수 출력 (20)
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))  # 문자열 출력 (파란, 빨간)
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))  # 변수 이름 사용 가능 (파란, 빨간)
# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))
# #방법4 (v3.6 이상~)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# print("백문이 불여일견 백견이 불여일타")
# #print("백문이 불여일견 # SyntaxError 발생
# #백견이 불여일타")
# print("백문이 불여일견\n백견이 불여일타")

# #print("저는 "나도코딩"입니다.")
# print("저는 '나도코딩'입니다.")
# # 또는
# print('저는 "나도코딩"입니다.')

# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# #print("C:\Users\Nadocoding\Desktop\PythonWorkspace") # SyntaxError 발생
# print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace")
# print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace")

# print("Red Apple\rPine")


# print("Redd\bApple")


# print("Red\tApple")

# #url = "http://naver.com"
# url = "http://daum.net" # dau40!
# # url = "http://google.com" # goo61!
# # url = "http://youtube.com" # you71!
# my_str = url.replace("http://", "") 
# # naver.com일 때 my_str.index(".")의 결과는 5이므로 다음 문장은 my_str = mystr[0:5]와 같음
# my_str = my_str[:my_str.index(".")] 
# password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# print("{0}의 비밀번호는 {1}입니다.".format(url, password))

# 리스트
# 지하철 칸별로 10명, 20명, 30명 승차
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호"))

# subway.append("하하")
# print(subway)

# subway.insert(1, "정형돈")
# print(subway)

# # 지하철 역마다 한 명씩 내림
# print(subway.pop()) 
# print(subway)
# print(subway.pop()) 
# print(subway)
# print(subway.pop()) 
# print(subway)

# # 지하철에서 모두 내림
# subway.clear()
# print(subway)

# # 같은 이름이 몇 명 있는지 확인
# subway.append("유재석") 
# print(subway)
# print(subway.count("유재석"))


# num_list = [5, 2, 4, 3, 1]

# num_list.sort() # 오름차순 정렬
# print(num_list)

# num_list.sort(reverse=True) # 내림차순 정렬
# print(num_list)

# num_list.reverse() # 순서 뒤집기
# print(num_list)

# num_list.clear() # 모두 지우기
# print(num_list)

# 다양한 자료형과 사용
# num_list = [5,4,3,2,1]
# mix_list = ["조세호", 20, True]
# # print(num_list)

# # 리스트의 확장
# num_list.extend(mix_list)
# print(num_list)

# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))

# print(cabinet[5]) 오류 발생
# print(cabinet.get(5)) none
# print(cabinet.get(5, "사용 가능")) 사용 가능 출력
# print("hi")

# print(3 in cabinet) #true
# print(5 in cabinet) # false

# cabinet = {"A-3":"유재석", "B-100" :"김태호"}
# print(cabinet["A-3"])
# print (cabinet["B-100" ])

# # 새 손님
# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print (cabinet)

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)
# # key 들만 출력
# print(cabinet.keys())
# # value 들만 출력
# print(cabinet.values())

# # key, Value 쌍으로 출력
# print(cabinet.items())
# # 목욕탕 폐점
# cabinet.clear()
# print(cabinet)

# 튜플 
# menu = ("돈까스", "치즈까스")
# print (menu [0])
# print(menu[1])
# #menu. add("생선까스" )
# # name = "김종국"
# # age = 20
# # hobby = "코딩"
# # print(name, age, hobby)
# (name, age, hobby) = ("김종국", 20, "코딩")
# print(name, age, hobby)

# 짐합(set)
# 중복 안됨, 순서 1없음
# my_set = {1,2,3,3,3}
# print (my_set)
# java= {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])
# #교집합 (java 와 python 을 모두 할 수 있는 개발자)
# print(java & python)
# print(java. intersection (python))
# #합집합 (java 할 수 있거나 python 할 수 있는 개발자)
# print(java | python)
# print(java.union (python))

# #차집합 (java 할 수 있지만 python 은 할 줄 모르는 개발자)
# print(java - python)
# print (java. difference(python))
# #python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)
# # java 를 잊었어요
# java.remove("김태호")
# print(java)

# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu) # 리스트로 변환
# print(menu, type(menu))

# menu = tuple(menu) # 튜플로 변환
# print(menu, type(menu))

# menu = set(menu) # 세트로 변환
# print(menu, type(menu))

# from random import * 

# users = range(1, 21) # 리스트 생성, 1부터 21 직전(20)까지 연속한 숫자 모음
# users = list(users) # users를 리스트 자료구조로 변환
# shuffle(users) # 리스트 섞기
# winners = sample(users, 4) # users 리스트에서 중복 없이 4명 추첨

# print("-- 당첨자 발표 -- ") # 당첨자 출력
# print("치킨 당첨자 : {0}".format(winners[0])) # 0번째 인덱스(1명)
# print("커피 당첨자 : {0}".format(winners[1:])) # 1번째부터 마지막까지 슬라이싱(3명)
# print("-- 축하합니다! --")

# weather = input("오늘 날씨는 어때요? ")
# #print(weather)

# if weather == "비" or weather =="눈":
#     print("우산을 챙기세요.")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요.")
# else:
#     print("준비물이 필요 없어요.")

# temp = int(input ("기온은 어때요? "))
# if 30 <= temp:
#     print ("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp < 30:
#     print("괜찮은 날씨에요")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for waiting_no in [1, 2, 3, 4, 5]:
#     print("대기번호 : {0}".format(waiting_no)) # {0} 위치에 waiting_no의 값이 들어감


# for waiting_no in range(5): # 0부터 5 직전까지(0~4)
#     print("대기번호 : {0}".format(waiting_no))


# for waiting_no in range(1, 6): # 1부터 6 직전까지(1~5)
#     print("대기번호 : {0}".format(waiting_no))

# starbucks = ["아이언맨", "토르", "아이엠그루트"] # 손님 닉네임 리스트
# for customer in starbucks:
#     print("{0} 님, 커피가 준비되었습니다.".format(customer))

# customer = "토르" # 손님 닉네임
# index = 5 # 초깃값, 부르는 횟수 최대 5번

# while index >= 1: # 부르는 횟수가 1 이상일 때만 실행
#     print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))
#     index -= 1 # 횟수 1회 차감
#     if index == 0: # 5번 모두 불렀다면
#         print("커피를 폐기 처분합니다.")
# customer = "아이언맨"
# index = 1
# while True:
#     index += 1
#     print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))

# customer = "토르"
# person = "Unknown"
# while person != customer :
#     print("{0}, 커피가 준비 되었습니다.". format(customer))
#     person= input("이름이 어떻게 되세요? ")

# absent = [2, 5] #결석

# no_book = [7] # 책을 깜빡했음
# for student in range(1, 11): # 1,2,3,4,5,6,7,8,9,10
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
#         break
#     print(" {0},책을 읽어봐" .format(student))

# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
# students = [1,2,3,4, 5]
# print(students)
# students = [i+100 for i in students]
# print(students)
# 학생의 이름을 길이로 변환 
# students = ["Iron man", "Thor", "I am groot"]
# students =  [len(i) for i in students]
# print(students)
# students = ["Iron man", "Thor", "I am groot"]
# students =  [i.upper() for i in students]
# print(students)

# from random import * 

# cnt = 0 # 총 탑승객 수

# for i in range(1, 51): # 손님 총 50명
#     time = randrange(5, 51) # 변수 정의 소요시간 5~50분
#     if 5 <= time <= 15: # 소요시간 5~15분인 손님만 매칭
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) # 매칭 성공 출력
#         cnt += 1 # 총 탑승객 수 증가 처리
#     else: # 매칭 실패 시
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time)) # 매칭 실패 출력

# print("총 탑승객 : {0}명".format(cnt)) # 총 탑승객 수 출력

# def open_account():
#     print("새로운 계좌가 생성 되었습니다.")

# def deposit(balance, money):  # 입금
#     if money <= 0:
#         print("입금 금액은 0보다 커야 합니다.")
#         return balance
#     else:
#         print("입금이 완료되었습니다. 잔액은 {}  원입니다.".format(balance + money))
#         return balance + money

# def withdraw(balance, money):  # 출금
#     if balance >= money:
#         print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
#         return balance - money
#     else:
#         print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
#         return balance
# def withdraw_night(balance, money): #저녁에 출금
#     commission = 100 # 수수료 100원
#     return commission, balance - money - commission

# balance = 0
# balance = deposit(balance, 1000)
# #balance = withdraw(balance, 2000)
# #balance = withdraw(balance, 500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))

# def profile (name, age, main_lang) :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#     . format (name, age, main_lang))
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# def profile (name, age=17, main_lang="파이썬") :
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}" \
#     . format (name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile (name, age, main_lang) :
#     print (name, age, main_lang)
# profile(name="유재석", main_lang="파이썬", age=20)
# profile(main_lang="자바", age=25, name="김태호")

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age))
#     print(lang1, lang2, lang3, lang4, lang5)


# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")
#     print( )
    


# profile("유재석", 20, "Python", "Java", "C", "C++", "C#",  "Javascript")
# profile("김태호", 25, "Kotlin", "Swift", "", "", "")

# gun = 10 #전역변수
# def checkpoint(soldiers): # 경계근무
#     global gun#전역변수 사용 
#     # gun = 20 #지역변수
#     gun = gun - soldiers 
#     print("[함수 내] 남은 총 : {0}" .format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print ("[함수 내] 남은 총 : {0}".format(gun))
#     return gun


# print("전체 총: {0}". format(gun))
# # checkpoint(2) # 2명이 경계 근무 나감
# gun =checkpoint_ret(gun, 2)
# print("남은 총: {0}". format (gun))

# def std_weight(height, gender): # 표준 체중 계산 함수 정의
#     if gender == "남자":
#         return height * height * 22
#     else:
#         return height * height * 21

# height = 175 # 전달값(키, cm 단위)을 저장한 변수 정의
# gender = "남자" # 전달값(성별)을 저장한 변수 정의
# # weight = std_weight(height / 100, gender) # 함수 호출(키는 cm 단위에서 m 단위로 변환)
# weight = round(std_weight(height / 100, gender), 2) # 반올림해서 소수점 둘째 자리까지 표시
# print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))

# print("Python", "Java", sep=",", end="?")
# print("무엇이 더 재미있을까요?")

# import sys
# print("Pyton", "Java", file=sys.stdout)
# print("Pyton", "Java", file=sys.stderr)

# 시험 성적
# scores= {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items ():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번표
#001, 002, 003, ....
# for num in range(1, 21):
#     print("대기 번호 :" + str(num).zfill(3))

# answer = input("아무값이나 입력하세요 : ")
# print(type(answer))
# print("입력하신 값은 " + answer + "입니다.")

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500))

# # 양수일 땐 +로 표시, 음수일 땐-로 표시
# print("{0: >+10}". format (500))
# print("{0: >+10}". format (-500))

# # 왼쪽 정렬하고, 빈칸으로 로 채움
# print("{0:_<10}". format (500))

# # 3자리 마다 콤마를 찍어주기
# print("{0:,}". format (100000000000))

# # 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
# print("{0:+,}". format(100000000000))
# print("{0:+,}". format(-100000000000))

# # 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^로 채워주기
# print(" {0:^<+30,}". format (100000000000))

# # 소수점 출력 
# print("{0:f}".format(5 / 3))
# # 소수점 이하 둘째 자리까지 출력 셋째 자리에서 반올림 
# print("{0:.2f}".format(5 / 3)) 

# score_file = open("score.txt", "w", encoding="utf8") # score.txt 파일을 쓰기 모드로 열기
# print("수학 : 0", file=score_file) # score.txt 파일에 내용 쓰기
# print("영어 : 50", file=score_file) # score.txt 파일에 내용 쓰기
# score_file.close() # score.txt 파일 닫기


# score_file = open("score.txt", "a", encoding="utf8") # score.txt 파일에 이어 쓰기 모드로 열기
# score_file.write("과학 : 80\n")
# # write() 함수는 줄 바꿈이 없으므로 \n 추가
# score_file.write("코딩 : 100\n")
# score_file.close()


# #8.4.3
# score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기 모드로 열기
# print(score_file.read()) # 파일 전체 읽어 오기
# score_file.close()



# score_file = open("score.txt", "r", encoding="utf8") # score.txt 파일을 읽기 모드로 열기
# print(score_file.readline(), end="") # 한 줄씩 읽어 오고 커서는 다음 줄로 이동
# print(score_file.readline(), end="") # end 값을 설정해 줄 바꿈 중복 수행 방지
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")

# while True:
#     line = score_file.readline()
#     if not line: # 더 이상 읽어 올 내용이 없을 때
#         break # 반복문 탈출
#     print(line, end="") # 읽어 온 내용 출력

# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines() # 파일에서 모든 줄을 읽어 와 리스트 형태로 저장

# for line in lines: # lines에 내용이 있을 때까지
#     print(line, end="") # 읽어 온 내용 출력

# score_file.close()

# import pickle

# # 파일 쓰기 부분 (현재 주석 처리되어 있음)
# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미": ["축구", "골프", "코딩"]}
# pickle.dump(profile, profile_file)
# profile_file.close()

# # 파일 읽기 부분
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# import pickle

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))

# # 학습 내용 저장 및 불러오기
# with open("study.txt", "w", encoding="utf-8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt", "r", encoding="utf-8") as study_file:
#     study_contents = study_file.read()
#     print(study_contents)

# for i in range(1, 51):
#     # 파일 이름 생성
#     filename = str(i) + "주차.txt"

#     # 파일 열기 및 쓰기
#     with open(filename, "w", encoding="utf-8") as report_file:
#         report_file.write("- {}주차 주간보고 -".format(i))
#         report_file.write("\n부서 : ")  # 줄 바꿈 처리
#         report_file.write("\n이름 : ")
#         report_file.write("\n업무 요약 : ")

# 마린: 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" # 이름
# hp = 40 # 체력
# damage = 5 # 공격력

# print("{} 유닛을 생성했습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크: 공격 유닛, 포를 쏠 수 있음, 두 가지 모드(일반/시지 모드)
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛을 생성했습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

# # 새로 탱크2 추가
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛을 생성했습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]".format(name, location, damage))

# attack(name, "1시", damage) # 보병 공격 명령
# attack(tank_name, "1시", tank_damage) # 탱크 공격 명령
# attack(tank2_name, "1시", tank2_damage) # 탱크2 공격 명령


# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name # 인스턴스 변수 name에 전달값 name 저장
#         self.hp = hp # 인스턴스 변수 hp에 전달값 hp 저장
#         self.damage = damage # 인스턴스 변수 damage에 전달값 damage 저장
#         print("{0} 유닛을 생성했습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5) # 마린1 생성, 전달값으로 이름/체력/공격력 전달
# marine2 = Unit("마린", 40, 5) # 마린2 생성, 전달값으로 이름/체력/공격력 전달
# tank = Unit("탱크", 150, 35) # 탱크 생성, 전달값으로 이름/체력/공격력 전달
# # marine3 = Unit("마린",) # 전달값 3개 중 1개만 넘김, TypeError 발생
# # marine3 = Unit("마린", 40) # 전달값 3개 중 2개만 넘김, TypeError 발생

# 
# class Unit:
#     def __init__(self, name, hp, damage): # 생성자, 전달값 3개
#         self.name = name # 인스턴스 변수 name
#         self.hp = hp # 인스턴스 변수 hp
#         self.damage = damage # 인스턴스 변수 damage
#         print("{0} 유닛을 생성했습니다.".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
# wraithl = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraithl.name, wraithl.damage)) # 인스턴스 변수 접근

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraithl2 = Unit("뺴앗은 레이스", 80, 5)
# wraithl2.cloaking = True 

# if wraithl2.cloaking == True: # 클로킹 상태라면
#     print("{0}는 현재 클로킹 상태입니다.".format(wraithl2.name))

# 오류 발생
# if wraithl1.cloaking == True: # 다른 레이스의 클로킹 여부
#     print("{0}는 현재 클로킹 상태입니다.".format(wraithl1.name)) 


# class AttackUnit: # 공격 유닛
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location): # 전달받은 방향으로 공격
#         print("{0} : {1} 방향 적군을 공격합니다. [공격력 {2}]" \
#             .format(self.name, location, self.damage))  

#     def damaged(self, damage): # damage만큼 유닛 피해
#         # 피해 정보 출력
#         print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
#         self.hp -= damage # 유닛의 체력에서 전달받은 damage만큼 감소
#         # 남은 체력 출력
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0: # 남은 체력이 0 이하이면
#             print("{0} : 파괴됐습니다.".format(self.name)) # 유닛 파괴 처리

# # 파이어뱃 : 공격 유닛, 화염방사기.
# flamethrower1 = AttackUnit("파이어뱃", 50, 16) # 객체 생성, 체력 50, 공격력 16
# flamethrower1.attack("5시") # 5시 방향으로 공격 명령

# # 25만큼의 공격을 2번 받는다고 과정
# flamethrower1.damaged(25) # 남은 체력 25
# flamethrower1.damaged(25) # 남은 체력 0
#--------------------------------------------------------------------------------------------- 프로젝트
# from random import *
# class Unit:
#     def __init__(self, name, hp, speed):  # speed 추가
#         self.name = name
#         self.hp = hp
#         self.speed = speed  # speed 추가
#         print("{0} 유닛을 생성했습니다.".format(name))

#     def move(self, location):  # move 메서드 추가
#         print("[지상 유닛 이동]") 
#         print(f"{self.name} : {location} 방향으로 이동합니다. [속도 {self.speed}]")
    
    
#     def damaged(self, damage):
#         print("{0} : {1}만큼 피해를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴됐습니다.".format(self.name))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print(f"{self.name} : {location} 방향 적군을 공격합니다. [공격력 {self.damage}]")

# # 마린 유닛
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 5, 1) # 이름, 체력, 공격력, 이동 속도

#     # 스팀택: 일정 시간 동안 이동 속도와 공격 속도 증가, 체력 10 감소
#     def booster(self):
#         if self.hp > 10:
#             self.hp -= 10 # 체력 10 소모
#             print("{0} : 스팀팩를 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족해 기술을 사용할 수 없습니다".format(self.name))
# # 탱크 유닛
# class Tank(AttackUnit):
#     # 시지 모드 : 탱크를 지상에 고정, 이동 불가, 공격력 증가
#     siege_developed = False # 시지 모드 개발 여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 35, 1) # 이름, 체력, 공격력, 이동 속도
#         self.siege_mode = False # 시지 모드(해제 상태)

#     # 시지 모드 설정
#     def set_siege_mode(self):
#         if Tank.siege_developed == False: # 시지 모드가 개발되지 않았으면 바로 반환
#             return
#         # 현재 일반 모드일 때
#         if self.siege_mode == False:
#             print("{0} : 시지 모드로 전환합니다.".format(self.name))
#             self.damage *= 2 # 공격력 2배 증가
#             self.siege_mode = True # 시지 모드 설정
#         # 현재 시지 모드일 때
#         else:
#             print("{0} : 시지 모드를 해제합니다.".format(self.name))
#             self.damage //= 2 # 공격력 절반으로 감소
#             self.siege_mode = False # 시지 모드 해제

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]") 
#         self.fly(self.name, location)

# # 레이스 유닛
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스", 80, 20, 5)
#         self.cloaked = False # 클로킹 모드(해제 상태)

#     # 클로킹 모드
#     def cloaking(self):
#     # 현재 클로킹 모드일 때
#         if self.cloaked == True:
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#             self.cloaked = False
#         # 현재 클로킹 모드가 아닐 때
#         else:
#             print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
#             self.cloaked = True

# # 게임 시작
# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# # 게임 종료
# def game_over():
#     print("Player : Good Game")
#     print("[Player] 님이 게임에서 퇴장했습니다.")

# # 실제 게임 진행
# game_start() # 게임 시작

# # 보병 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# ta1 = Tank()
# ta2 = Tank()

# # 전투기 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리(생성된 모든 유닛 추가)
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(ta1)
# attack_units.append(ta2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈 모드 개발
# Tank.siege_developed = True
# print("[알림] 탱크의 시즈 모드 개발이 완료됐습니다.")

# # 공격 모드 준비(마린: 스팀팩, 탱크: 시즈 모드, 레이스: 클로킹 모드)
# for unit in attack_units:
#     if isinstance(unit, Marine): # Marine 클래스의 인스턴스이면 스팀팩
#         unit.booster()
#     elif isinstance(unit, Tank): # Tank 클래스의 인스턴스이면 시지 모드
#         unit.set_siege_mode()
#     elif isinstance(unit, Wraith): # Wraith 클래스의 인스턴스이면 은폐 모드
#         unit.cloaking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 20)) # 피해는 무작위로 받음(5~20)
    
# # 게임 종료
# game_over()

#--------------------------------------------------------------------------------------------- 프로젝트

# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사.
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.move("3시")  # fly 대신 move 사용

# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐", 80, 10, 20)  # speed와 damage의 위치를 바꿈
# vulture.move("11시")

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)
# battlecruiser.move("9시")  # fly 대신 move 사용

# # 건물
# # class BuildingUnit(Unit):
# #     def __init__ (self, name, hp, location):
# #         pass
# # #서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# # supply_depot= BuildingUnit("서플라이 디폿", 500, "7시")
# # def game_start():
# #     print ("[알림] 새로운 게임을 시작합니다.")
# # def game_over () :
# #     pass
# # game_start()
# # game_over()

# # class BuildingUnit(Unit):
# #     def __init__ (self, name, hp, location):
# #         #Unit.init_ (self, name, hp, 0)
# #         super().__init__(name, hp, 0)
# #         self.location = location

# class House:
#     # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공연도
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type, \
#         self.price, self.completion_year)

# houses = []
# house1 = House("강남", "아파트", "매매", "10억 원", "2010년")
# house2 = House("마포", "오피스텔", "전세", "5억 원", "2007년")
# house3 = House("송파", "빌라", "월세", "500/50만 원", "2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}가지 매물이 있습니다.".format(len(houses)))
# for house in houses:
#     house.show_detail()

# print("나누기 전용 계산기입니다.") #예외 처리전
# num1 = int(input("첫 번째 숫자를 입력하세요 : "))
# num2 = int(input("두 번째 숫자를 입력하세요 : "))
# print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))


# try:
#     print("나누기 전용 계산기입니다.") #예외 처리후
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))

# except ValueError:
#     print("오류 발생! 잘못된 값을 입력했습니다.")

# try:
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("오류 발생! 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)

# try: #리스트 예외처리
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
#     #nums.append(int(nums[0] / nums[1])) # 연산 결과를 리스트에 추가
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("오류 발생! 잘못된 값을 입력했습니다.")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 오류가 발생했습니다.")
#     print(err)

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")

# class BigNumberError(Exception): # 사용자 정의 예외 처리, Exception 클래스 상속
#     #pass
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg
#         #return "[오류 코드 001] " + self.msg # 오류 메시지 가공

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10: # 입력받은 수가 한 자리인지 확인
#         # raise ValueError
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) # 자세한 오류 메시지
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err: # 사용자 정의 예외 처리
#     print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
#     print(err) # 오류 메시지 출력

# class BigNumberError(Exception): 
#     #pass
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 : "))
#     num2 = int(input("두 번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10: 
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) 
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("값을 잘못 입력했습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err: 
#     print("오류가 발생했습니다. 한 자리 숫자만 입력하세요.")
#     print(err) 
# finally: # 오류 발생 여부와 상관없이 항상 실행
#     print("계산기를 이용해 주셔서 감사합니다.")

# class SoldOutError(Exception):
#     pass

# chicken = 10 # 남은 치킨 수
# waiting = 1 # 대기 번호, 1부터 시작

# while True:
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨을 몇 마리 주문하시겠습니까? "))
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기 번호 {0}] {1}마리를 주문했습니다.".format(waiting, order))
#             waiting += 1 # 대기 번호 증가
#             chicken -= order # 주문 수만큼 남은 치킨 감소
#         if chicken == 0:
#             raise SoldOutError
#     except ValueError:
#         print("잘못된 값을 입력했습니다.")
#     except SoldOutError:
#         print("재료가 소진돼 더 이상 주문을 받지 않습니다.")
#         break

# import theater_module # 모듈 가져오기

# theater_module.price(3) # 3명이 영화를 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이 조조 영화를 보러 갔을 때 가격
# theater_module.price_soldier(5) # 군인 5명이 영화를 보러 갔을 때 가격

# import theater_module as mv # theater_module을 별명인 mv로 사용한다는 의미
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import * # theater_module에서 모든 기능을 가져와 사용함

# price(3) # theater_module.을 작성할 필요 없음
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 모듈에서 일부 함수만 가져와 사용함

# price(5) # 5명
# price_morning(6) # 6명
# price_soldier(7) # import하지 않아서 사용 불가

# from theater_module import price_soldier as price

# price(5) # price_soldier() 함수 호출

# import travel.thailand # travel 패키지의 thailand 모듈 가져오기

# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()


"""
import travel.thailand.ThailandPackage # 클래스 import 불가

trip_to = travel.thailand.ThailandPackage()
trip_to.detail()
"""


# travel.thailand 모듈에서 ThailandPackage 클래스 가져오기
# from travel.thailand import ThailandPackage 

# trip_to = ThailandPackage() # from~import 문에서는 travel.thailand. 제외
# trip_to.detail()

# from travel import *

# trip_to = vietnam.VietnamPackage() # 베트남
# #trip_to = thailand.ThailandPackage() # 태국
# trip_to.detail()

# import inspect
# import random
# print(inspect.getfile(random)) # random 모듈 위치(경로)
# import inspect
# from travel import *
# print(inspect.getfile(thailand)) # thailand 모듈 위치



# pip install beautifulsoup4 원도우 pip3 install beautifulsoup4 맥os

# from bs4 import BeautifulSoup

# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

# input은 사용자가 입력 받는 함수
# language = input("어떤 언어를 좋아하세요? ")
# print("{0}은 아주 좋은 언어입니다!".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
# print(dir())
# import random # random 모듈 가져다 쓰기
# #import random # 외장 함수
# print(dir())
# import pickle # pickle 모듈 가져다 쓰기
# print(dir())

# import random
# print(dir(random))


# lst = [1, 2, 3]
# print(dir(lst))


# name = "Jim"
# print(dir(name))

#glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob

# print(glob.glob("*.py")) # 확장자가 py인 모든 파일 출력


# os : 운영체제에서 제공하는 기본 기능
# import os

# print(os.getcwd()) # 현재 작업 폴더 위치(경로)


# folder = "sample_dir"
# if os.path.exists(folder): # 같은 이름의 폴더가 존재한다면
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder) # 폴더 삭제
#     print(folder, "폴더를 삭제했습니다.") # 삭제 문구 출력
# else: # 폴더가 존재하지 않으면
#     os.makedirs(folder) # 폴더 생성
#     print(folder, "폴더를 생성했습니다.")

# print(os.listdir()) # 현재 작업 폴더 안의 폴더와 파일 목록 출력

# # time : 시간 관련 함수
# import time

# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S")) # 연-월-일 시:분:초


# import datetime

# print("오늘 날짜는", datetime.date.today())
# today = datetime.date.today() # 오늘 날짜 저장
# td = datetime.timedelta(days=100) # 100일째 날짜 저장
# print("우리가 만난 지 100일은", today + td) # 오늘부터 100일 후 날짜

# import byme

# byme.sign()