import random

# 번호 선택의 최소값, 최대값 및 선택 숫자 갯수
NUM_MIN, NUM_MAX, NUM_LEN = 1, 45, 6
NUM_RANGE = NUM_MAX - NUM_MIN + 1
LOTTO_GAME_LEN = 1          # 플레이할 로또 게임의 수
STRAIGHT_NUMS_LIMIT = 2     # 한번에 연속되는 번호 갯수 제한

if NUM_MIN < 1:
    raise ValueError("번호는 양수만 가능합니다.")
if NUM_MIN > NUM_MAX:
    raise ValueError("최소값이 최대값보다 큽니다.")
if NUM_RANGE < NUM_LEN:
    raise ValueError("선택 해야할 번호가 선택 가능한 번호보다 많습니다.")
if STRAIGHT_NUMS_LIMIT < 1:
    raise ValueError("연속수 제한값이 올바르지 않습니다.")
if NUM_RANGE - NUM_LEN < NUM_LEN / STRAIGHT_NUMS_LIMIT - 1:
    raise ValueError("연속수 제한값 적용시 선택 가능한 번호가 부족합니다.")


lotto_game_list = []

def get_lotto_nums():
    num_set = []
    
    while len(num_set) < NUM_LEN:
        num = random.randint(NUM_MIN, NUM_MAX)
        if not num in num_set:
            num_set.append(num)
    
    return sorted(num_set)


def is_valid_nums(num_set):
    count = 0
    for i in range(len(num_set) - 1):
        if num_set[i] + 1 == num_set[i + 1]:
            count += 1
        else:
            count = 0
        if count >= STRAIGHT_NUMS_LIMIT:
            return False
    return True


while len(lotto_game_list) < LOTTO_GAME_LEN:
    lotto_game = get_lotto_nums()
    
    if is_valid_nums(lotto_game):
        lotto_game_list.append(lotto_game)


for lotto_game in lotto_game_list:
    print(lotto_game)
