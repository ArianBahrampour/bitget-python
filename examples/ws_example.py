from bitget.utils.consts import CONTRACT_WS_URL
from bitget.ws.ws_client import BitgetWsClient, SubscribeReq


def handle(message):
    print("handle:" + message)


def handel_error(message):
    print("handle_error:" + message)


def handel_btcusd(message):
    print("handel_btcusd:" + message)


if __name__ == '__main__':
    api_key = ""
    secret_key = ""
    passphrase = ""
    symbol = 'btcusd'

    client = BitgetWsClient(CONTRACT_WS_URL, need_login=True) \
        .api_key(api_key) \
        .api_secret_key(secret_key) \
        .passphrase(passphrase) \
        .error_listener(handel_error) \
        .build()

    channles = [SubscribeReq("mc", "ticker", "BTCUSD"), SubscribeReq("SP", "candle1W", "BTCUSDT")]
    client.subscribe(channles,handle)

    channles = [SubscribeReq("mc", "ticker", "ETHUSD")]
    client.subscribe(channles, handel_btcusd)

