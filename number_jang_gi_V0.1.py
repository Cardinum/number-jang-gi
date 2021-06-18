#숫자장기
#V0.0 -- 실행 불가 버전입니다.
#V0.0.1 -- 실행 가능 버전입니다. 버그가 다소 있을 수 있습니다. hot_fix -- 맨 마지막 자리 최적화 -- 중간자리 시스템 추가 및 개편 혹은 안정화 완료-- 첫 자리
import time as ti
# ******왼쪽 위 부터 1,1 오른쪽위 1,9 왼쪽 아래 6,1 오른쪽 아래 ㅗㅜㅑ
# ******왼쪽이 player_a 오른쪽이 player_b

#제일 작은 리스트 [0]= 0(NONE)1(player_a)2(player_b) [1]=marker
#tile = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
#테스트 타일
tile=[[[0, 0], [1, '10'], [1, 'K'], [0, 0], [1, '1'], [1, '2']], [[1, '9'], [0, 0], [1, '7'], [1, 'M'], [1, '3'], [1, '8']], [[0, 0], [1, 'M'], [1, '4'], [1, '6'], [1, '5'], [1, 'M']], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[2, 'M'], [2, '9'], [2, '3'], [2, '10'], [0, 0], [2, '5']], [[2, '7'], [2, '1'], [2, '8'], [2, '2'], [2, 'M'], [0, 0]], [[0, 0], [2, 'M'], [2, 'K'], [2, '6'], [2, '4'], [0, 0]]]
#리스트가 이조랄 난 이유는 잡것 폴더의 test.py 참조
player_a_remain = ['1','2','3','4','5','6','7','8','9','10','M','M','M','K']
player_b_remain = ['1','2','3','4','5','6','7','8','9','10','M','M','M','K']
player_a_dead = []
player_b_dead = []

#player_a 타일 준비
def prepare_tile_a():
    while not player_a_remain ==[] :
        pas = 0
        #타일 위치, 정보 입력부
        try:
            x,y=input("x,y를 공백으로 구분하여 입력하여 주십시오.").split()
            marker = input("놓을 말을 입력해 주십시오. (1~10까지의 정수,M,K)")
            x=int(x)
            y=int(y)
            marker=str(marker)
        except:
            print("잘못된 입력입니다.")
            continue
        #타일 예외 방지 (자기 진영 아닌곳, 말이 이미 배치되어 있는 곳에 놓는 것, 이미 놓은 말을 다시 시도하는 것)
        while True:
            if(x>3)or(y>6):
                print("자신의 진영이 아닌 곳에서는 말을 놓을 수 없습니다. x=3이하인 부분에서 다시 시도해주십시오.")
                pas = 0
                break
            elif not(tile[x-1][y-1][0]==0):
                print("이미 말이 배치되어 있는 자리입니다. 다른 자리에 다시 시도해주십시오.")
                pas = 0
                break
            else:
                try:
                    player_a_remain.remove(marker)
                    print("( "+str(x)+" , "+str(y)+" ) 지점에 말 "+marker+"을 배치했습니다.")
                    pas = 1
                    break
                except:
                    print("이미 놓은 말입니다.")
                    print("현재 배치할 수 있는 남은 말은"+str(player_a_remain)+"입니다.")
                    pas = 0
                    break
        if pas == 0:
            continue
        else: 
            tile[x-1][y-1][1]=marker
            tile[x-1][y-1][0]=1
            continue

#player_b 타일 준비 (a와 같음)
def prepare_tile_b():
    while not player_b_remain ==[] :
        pas = 0
        try:
            x,y=input("놓을 말의 x값,y값을 공백으로 구분하여 입력하여 주십시오.").split()
            marker = input("놓을 말을 입력해 주십시오. (1~10까지의 정수,M,K)")
            x=int(x)
            y=int(y)
            marker=str(marker)
        except:
            print("잘못된 입력입니다.")
            continue
        while True:
            if(x<7) or (y>6):
                print("자신의 진영이 아닌 곳에서는 말을 놓을 수 없습니다. x=7이상인 부분에서 다시 시도해주십시오.")
                pas = 0
                break
            elif not(tile[x-1][y-1][0]==0):
                print("이미 말이 배치되어 있는 자리입니다. 다른 자리에 다시 시도해주십시오.")
                pas = 0
                break
            else:
                try:
                    player_b_remain.remove(marker)
                    print("( "+str(x)+" , "+str(y)+" ) 지점에 말 "+marker+"을 배치했습니다.")
                    pas = 1
                    break
                except:
                    print("이미 놓은 말입니다.")
                    print("현재 배치할 수 있는 남은 말은"+str(player_b_remain)+"입니다.")
                    pas = 0
                    break
        if pas == 0:
            continue
        else: 
            tile[x-1][y-1][1]=marker
            tile[x-1][y-1][0]=2
            continue

#말의 정보를 3단위로 나누어주는 부분 ++
def spac(sth):
    if sth=='10':
        result = '1 0'
    elif sth == 0:
        result='   '
    else:
        result = ' '+sth+' '
    return result

#말 판을 시각화 해 주는 부분(player_a가 왼쪽 b가 오른쪽)
def visualize_a():
    space=' '
    t_tile=''
    for i_tile in range(54):
        if i_tile == 0:
            print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┐")
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')
        elif i_tile == 53:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')
            print("│")
            print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")
        elif i_tile % 9 == 0:
            print("├───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')
        elif i_tile % 9 == 8:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')
            print("│")
        else:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')

def visualize_b():
    space=' '
    t_tile=''
    for i_tile in range(54):
        if i_tile == 0:
            print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┐")
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')
        elif i_tile == 53:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')
            print("│")
            print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")
        elif i_tile % 9 == 0:
            print("├───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')
        elif i_tile % 9 == 8:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')
            print("│")
        else:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print(" □ ",end = '')

def visualize_all():
    space=' '
    t_tile=''
    for i_tile in range(54):
        if i_tile == 0:
            print("┌───┬───┬───┬───┬───┬───┬───┬───┬───┐")
            print("│",end='')
            print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
        elif i_tile == 53:
            print("│",end='')
            print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            print("│")
            print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")
        elif i_tile % 9 == 0:
            print("├───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            print("│",end='')
            print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
        elif i_tile % 9 == 8:
            print("│",end='')
            print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            print("│")
        else:
            print("│",end='')
            print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
        
def move_a():
    while True:
        try:
            before_tile_x,before_tile_y = input("움직일 말의 x값,y값을 공백으로 구분하여 입력하여 주십시오.").split()
            before_tile_x = int(before_tile_x) - 1
            before_tile_y = int(before_tile_y) - 1
        except:
            print("잘못된 입력입니다.")
            continue
        move_size = 1
        dire = input("움직일 방향을 설정해 주십시오. [1]상단[2]우측 상단[3]오른쪽(최대 2칸)[4]우측 하단[5]하단")
        dire = int(dire)
        if dire == 3:
            move_size = input("움직일 칸 수를 설정해 주십시오. [1]1칸[2]2칸")
            move_size = int(move_size)
        else:
            pass
        
        if dire == 1:
            after_tile_x = before_tile_x
            after_tile_y = before_tile_y - 1
        elif dire == 2:
            after_tile_x = before_tile_x + 1
            after_tile_y = before_tile_y - 1
        elif dire == 3:
            after_tile_y= before_tile_y
            if move_size == 1:
                after_tile_x = before_tile_x + 1
            else:
                after_tile_x = before_tile_x + 2
        elif dire == 4:
            after_tile_x = before_tile_x + 1
            after_tile_y = before_tile_y + 1
        else:
            after_tile_x = before_tile_x 
            after_tile_y = before_tile_y + 1

        if after_tile_x > 8 or after_tile_x < 0 or after_tile_y > 5 or after_tile_y < 0:
            print("빈 공간으로는 이동이 불가능합니다. 다시 움직여 주십시오.")
            continue
        elif not tile[after_tile_x][after_tile_y][1] == 0:
            print("이미 말이 있는 칸입니다. 다시 움직여 주십시오.")
            continue
        elif tile[after_tile_x + 1][after_tile_y][0] == 1:
            print("자신의 말은 뛰어 넘을 수 없습니다. 다시 움직여 주십시오.")
            continue
        elif tile[before_tile_x][before_tile_y][1] == 'M':
            print("지뢰는 움직일 수 없습니다.다시 움직여 주십시오.")
            continue
        elif tile[before_tile_x][before_tile_y][1] == 0:
            print("비어있는 칸을 움직일 수 없습니다.다시 움직여 주십시오.")
        else:
            break

    tile[after_tile_x][after_tile_y][1] = tile[before_tile_x][before_tile_y][1]
    tile[after_tile_x][after_tile_y][0] = tile[before_tile_x][before_tile_y][0]
    tile[before_tile_x][before_tile_y][0] = 0
    tile[before_tile_x][before_tile_y][1] = 0

    if tile[after_tile_x][after_tile_y][1] == 'K' and tile[after_tile_x][after_tile_y][0] == 1 and after_tile_x == 9:
        lose(2,'k_forward')

    meet_check(after_tile_x, after_tile_y)
        
def move_b():
    while True:
        try:
            before_tile_x,before_tile_y = input("움직일 말의 x값,y값을 공백으로 구분하여 입력하여 주십시오.").split()
            before_tile_x = int(before_tile_x) - 1
            before_tile_y = int(before_tile_y) - 1
        except:
            print("잘못된 입력입니다.")
            continue
        move_size = 1
        dire = input("움직일 방향을 설정해 주십시오. [1]상단[2]좌측 상단[3]왼쪽(최대 2칸)[4]좌측 하단[5]하단")
        dire = int(dire)
        if dire == 3:
            move_size = input("움직일 칸 수를 설정해 주십시오. [1]1칸[2]2칸")
            move_size = int(move_size)
        else:
            pass
        
        if dire == 1:
            after_tile_x = before_tile_x
            after_tile_y = before_tile_y - 1
        elif dire == 2:
            after_tile_x = before_tile_x - 1
            after_tile_y = before_tile_y - 1
        elif dire == 3:
            after_tile_y = before_tile_y
            if move_size == 1:
                after_tile_x = before_tile_x - 1
            else:
                after_tile_x = before_tile_x - 2
        elif dire == 4:
            after_tile_x = before_tile_x - 1
            after_tile_y = before_tile_y + 1
        else:
            after_tile_x = before_tile_x 
            after_tile_y = before_tile_y + 1

        if after_tile_x > 8 or after_tile_x < 0 or after_tile_y > 5 or after_tile_y < 0:
            print("빈 공간으로는 이동이 불가능합니다. 다시 움직여 주십시오.")
            continue
        elif not tile[after_tile_x][after_tile_y][1] == 0:
            print("이미 말이 있는 칸입니다. 다시 움직여 주십시오.")
            continue
        elif tile[after_tile_x - 1][after_tile_y][0] == 2:
            print("자신의 말은 뛰어 넘을 수 없습니다. 다시 움직여 주십시오.")
            continue
        elif tile[before_tile_x][before_tile_y][1] == 'M':
            print("지뢰는 움직일 수 없습니다.다시 움직여 주십시오.")
            continue
        elif tile[before_tile_x][before_tile_y][1] == 0:
            print("비어있는 칸을 움직일 수 없습니다.다시 움직여 주십시오.")
        else:
            break

    tile[after_tile_x][after_tile_y][1] = tile[before_tile_x][before_tile_y][1]
    tile[after_tile_x][after_tile_y][0] = tile[before_tile_x][before_tile_y][0]
    tile[before_tile_x][before_tile_y][0] = 0
    tile[before_tile_x][before_tile_y][1] = 0

    if tile[after_tile_x][after_tile_y][1] == 'K' and tile[after_tile_x][after_tile_y][0] == 2 and after_tile_x == 1:
        lose(1,'k_forward')

    meet_check(after_tile_x, after_tile_y)
        
#start_time은 턴 시작과 동시에 카운트
#lose_check는 턴 종료에 카운트 
def lose_check(player):
    end_time = ti.time()
    tot_time = end_time - start_time
    if tot_time > 60 :
        lose(player, 'time_out')
    elif player_a_dead == ['1','2','3','4','5','6','7','8','9','10','M','M','M']:
        lose(1,'other_dead')
    elif player_b_dead == ['1','2','3','4','5','6','7','8','9','10','M','M','M']:
        lose(2,'other_dead')

#x에 after_tile_x,y에 after_tile_y 넣어서 활용
#2번 싸우는거 인식 안되는 경우 있음
def meet_check(x,y):
    x = int(x)
    y = int(y)
    team = tile[x][y][0]
    b = [0,0,0,0]#x+, x-, y+, y-
    try:
        if tile[x + 1][y][0] != team and tile[x + 1][y][0] != 0:
            b[0] = 1
    except:
        pass
    try:
        if tile[x - 1][y][0] != team and tile[x - 1][y][0] != 0:
            b[1] = 1
    except:
        pass
    try:
        if tile[x][y + 1][0] != team and tile[x][y + 1][0] != 0:
            b[2] = 1
    except:pass
    try:
        if tile[x][y - 1][0] != team and tile[x][y - 1][0] != 0:
            b[3] = 1
    except:
        pass

    b_count= b.count(1)
    if b_count == 0:
        pass
    elif b_count == 1:
        if b[0] == 1:
            battle(x,y,x+1,y)
        elif b[1] == 1:
                battle(x,y,x-1,y)
        elif b[2] == 1:
            battle(x,y,x,y+1)
        elif b[3] == 1:
            battle(x,y,x,y-1)
        else:
            pass
    elif b_count == 2:
        prnit("b_count =2")
        b_x = 10
        b_y = 10
        c_x = 10
        c_y = 10
        if b_x == 10 and b_y == 10:
            if b[0] == 1:
                b_x = x+1
                b_y = y
                b[0] = 0
            elif b[1] == 1:
                b_x = x-1
                b_y = y
                b[1] = 0
            elif b[2] == 1:
                b_x = x
                b_y = y+1
                b[2] = 0
            elif b[3] == 1:
                b_x = x-1
                b_y = y-1
                b[3] = 0
            else: pass
        else:
            if b[0] == 1:
                c_x = x+1
                c_y = y
                b[0] = 0
            elif b[1] == 1:
                c_x = x-1
                c_y = y
                b[1] = 0
            elif b[2] == 1:
                c_x = x
                c_y = y+1
                b[2] = 0
            elif b[3] == 1:
                c_x = x-1
                c_y = y-1
                b[3] = 0
            else: pass
        print(c_x,c_y)
        battle(x,y,b_x,b_y,c_x,c_y)
    elif b_count == 3:
        print("b_count = 3")
        b_x = 10
        b_y = 10
        c_x = 10
        c_y = 10
        d_x = 10
        d_y = 10
        if b_x == 10 and b_y == 10:
            if b[0] == 1:
                b_x = x+1
                b_y = y
                b[0] = 0
            elif b[1] == 1:
                b_x = x-1
                b_y = y
                b[1] = 0
            elif b[2] == 1:
                b_x = x
                b_y = y+1
                b[2] = 0
            elif b[3] == 1:
                b_x = x-1
                b_y = y-1
                b[3] = 0
            else: pass
        elif c_x == 10 and c_y == 10:
            if b[0] == 1:
                c_x = x+1
                c_y = y
                b[0] = 0
            elif b[1] == 1:
                c_x = x-1
                c_y = y
                b[1] = 0
            elif b[2] == 1:
                c_x = x
                c_y = y+1
                b[2] = 0
            elif b[3] == 1:
                c_x = x-1
                c_y = y-1
                b[3] = 0
            else: pass
        else:
            if b[0] == 1:
                d_x = x+1
                d_y = y
                b[0] = 0
            elif b[1] == 1:
                d_x = x-1
                d_y = y
                b[1] = 0
            elif b[2] == 1:
                d_x = x
                d_y = y+1
                b[2] = 0
            elif b[3] == 1:
                d_x = x-1
                d_y = y-1
                b[3] = 0
            else: pass
        battle(x,y,b_x,b_y,c_x,c_y,d_x,d_y)
    else:pass    
              
def pn_to_p(player_number):
    if player_number == 1:
        return 'player_a'
    else:
        return 'player_b'

#a가 전진 후 대결이 발생하므로 b,c,d 간의 대결은 미고려
def battle(a_x,a_y, b_x,b_y, c_x = 10, c_y = 10, d_x = 10, d_y = 10):
    marker_a = tile[a_x][a_y][1]
    marker_b = tile[b_x][b_y][1]
    try:
        marker_c = tile[c_x][c_y][1]
    except:
        pass
    try:
        marker_d = tile[d_x][d_y][1]
    except:
        pass
    a_live = True
    b_live = True
    c_live = True
    d_live = True
    none_c = False
    none_d = False
    if c_x == 10 and c_y == 10 :
        none_c = True
        if d_x == 10 and d_y == 10:
            none_d = True
        else:pass
    else:pass

    print(c_x,c_y,d_x,d_y,none_c,none_d)

    

    print("==========대결 발생==========")
    print("제 1 대결")
    print(pn_to_p(tile[a_x][a_y][0])+"의 말 : "+marker_a)
    print(pn_to_p(tile[b_x][b_y][0])+"의 말 : "+marker_b)
    if marker_a == 'K':
        a_live = False
    elif marker_b == 'K':
        b_live = False
    elif marker_a == 'M' or marker_b == 'M':
        print("지뢰와 대결하여 player_a의 말과 player_b의 말 둘 다 사망입니다.")
        a_live = False
        b_live = False
    elif int(marker_a)+int(marker_b) < 10:
        if int(marker_a) > int(marker_b):
            print("두 수의 합이 10보다 낮으므로 낮은 숫자인 "+marker_b+" 승리")
            a_live = False
        elif int(marker_a) < int(marker_b):
            print("두 수의 합이 10보다 낮으므로 낮은 숫자인 "+marker_a+" 승리")
            b_live = False
        else:
            print("무승부이므로 말 둘 다 사망입니다.")
            a_live = False
            b_live = False
    elif int(marker_a)+int(marker_b) >9:
        if int(marker_a) > int(marker_b):
            print("두 수의 합이 10보다 크므로 높은 숫자인 "+marker_a+" 승리")
            b_live = False
        elif int(marker_a) < int(marker_b):
            print("두 수의 합이 10보다 크므로 높은 숫자인 "+marker_b+" 승리")
            a_live = False
        else:
            print("무승부이므로 말 둘 다 사망입니다.")
            a_live = False
            b_live = False
    elif ( a_y + b_y == 3 and abs(a_y - b_y) == 1) or ( a_y + b_y == 7 and abs(a_y - b_y) == 1):
        if abs(int(marker_a) - int(marker_b)) < 10:
            if int(marker_a) > int(marker_b):
                print("*******마이너스 대결입니다.")
                print("두 수의 차가 10보다 낮으므로 낮은 숫자인 "+marker_b+" 승리")
                a_live = False
            elif int(marker_a) < int(marker_b):
                print("*******마이너스 대결입니다.")
                print("두 수의 차가 10보다 낮으므로 낮은 숫자인 "+marker_a+" 승리")
                b_live = False
            else:
                print("*******마이너스 대결입니다.")
                print("무승부이므로 말 둘 다 사망입니다.")
                a_live = False
                b_live = False
        elif abs(int(marker_a) - int(marker_b))>10:
            if int(marker_a) > int(marker_b):
                print("*******마이너스 대결입니다.")
                print("두 수의 차가 10보다 크므로 높은 숫자인 "+marker_a+" 승리")
                b_live = False
            elif int(marker_a) < int(marker_b):
                print("*******마이너스 대결입니다.")
                print("두 수의 차가 10보다 크므로 높은 숫자인 "+marker_b+" 승리")
                a_live = False
            else:
                print("*******마이너스 대결입니다.")
                print("무승부이므로 말 둘 다 사망입니다.")
                a_live = False
                b_live = False
    
    if not none_c :
        print("==========대결 발생==========")
        print("제 2 대결")
        print(pn_to_p(tile[a_x][a_y][0])+"의 말 : "+marker_a)
        print(pn_to_p(tile[c_x][c_y][0])+"의 말 : "+marker_c)
        if marker_a == 'K':
            a_live = False
        elif marker_c == 'K':
            c_live = False
        elif marker_a == 'M' or marker_c == 'M':
            print("지뢰와 대결하여 player_a의 말과 player_b의 말 둘 다 사망입니다.")
            a_live = False
            c_live = False
        elif int(marker_a)+int(marker_c) < 10:
            if int(marker_a) > int(marker_c):
                print("두 수의 합이 10보다 낮으므로 낮은 숫자인 "+marker_c+" 승리")
                a_live = False
            elif int(marker_a) < int(marker_c):
                print("두 수의 합이 10보다 낮으므로 낮은 숫자인 "+marker_a+" 승리")
                c_live = False
            else:
                print("무승부이므로 말 둘 다 사망입니다.")
                a_live = False
                c_live = False
        elif int(marker_a)+int(marker_c) >9:
            if int(marker_a) > int(marker_c):
                print("두 수의 합이 10보다 크므로 높은 숫자인 "+marker_a+" 승리")
                c_live = False
            elif int(marker_a) < int(marker_c):
                print("두 수의 합이 10보다 크므로 높은 숫자인 "+marker_c+" 승리")
                a_live = False
            else:
                print("무승부이므로 말 둘 다 사망입니다.")
                a_live = False
                c_live = False
        elif ( a_y + c_y == 3 and abs(a_y - c_y) == 1) or ( a_y + c_y == 7 and abs(a_y - c_y) == 1):
            if abs(int(marker_a) - int(marker_c)) < 10:
                if int(marker_a) > int(marker_c):
                    print("*******마이너스 대결입니다.")
                    print("두 수의 차가 10보다 낮으므로 낮은 숫자인 "+marker_c+" 승리")
                    a_live = False
                elif int(marker_a) < int(marker_c):
                    print("*******마이너스 대결입니다.")
                    print("두 수의 차가 10보다 낮으므로 낮은 숫자인 "+marker_a+" 승리")
                    c_live = False
                else:
                    print("*******마이너스 대결입니다.")
                    print("무승부이므로 말 둘 다 사망입니다.")
                    a_live = False
                    c_live = False
            elif abs(int(marker_a) - int(marker_c))>10:
                if int(marker_a) > int(marker_c):
                    print("*******마이너스 대결입니다.")
                    print("두 수의 차가 10보다 크므로 높은 숫자인 "+marker_a+" 승리")
                    c_live = False
                elif int(marker_a) < int(marker_c):
                    print("*******마이너스 대결입니다.")
                    print("두 수의 차가 10보다 크므로 높은 숫자인 "+marker_c+" 승리")
                    a_live = False
                else:
                    print("*******마이너스 대결입니다.")
                    print("무승부이므로 말 둘 다 사망입니다.")
                    a_live = False
                    c_live = False
    
    if not none_d :
        print("==========대결 발생==========")
        print("제 3 대결")
        print(pn_to_p(tile[a_x][a_y][0])+"의 말 : "+marker_a)
        print(pn_to_p(tile[d_x][d_y][0])+"의 말 : "+marker_d)
        if marker_a == 'K':
            a_live = False
        elif marker_d == 'K':
            d_live = False
        elif marker_a == 'M' or marker_d == 'M':
            print("지뢰와 대결하여 player_a의 말과 player_b의 말 둘 다 사망입니다.")
            a_live = False
            d_live = False
        elif int(marker_a)+int(marker_d) < 10:
            if int(marker_a) > int(marker_d):
                print("두 수의 합이 10보다 낮으므로 낮은 숫자인 "+marker_d+" 승리")
                a_live = False
            elif int(marker_a) < int(marker_d):
                print("두 수의 합이 10보다 낮으므로 낮은 숫자인 "+marker_a+" 승리")
                d_live = False
            else:
                print("무승부이므로 말 둘 다 사망입니다.")
                a_live = False
                d_live = False
        elif int(marker_a)+int(marker_d) >9:
            if int(marker_a) > int(marker_d):
                print("두 수의 합이 10보다 크므로 높은 숫자인 "+marker_a+" 승리")
                d_live = False
            elif int(marker_a) < int(marker_d):
                print("두 수의 합이 10보다 크므로 높은 숫자인 "+marker_d+" 승리")
                a_live = False
            else:
                print("무승부이므로 말 둘 다 사망입니다.")
                a_live = False
                d_live = False
        elif ( a_y + d_y == 3 and abs(a_y - d_y) == 1) or ( a_y + d_y == 7 and abs(a_y - d_y) == 1):
            if abs(int(marker_a) - int(marker_d)) < 10:
                if int(marker_a) > int(marker_d):
                    print("*******마이너스 대결입니다.")
                    print("두 수의 차가 10보다 낮으므로 낮은 숫자인 "+marker_d+" 승리")
                    a_live = False
                elif int(marker_a) < int(marker_d):
                    print("*******마이너스 대결입니다.")
                    print("두 수의 차가 10보다 낮으므로 낮은 숫자인 "+marker_a+" 승리")
                    d_live = False
                else:
                    print("*******마이너스 대결입니다.")
                    print("무승부이므로 말 둘 다 사망입니다.")
                    a_live = False
                    d_live = False
            elif abs(int(marker_a) - int(marker_d))>10:
                if int(marker_a) > int(marker_d):
                    print("*******마이너스 대결입니다.")
                    print("두 수의 차가 10보다 크므로 높은 숫자인 "+marker_a+" 승리")
                    d_live = False
                elif int(marker_a) < int(marker_d):
                    print("*******마이너스 대결입니다.")
                    print("두 수의 차가 10보다 크므로 높은 숫자인 "+marker_d+" 승리")
                    a_live = False
                else:
                    print("*******마이너스 대결입니다.")
                    print("무승부이므로 말 둘 다 사망입니다.")
                    a_live = False
                    d_live = False
    
    if not a_live:
        dead(a_x,a_y)
    if not b_live:
        dead(b_x,b_y)
    if not c_live:
        dead(c_x,c_y)
    if not d_live:
        dead(d_x,d_y)

def dead(x,y):
    if tile[x][y][1] == 'K':
        if tile[x][y][0] == 1:
            lose(player_a, 'k_dead')
        else:
            lose(player_b, 'k_dead')
    else:
        if tile[x][y][0] == 1:
            tile[x][y][0]=0
            player_a_dead.append(tile[x][y][1])
            tile[x][y][1]=0
        elif tile [x][y][0] == 2:
            tile[x][y][0]=0
            player_b_dead.append(tile[x][y][1])
            tile[x][y][1]=0 
        else:
            tile [x][y][0] = 0
            tile [x][y][1] = 0

def lose(player, cause):
    global game_end
    if player == 1:
        if cause == 'k_dead':
            print("player_a : 패배 player_b : 승리")
            print("패배 이유 : player_a의 왕이 잡혔습니다.")
            game_end = True
        elif cause == 'other_dead':
            print("player_a : 패배 player_b : 승리")
            print("패배 이유 : player_a의 왕을 제외한 모든 말이 잡혔습니다.")
            game_end = True
        elif cause == 'time_out':
            print("player_a : 패배 player_b : 승리")
            print("패배 이유: 말을 놓을 수 있는 시간(60초)이 다 지났습니다.")
            game_end = True
        elif cause == 'k_forward':
            print("player_a : 패배 player_b : 승리")
            print("player_b의 왕이 player_a의 진영 끝에 도달했습니다.")
            game_end = True
        else:
            print("버그 발생 오류코드:lose_cause_error")
    else:
        if cause == 'k_dead':
            print("player_a : 승리 player_b : 패배")
            print("패배 이유 : player_b의 왕이 잡혔습니다.")
            game_end = True
        elif cause == 'other_dead':
            print("player_a : 승리 player_b : 패배")
            print("패배 이유 : player_b의 왕을 제외한 모든 말이 잡혔습니다.")
            game_end = True
        elif cause == 'time_out':
            print("player_a : 승리 player_b : 패배")
            print("패배 이유: 말을 놓을 수 있는 시간(60초)이 다 지났습니다.")
            game_end = True
        elif cause == 'k_forward':
            print("player_a : 승리 player_b : 패배")
            print("player_a의 왕이 player_b의 진영 끝에 도달했습니다.")
            game_end = True
        else:
            print("버그 발생 오류코드:lose_cause_error")

def player_change(a):
    for i in range (30):
        print(" ")
    if a == 'a':
        print("현재 플레이어 : player_a")
    elif a == 'b':
        print("현재 플레이어 : player_b")
    elif a == 'both':
        print("현재 플레이어 : 둘 다")
    input("플레이어를 바꾼 뒤 enter키를 입력해주십시오...")

game_end = False
#visualize_all()
#player_change('a')
#prepare_tile_a()
#visualize_a()
#input("다음과 같이 배치되었습니다.")
#player_change('b')
#prepare_tile_b()
#visualize_b()
#input("다음과 같이 배치되었습니다.")
#player_change('both')
print(tile)
print("==========================주의 사항==========================")
print("1.패배 조건은 다음과 같습니다.")
print("1-1. 자신의 왕이 잡혔을 경우")
print("1-2. 자신의 왕을 제외한 모든 말이 잡혔을 경우")
print("1-3. 상대의 왕이 자신의 진영 맨 끝쪽에 도달했을 경우")
print("1-4. 60초 이내에 어디로 말을 움직일지 결정하지 못했을 경우(단, 몇초가 지났는지는 중간에 말해주지 않고, 말을 두는 시점이 60초가 넘었는지 아닌지만 판정합니다.")
print("2.제발 하라는 짓만 하십시오.")
#input("==========================게임 시작==========================")
while True:
    player_change('a')
    start_time = ti.time()
    visualize_a()
    move_a()
    lose_check(1)
    if game_end:
        break
    visualize_a()
    input("다음과 같이 움직였습니다.")
    player_change('b')
    start_time = ti.time()
    visualize_b()
    move_b()
    lose_check(2)
    if game_end:
        break
    visualize_b()
    input("다음과 같이 움직였습니다.")

input("프로그램을 종료합니다.")



