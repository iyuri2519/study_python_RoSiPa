import random as rd

# 가위바위보 함수를 시행하고, 플레이어가 선택한 index를 반환합니다.
def run_rsp(RSP:list) -> int:
    while True:
        player = input().strip()
        if player not in RSP:
            print(f"{RSP[0]}, {RSP[1]}, {RSP[2]} 중에 내주세요! Ex) {RSP[0]}")
        else:
            return RSP.index(player)

# 플레이어 기준으로 승부를 판단합니다.
# 플레이어 승 : 1, 컴퓨터 승 : 0, 무승부 : -1
def is_player_win(player_idx:int, com_idx:int) -> int:
    if player_idx == com_idx:
        return -1
    elif player_idx == (com_idx+1) % 3:
        return 1
    return 0

# 묵찌빠의 결과를 결정합니다.
# pass : 건너뛰기, win : 플레이어 승, lose : 플레이어 패배, change : 교체
def decide_mzp_result(attacker:int, win_num:int) -> str:
    if (attacker + win_num) == 1:   # 공격권이 넘어가는 경우
        return "change"
    elif win_num == -1:     # 같은 걸 낸 경우
        if attacker == 1:
            return "win"
        return "lose"
    return "pass"           # 공격권이 유지되는 경우 


RSP = ["가위", "바위", "보"]
MZP = ["찌", "묵", "빠"]
print("묵찌빠 게임을 진행합니다. 3판 2승제 입니다.")
print("무승부는 승부에 포함 안합니다.\n")

win_num = 0             # 플레이어 승 : 1, 컴퓨터 승 : 0, 무승부 : -1
attacker = 0            # 플레이어 : 1, 컴퓨터 : 0

while True:
    print("가위 바위 보!\n플레이어 : ", end="")
    player_idx = run_rsp(RSP)       # 가위바위보 시행
    com_idx = rd.randint(0,2)       # SiRoPa의 index를 랜덤으로 두개 고름
    print(f"컴퓨터 : {RSP[com_idx]}!")

    win_num = is_player_win(player_idx, com_idx)
    if win_num == -1:
        print("\n무승부! ", end="")
        continue
    attacker = win_num
    break

while True:
    if attacker:
        print(f"플레이어 : ", f"{MZP[player_idx]}"*2, "... ", end="")
        player_idx = run_rsp(MZP)
        com_idx = rd.randint(0,2)
        print(f"컴퓨터 : {MZP[com_idx]}!")
    else:
        player_idx = run_rsp(MZP)
        print(f"컴퓨터 : ", f"{MZP[com_idx]}"*2, "... ", end="")
        com_idx = rd.randint(0,2)
        print(f"{MZP[com_idx]}!")
        print(f"플레이어 : {MZP[player_idx]}")

    win_num = is_player_win(player_idx, com_idx)
    mzp_result = decide_mzp_result(attacker, win_num)
    if mzp_result == "pass":
        continue
    elif mzp_result == "change":
        attacker = int(not attacker)
        continue
    elif mzp_result == "win":
        print("\n플레이어 승리...")
    elif mzp_result == "lose":
        print("\n허졉")
    break