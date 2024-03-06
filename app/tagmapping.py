
TAG_MAP = {
    'Call': (1, 'OptionType'),
    'Put': (2, 'OptionType'),

    '5sec': (3, 'TimeFrame'),
    '30sec': (4, 'TimeFrame'),
    '1min': (5, 'TimeFrame'),
    '5min': (6, 'TimeFrame'),

    'AtTheMoney': (7, 'RelativeToMoney'),
    '1StrikeOTM': (8, 'RelativeToMoney'),
    '2StrikesOTM': (9, 'RelativeToMoney'),
    '3StrikesOTM': (10, 'RelativeToMoney'),
    '4StrikesOTM': (11, 'RelativeToMoney'),
    '5StrikesOTM': (12, 'RelativeToMoney'),
    '1StrikeITM': (13, 'RelativeToMoney'),
    '2StrikesITM': (14, 'RelativeToMoney'),
    '3StrikesITM': (15, 'RelativeToMoney'),
    '4StrikesITM': (16, 'RelativeToMoney'),
    '5StrikesITM': (17, 'RelativeToMoney'),

    'Hour1': (18, 'TimeOfDay'),
    'Hour2': (19, 'TimeOfDay'),
    'Hour3': (20, 'TimeOfDay'),
    'Hour4': (21, 'TimeOfDay'),
    'Hour5': (22, 'TimeOfDay'),
    'Hour6': (23, 'TimeOfDay'),
    'Hour7': (24, 'TimeOfDay'),

    'VolumeOver1_StandardDeviations': (25, 'VolumeStDev'),
    'VolumeOver2_StandardDeviations': (26, 'VolumeStDev'),
    'VolumeOver3_StandardDeviations': (27, 'VolumeStDev'),
    'VolumeOver4_StandardDeviations': (28, 'VolumeStDev'),
    'VolumeUnder1_StandardDeviations': (29, 'VolumeStDev'),

    'VolumeOver100': (30, 'VolumeThreshold'),
    'VolumeOver250': (31, 'VolumeThreshold'),
    'VolumeOver500': (32, 'VolumeThreshold'),
    'VolumeOver1000': (33, 'VolumeThreshold'),
    'LowVolumeSignificance': (34, 'VolumeThreshold'),

    'Under1_UnderlyingPriceStdDevs': (35, 'UnderlyingPriceDelta'),
    'Under2_UnderlyingPriceStdDevs': (36, 'UnderlyingPriceDelta'),
    'Over2_UnderlyingPriceStdDevs': (37, 'UnderlyingPriceDelta'),
    'Under1_OptionPriceStdDevs': (38, 'OptPriceDelta'),
    'Under2_OptionPriceStdDevs': (39, 'OptPriceDelta'),
    'Over2_OptionPriceStdDevs': (40, 'OptPriceDelta'),

    'UnderlyingNearDailyLow': (41, 'UnderlyingDailyHighLow'),
    'UnderlyingNearDailyHigh': (42, 'UnderlyingDailyHighLow'),
    'UnderlyingInsideDailyRange': (43, 'UnderlyingDailyHighLow'),
    'OptionNearDailyLow': (44, 'DailyHighLow'),
    'OptionNearDailyHigh': (45, 'DailyHighLow'),
    'OptionInsideDailyRange': (46, 'DailyHighLow'),

    'UnderlyingNearLocalLow': (47, 'UnderlyingLocalHighLow'),
    'UnderlyingNearLocalHigh': (48, 'UnderlyingLocalHighLow'),
    'UnderlyingInsideLocalRange': (49, 'UnderlyingLocalHighLow'),
    'OptionNearLocalLow': (50, 'LocalHighLow'),
    'OptionNearLocalHigh': (51, 'LocalHighLow'),
    'OptionInsideLocalRange': (52, 'LocalHighLow'),

    '30min': (53, 'TimeFrame'),
    '1hr': (54, 'TimeFrame'),

    'OptionVolumeIncreasing': (55, 'OptionVolumeTrend'),
    'OptionVolumeSustainedIncrease': (56, 'OptionVolumeTrend'),
    'OptionVolumeDecreasing': (57, 'OptionVolumeTrend'),
    'OptionVolumeInsignificant': (58, 'OptionVolumeTrend'),

    'OptionPriceIncreasing': (59, 'OptionPriceTrend'),
    'OptionPriceSustainedIncrease': (60, 'OptionPriceTrend'),
    'OptionPriceDecreasing': (61, 'OptionPriceTrend'),
    'OptionPriceSustainedDecrease': (62, 'OptionPriceTrend'),
    'OptionPriceInsignificant': (63, 'OptionPriceTrend'),

    'BullishIntradayTrend': (64, 'IntradayTrend'),
    'BearishIntradayTrend': (65, 'IntradayTrend'),
    'SidewaysIntradayTrend': (66, 'IntradayTrend'),

    'BullishDailyTrend': (67, 'DailyTrend'),
    'BearishDailyTrend': (68, 'DailyTrend'),
    'SidewaysDailyTrend': (69, 'DailyTrend')
}

REVERSE_TAG_MAPPING = {v[0]: k for k, v in TAG_MAP.items()}

tag_cache = {} # For int to tag caching

def get_tag_string(tag_int):
    if tag_int not in tag_cache:
        tag_cache[tag_int] = REVERSE_TAG_MAPPING.get(tag_int, "Unknown")
    return tag_cache[tag_int]