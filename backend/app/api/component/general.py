class General:
    def __init__(self, player_hand, com_hand, player_protect, com_protect, is_player):
        self.player_hand = player_hand
        self.com_hand = com_hand
        self.player_protect = player_protect
        self.com_protect = com_protect
        self.is_player = is_player
        self.messages = []

    def first_process(self):
        if self.is_player:
            self.messages.append("プレイヤーが将軍(6)をプレイしました。") 
        else:
            self.messages.append("コンピューターが将軍(6)をプレイしました。")
        self.messages.append("お互いの手札を交換します。")
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
        value1 = self.player_hand.pop()
        value2 = self.com_hand.pop()
        self.player_hand.append(value2)
        self.com_hand.append(value1)
        self.messages.append("手札を交換しました。")
        return self.messages