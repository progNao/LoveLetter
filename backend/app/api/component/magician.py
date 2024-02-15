from api.result import Result

class Magician:
    def __init__(self, player_hand, com_hand, player_protect, com_protect, is_player, deck):
        self.player_hand = player_hand
        self.com_hand = com_hand
        self.player_protect = player_protect
        self.com_protect = com_protect
        self.is_player = is_player
        self.deck = deck
        self.messages = []
    
    def first_process(self):
        if self.is_player:
            self.messages.append("プレイヤーが魔術師(5)をプレイしました。")
            self.messages.append("どちらの手札を捨てるか選んでください。")  
        else:
            self.messages.append("コンピューターが魔術師(5)をプレイしました。")
            self.messages.append("コンピューターが捨てさせる対象を選びます。")
        return self.messages
    
    def main_process(self, input_number):
        if self.is_player:
            if input_number == 1:
                self.messages.append("プレイヤーが選択されました。")
                if self.player_protect:
                    self.messages.append("プレイヤーは僧侶の効果中で対象にされません。")
                    return self.messages
                else:
                    return self.calc(True)
            else:
                self.messages.append("コンピューターが選択されました。")
                if self.com_protect:
                    self.messages.append("コンピューターは僧侶の効果中で対象にできません。")
                    return self.messages
                else:
                    return self.calc(False)
        else:
            if input_number == 1:
                self.messages.append("プレイヤーが選択されました。")
                if self.player_protect:
                    self.messages.append("プレイヤーは僧侶の効果中で対象にされません。")
                    return self.messages
                else:
                    return self.calc(True)
            else:
                self.messages.append("コンピューターが選択されました。")
                if self.com_protect:
                    self.messages.append("コンピューターは僧侶の効果中で対象にできません。")
                    return self.messages
                else:
                    return self.calc(False)
    
    def calc(self, is_player):
        if is_player:
            if self.player_hand[0] == 8:
                self.messages.append("姫(8)が捨てられたため、プレイヤーは脱落します。")
                self.messages.append(Result.LOOSE)
                return self.messages
            else:
                value_out = self.player_hand.pop()
                value_in = self.deck.draw()
                self.player_hand.append(value_in)
                self.messages.append(f"{value_out}を捨てました。")
                self.messages.append(f"{value_in}をドローしました。")
                return self.messages
        else:
            if self.com_hand[0] == 8:
                self.messages.append("姫(8)が捨てられたため、コンピューターは脱落します。")
                self.messages.append(Result.WIN)
                return self.messages
            else:
                value_out = self.com_hand.pop()
                self.com_hand.append(self.deck.draw())
                self.messages.append(f"{value_out}を捨てました。")
                return self.messages