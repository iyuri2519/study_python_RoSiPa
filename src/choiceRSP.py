import random as rd

# 3판 2선승제 게임에서 종료할 상황인지 판단합니다.
# True : 계속, False : 종료
def is_game_continue(player_a:int, player_b:int) -> bool:
    if (player_a + player_b) < 3 and player_a < 2 and player_b < 2:
        return True
    return False

# 길이 2의 문자열리스트를 받아 arr의 index를 배열로 출력합니다.
# 시행할 수 없다면 안내 메시지를 출력하고 -1을 반환합니다.
def TwoRSP_idx_find(arr:list, val_li:list[str]):
    s1, s2 = val_li[0], val_li[-1]
    if len(val_li) != 2:
        print("두 단어를 입력해주세요! Ex) 가위 바위")
    elif s1 == s2:
        print("다른 걸 내주세요! Ex) 가위 바위")
    elif s1 not in arr or s2 not in arr:
        print("가위, 바위, 보 중에 내주세요! Ex) 가위 바위")
    else:
        return [arr.index(s1), arr.index(s2)]
    return -1

# 길이 2의 배열에서 index()를 시행합니다.
# 시행할 수 없다면 안내 메시지를 출력하고 -1을 반환합니다.
def ChoiceRSP_idx_find(arr:list, choice_arr:list, value:str) -> int:
    if value not in choice_arr:
        print(f"{choice_arr[0]}, {choice_arr[1]} 중에 내주세요! Ex) {choice_arr[0]}")
        return -1
    return arr.index(value)

# 플레이어 기준으로 승부를 판단합니다.
# 플레이어 승 : 1, 상대 승 : -1, 무승부 : 0
def is_player_win(player_idx:int, other_idx:int) -> int:
    if player_idx == other_idx:
        return 0
    elif player_idx == (other_idx+1) % 3:
        return 1
    return -1               # player_idx < 0 인 경우도 포함


RSP = ["가위", "바위", "보"]
print("하나 빼기 게임을 진행합니다. 3판 2승제 입니다.")
print("무승부는 승부에 포함 안합니다.")

player_win = 0
com_win = 0

while is_game_continue(player_win, com_win):
    print("\n가위 바위 보!")
    player = input("플레이어 : ").split()
    player_idx = TwoRSP_idx_find(RSP, player)
    if type(player_idx) == int:
        continue

    com_idx = rd.sample([0, 1, 2], 2)     # SiRoPa의 index를 랜덤으로 고름
    print(f"컴퓨터 : {RSP[com_idx[0]]} {RSP[com_idx[1]]}")

    print("하나 빼기!")
    while True:
        player_choice = input("플레이어 선택 : ")
        player_choice_idx = ChoiceRSP_idx_find(RSP, player, player_choice)
        if player_choice_idx == -1:
            continue
        break
    com_choice_idx = rd.choice(com_idx)     # com_idx에서 하나 고름
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