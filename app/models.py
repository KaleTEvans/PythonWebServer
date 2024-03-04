# models.py
from flask_sqlalchemy import SQLAlchemy
from .tagmapping import get_tag_string

db = SQLAlchemy()

class UnixValues(db.Model):
    __tablename__ = 'UnixValues'
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.Integer, unique=True, nullable=False)

    def to_dict(self):
        return {
            'ID': self.id,
            'Time': self.time
        }

class UnderlyingCandles(db.Model):
    __tablename__ = 'UnderlyingCandles'
    id = db.Column(db.Integer, primary_key=True)
    reqid = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    open = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    timeframe = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        # Reverse mapping for tags
        # print(f"Timeframe value: {self.timeframe}")  # Debug print
        # print(f"REVERSE_TAG_MAPPING: {REVERSE_TAG_MAPPING}")  # Debug print
        # timeframe_str = REVERSE_TAG_MAPPING.get(self.timeframe)

        return {
            'ID': self.id,
            'ReqID': self.reqid,
            'Date': self.date,
            'Time': self.time,
            'Open': self.open,
            'Close': self.close,
            'High': self.high,
            'Low': self.low,
            'TimeFrame': self.timeframe
        }

class OptionCandles(db.Model):
    __tablename__ = 'OptionCandles'
    candleid = db.Column(db.Integer, primary_key=True)
    reqid = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String, nullable=False)
    time = db.Column(db.Integer, nullable=False)
    open = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Integer, nullable=False)
    timeframe = db.Column(db.Integer, nullable=False)
    optiontype = db.Column(db.Integer, nullable=False)
    timeofday = db.Column(db.Integer, nullable=False)
    relativetomoney = db.Column(db.Integer, nullable=False)
    volumestdev = db.Column(db.Integer, nullable=False)
    volumethreshold = db.Column(db.Integer, nullable=False)
    optpricedelta = db.Column(db.Integer, nullable=False)
    dailyhighlow = db.Column(db.Integer, nullable=False)
    localhighlow = db.Column(db.Integer, nullable=False)
    underlyingpricedelta = db.Column(db.Integer, nullable=False)
    underlyingdailyhighlow = db.Column(db.Integer, nullable=False)
    underlyinglocalhighlow = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'CandleID': self.candleid,
            'ReqID': self.reqid,
            'Date': self.date,
            'Time': self.time,
            'Open': self.open,
            'Close': self.close,
            'High': self.high,
            'Low': self.low,
            'Volume': self.volume,
            'TimeFrame': get_tag_string(self.timeframe),
            'OptionType': get_tag_string(self.optiontype),
            'TimeOfDay': self.timeofday,
            'RelativeToMoney': self.relativetomoney,
            'VolumeStDev': self.volumestdev,
            'VolumeThreshold': self.volumethreshold,
            'OptPriceDelta': self.optpricedelta,
            'DailyHighLow': self.dailyhighlow,
            'LocalHighLow': self.localhighlow,
            'UnderlyingPriceDelta': self.underlyingpricedelta,
            'UnderlyingDailyHighLow': self.underlyingdailyhighlow,
            'UnderlyingLocalHighLow': self.underlyinglocalhighlow
        }
