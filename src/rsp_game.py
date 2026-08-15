import random as rd
import rsp_logic

RSP = ["가위", "바위", "보"]
MZP = ["찌", "묵", "빠"]
win_num = 0             # 플레이어 승 : 1, 컴퓨터 승 : 0, 무승부 : -1
attacker = 0            # 플레이어 : 1, 컴퓨터 : 0

game = rsp_logic.MZP(RSP)
print("묵찌빠 게임을 진행합니다.")
print("무승부는 승부에 포함 안합니다.\n")

while True:
    print("가위 바위 보!\n플레이어 : ", end="")
    player_idx = game.get_player_choice()       # 가위바위보 시행
    com_idx = rd.randint(0,2)       # SiRoPa의 index를 랜덤으로 두개 고름
    print(f"컴퓨터 : {RSP[com_idx]}!")

    win_num = game.is_player_win(player_idx, com_idx)
    if win_num == -1:
        print("\n무승부! ", end="")
        continue
    attacker = win_num
    break

game.change_choice_arr(MZP)     # 가위바위보 가 아닌 묵찌빠 로 입력하도록 바꿈
while True:
    if attacker:
        print(f"플레이어 공격 : {MZP[player_idx]*2}... ", end="")
        player_idx = game.get_player_choice()
        com_idx = rd.randint(0,2)
        print(f"컴퓨터 : {MZP[com_idx]}!")
    else:
        print(f"플레이어 수비 : ", end="")
        player_idx = game.get_player_choice()
        print(f"컴퓨터 : {MZP[com_idx]*2}... ", end="")
        com_idx = rd.randint(0,2)
        print(f"{MZP[com_idx]}!")
    
    win_num = game.is_player_win(player_idx, com_idx)
    mzp_result = game.decide_mzp_result(attacker, win_num)
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