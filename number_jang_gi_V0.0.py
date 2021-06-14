#숫자장기
#V0.0 -- 실행 불가 버전입니다.
import time as ti
# ******왼쪽 위 부터 1,1 오른쪽위 1,9 왼쪽 아래 6,1 오른쪽 아래 ㅗㅜㅑ
# ******왼쪽이 player_a 오른쪽이 player_b

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
            break

    tile[after_tile_x][after_tile_y][1] = tile[before_tile_x][before_tile_y][1]
    tile[after_tile_x][after_tile_y][0] = tile[before_tile_x][before_tile_y][0]
    tile[before_tile_x][before_tile_y][0] = 0
    tile[before_tile_x][before_tile_y][1] = 0

    if tile[after_tile_x][after_tile_y][1] == 'K' and tile[after_tile_x][after_tile_y][0] == 1 and after_tile_x == 9:
        lose(2,k_forward)

    meet_check(after_tile_x, after_tile_y)
        
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
            break

    tile[after_tile_x][after_tile_y][1] = tile[before_tile_x][before_tile_y][1]
    tile[after_tile_x][after_tile_y][0] = tile[before_tile_x][before_tile_y][0]
    tile[before_tile_x][before_tile_y][0] = 0
    tile[before_tile_x][before_tile_y][1] = 0

    if tile[after_tile_x][after_tile_y][1] == 'K' and tile[after_tile_x][after_tile_y][0] == 2 and after_tile_x == 1:
        lose(1,k_forward)

    meet_check(after_tile_x, after_tile_y)
        

#start_time은 턴 시작과 동시에 카운트
#lose_check는 턴 종료에 카운트
def lose_check(player):
    end_time = ti.time()
    tot_time = end_time - start_time
    if tot_time > 60 :
        lose(player, time_out)
    elif player_a_dead == ['1','2','3','4','5','6','7','8','9','10','M','M','M']:
        lose(1,other_dead)
    elif player_b_dead == ['1','2','3','4','5','6','7','8','9','10','M','M','M']:
        lose(2,other_dead)
#x에 after_tile_x,y에 after_tile_y 넣어서 활용
def meet_check(x,y):
    team = tile[x][y][0]
    battle = [0,0,0,0]#x+, x-, y+, y-
    if tile[x + 1][y][0] != team:
        battle[0] = 1
    elif tile[x - 1][y][0] != team:
        battle[1] = 1
    elif tile[x][y + 1][0] != team:
        battle[2] = 1
    elif tile[x][y - 1][0] != team:
        battle[3] = 1
    else:
        pass

    b_count= battle.count(1)
    if b_count == 0:
        pass
    else:
        for i in range(b_count):
            if battle[0] == 1:
                battle(x,y,x+1,y)
            elif battle[1] == 1:
                    battle(x,y,x-1,y)
            elif battle[2] == 1:
                battle(x,y,x,y+1)
            elif battle[3] == 1:
                battle(x,y,x,y-1)
            else:
                pass
    
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
            print("패배 이유 : player_a의 왕이 잡혔습니다.")
        elif cause == 'other_dead':
            print("player_a : 패배 player_b : 승리")
            print("패배 이유 : player_a의 왕을 제외한 모든 말이 잡혔습니다.")
        elif cause == 'time_out':
            print("player_a : 패배 player_b : 승리")
            print("패배 이유: 말을 놓을 수 있는 시간(60초)이 다 지났습니다.")
        elif cause == 'k_forward':
            print("player_a : 패배 player_b : 승리")
            print("player_b의 왕이 player_a의 진영 끝에 도달했습니다.")
        else:
            print("버그 발생 오류코드:lose_cause_error")
    else:
        if cause == 'k_dead':
            print("player_a : 승리 player_b : 패배")
            print("패배 이유 : player_b의 왕이 잡혔습니다.")
        elif cause == 'other_dead':
            print("player_a : 승리 player_b : 패배")
            print("패배 이유 : player_b의 왕을 제외한 모든 말이 잡혔습니다.")
        elif cause == 'time_out':
            print("player_a : 승리 player_b : 패배")
            print("패배 이유: 말을 놓을 수 있는 시간(60초)이 다 지났습니다.")
        elif cause == 'k_forward':
            print("player_a : 승리 player_b : 패배")
            print("player_a의 왕이 player_b의 진영 끝에 도달했습니다.")
        else:
            print("버그 발생 오류코드:lose_cause_error")

def player_change():
    for i in range (30):
        print(" ")
    input("플레이어를 바꾼 뒤 enter키를 입력해주십시오...")





visualize_all()
prepare_tile_a()
visualize_all()
prepare_tile_b()
visualize_all()


