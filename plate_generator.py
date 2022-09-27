import random as r #载入随机数模块重命名为r
def license_plate(s):
    '''车辆号牌随机'''
    plate = [] #号码字符结构列表
    #号牌字头字母选择字符串
    s0 = 'ABDEFGH'
    #第2～5位选择字符串
    s25 = '0123456789ABCDEFGHIJKLMNPQRSTUVWXYZ'
    #生成号牌字头
    plate.append(f'{s}{r.choice(s0)}-')
    #生成第一位数字
    plate.append(str(r.randint(0, 9)))
    #生成号牌第2～5位字符
    plate.append(''.join([r.choice(s25) for i in range(5)]))
    return ''.join(plate)

if __name__=='__main__':
    city = '川' #更改城市简称，即可生成该城市牌号
    print()
    license_plates = []
    for i in range(5):
        s = f'{(i+1):2d}. {license_plate(city)}'
        print(f'    {s}')
        license_plates.append(s[4:])

        
    # print('﹊'*21)
    # choice = int(input(f'\n请选择您心仪的号码:'))
    # print('\n'*1)
    # print('﹊'*21)
    # print(f'    您选中的号牌是：{license_plates[choice-1]}')
    # print('﹊'*21)
