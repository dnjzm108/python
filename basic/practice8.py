# # class

# # 마린 : 공격 유닛 , 군인 , 총을 쓸 수 있음
# name = '마린'  #유닛의 이름
# hp = 40  # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print(f'{name} 유닛이 생성되었습니다.')
# print(f'체력 {hp}, 공격력 {damage}\n')

# # 탱크 : 공격 유닛, 탱크 , 포를 쏘 수잇는데  일반 모드 / 시즈 모드.
# tank_name = '탱크'
# tank_hp = 150
# tank_damage = 35

# print(f'{tank_name} 유닛이 생성되었습니다.')
# print(f'체력 {tank_hp}, 공격력 {tank_damage}\n')

# def attack(name,location,damage):
#     print(f'{name} : {location} 방향으로 적군을 공격 합니다.[공격력 {damage}]')

# attack(name,'1시',damage)
# attack(tank_name,'1시',tank_damage)


# # 이렇게 일일히 하나씩 만들기 번거로워서 class 가 필요  class 는 붕어빵 틀 같은것 제료만 넣어주면 무한정 만들어 낼 수 있음


# class unit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print(f'{self.name} 유닛이 생성되었습니다.')
#         print(f'체력 : {hp},공격력 {damage}')

# marien1 = unit('마린',40,5)
# marien2 = unit('마린',40,5)
# tank = unit('탱크',150,35)

# # __init__
# # python 에서 쓰이는 생성자  클래스로 부터 만들러지는 객체가 생성될떼 자동으로 호출되는 부분
# # self 를 뺀 나머지 인자값을 모두 써주어야 한다 . 안그럼 에러가 남
# # 여기서 marien,tank 부분을 인스턴스라고 한다.


# # 멤버 변수
# # 클래스 안에 self.name ,self.hp 가 멤버 변수 이다.

# # 레이스 : 공중유닛 ,비행기,클로킹 (상대방에게 보이지 않음)
# wraith1 = unit('레이스',80,5)
# print(f'유닛 이름 : {wraith1.name},공격력 : {wraith1.damage}')

# # 마인드 컨트롤 : 상대방 유닛을 내 것 으로 만드는 것 (빼앗음)
# wraith2 = unit('빼앗은 레이스',80,5)
# wraith2.clocking = True
# # 외부에서 확장 가능 . 변수 할당을 할 수 있음. 다른 객체에 영향을 안줌. 내가 확장한 이외에 객체에서 찾으려고 하면 에러가 남.


# if wraith2.clocking == True:
#     print(f'{wraith2.name} 는 현재 클로킹 상태 입니다.')


# # 메소드

# # 일반 유닛
# class Unit:
#     def __init__(self,name,hp):
#         self.name = name
#         self.hp = hp
#         # self.damage = damage
#         # print(f'{self.name} 유닛이 생성되었습니다.')
#         # print(f'체력 : {hp},공격력 {damage}')

# class AttackUnit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self,location):
#         print(f'{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]')

#     def damaged(self,damage):
#         print(f'{self.name} : {damage} 데메지를 입었습니다.')
#         self.hp -= damage
#         print(f'{self.name}: 현재 체력은 {self.hp} 입니다.')
#         if self.hp <= 0:
#             print(f'{self.name} : 파괴되었습니다.')

# # 파이어뱃 : 공격 유닛 , 화염 방사기.
# firebat1 = AttackUnit('파이어뱃',50,16)
# firebat1.attack('5시')

# # 공격 2번 받는 다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)


# #  상속

# # class AttackUnit(Unit):
# #     def __init__(self,name,hp,damage):
# #         Unit.__init__(self,name,hp)  # class 인자로 다른 클래스에 상속 받아 사용 가능
# #         self.damage = damage


# # 다중 상속

# # 날 수 있는 기능을 가진 클래스
# class Flyable:
#     def __init__(self,flying_speed):
#         self.flyng_speed = flying_speed

#     def fly(self,name,location):
#         print(f'{name} : {location} 방향으로 날아간다. [속도{self.flyng_speed}]')

# class FlyableAttackUnit(AttackUnit,Flyable):
#     def __init__(self,name,hp,damage,flying_speed):
#         AttackUnit.__init__(self,name,hp,damage)
#         Flyable.__init__(self,flying_speed)


# valkyrie = FlyableAttackUnit('발키리',200,6,5)
# valkyrie.fly(valkyrie.name,'3시')


# # 메소드 오버라이딩  - 자식 클래스 에서 정의한 매소드를 쓰고 싶을때 매소드를 새롭게 정의하여 사용하는 방법

class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print('[지상 유닛 이동]')
        print(f'{self.name}:{location} 방향으로 이동 합니다. [속도 {self.speed}]')


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print(f'{self.name} : {location} 방향으로 적군을 공격 합니다. [공격력 {self.damage}]')

    def damaged(self, damage):
        print(f'{self.name} : {damage} 데미지 입엇습니다.')
        self.hp -= damage
        print(f'{self.name} : 현재 체력은 {self.hp} 입니다.')
        if self.hp <= 0:
            print(f'{self.name} : 파괴되었습니다.')


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f'{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]')


class FlyableAttckUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

# vulture = AttackUnit('벌쳐',80,10,20)

# battlecruiser = FlyableAttckUnit('배틀 크루저',500,25,3)

# vulture.move('11시')
# battlecruiser.move('9시')


# # pass
# # 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self,name,hp,0)
#         super().__init__(name, hp, 0)
#         self.location = location


# # 서플라이 디폿 : 건물 , 1개 건물 = 8 유닛
# supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')

# def game_start():
#     print('[알림] 새로운 게임을 시작합니다.')

# def game_over():
#     pass

# game_start()
# game_over()


# # super
# class Unit:
#     def __init__(self):
#         print('Unit 생성자')

# class Flyable:
#     def __init__(self):
#         print('Flyable 생성자')

# class FlyableUnit(Flyable,Unit):
#     def __init__(self):
#         Unit.__init__(self)
#         Flyable.__init__(self)
# # 드림쉽
# dropship = FlyableUnit()


# Quiz) 주어진 코드를 활용하여 부동산 프로그램을 작성하시오.

# 출력예제)
# 총 3대의 매물이 있습니다.
# 강남 아파트 매매 10억 2010년
# 마포 오피스텔 전세 5억 2007년
# 송파 빌라 월세 500/50 2000년

# 코드)

class House:
    # 매물 초기화
    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.comletion_year = completion_year

    # 매물 정보 표시
    def show_detail(self):
        print(self.location, self.house_type, self.deal_type,
              self.deal_type, self.price, self.comletion_year)

houses = []
house1 = House('강남','아파트','매매','10억','2010년')
house2 = House('마포','오피스텔','전세','5억','2007년')
house3 = House('송파','빌라','월세','500/50','2000년')

houses.append(house1)
houses.append(house2)
houses.append(house3)

print(f'총 {len(houses)}대 매물이 있습니다.')
for house in houses:
    house.show_detail()