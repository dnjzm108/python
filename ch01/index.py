from random import *

def random(num,min,max):
    result = []
    for i in range(int(num)):
        result.append(randint(min,max))

    return result

if __name__ in '__main__':
    print(random(6,1,46))

