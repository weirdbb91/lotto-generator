import random

from config import setting


lotto_game_list = []

def get_lotto_nums():
    nums = list(range(setting.NUM_MIN, setting.NUM_MAX + 1))
    num_set = []
    while len(num_set) < setting.NUM_LEN:
        num_idx = random.randint(0, len(nums) - 1)
        num_set.append(nums.pop(num_idx))
    return sorted(num_set)


def has_straight_nums(num_set):
    count = 0
    for i in range(len(num_set) - 1):
        if num_set[i] + 1 == num_set[i + 1]:
            count += 1
        else:
            count = 0
        if count >= setting.STRAIGHT_NUMS_LIMIT:
            return True
    return False


def is_valid_nums(num_set):
    return setting.STRAIGHT_NUMS_ALLOWED or not has_straight_nums(num_set)


while len(lotto_game_list) < setting.LOTTO_GAME_LEN:
    lotto_game = get_lotto_nums()
    
    if is_valid_nums(lotto_game):
        lotto_game_list.append(lotto_game)


for lotto_game in lotto_game_list:
    print(lotto_game)
