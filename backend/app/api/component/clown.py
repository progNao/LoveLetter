class Clown:
    def __init__(self, player_hand, com_hand, player_protect, com_protect, is_player):
        self.player_hand = player_hand
        self.com_hand = com_hand
        self.player_protect = player_protect
        self.com_protect = com_protect
        self.is_player = is_player
        self.messages = []
    
    def first_process(self):
        if self.is_player:
            self.messages.append("プレイヤーが道化(2)をプレイしました。")
            self.messages.append("コンピューターの手札を確認します。")
        else:
            self.messages.append("コンピューターが道化(2)をプレイしました。")
            self.messages.append("コンピューターがプレイヤーの手札を確認します。")
        return self.messages
    
    def main_process(self):
        if self.is_player:
            if self.com_protect:
                self.messages.append("コンピューターは僧侶の効果中で対象にできません。")
                return self.messages
            else:
                self.messages.append(f"コンピューターの手札は{self.com_hand}です。")
                return self.messages
        else:
            if self.player_protect:
                self.messages.append("プレイヤーは僧侶の効果中で対象にされません。")
                return self.messages
            else:
                self.messages.append("コンピューターがプレイヤーの手札を確認しました。")
                return self.messages