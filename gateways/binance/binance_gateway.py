# codding:utf-8
import os
import json
import zipfile
from io import BytesIO
import requests
import pandas as pd
import duckdb
from datetime import datetime, date
from urllib.parse import urljoin
from gateway import BaseGateway
from .binance_database import BinanceDatabase


class BinanceGateway(BaseGateway):
    def __init__(self, api_key='', api_secret_key='', flag='1', proxy=None):
        self.api_key = api_key
        self.api_secret_key = api_secret_key
        self.flag = flag
        self.proxy = proxy
        self.base_url = "https://api.binance.com"
        self.database = BinanceDatabase(database_path='data/binance.db')

    def api_request(self, url, params=None, headers=None):
        if self.flag == "1":
            response = requests.get(urljoin(self.base_url, url), params=params, headers=headers, proxies=self.proxy)
        else:
            response = requests.get(urljoin(self.base_url, url), params=params, headers=headers)
        return response

    def test_connect(self):
        url = "/api/v3/ping"
        headers = {
            "X-MBX-APIKEY": self.api_key
        }
        response = requests.get(urljoin(self.base_url, url), headers=headers, proxies=self.proxy)
        if response.status_code == 200:
            return True
        else:
            return False

    def get_bar_data(self, symbol, after, before, interval="15m"):
        start = self.convert_to_date_object(after)
        end = self.convert_to_date_object(before)
        # start_ts = self.convert_to_time_stamp(start)
        # end_ts = self.convert_to_time_stamp(end)
        # bars = self.database.load_bar_data(symbol, interval, start_ts, end_ts)
        # if len(bars) > 0:
        #     return bars
        dates = pd.date_range(end=end, periods=(end - start).days + 1).to_pydatetime().tolist()
        dates = [i.strftime("%Y-%m-%d") for i in dates]
        trading_type = 'spot'
        bar = self.download_daily_klines(trading_type, symbol, interval, dates)
        return bar

    def get_all_symbols(self):
        response = requests.get("https://api.binance.com/api/v3/exchangeInfo")
        return list(map(lambda symbol: symbol['symbol'], response.json()['symbols']))

    @staticmethod
    def convert_to_time_stamp(d):
        # 将 date 对象转换为 datetime 对象
        dt = datetime.combine(d, datetime.min.time())
        # 获取时间戳
        ts = int(dt.timestamp())
        return ts

    @staticmethod
    def convert_to_date_object(d):
        year, month, day = [int(x) for x in d.split('-')]
        date_obj = date(year, month, day)
        return date_obj

    def get_start_end_date_objects(self, date_range):
        start, end = date_range.split()
        start_date = self.convert_to_date_object(start)
        end_date = self.convert_to_date_object(end)
        return start_date, end_date

    @staticmethod
    def get_path(trading_type, market_data_type, time_period, symbol, interval=None):
        trading_type_path = 'data/spot'
        if trading_type != 'spot':
            trading_type_path = f'data/futures/{trading_type}'
        if interval is not None:
            path = f'{trading_type_path}/{time_period}/{market_data_type}/{symbol.upper()}/{interval}/'
        else:
            path = f'{trading_type_path}/{time_period}/{market_data_type}/{symbol.upper()}/'
        return path

    def download_daily_klines(self, trading_type, symbol, interval, dates):
        bar_data = []
        base_url = "https://data.binance.vision/"
        columns = [
            "open_time", "open_price", "high_price", "low_price", "close_price",
            "volume", "close_time", "quote_asset_volume", "number_of_trades",
            "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
        ]
        for item in dates:
            path = self.get_path(trading_type, "klines", "daily", symbol, interval)
            file_name = "{}-{}-{}.zip".format(symbol, interval, item)
            download_url = urljoin(base_url, f"{path}{file_name}")
            df = self.download_and_read_zip(download_url)
            df.columns = columns
            data = df.to_dict(orient='records')
            bar_data += data
            # self.database.save_bar_data(symbol, interval,data)
        return bar_data

    @staticmethod
    def download_and_read_zip(url):
        """
        从指定 URL 下载 ZIP 文件，并将其中的 CSV 文件读取到 Pandas DataFrame 中。
        参数:
            url (str): ZIP 文件的下载 URL。
        返回值:
            pd.DataFrame: 包含 ZIP 文件中 CSV 数据的 DataFrame。
        """
        # 发送 GET 请求下载 ZIP 文件
        response = requests.get(url)
        # 使用 BytesIO 将响应内容转换为字节流
        zip_file = zipfile.ZipFile(BytesIO(response.content))
        # 假设 ZIP 文件中只有一个 CSV 文件，读取该文件到 DataFrame
        with zip_file.open(zip_file.namelist()[0]) as file:
            df = pd.read_csv(file)
        return df


if __name__ == "__main__":
    gateway = BinanceGateway()
    after = "2023-01-01"
    before = "2023-01-02"
    after_ts = datetime.strptime(after, '%Y-%m-%d')
    after_ts = int(after_ts.timestamp())
    before_ts = datetime.strptime(before, '%Y-%m-%d')
    before_ts = int(before_ts.timestamp())
    res = gateway.get_bar_data("ETHUSDT", "2025-01-01", "2025-01-02", "15m")
    print(len(res))
