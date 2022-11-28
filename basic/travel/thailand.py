class ThaileandPackage:
    def detail(self):
        print('[탸국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원')

if __name__ == '__main__':
    print('Thailand 모듈을 직접 실행')
    print('이 문장은 모듈을 직접 실행할 때만 실행되요')
    trip_to = ThaileandPackage()
    trip_to.detail()
else:
    print('Thailand 외부에서 실행')