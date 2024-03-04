
TAG_MAP = {
    'Call': 1,
    'Put': 2,

    '5sec': 3,
    '30sec': 4,
    '1min': 5,
    '5min': 6,
    '30min': 53,
    '1hr': 54,

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
    'VolumeUnder1_StandardDeviation': 29,

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
    'Over2_OptionPriceStdDevs': 40 
}

REVERSE_TAG_MAPPING = {v: k for k, v in TAG_MAP.items()}

tag_cache = {} # For int to tag caching

def get_tag_string(tag_int):
    if tag_int not in tag_cache:
        tag_cache[tag_int] = REVERSE_TAG_MAPPING.get(tag_int, "Unknown")
    return tag_cache[tag_int]

# int tag_to_db_key(PriceDelta val, TagCategory tc) {
#     if (tc == TagCategory::UnderlyingPriceDelta) {
#         switch (val)
#         {
#         case PriceDelta::Under1: return 35;
#         case PriceDelta::Under2: return 36;
#         case PriceDelta::Over2: return 37;
#         default: return 0;
#         }
#     } else if (tc == TagCategory::OptionPriceDelta) {
#         switch (val)
#         {
#         case PriceDelta::Under1: return 38;
#         case PriceDelta::Under2: return 39;
#         case PriceDelta::Over2: return 40;
#         default: return 0;
#         }
#     } else {
#         std::cout << "Enum Error: Invalid TagCategory and PriceDelta" << std::endl;
#         return 0;
#     }
# }

# int tag_to_db_key(DailyHighsAndLows val, TagCategory tc) {
#     if (tc == TagCategory::UnderlyingDailyHighsAndLows) {
#         switch (val)
#         {
#         case DailyHighsAndLows::NDL: return 41;
#         case DailyHighsAndLows::NDH: return 42;
#         case DailyHighsAndLows::Inside: return 43;
#         default: return 0;
#         }
#     } else if (tc == TagCategory::OptionDailyHighsAndLows) {
#          switch (val)
#         {
#         case DailyHighsAndLows::NDL: return 44;
#         case DailyHighsAndLows::NDH: return 45;
#         case DailyHighsAndLows::Inside: return 46;
#         default: return 0;
#         }
#     } else {
#         std::cout << "Enum Error: Invalid TagCategory and DHL" << std::endl;
#         return 0;
#     }
# }

# int tag_to_db_key(LocalHighsAndLows val, TagCategory tc) {
#     if (tc == TagCategory::UnderlyingLocalHighsAndLows) {
#         switch (val)
#         {
#         case LocalHighsAndLows::NLL: return 47;
#         case LocalHighsAndLows::NLH: return 48;
#         case LocalHighsAndLows::Inside: return 49;
#         default: return 0;
#         }
#     } else if (tc == TagCategory::OptionLocalHighsAndLows) {
#         switch (val)
#         {
#         case LocalHighsAndLows::NLL: return 50;
#         case LocalHighsAndLows::NLH: return 51;
#         case LocalHighsAndLows::Inside: return 52;
#         default: return 0;
#         }
#     } else {
#         std::cout << "Enum Error: Invalid TagCategory and LHL" << std::endl;
#         return 0;
#     }
# }

# int tag_to_db_key(VolumeROC val) {
#     switch (val)
#     {
#     case VolumeROC::VolumeIncrease: return 55;
#     case VolumeROC::HighVolumeIncrease: return 56;
#     case VolumeROC::VolumeDecrease: return 57;
#     default: return 0;
#     }
# }

# int tag_to_db_key(PriceROC val) {
#     switch (val)
#     {
#     case PriceROC::PriceIncrease: return 58;
#     case PriceROC::HighPriceIncrease: return 59;
#     case PriceROC::PriceDecrease: return 60;
#     case PriceROC::HighPriceDecrease: return 61;
#     default: return 0;
#     }
# }

# int tag_to_db_key(TrendingDirectionIntraday val) {
#     switch (val)
#     {
#     case TrendingDirectionIntraday::Bullish: return 62;
#     case TrendingDirectionIntraday::Bearish: return 63;
#     case TrendingDirectionIntraday::Sideways: return 64;
#     default: return 0;
#     }
# }

# int tag_to_db_key(TrendingDirectionDaily val) {
#     switch (val)
#     {
#     case TrendingDirectionDaily::Bullish: return 65;
#     case TrendingDirectionDaily::Bearish: return 66;
#     case TrendingDirectionDaily::Sideways: return 67;
#     default: return 0;
#     }
# }