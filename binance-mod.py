from binance.client import Client
from pybit.unified_trading import HTTP

client = Client()
session = HTTP(
    testnet=False,
)
s_list = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT', 'EOSUSDT', 'TUSDUSDT', 'XLMUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT', 'USDCUSDT', 'LINKUSDT', 'WAVESUSDT', 'BTTUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT', 'BATUSDT', 'ZECUSDT', 'DASHUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MATICUSDT', 'ATOMUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'DOGEUSDT', 'ANKRUSDT', 'CHZUSDT', 'BEAMUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT', 'STXUSDT', 'KAVAUSDT', 'BCHUSDT', 'FTTUSDT', 'BNTUSDT', 'SOLUSDT', 'LRCUSDT', 'COMPUSDT', 'SCUSDT', 'ZENUSDT', 'SNXUSDT', 'DGBUSDT', 'MKRUSDT', 'DAIUSDT', 'DCRUSDT', 'MANAUSDT', 'YFIUSDT', 'JSTUSDT', 'SRMUSDT', 'CRVUSDT', 'SANDUSDT', 'DOTUSDT', 'LUNAUSDT', 'PAXGUSDT', 'SUSHIUSDT', 'KSMUSDT', 'EGLDUSDT', 'RUNEUSDT', 'UMAUSDT', 'BELUSDT', 'UNIUSDT', 'SUNUSDT', 'AVAXUSDT', 'HNTUSDT', 'AAVEUSDT', 'NEARUSDT', 'FILUSDT', 'INJUSDT', 'AXSUSDT', 'ROSEUSDT', 'AVAUSDT', 'XEMUSDT', 'GRTUSDT', 'JUVUSDT', 'PSGUSDT', '1INCHUSDT', 'CELOUSDT', 'TWTUSDT', 'CAKEUSDT', 'ACMUSDT', 'PERPUSDT', 'BTGUSDT', 'BARUSDT', 'SLPUSDT', 'SHIBUSDT', 'ICPUSDT', 'ARUSDT', 'MASKUSDT', 'KLAYUSDT', 'C98USDT', 'QNTUSDT', 'FLOWUSDT', 'TVKUSDT', 'MINAUSDT', 'MBOXUSDT', 'WAXPUSDT', 'TRIBEUSDT', 'XECUSDT', 'DYDXUSDT', 'GALAUSDT', 'FIDAUSDT', 'AGLDUSDT', 'MOVRUSDT', 'CITYUSDT', 'ENSUSDT', 'JASMYUSDT', 'RNDRUSDT', 'BICOUSDT', 'FXSUSDT', 'PEOPLEUSDT', 'SPELLUSDT', 'ACHUSDT', 'IMXUSDT', 'GLMRUSDT', 'SCRTUSDT', 'ACAUSDT', 'WOOUSDT', 'TUSDT', 'GMTUSDT', 'KDAUSDT', 'APEUSDT', 'NEXOUSDT', 'GALUSDT', 'LDOUSDT', 'OPUSDT', 'LEVERUSDT', 'STGUSDT', 'LUNCUSDT', 'GMXUSDT', 'APTUSDT', 'HFTUSDT', 'HOOKUSDT', 'MAGICUSDT', 'RPLUSDT', 'AGIXUSDT', 'GNSUSDT', 'SSVUSDT', 'USTCUSDT', 'IDUSDT', 'ARBUSDT', 'RDNTUSDT', 'WBTCUSDT', 'SUIUSDT', 'PEPEUSDT', 'FLOKIUSDT', 'PENDLEUSDT', 'ARKMUSDT', 'WLDUSDT', 'SEIUSDT', 'CYBERUSDT', 'TIAUSDT', 'MEMEUSDT', 'ORDIUSDT', 'VICUSDT', 'BLURUSDT', 'VANRYUSDT', 'JTOUSDT', 'BONKUSDT', 'XAIUSDT', 'MANTAUSDT']
s_list_val = []


def get_price_symbol():
    for s in s_list:
        symbol_binance = client.get_symbol_ticker(symbol=s)
        symbol_bybit = session.get_tickers(category="spot", symbol=s)['result']['list'][0]
        symbol_difference = abs(round(float(symbol_binance['price']) - float(symbol_bybit['lastPrice']), 4))
        # symbol_sum = f"{s}: ціна на бінанс: {symbol_binance['price']} Ціна на байбіт: {symbol_bybit['lastPrice']}"
        if symbol_difference > 1:
            symbol_sum = f"{s}: {symbol_difference} --> Бінанс: {symbol_binance['price']} Байбіт: {symbol_bybit['lastPrice']}"
            print(symbol_sum)




def get_symbol(symbol):
    try:
        symbol_info = session.get_tickers(category="spot", symbol=symbol,)['result']['list']
        symbol_info = symbol_info['result']
        symbol_info = symbol_info['list']
        for symbol in symbol_info:
            symbol_tiker = [symbol['symbol'], symbol['lastPrice']]
            print(symbol_tiker)
            s_list.append(symbol['symbol'])

    except Exception as ex:
        print(ex)


get_price_symbol()




# print(symbol_dict)
# print(len(symbol_dict))

# print(session)
