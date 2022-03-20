class Setting():
    NUM_MIN: int = 1                    # 선택 가능한 최소 번호
    NUM_MAX: int = 45                   # 선택 가능한 최대 번호
    NUM_LEN: int = 6                    # 한게임당 선택할 번호 개수
    LOTTO_GAME_LEN: int = 5             # 플레이할 로또 게임의 수
    
    STRAIGHT_NUMS_ALLOWED: bool = False # 연속되는 번호 선택 가능 여부
    STRAIGHT_NUMS_LIMIT: int = 2        # 선택 가능한 연속 번호 갯수

    NUM_RANGE = NUM_MAX - NUM_MIN + 1   # 선택 가능한 번호 범위
    
    
    def __init__(self):
        if self.NUM_MIN < 1:
            raise ValueError("번호는 양수만 가능합니다.")
        if self.NUM_MIN > self.NUM_MAX:
            raise ValueError("최소값이 최대값보다 큽니다.")
        if self.NUM_RANGE < self.NUM_LEN:
            raise ValueError("선택 해야할 번호가 선택 가능한 번호보다 많습니다.")
        
        if not self.STRAIGHT_NUMS_ALLOWED:
            if self.STRAIGHT_NUMS_LIMIT < 1:
                raise ValueError("연속수 제한값이 올바르지 않습니다.")
            if self.NUM_RANGE - self.NUM_LEN < self.NUM_LEN / self.STRAIGHT_NUMS_LIMIT - 1:
                raise ValueError("연속수 제한값 적용시 선택 가능한 번호가 부족합니다.")

setting = Setting()
