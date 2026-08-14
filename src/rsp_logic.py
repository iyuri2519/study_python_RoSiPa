class RSP:
    rsp = ["가위", "바위", "보"]

    # 반드시 [0] <= [1] <= [2] <= [0] 순이 되도록 입력해주세요.
    # 기본 : 가위 바위 보
    def __init__(self, rsp_arr:list[str]=rsp):
        self.rsp[0] = rsp_arr[0]
        self.rsp[1] = rsp_arr[1]
        self.rsp[2] = rsp_arr[2]

    # 선택지 배열을 바꿉니다. (기본 : 가위 바위 보)
    def change_choice_arr(self, rsp_arr:list[str]=rsp):
        self.rsp[0] = rsp_arr[0]
        self.rsp[1] = rsp_arr[1]
        self.rsp[2] = rsp_arr[2]

    # 가위바위보 함수를 시행하고, 플레이어가 선택한 index를 반환합니다.
    def get_player_choice(self) -> int:
        while True:
            player = input().strip()
            if player not in self.rsp:
                print(f"{self.rsp[0]}, {self.rsp[1]}, {self.rsp[2]} 중에 내주세요! Ex) {self.rsp[0]}")
            else:
                return self.rsp.index(player)

    # 플레이어 기준으로 승부를 판단합니다.
    # 플레이어 승 : 1, 컴퓨터 승 : 0, 무승부 : -1
    def is_player_win(self, player_idx:int, com_idx:int) -> int:
        if player_idx == com_idx:
            return -1
        elif player_idx == (com_idx+1) % 3:
            return 1
        return 0


class MZP(RSP):
    mzp = ["찌", "묵", "빠"]

    # 선택지 배열을 바꿉니다. (기본 : 찌 묵 빠)
    def change_choice_arr(self, mzp_arr:list[str]=mzp):
        self.rsp[0] = mzp_arr[0]
        self.rsp[1] = mzp_arr[1]
        self.rsp[2] = mzp_arr[2]

    # 묵찌빠의 결과를 결정합니다.
    # pass : 건너뛰기, win : 플레이어 승, lose : 플레이어 패배, change : 교체
    def decide_mzp_result(self, attacker:int, player_state:int) -> str:
        if (attacker + player_state) == 1:   # 공격권이 넘어가는 경우
            return "change"
        elif player_state == -1:     # 같은 걸 낸 경우
            if attacker == 1:
                return "win"
            return "lose"
        return "pass"           # 공격권이 유지되는 경우 

