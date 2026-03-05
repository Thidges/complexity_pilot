from otree.api import Currency as c, currency_range, expect, Bot
from . import *
import random

class PlayerBot(Bot):
    def play_round(self):
        yield Questionnaire, {
            'strategy_text': 'not much', 
            'comments': ''
        }
        yield FinalScreen