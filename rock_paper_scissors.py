#!/usr/bin/env python3
"""
石头剪刀布游戏 - Rock Paper Scissors Game
经典的玩家 vs 电脑游戏
"""

import random


def play_rock_paper_scissors():
    """主游戏函数"""
    print("=" * 50)
    print("欢迎来到石头剪刀布游戏！Welcome to Rock Paper Scissors!")
    print("=" * 50)
    
    player_score = 0
    computer_score = 0
    
    while True:
        print(f"\n当前分数 / Current Score - 你 / You: {player_score}, 电脑 / Computer: {computer_score}")
        print("\n请选择 / Choose your move:")
        print("1. 石头 (Rock)")
        print("2. 剪刀 (Scissors)")
        print("3. 布 (Paper)")
        print("4. 退出 (Quit)")
        
        try:
            choice = input("\n输入选择 (Enter choice 1-4): ").strip()
            
            if choice == "4":
                print("\n" + "=" * 50)
                print(f"最终分数 / Final Score:")
                print(f"你 / You: {player_score}")
                print(f"电脑 / Computer: {computer_score}")
                if player_score > computer_score:
                    print("🎉 你赢了！(You won!)")
                elif player_score < computer_score:
                    print("😢 电脑赢了！(Computer won!)")
                else:
                    print("🤝 打成平手！(It's a tie!)")
                print("=" * 50)
                print("\n谢谢游玩！再见！(Thanks for playing! Goodbye!)\n")
                break
            
            choices = {"1": "石头/Rock", "2": "剪刀/Scissors", "3": "布/Paper"}
            if choice not in choices:
                print("❌ 无效选择！请输入 1-4。(Invalid choice! Please enter 1-4.)")
                continue
            
            player_move = choice
            computer_move = str(random.randint(1, 3))
            
            player_name = choices[player_move]
            computer_name = choices[computer_move]
            
            print(f"\n你选择了: {player_name} / You chose: {player_name}")
            print(f"电脑选择了: {computer_name} / Computer chose: {computer_name}")
            
            # 判断胜负
            result = determine_winner(player_move, computer_move)
            
            if result == "win":
                print("🎉 你赢了！(You win!)")
                player_score += 1
            elif result == "lose":
                print("😢 电脑赢了！(Computer wins!)")
                computer_score += 1
            else:
                print("🤝 平手！(It's a tie!)")
                
        except Exception as e:
            print(f"❌ 出错了！(Error: {e})")


def determine_winner(player, computer):
    """
    判断胜负
    1: 石头, 2: 剪刀, 3: 布
    """
    if player == computer:
        return "tie"
    
    win_conditions = {
        ("1", "2"): "win",   # 石头赢剪刀
        ("2", "3"): "win",   # 剪刀赢布
        ("3", "1"): "win",   # 布赢石头
    }
    
    if (player, computer) in win_conditions:
        return "win"
    else:
        return "lose"


if __name__ == "__main__":
    try:
        play_rock_paper_scissors()
    except KeyboardInterrupt:
        print("\n\n游戏已中断。再见！(Game interrupted. Goodbye!)")
