from api.result import Result
from api.component import *
from .deck import Deck
from switch import Switch

class LoveLetter:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = []
        self.com_hand = []
        self.player_protect = False
        self.com_protect = False
    
    def deal_initial_cards(self):
        self.player_hand = [self.deck.draw()]
        self.com_hand = [self.deck.draw()]
    
    def player_draw(self):
        self.player_hand.append(self.deck.draw())
    
    def card_play(self, is_player, card_number, is_main, input_number):
        if is_player:
            self.player_hand.remove(card_number)
            with Switch(card_number) as case:
                if case(1):
                    if not is_main:
                        return Soldier(*self.context(), True).first_process()
                    else:
                        message = Soldier(*self.context(), True).main_process(input_number)
                        if message[-1] == Result.WIN:
                            message.append(Result.WIN)
                            return message
                        else:
                            return message
                if case(2):
                    if not is_main:
                        return Clown(*self.context(), True).first_process()
                    else:
                        return Clown(*self.context(), True).main_process()
                if case(3):
                    if not is_main:
                        return Knight(*self.context(), True).first_process()
                    else:
                        return Knight(*self.context(), True).main_process()
                if case(4):
                    if not is_main:
                        return Monk(*self.context(), True).first_process()
                    else:
                        self.player_protect = Monk(*self.context(), True).main_process()
                        message = ["僧侶(4)の効果を使用します。"]
                        return message
                if case(5):
                    if not is_main:
                        return Magician(*self.context(), True, self.deck).first_process()
                    else:
                        return Magician(*self.context(), True, self.deck).main_process(input_number)
                if case(6):
                    if not is_main:
                        return General(*self.context(), True).first_process()
                    else:
                        return General(*self.context(), True).main_process()
                if case(7):
                    if not is_main:
                        return Minister(*self.context(), True).first_process()
                    else:
                        return Minister(*self.context(), True).main_process()
                else:
                    pass
        else:
            self.com_hand.remove(card_number)
            with Switch(card_number) as case:
                if case(1):
                    if not is_main:
                        return Soldier(*self.context(), False).first_process()
                    else:
                        message = Soldier(*self.context(), False).main_process(input_number)
                        if message[-1] == Result.LOOSE:
                            message.append(Result.LOOSE)
                            return message
                        else:
                            return message
                if case(2):
                    if not is_main:
                        return Clown(*self.context(), False).first_process()
                    else:
                        return Clown(*self.context(), False).main_process()
                if case(3):
                    if not is_main:
                        return Knight(*self.context(), False).first_process()
                    else:
                        return Knight(*self.context(), False).main_process()
                if case(4):
                    if not is_main:
                        return Monk(*self.context(), False).first_process()
                    else:
                        self.com_protect = Monk(*self.context(), False).main_process()
                        message = ["僧侶(4)の効果を使用します。"]
                        return message
                if case(5):
                    if not is_main:
                        return Magician(*self.context(), False, self.deck).first_process()
                    else:
                        return Magician(*self.context(), False, self.deck).main_process(input_number)
                if case(6):
                    if not is_main:
                        return General(*self.context(), False).first_process()
                    else:
                        return General(*self.context(), False).main_process()
                if case(7):
                    if not is_main:
                        return Minister(*self.context(), False).first_process()
                    else:
                        return Minister(*self.context(), False).main_process()
                else:
                    pass
    
    def com_draw(self):
        self.com_hand.append(self.deck.draw())
    
    def deck_len(self):
        return self.deck.remaining_cards()
    
    def deck_len_check(self):
        if self.deck.remaining_cards() == 0:
            if self.player_hand[0] > self.com_hand[0]:
                return Result.WIN
            elif self.player_hand[0] > self.com_hand[0]:
                return Result.LOOSE
            else:
                return Result.DRAW
        else:
            pass
    
    def minister_check(self, is_player):
        if is_player:
            if 12 <= sum(self.player_hand) and 7 in self.player_hand:
                return Result.LOOSE
            else:
                return Result.WIN
        else:
            if 12 <= sum(self.com_hand) and 7 in self.com_hand:
                return Result.LOOSE
            else:
                return Result.WIN
    
    def context(self):
        return [self.player_hand, self.com_hand, self.player_protect, self.com_protect]