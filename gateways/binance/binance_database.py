# coding=utf-8
from datetime import datetime, date
from database import BaseDatabase
import duckdb


class BinanceDatabase(BaseDatabase):
    def __init__(self, database_path: str):
        self.database_path: str = 'binance.db'

    def load_bar_data(self, symbol: str, interval: '', start: int, end: int) -> list:
        bar = []
        db = duckdb.connect(self.database_path)
        try:
            query = f"SELECT * FROM {symbol}_{interval} WHERE open_time >= '{start}' AND open_time <= '{end}'"
            bar = db.execute(query).fetchall()
        except Exception as e:
            print(e)
        db.close()
        return bar

    def save_bar_data(self, symbol: str, interval: '', bars: list) -> bool:
        table_name = f"{symbol}_{interval}"
        try:
            db = duckdb.connect(self.database_path)
            db.execute(f"""
            CREATE TABLE IF NOT EXISTS {table_name} (
                open_time BIGINT,
                open_price VARCHAR,
                high_price VARCHAR,
                low_price VARCHAR,
                close_price VARCHAR,
                volume VARCHAR,
                close_time BIGINT,
                quote_asset_volume VARCHAR,
                number_of_trades INTEGER,
                taker_buy_base_asset_volume VARCHAR,
                taker_buy_quote_asset_volume VARCHAR,
                ignore VARCHAR
            )""")
            for record in bars:
                db.execute(f"""
                INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, list(record.values()))
        except Exception as e:
            print(e)
            return False
        return True

    def delete_bar_data(self, symbol: str, interval: '') -> int:
        pass
