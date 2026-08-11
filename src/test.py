import random as rd

# 5판 3선승제 게임에서 종료할 상황인지 판단합니다.
# True : 계속, False : 종료
def is_game_continue(player_a:int, player_b:int) -> bool:
    if (player_a + player_b) < 5 and player_a < 3 and player_b < 3:
        return True
    return False

# index() 함수를 시행합니다.
# 시행할 수 없다면 -1을 반환합니다.
def no_error_find(arr:list, value:str) -> int:
    if value not in arr:
        return -1
    return arr.index(value)

# 플레이어 기준으로 승부를 판단합니다.
# 플레이어 승 : 1, 상대 승 : -1, 무승부 : 0
def decide_win(player_idx:int, other_idx:int) -> int:
    if player_idx == other_idx:
        return 0
    elif player_idx == (other_idx+1) % 3:
        return 1
    return -1               # player_idx < 0 인 경우도 포함


SiRoPa = ["가위", "바위", "보"]
print("먼저 내세요. 5전 3승제 입니다.")
print("무승부는 승부에 포함 안합니다.")
print("이상한 거 내면 제가 이긴거로 칩니다.")

player_win = 0
com_win = 0

while is_game_continue(player_win, com_win) :
    ans = input()
    ans_idx = no_error_find(SiRoPa, ans)
    com_idx = rd.randint(0,2)     # SiRoPa의 index를 랜덤으로 고름

    win_num = decide_win(ans_idx, com_idx)
    if win_num == 1:
        print("플레이어 승리...")
        player_win += 1
    elif win_num == -1:
        print("컴퓨터 승리!")
        com_win += 1
    else:
        print("무승부! 다시!")


print(f"\n최종 결과는 플레이어 {player_win}승 : 컴퓨터 {com_win}승")
if player_win == 3:
    print("나의 패배다...")
else:
    print("인간 허졉")