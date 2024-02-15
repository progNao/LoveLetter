class Monk:
    def __init__(self, player_hand, com_hand, player_protect, com_protect, is_player):
        self.player_hand = player_hand
        self.com_hand = com_hand
        self.player_protect = player_protect
        self.com_protect = com_protect
        self.is_player = is_player
        self.messages = []
    
    def first_process(self):
        if self.is_player:
            self.messages.append("プレイヤーが僧侶(4)をプレイしました。")
        else:
            self.messages.append("コンピューターが僧侶(4)をプレイしました。")
        self.messages.append("次の手番まで、効果を無効にします。")
        return self.messages
    
    def main_process(self):
        if self.is_player:
            self.player_protect = True
            return self.player_protect
        else:
            self.com_protect = True
            return self.com_protect