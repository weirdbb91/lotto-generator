import random

# 번호 선택의 최소값, 최대값 및 선택 숫자 갯수
NUM_MIN, NUM_MAX, NUM_LEN = 1, 45, 6
LOTTO_GAME_LEN = 5 # 플레이할 로또 게임의 수

if NUM_MIN < 1:
    raise ValueError("번호는 양수만 가능합니다.")
if NUM_MIN > NUM_MAX:
    raise ValueError("최소값이 최대값보다 큽니다.")
if NUM_MAX - NUM_MIN + 1 < NUM_LEN:
    raise ValueError("선택 해야할 번호가 선택 가능한 번호보다 많습니다.")


lotto_game_list = []

def get_lotto_nums():
    num_set = []
    
    while len(num_set) < NUM_LEN:
        num = random.randint(NUM_MIN, NUM_MAX)
        if not num in num_set:
            num_set.append(num)
    
    return sorted(num_set)


while len(lotto_game_list) < LOTTO_GAME_LEN:
    lotto_game_list.append(get_lotto_nums())


for lotto_game in lotto_game_list:
    print(lotto_game)
