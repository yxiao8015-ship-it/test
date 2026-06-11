#!/usr/bin/env python3
"""
井字棋游戏 - Tic Tac Toe Game
经典的两人对战游戏，玩家 vs 电脑
"""

import random


class TicTacToe:
    """井字棋游戏类"""
    
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.human = 'X'
        self.computer = 'O'
    
    def print_board(self):
        """打印棋盘"""
        print("\n")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]}")
        print("---+---+---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]}")
        print("---+---+---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]}")
        print("\n")
    
    def print_positions(self):
        """打印位置编号"""
        print("位置编号 / Positions:")
        print(" 0 | 1 | 2")
        print("---+---+---")
        print(" 3 | 4 | 5")
        print("---+---+---")
        print(" 6 | 7 | 8")
        print()
    
    def is_winner(self, player):
        """检查玩家是否获胜"""
        win_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # 行
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # 列
            [0, 4, 8], [2, 4, 6]              # 对角线
        ]
        for combo in win_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False
    
    def is_board_full(self):
        """检查棋盘是否满了"""
        return ' ' not in self.board
    
    def get_available_moves(self):
        """获取可用的位置"""
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def human_move(self):
        """获取玩家的移动"""
        while True:
            try:
                position = int(input("你的回合 / Your move (0-8): "))
                if position < 0 or position > 8:
                    print("❌ 请输入 0-8 之间的数字。(Please enter a number between 0-8.)")
                    continue
                if self.board[position] != ' ':
                    print("❌ 这个位置已经被占用了！(That position is already taken!)")
                    continue
                self.board[position] = self.human
                return
            except ValueError:
                print("❌ 输入错误！请输入一个数字。(Invalid input! Please enter a number.)")
    
    def computer_move(self):
        """电脑的移动（简单AI）"""
        available = self.get_available_moves()
        
        # 先检查是否能赢
        for move in available:
            self.board[move] = self.computer
            if self.is_winner(self.computer):
                print(f"电脑选择位置 {move} / Computer chooses position {move}")
                return
            self.board[move] = ' '
        
        # 否则检查是否需要防守
        for move in available:
            self.board[move] = self.human
            if self.is_winner(self.human):
                self.board[move] = self.computer
                print(f"电脑选择位置 {move} / Computer chooses position {move}")
                return
            self.board[move] = ' '
        
        # 优先选择中心
        if 4 in available:
            self.board[4] = self.computer
            print(f"电脑选择位置 4 / Computer chooses position 4")
            return
        
        # 否则选择角落
        corners = [0, 2, 6, 8]
        corner_moves = [c for c in corners if c in available]
        if corner_moves:
            move = random.choice(corner_moves)
            self.board[move] = self.computer
            print(f"电脑选择位置 {move} / Computer chooses position {move}")
            return
        
        # 否则随机选择
        move = random.choice(available)
        self.board[move] = self.computer
        print(f"电脑选择位置 {move} / Computer chooses position {move}")
    
    def play(self):
        """玩一局游戏"""
        print("=" * 50)
        print("欢迎来到井字棋游戏！Welcome to Tic Tac Toe!")
        print("=" * 50)
        self.print_positions()
        
        while True:
            self.print_board()
            
            # 玩家回合
            self.human_move()
            self.print_board()
            
            if self.is_winner(self.human):
                print("🎉 你赢了！(You win!)")
                return
            
            if self.is_board_full():
                print("😐 平手！(It's a tie!)")
                return
            
            # 电脑回合
            print("电脑思考中... / Computer is thinking...")
            self.computer_move()
            
            if self.is_winner(self.computer):
                self.print_board()
                print("😢 电脑赢了！(Computer wins!)")
                return
            
            if self.is_board_full():
                self.print_board()
                print("😐 平手！(It's a tie!)")
                return


def main():
    """主函数"""
    while True:
        game = TicTacToe()
        game.play()
        
        play_again = input("\n你想再玩一次吗？/ Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ['yes', 'y', '是']:
            print("\n谢谢游玩！再见！(Thanks for playing! Goodbye!)\n")
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n游戏已中断。再见！(Game interrupted. Goodbye!)")
