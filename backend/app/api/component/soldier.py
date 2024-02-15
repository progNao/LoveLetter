from api.result import Result

class Soldier:
    def __init__(self, player_hand, com_hand, player_protect, com_protect, is_player):
        self.player_hand = player_hand
        self.com_hand = com_hand
        self.player_protect = player_protect
        self.com_protect = com_protect
        self.is_player = is_player
        self.messages = []
    
    def first_process(self):
        if self.is_player:
            self.messages.append("プレイヤーが兵士(1)をプレイしました。")
            self.messages.append("兵士(1)以外のカード番号(2-8)を選択してください。")  
        else:
            self.messages.append("コンピューターが兵士(1)をプレイしました。")
            self.messages.append("コンピューターがカード番号(2-8)を選択します。")
        return self.messages
    
    def main_process(self, input_number):
        if self.is_player:
            if self.com_protect:
                self.messages.append("コンピューターは僧侶の効果中で対象にできません。")
                return self.messages
            else:
                if self.com_hand[0] == input_number:
                    self.messages.append("お見事!")
                    self.messages.append("コンピューターの手札を当てました!")
                    self.messages.append(Result.WIN)
                    return self.messages
                else:
                    self.messages.append("ハズレです。")
                    return self.messages
        else:
            if self.player_protect:
                self.messages.append("プレイヤーは僧侶の効果中で対象にされません。")
                return self.messages
            else:
                if self.player_hand[0] == input_number:
                    self.messages.append("残念...")
                    self.messages.append("プレイヤーの手札を当てられました...")
                    self.messages.append(Result.LOOSE)
                    return self.messages
                else:
                    self.messages.append("ハズレです。")
                    return self.messages