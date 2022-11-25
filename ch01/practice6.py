# 함수

def open_account():  # 함수 선언 하는 부분
    print('새로운 계좌가 생성되었습니다.')


open_account()  # 함수 호출 하는 부분


def deposit(balance, money):
    print(f'입금이 완료 되었습니다. 잔액은 {balance + money} 원 입니다.')
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print(f'출금이 완료되었습니다. 잔액은 {balance - money} 원 입니다.')
        return balance - money
    else:
        print(f'출금이 완료되지 않았습니다. 작액은 {balance} 원 입니다.')
        return balance


def withdraw_night(balance, money):
    commission = 100  # 수수료 100원
    return commission, balance - money - commission


balance = 0  # 잔액
balance = deposit(balance, 1000)
balance = withdraw(balance, 300)

commission, balance = withdraw_night(balance, 500)
print(f'수수료 {commission} 원 이며, 잔액은 {balance}원 입니다.')


# 기본값

def profile(name, age, main_lang):
    print(f'이름 : {name}\t나이 : {age}\t주 사용 언어 : {main_lang}')


profile('유재석', 20, '파이썬')
profile('김태호', 25, '자바')

# 같은 학교 같은 학년 같은 반 같은 수업


def profile(name, age=17, main_lang="파이썬"):
    print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}'
          .format(name, age, main_lang))


profile('유재석', 33, 'java')
profile('김태호')


def profile(name, age, main_lang):
    print(name, age, main_lang)


profile(name='유재석', main_lang='파이썬', age=20)
profile(main_lang='자바', age=20, name='김태호')


# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    # end=' ' 를 하면 줄바꿈이 되지 않고 옆으로 작성된다.
    print('이름 : {0}\t나이 : {1}\t'.format(name, age), end=' ')
    print(lang1, lang2, lang3, lang4, lang5)


print('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#')
print('김태호', 25, 'Kotlin', 'Swift', '', '', '')


def profile(name, age, *language):  # *변수  가변 인자
    print('이름 : {0}\t나이 : {1}\t'.format(name, age), end=' ')
    for lang in language:
        print(lang, end=" ")
    print()  # 마지막 줄바꿈을 위해서


print('유재석', 20, 'Python', 'Java', 'C', 'C++', 'C#')
print('김태호', 25, 'Kotlin', 'Swift', '', '', '')


# 지역 변수 와 전역 변수
# 지역변수 함수 안에서만 사용되는 변수 전역 변수는 어디서든 호출 가능한 변수

gun = 10


def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')


def checkpotint_ret(gun, soldiers):
    gun = gun - soldiers
    print(f'[함수 내] 남은 총 : {gun}')
    return gun


print(f'전체 총 : {gun}')
gun = checkpotint_ret(gun, 2)
print(f'남은 총 : {gun}')


# Quiz) 표준 체중을 구하는 프로그램을 작성하시오.
# * 표준체중 : 각 개인의 키레 적당한 체중

# (성별에 따른 공식)
# 남자 : 키(m) * 키(m) * 22
# 여자 : 키(m) * 키(m) * 21

# 조건 1: 표준체중은 별고의 함수 내에서 계산
#      * 함수명 : std_weight
#      * 전달값 : 키(height) , 성별(gender)
# 조건 2: 표준 체중은 소수점 둘째자리까지 표시

# (출력 예제)
# 키 175 cm 남자의 표준 체중은 67.38kg 입니다.

def sdt_weight(gender, height):  # 키는 m 단위 (실수) , 성별 남자/ 여자

    if gender == '남자':
       return round(height * height * 22, 2)
    else:
        return round(height * height * 21, 2)


height = 175
gender = '남자'
weight = sdt_weight(gender, height / 100)
print(f'키 {height}cm {gender}의 표준 체중은 {weight}kg 입니다.')
