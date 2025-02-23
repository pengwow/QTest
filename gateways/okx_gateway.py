from datetime import datetime
import okx.Account as Account
import okx.MarketData as MarketData
import okx.TradingData as TradingData
from gateway import BaseGateway


class OkxGateway(BaseGateway):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', flag="1", proxy=None):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.passphrase = passphrase
        self.flag = flag
        self.proxy = proxy

        # super().__init__(event_engine, "OKEX")
        # self.database = get_database()
        # self.database.create_table(self.gateway_name)
        # self.database.create_table(self.gateway_name, "tick")
        # self.database.create_table(self.gateway_name, "bar")
        # self.database.create_table(self.gateway_name, "order")
        # self.database.create_table(self.gateway_name, "trade")
        # self.database.create_table(self.gateway_name, "position")
        # self.database.create_table(self.gateway_name, "account")
        # self.database.create_table(self.gateway_name, "log")
        # self.database.create_table(self.gateway_name, "contract")
        # self.database.create_table(self.gateway_name, "subscription")
        # self.database.create_table(self.gateway_name, "setting")

    # flag = "1"
    # api_key = "7361a754-6fcf-4d8c-a81e-82abe6419911"
    # secret_key = "D44AF42935AF27262DDFE4DDE3B63103"
    # passphrase = 'lwobqobj6L..'
    # proxy = 'http://127.0.0.1:33210'
    # accountAPI = Account.AccountAPI(api_key, secret_key, passphrase, False, flag, proxy=proxy)

    # result = accountAPI.get_account_balance()
    # print(result)
    #
    # # marketDataAPI = MarketData.MarketAPI(flag=flag, proxy=proxy)
    # # result = marketDataAPI.get_tickers(instType="SPOT")
    # # print(result)
    # # 获取所有产品行情数据
    # result = MarketData.MarketAPI(flag=flag, proxy=proxy).get_tickers(instType="SPOT")
    # print(result)

    def get_bar_data(self, symbol, after, before, interval="15m"):
        #  转换为时间戳（秒）
        after_ts = datetime.strptime(after, '%Y-%m-%d')
        after_ts = int(after_ts.timestamp())
        before_ts = datetime.strptime(before, '%Y-%m-%d')
        before_ts = int(before_ts.timestamp())
        market_api = MarketData.MarketAPI(api_key=self.api_key, api_secret_key=self.api_secret_key, passphrase=self.passphrase,
                                          flag=self.flag, proxy=self.proxy)
        res = market_api.get_history_candlesticks(instId=symbol, after=after_ts, before=before_ts, bar=interval)
        print(res)
        return res


if __name__ == '__main__':
    flag = "1"
    api_key = "7361a754-6fcf-4d8c-a81e-82abe6419911"
    api_secret_key = "D44AF42935AF27262DDFE4DDE3B63103"
    passphrase = 'lwobqobj6L..'
    proxy = 'http://127.0.0.1:33210'
    okx_gateway = OkxGateway(api_key, api_secret_key, passphrase, flag, proxy)
    res = okx_gateway.get_bar_data("BTC-USDT", "2023-01-01", "2023-01-02", "15m")
    print(res)
