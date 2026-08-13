import random as rd

# 가위바위보 함수를 시행하고, 플레이어가 선택한 두개의 index를 반환합니다.
def run_rsp(arr:list) -> list[int]:
    while True:
        player = input("플레이어 : ").strip().split()
        if len(player) != 2:
            print("두 단어를 입력해주세요!")
            continue

        s1, s2 = player[0], player[-1]
        if s1 == s2:
            print("다른 걸 내주세요!", end="")
        elif s1 not in arr or s2 not in arr:
            print("가위, 바위, 보 중에 내주세요!", end="")
        else:
            return [arr.index(s1), arr.index(s2)]
        print(f" Ex) {arr[0]} {arr[1]}")

# 하나빼기 함수를 시행하고, 플레이어가 선택한 것의 index를 반환합니다.
def choice_rsp(arr:list, player_indices:list) -> int:
    player_arr = [arr[player_indices[0]], arr[player_indices[1]]]
    while True:
        player_choice = input("플레이어 선택 : ").strip()
        if player_choice not in player_arr:
            print(f"{player_arr[0]}, {player_arr[1]} 중에 내주세요! Ex) {player_arr[0]}")
            continue
        return arr.index(player_choice)

# 플레이어 기준으로 승부를 판단합니다.
# 플레이어 승 : 1, 상대 승 : -1, 무승부 : 0
def is_player_win(player_idx:int, other_idx:int) -> int:
    if player_idx == other_idx:
        return 0
    elif player_idx == (other_idx+1) % 3:
        return 1
    return -1


RSP = ["가위", "바위", "보"]
print("하나 빼기 게임을 진행합니다. 3판 2승제 입니다.")
print("무승부는 승부에 포함 안합니다.")

player_win = 0
com_win = 0

while player_win < 2 and com_win < 2:
    print("\n가위 바위 보!")
    player_indices = run_rsp(RSP)            # 가위바위보 (두개내기) 를 시행
    com_indices = rd.sample([0, 1, 2], 2)   # SiRoPa의 index를 랜덤으로 두개 고름
    print(f"컴퓨터 : {RSP[com_indices[0]]} {RSP[com_indices[1]]}")

    print("하나 빼기!")
    player_choice_idx = choice_rsp(RSP, player_indices)  # 하나빼기를 시행
    com_choice_idx = rd.choice(com_indices)         # com_idx에서 하나 고름
    print(f"컴퓨터 선택 : {RSP[com_choice_idx]}")
    
    win_num = is_player_win(player_choice_idx, com_choice_idx)
    if win_num == 1:
        print("플레이어 승리...")
        player_win += 1 
    elif win_num == -1:
        print("컴퓨터 승리!")
        com_win += 1
    else:
        print("무승부! 다시!")


print(f"\n최종 결과는 플레이어 {player_win}승 : 컴퓨터 {com_win}승")
if player_win == 2:
    print("나의 패배다...")
else:
    print("인간 허졉")
