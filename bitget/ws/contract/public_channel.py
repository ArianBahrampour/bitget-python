from bitget.utils.consts import SWAP_TICKER, SUBSCRIBE, SWAP_TRADE, SWAP_DEPTH, SWAP_FUNDING_RATE, SWAP_MARK_PRICE, SWAP_PRICE_RANGE
from bitget.ws.server import WebsocketServer

class PublicChannel(WebsocketServer):
    def __init__(self, url, api_key, api_secret_key, passphrase):
        super(PublicChannel, self).__init__(url, api_key, api_secret_key, passphrase, isLogin=False)

    def ticker(self, symbol):
        super().set_args(SUBSCRIBE, [SWAP_TICKER+":"+symbol])
        super().connect()

    def candle(self, symbol, period):
        super().set_args(SUBSCRIBE, [period+":"+symbol])
        super().connect()

    def trade(self, symbol):
        super().set_args(SUBSCRIBE, [SWAP_TRADE+":"+symbol])
        super().connect()

    def depth(self, symbol):
        super().set_args(SUBSCRIBE, [SWAP_DEPTH+":"+symbol])
        super().connect()

    def funding_rate(self, symbol):
        super().set_args(SUBSCRIBE, [SWAP_FUNDING_RATE+":"+symbol])
        super().connect()

    def mark_price(self, symbol):
        super().set_args(SUBSCRIBE, [SWAP_MARK_PRICE+":"+symbol])
        super().connect()

    def price_range(self, symbol):
        super().set_args(SUBSCRIBE, [SWAP_PRICE_RANGE+":"+symbol])
        super().connect()
