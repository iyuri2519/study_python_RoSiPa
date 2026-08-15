class RSP:
    # 반드시 [0] <= [1] <= [2] <= [0] 순이 되도록 입력해주세요.
    # rsp_arr 에는 문자열 리스트가 들어올 수 있으며, 입력하지 않으면 None으로 처리됩니다.
    def __init__(self, rsp_arr:list[str] | None = None):
        self.change_choice_arr(rsp_arr)

    # 선택지 배열을 바꿉니다. None이면 default_choices를 사용합니다.
    def change_choice_arr(self, rsp_arr:list[str] | None = None):
        if rsp_arr is not None:
            self.rsp = rsp_arr.copy()
        else:
            self.rsp = self.default_choices

    # 가위바위보 함수를 시행하고, 플레이어가 선택한 index를 반환합니다.
    def get_player_choice(self) -> int:
        while True:
            player = input().strip()
            if player in self.rsp:
                return self.rsp.index(player)
            print(f"{self.rsp[0]}, {self.rsp[1]}, {self.rsp[2]} 중에 내주세요! Ex) {self.rsp[0]}")

    # 플레이어 기준으로 승부를 판단합니다.
    # 플레이어 승 : 1, 컴퓨터 승 : 0, 무승부 : -1
    @staticmethod
    def is_player_win(player_idx:int, com_idx:int) -> int:
        if player_idx == com_idx:
            return -1
        elif player_idx == (com_idx+1) % 3:
            return 1
        return 0


class MZP(RSP):
    default_choices = ["찌", "묵", "빠"]

    # 묵찌빠의 결과를 결정합니다.
    # pass : 건너뛰기, win : 플레이어 승, lose : 플레이어 패배, change : 교체
    @staticmethod
    def decide_mzp_result(attacker:int, player_state:int) -> str:
        if (attacker + player_state) == 1:   # 공격권이 넘어가는 경우
            return "change"
        elif player_state == -1:     # 같은 걸 낸 경우
            if attacker == 1:
                return "win"
            return "lose"
        return "pass"           # 공격권이 유지되는 경우 

