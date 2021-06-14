#숫자장기
#V0.0 -- 실행 불가 버전입니다.

#모듈 그딴거 없다. 히히 랜덤 나중에 넣어야지
import time as ti
#┌─┬─┬─┬─┬─┬─┬─┬─┬─┐ ******왼쪽 위 부터 1,1 오른쪽위 1,9 왼쪽 아래 6,1 오른쪽 아래 ㅗㅜㅑ
#│ │ │ │ │ │ │ │ │ │ ******왼쪽이 player_a 오른쪽이 player_b
#├─┼─┼─┼─┼─┼─┼─┼─┼─┤ 
#│ │ │ │ │ │ │ │ │ │
#├─┼─┼─┼─┼─┼─┼─┼─┼─┤
#│ │ │ │ │ │ │ │ │ │
#├─┼─┼─┼─┼─┼─┼─┼─┼─┤
#│ │ │ │ │ │ │ │ │ │
#├─┼─┼─┼─┼─┼─┼─┼─┼─┤
#│ │ │ │ │ │ │ │ │ │
#├─┼─┼─┼─┼─┼─┼─┼─┼─┤
#│ │ │ │ │ │ │ │ │ │
#└─┴─┴─┴─┴─┴─┴─┴─┴─┘

#제일 작은 리스트 [0]= 0(NONE)1(player_a)2(player_b) [1]=marker
tile = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]]
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
                print("□",end = '')
        elif i_tile == 53:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print("□",end = '')
            print("│")
            print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")
        elif i_tile % 9 == 0:
            print("├───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print("□",end = '')
        elif i_tile % 9 == 8:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print("□",end = '')
            print("│")
        else:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 2:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print("□",end = '')

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
                print("□",end = '')
        elif i_tile == 53:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print("□",end = '')
            print("│")
            print("└───┴───┴───┴───┴───┴───┴───┴───┴───┘")
        elif i_tile % 9 == 0:
            print("├───┼───┼───┼───┼───┼───┼───┼───┼───┤")
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print("□",end = '')
        elif i_tile % 9 == 8:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print("□",end = '')
            print("│")
        else:
            print("│",end='')
            if not tile[i_tile % 9][i_tile // 9][0] == 1:
                print(spac(tile[i_tile % 9][i_tile // 9][1]),end='')
            else:
                print("□",end = '')

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
        
#막아야 할 거
#빈 공간으로 움직이기 (Done)
#다른 말이 있는 공간으로 움직이기(Done)
#자신의 말을 넘어 가기(전진 시 만 고려하면 됨)(Done)
#지뢰 이동
def move_a():
    while True:
        try:
            before_tile_x,before_tile_y = input("움직일 말의 x값,y값을 공백으로 구분하여 입력하여 주십시오.").split()
        except:
            print("잘못된 입력입니다.")
            continue
        move_size = 1
        dire = input("움직일 방향을 설정해 주십시오. [1]상단[2]우측 상단[3]오른쪽(최대 2칸)[4]우측 하단[5]하단")
        if dire == 3:
            move_size = input("움직일 칸 수를 설정해 주십시오. [1]1칸[2]2칸")
        else:
            pass
        
        if dire == 1:
            after_tile_x = before_tile_x
            after_tile_y = before_tile_y + 1
        elif dire == 2:
            after_tile_x = before_tile_x + 1
            after_tile_y = before_tile_y + 1
        elif dire == 3:
            after_tile_y= before_tile_y
            if move_size == 1:
                after_tile_x = before_tile_x + 1
            else:
                after_tile_x = before_tile_x + 2
        elif dire == 4:
            after_tile_x = before_tile_x + 1
            after_tile_y = before_tile_y - 1
        else:
            after_tile_x = before_tile_x 
            after_tile_y = before_tile_y - 1

        if after_tile_x > 8 or after_tile_x < 0 or after_tile_y > 5 or after_tile_y < 0:
            print("빈 공간으로는 이동이 불가능합니다. 다시 움직여 주십시오.")
            continue
        elif not tile[after_tile_x][after_tile_y][1] == 0:
            print("이미 말이 있는 칸입니다. 다시 움직여 주십시오.")
            continue
        elif tile[after_tile_x][after_tile_y - 1][0] == 1:
            print("자신의 말은 뛰어 넘을 수 없습니다. 다시 움직여 주십시오.")
            continue
        elif tile[before_tile_x][before_tile_y][1] == 'M':
            print("지뢰는 움직일 수 없습니다.다시 움직여 주십시오.")
            continue
        else:
            pass

        tile[after_tile_x][after_tile_y][1] = tile[before_tile_x][before_tile_y][1]
        tile[after_tile_x][after_tile_y][0] = tile[before_tile_x][before_tile_y][0]
        tile[before_tile_x][before_tile_y][0] = 0
        tile[before_tile_x][before_tile_y][1] = 0
        
def move_b():
    while True:
        try:
            before_tile_x,before_tile_y = input("움직일 말의 x값,y값을 공백으로 구분하여 입력하여 주십시오.").split()
        except:
            print("잘못된 입력입니다.")
            continue
        move_size = 1
        dire = input("움직일 방향을 설정해 주십시오. [1]상단[2]좌측 상단[3]왼쪽(최대 2칸)[4]좌측 하단[5]하단")
        if dire == 3:
            move_size = input("움직일 칸 수를 설정해 주십시오. [1]1칸[2]2칸")
        else:
            pass
        
        if dire == 1:
            after_tile_x = before_tile_x
            after_tile_y = before_tile_y + 1
        elif dire == 2:
            after_tile_x = before_tile_x - 1
            after_tile_y = before_tile_y + 1
        elif dire == 3:
            after_tile_y = before_tile_y
            if move_size == 1:
                after_tile_x = before_tile_x - 1
            else:
                after_tile_x = before_tile_x - 2
        elif dire == 4:
            after_tile_x = before_tile_x - 1
            after_tile_y = before_tile_y - 1
        else:
            after_tile_x = before_tile_x 
            after_tile_y = before_tile_y - 1

        if after_tile_x > 8 or after_tile_x < 0 or after_tile_y > 5 or after_tile_y < 0:
            print("빈 공간으로는 이동이 불가능합니다. 다시 움직여 주십시오.")
            continue
        elif not tile[after_tile_x][after_tile_y][1] == 0:
            print("이미 말이 있는 칸입니다. 다시 움직여 주십시오.")
            continue
        elif tile[after_tile_x][after_tile_y + 1][0] == 2:
            print("자신의 말은 뛰어 넘을 수 없습니다. 다시 움직여 주십시오.")
            continue
        elif tile[before_tile_x][before_tile_y][1] == 'M':
            print("지뢰는 움직일 수 없습니다.다시 움직여 주십시오.")
            continue
        else:
            pass

        tile[after_tile_x][after_tile_y][1] = tile[before_tile_x][before_tile_y][1]
        tile[after_tile_x][after_tile_y][0] = tile[before_tile_x][before_tile_y][0]
        tile[before_tile_x][before_tile_y][0] = 0
        tile[before_tile_x][before_tile_y][1] = 0

#x에 after_tile_x,y에 after_tile_y 넣어서 활용
def meet_check(x,y):
    team = tile[x][y][0]
    x_plus_battle = '0'
    x_minus_battle = '0'
    y_plus_battle = '0'
    y_minus_battle = '0'
    if tile[x + 1][y][0] != team:
        x_plus_battle = '1'
    elif tile[x - 1][y][0] != team:
        x_minus_battle = '1'
    elif tile[x][y + 1][0] != team:
        y_plus_battle = '1'
    elif tile[x][y - 1][0] != team:
        y_minus_battle = '1'
    else:
        pass

    tot_battle= x_plus_battle + x_minus_battle + y_plus_battle + y_minus_battle
    battle_count = tot_battle.count('1')

def battle(a_x,a_y,b_x,b_y):
    if tile[a_x][a_y][1] == 'K':
        dead(a_x,a_y)
    elif tile[b_x][b_y][1] == 'K':
        dead(b_x,b_y)
    elif tile[a_x][a_y][1] == 'M' or tile[b_x][b_y][1] == 'M':
        dead(a_x,a_y)
        dead(b_x,b_y)
    elif int(tile[a_x][a_y][1])+int(tile[b_x][b_y][1]) < 10:
        if int(tile[a_x][a_y][1]) > int(tile[b_x][b_y][1]):
            dead(a_x,a_y)
        elif int(tile[a_x][a_y][1]) < int(tile[b_x][b_y][1]):
            dead(b_x,b_y)
        else:
            dead(a_x,a_y)
            dead(b_x,b_y)
    elif int(tile[a_x][a_y][1])+int(tile[b_x][b_y][1]) >9:
        if int(tile[a_x][a_y][1]) > int(tile[b_x][b_y][1]):
            dead(b_x,b_y)
        elif int(tile[a_x][a_y][1]) < int(tile[b_x][b_y][1]):
            dead(a_x,a_y)
        else:
            dead(a_x,a_y)
            dead(b_x,b_y)
    elif ( a_y + b_y == 3 and abs(a_y - b_y) == 1) or ( a_y + b_y == 7 and abs(a_y - b_y) == 1):
        if abs(int(tile[a_x][a_y][1]) - int(tile[b_x][b_y][1])) < 10:
            if int(tile[a_x][a_y][1]) > int(tile[b_x][b_y][1]):
                dead(a_x,a_y)
            elif int(tile[a_x][a_y][1]) < int(tile[b_x][b_y][1]):
                dead(b_x,b_y)
            else:
                dead(a_x,a_y)
                dead(b_x,b_y)
        elif abs(int(tile[a_x][a_y][1]) - int(tile[b_x][b_y][1]))>10:
            if int(tile[a_x][a_y][1]) > int(tile[b_x][b_y][1]):
                dead(b_x,b_y)
            elif int(tile[a_x][a_y][1]) < int(tile[b_x][b_y][1]):
                dead(a_x,a_y)
            else:
                dead(a_x,a_y)
                dead(b_x,b_y)

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
        else:
            tile[x][y][0]=0
            player_b_dead.append(tile[x][y][1])
            tile[x][y][1]=0 

def lose(player, cause):
    if player == 1:
        if cause == 'k_dead':
            print("player_a : 패배 player_b : 승리")
            print("pla")
        elif cause == 'other_dead':
            print("")
        elif cause == 'time_out':
            print("")
        elif cause == 'k_forward':
            print("")
        else:
            print("버그")
    else:
        if cause == 'k_dead':
            print("뭐 대충 적겄지")
        elif cause == 'other_dead':
            print("")
        elif cause == 'time_out':
            print("")
        elif cause == 'k_forward':
            print("")
        else:
            print("버그")
print(tile)
visualize_all()
prepare_tile_a()
visualize_all()
prepare_tile_b()
visualize_all()


