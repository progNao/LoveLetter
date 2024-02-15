from api.result import Result
from .loveletter import LoveLetter

class Game:
    def __init__(self):
        self.card = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.game = LoveLetter()
        self.game.deal_initial_cards()
        self.messages = []
        self.is_deck = True
    
    def deleteComma(self, array):
        return "|".join(map(str, array))
    
    def start(self):
        return "*****[Game Start!]*****"
    
    def end(self):
        return "*****[Game Over..]*****"
    
    def len_check(self):
        self.messages = []
        result = self.game.deck_len_check()
        if result in [Result.WIN, Result.LOOSE, Result.DRAW]:
            if result == Result.WIN:
                self.is_deck = False
                self.messages.append("プレイヤーの勝利!")
            elif result == Result.LOOSE:
                self.is_deck = False
                self.messages.append("コンピューターの勝利...")
            else:
                self.is_deck = False
                self.messages.append("引き分けです。")
            return self.messages
        else:
            self.is_deck = True
            return self.messages.append(f"山札は{self.game.deck_len()-1}です。")
    
    def player_turn(self):
        self.game.player_protect = False
        self.messages.append("プレイヤーのターンです。")
        self.messages.append("カードをドローします。")
        self.game.player_draw()
        self.messages.append(f"プレイヤーの手札：{self.deleteComma(self.game.player_hand)}")
        if self.game.minister_check(True) == Result.LOOSE:
            self.messages.append("手札に大臣(7)があり、かつ合計が12以上のためプレイヤーは脱落します。")
            return self.messages
        else:
            self.messages.append("手札のカードを1枚プレイしてください。")
            return self.messages
    
    def com_turn(self):
        self.game.com_protect = False
        self.messages.append("コンピューターのターンです。")
        self.messages.append("カードをドローします。")
        self.game.com_draw()
        if self.game.minister_check(False) == Result.LOOSE:
            self.messages.append("手札に大臣(7)があり、かつ合計が12以上のためコンピュータ-は脱落します。")
            return self.messages
        else:
            self.messages.append("コンピューターが手札のカードを1枚プレイします。")
            return self.messages
    
    def player_play_card(self, card_number, is_main, input_number):
        self.messages = []
        result = self.game.card_play(True, card_number, is_main, input_number)
        if result[-1] == Result.WIN:
            result = [i for i in result if i != Result.WIN]
            result.append("プレイヤーの勝利です!")
            return result
        elif result[-1] == Result.LOOSE:
            result = [i for i in result if i != Result.LOOSE]
            result.append("コンピューターの勝利です...")
            return result
        elif result[-1] == Result.DRAW:
            result = [i for i in result if i != Result.DRAW]
            result.append("引き分けです。")
            return result
        else:
            return result
    
    def com_play_card(self, card_number, is_main, input_number):
        self.messages = []
        result = self.game.card_play(False, card_number, is_main, input_number)
        if result[-1] == Result.WIN:
            result = [i for i in result if i != Result.WIN]
            result.append("プレイヤーの勝利です!")
            return result
        elif result[-1] == Result.LOOSE:
            result = [i for i in result if i != Result.LOOSE]
            result.append("コンピューターの勝利です...")
            return result
        elif result[-1] == Result.DRAW:
            result = [i for i in result if i != Result.DRAW]
            result.append("引き分けです。")
            return result
        else:
            return result