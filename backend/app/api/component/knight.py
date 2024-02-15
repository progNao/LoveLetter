from api.result import Result

class Knight:
    def __init__(self, player_hand, com_hand, player_protect, com_protect, is_player):
        self.player_hand = player_hand
        self.com_hand = com_hand
        self.player_protect = player_protect
        self.com_protect = com_protect
        self.is_player = is_player
        self.messages = []
    
    def first_process(self):
        if self.is_player:
            self.messages.append("プレイヤーが騎士(3)をプレイしました。") 
        else:
            self.messages.append("コンピューターが騎士(3)をプレイしました。")
        self.messages.append("手札の数字を比較し、小さい方を脱落させます。")
        return self.messages
    
    def main_process(self):
        if self.is_player:
            if self.com_protect:
                self.messages.append("コンピューターは僧侶の効果中で対象にできません。")
                return self.messages
            else:
                self.calc()
                return self.messages
        else:
            if self.player_protect:
                self.messages.append("プレイヤーは僧侶の効果中で対象にされません。")
                return self.messages
            else:
                self.calc()
                return self.messages
    
    def calc(self):
        self.messages.append(f"プレイヤーの手札：{self.player_hand}")
        self.messages.append(f"コンピューターの手札：{self.com_hand}")
        if self.player_hand[0] > self.com_hand[0]:
            return self.messages.append(Result.WIN)
        elif self.player_hand[0] < self.com_hand[0]:
            return self.messages.append(Result.LOOSE)
        else:
            return self.messages.append(Result.DRAW)