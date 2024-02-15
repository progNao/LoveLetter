class Minister:
    def __init__(self, player_hand, com_hand, player_protect, com_protect, is_player):
        self.player_hand = player_hand
        self.com_hand = com_hand
        self.player_protect = player_protect
        self.com_protect = com_protect
        self.is_player = is_player
        self.messages = []
    
    def first_process(self):
        if self.is_player:
            self.messages.append("プレイヤーが大臣(7)をプレイしました。")
        else:
            self.messages.append("コンピューターが大臣(7)をプレイしました。")
        return self.messages
    
    def main_process(self):
        self.messages.append("大臣(7)はプレイしても何も起きません。")
        return self.messages