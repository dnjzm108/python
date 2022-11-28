
# # 예외 처리 - 에러가 발생 하였을때에 예외 처리

# try:
#     print('나누기 전용 계산기 입니다.')
#     nums = []
#     nums.append(int(input('첫 번째 숫자를 입력하세요 : ')))
#     nums.append(int(input('두 번째 숫자를 입력하세요 : ')))
#     nums.append(int(nums[0]/nums[1]))
#     print(f'{nums[0]} / {nums[1]} = {nums[2]}')

# except ValueError:
#     print('에러! 잘못된 값을 입력하였습니다.')
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print('알 수 없는 에러가 발생하였습니다.')
#     print(err)


# # 에러 발생 시키기
# try:
#     print('한 자리 숫자 나누기 전용기 계산기 입니다.')
#     num1 = int(input('첫번째 숫자를 입력하세요 : '))
#     num2 = int(input('두번째 숫자를 입력하세요 : '))
#     if num1 >= 10 or num2 > 10:
#         raise ValueError
#     print(f'{num1} / {num2} ={int(num1/num2)}')
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')


# # 사용자 정의 예외처리
# # class BigNumberError(Exception):
# #     pass
# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# try:
#     print('한 자리 숫자 나누기 전용기 계산기 입니다.')
#     num1 = int(input('첫번째 숫자를 입력하세요 : '))
#     num2 = int(input('두번째 숫자를 입력하세요 : '))
#     if num1 >= 10 or num2 > 10:
#         raise BigNumberError(f'입력값 : {num1} , {num2}')
#     print(f'{num1} / {num2} ={int(num1/num2)}')
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
# except BigNumberError as err:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
#     print(err)


# # finally - 에러가 나든 안나든 실행됨
# class BigNumberError(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg
# try:
#     print('한 자리 숫자 나누기 전용기 계산기 입니다.')
#     num1 = int(input('첫번째 숫자를 입력하세요 : '))
#     num2 = int(input('두번째 숫자를 입력하세요 : '))
#     if num1 >= 10 or num2 > 10:
#         raise BigNumberError(f'입력값 : {num1} , {num2}')
#     print(f'{num1} / {num2} ={int(num1/num2)}')
# except ValueError:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
# except BigNumberError as err:
#     print('잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.')
#     print(err)
# finally:
#     print('계산기를 이용해 주셔서 감사합니다.')


# Quiz ) 동네에 항상 대기 손님이 있는 맛있는 치킨집이 있습니다.
# 대기 손님의 치킨 요리 시간을 줄이고자 자동 주문 시스템을 제작하였습니다.
# 시스템 코드를 확인 하고 적절한 예외처리 구문을 넣으시오.

# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 ValueError 로 처리
#    출력 메세지 : '잘못된 값을 입력하였습니다.'
# 조건 2 : 대기 손님이 주문할 수 있는 총 치킨량을 10마리로 한정
#    치킨 소진 시 사용자 정의 에러 [SoldOutError]를 발생시키고 프로그램 종료
#    출력 메세지 : '재고가 소진되어 더 이상 주문을 받지 않습니다.'

# [ 코드 ]
chicken = 10
waiting = 1  # 홀 안에는 현재 만석,대기번호 1부터 시작


# class ValueError:
#     def __init__(self):
#         print('잘못된 값을 입력하였습니다.')


class SoldOutError(Exception):
    def __init__(self):
       pass


while (True):
    try:
        if chicken == 0:
            raise SoldOutError
        else:
            print(f'[남은 치킨 : {chicken}]')
            order = int(input('치킨 몇 마리 주문하시겠습니까?'))
            if order > chicken:  # 남은 치킨보다 주문량이 많을때
                raise ValueError
                # print('재료가 부족 합니다.')
            elif order == 0:
                raise ValueError
            else:
                print(f'[대기 번호 {waiting}] {order} 마리 주문이 완료 되엇습니다.')
                waiting += 1
                chicken -= order
    except ValueError as err:
        print('잘못된 값을 입력하였습니다.')
    except SoldOutError as err:
        print('재고가 소진되어 더이상 주문을 받지 않습니다.')
        break
