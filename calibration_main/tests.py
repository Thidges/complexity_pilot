from otree.api import Currency as c, currency_range, expect, Bot
from . import *

class PlayerBot(Bot):
    def play_round(self):
        yield Preface
        yield Task, {
            'total_revenue': 10,
            'total_request_cost': 5,
            'total_inventory_cost': 2,
            'total_items_sold': 1
        }
        yield Summary