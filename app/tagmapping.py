
TAG_MAP = {
    'Call': 1,
    'Put': 2,

    '5sec': 3,
    '30sec': 4,
    '1min': 5,
    '5min': 6,

    'AtTheMoney': 7,
    '1StrikeOTM': 8,
    '2StrikesOTM': 9,
    '3StrikesOTM': 10,
    '4StrikesOTM': 11,
    '5StrikesOTM': 12,
    '1StrikeITM': 13,
    '2StrikesITM': 14,
    '3StrikesITM': 15,
    '4StrikesITM': 16,
    '5StrikesITM': 17,

    'Hour1': 18,
    'Hour2': 19,
    'Hour3': 20,
    'Hour4': 21,
    'Hour5': 22,
    'Hour6': 23,
    'Hour7': 24,

    'VolumeOver1_StandardDeviations': 25,
    'VolumeOver2_StandardDeviations': 26,
    'VolumeOver3_StandardDeviations': 27,
    'VolumeOver4_StandardDeviations': 28,
    'VolumeUnder1_StandardDeviations': 29,

    'VolumeOver100': 30,
    'VolumeOver250': 31,
    'VolumeOver500': 32,
    'VolumeOver1000': 33,
    'LowVolumeSignificance': 34,

    'Under1_UnderlyingPriceStdDevs': 35,
    'Under2_UnderlyingPriceStdDevs': 36,
    'Over2_UnderlyingPriceStdDevs': 37,
    'Under1_OptionPriceStdDevs': 38,
    'Under2_OptionPriceStdDevs': 39,
    'Over2_OptionPriceStdDevs': 40,

    'UnderlyingNearDailyLow': 41,
    'UnderlyingNearDailyHigh': 42,
    'UnderlyingInsideDailyRange': 43,
    'OptionNearDailyLow': 44,
    'OptionNearDailyHigh': 45,
    'OptionInsideDailyRange': 46,

    'UnderlyingNearLocalLow': 47,
    'UnderlyingNearLocalHigh': 48,
    'UnderlyingInsideLocalRange': 49,
    'OptionNearLocalLow': 50,
    'OptionNearLocalHigh': 51,
    'OptionInsideLocalRange': 52,

    '30min': 53,
    '1hr': 54,

    'OptionVolumeIncreasing': 55,
    'OptionVolumeSustainedIncrease': 56,
    'OptionVolumeDecreasing': 57,
    'OptionVolumeInsignificant': 58,

    'OptionPriceIncreasing': 59,
    'OptionPriceSustainedIncrease': 60,
    'OptionPriceDecreasing': 61,
    'OptionPriceSustainedDecrease': 62,
    'OptionPriceInsignificant': 63,

    'BullishIntradayTrend': 64,
    'BearishIntradayTrend': 65,
    'SidewaysIntradayTrend': 66,

    'BullishDailyTrend': 67,
    'BearishDailyTrend': 68,
    'SidewaysDailyTrend': 69
}

REVERSE_TAG_MAPPING = {v: k for k, v in TAG_MAP.items()}

tag_cache = {} # For int to tag caching

def get_tag_string(tag_int):
    if tag_int not in tag_cache:
        tag_cache[tag_int] = REVERSE_TAG_MAPPING.get(tag_int, "Unknown")
    return tag_cache[tag_int]