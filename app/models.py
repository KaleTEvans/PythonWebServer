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
    candleid = db.Column(db.Integer, primary_key=True, nullable=False)
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
            'TimeOfDay': get_tag_string(self.timeofday),
            'RelativeToMoney': get_tag_string(self.relativetomoney),
            'VolumeStDev': get_tag_string(self.volumestdev),
            'VolumeThreshold': get_tag_string(self.volumethreshold),
            'OptPriceDelta': get_tag_string(self.optpricedelta),
            'DailyHighLow': get_tag_string(self.dailyhighlow),
            'LocalHighLow': get_tag_string(self.localhighlow),
            'UnderlyingPriceDelta': get_tag_string(self.underlyingpricedelta),
            'UnderlyingDailyHighLow': get_tag_string(self.underlyingdailyhighlow),
            'UnderlyingLocalHighLow': get_tag_string(self.underlyinglocalhighlow)
        }

    @classmethod
    def string_to_category(self, category):
        if category == 'TimeFrame': return self.timeframe
        if category == 'OptionType': return self.optiontype
        if category == 'TimeOfDay': return self.timeofday
        if category == 'RelativeToMoney': return self.relativetomoney
        if category == 'VolumeStDev': return self.volumestdev
        if category == 'VolumeThreshold': return self.volumethreshold
        if category == 'OptPriceDelta': return self.optpricedelta
        if category == 'DailyHighLow': return self.dailyhighlow
        if category == 'LocalHighLow': return self.localhighlow
        if category == 'UnderlyingPriceDelta': return self.underlyingpricedelta
        if category == 'UnderlyingDailyHighLow': return self.underlyingdailyhighlow
        if category == 'UnderlyingLocalHighLow': return self.underlyinglocalhighlow

class CandlePerformance(db.Model):
    __tablename__ = 'CandlePerformance'
    performanceid = db.Column(db.Integer, primary_key=True, nullable=False)
    candleid = db.Column(db.Integer, db.ForeignKey('OptionCandles.CandleID'), nullable=False)
    percentwin = db.Column(db.Float, nullable=False)
    winloss = db.Column(db.Float, nullable=False)
    timetowin = db.Column(db.Integer, nullable=False)

def option_candle_performance_data(option_candle, candle_performance):
    return {
        # Option Candle Columns
        'CandleID': option_candle.candleid,
        'ReqID': option_candle.reqid,
        'Date': option_candle.date,
        'Time': option_candle.time,
        'Open': option_candle.open,
        'Close': option_candle.close,
        'High': option_candle.high,
        'Low': option_candle.low,
        'Volume': option_candle.volume,
        'TimeFrame': get_tag_string(option_candle.timeframe),
        'OptionType': get_tag_string(option_candle.optiontype),
        'TimeOfDay': get_tag_string(option_candle.timeofday),
        'RelativeToMoney': get_tag_string(option_candle.relativetomoney),
        'VolumeStDev': get_tag_string(option_candle.volumestdev),
        'VolumeThreshold': get_tag_string(option_candle.volumethreshold),
        'OptPriceDelta': get_tag_string(option_candle.optpricedelta),
        'DailyHighLow': get_tag_string(option_candle.dailyhighlow),
        'LocalHighLow': get_tag_string(option_candle.localhighlow),
        'UnderlyingPriceDelta': get_tag_string(option_candle.underlyingpricedelta),
        'UnderlyingDailyHighLow': get_tag_string(option_candle.underlyingdailyhighlow),
        'UnderlyingLocalHighLow': get_tag_string(option_candle.underlyinglocalhighlow),

        # Candle Performance Columns
        'PercentWin': candle_performance.percentwin,
        'WinLoss': candle_performance.winloss,
        'TimeToWin': candle_performance.timetowin
    }