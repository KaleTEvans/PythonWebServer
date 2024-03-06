from flask import Blueprint, jsonify, request, render_template
from sqlalchemy import select
from .models import db, UnixValues, UnderlyingCandles, OptionCandles, CandlePerformance 
from .models import option_candle_performance_data
from .tagmapping import TAG_MAP

home_page = Blueprint('home_page', __name__)
unix_values = Blueprint('unix_values', __name__)
underlying_candles = Blueprint('underlying_candles', __name__)
option_candles = Blueprint('option_candles', __name__)
candle_performance = Blueprint('candle_performance', __name__)

@home_page.route('/')
def index():
    return render_template('index.html')

@unix_values.route('/unix', methods=['GET'])
def get_unix():
    # Try to convert limit parameter to an integer, if provided
    try:
        limit = abs(int(request.args.get('limit', '1000')))  # Default to 1000 if not provided
    except ValueError:
        return jsonify({"error": "Invalid limit parameter"}), 400  # Bad request

    unix = db.session.execute(select(UnixValues).order_by(UnixValues.time).limit(limit)).scalars()
    return jsonify({'UnixValues': [u.to_dict() for u in unix]})

@underlying_candles.route('/underlying', methods=['GET'])
def get_underlying_candles():
    # Query filtering options
    timeframe_str = request.args.get('timeframe')
    limit = abs(int(request.args.get('limit', '1000')))

    query = select(UnderlyingCandles).order_by(UnderlyingCandles.time.desc())

    if timeframe_str:
        query = query.filter(UnderlyingCandles.timeframe == timeframe_str)

    underlying = db.session.execute(query.limit(limit)).scalars()

    return jsonify({'UnderlyingCandles': [u.to_dict() for u in underlying]})

@option_candles.route('/option', methods=['GET'])
def get_option_candles():
    # Query filtering options
    limit = abs(int(request.args.get('limit', '1000')))

    tag_params = request.args.get('tags')

    query = select(OptionCandles).order_by(OptionCandles.time.desc())

    if tag_params:
        tags_list = tag_params.split(',')
        for tag in tags_list:
            tag_id = TAG_MAP.get(tag)[0]
            tag_category_str = TAG_MAP.get(tag)[1]

            query = query.filter(OptionCandles.string_to_category(tag_category_str) == tag_id)

    optiondata = db.session.execute(query.limit(limit)).scalars()
    return jsonify({'OptionCandles': [c.to_dict() for c in optiondata]})

@option_candles.route('/option/tags', methods=['Get'])
def get_option_tags():
    return jsonify({'OptionTags': TAG_MAP})

@option_candles.route('/option/performance', methods=['GET'])
def get_option_candle_performance():
    # Query filtering options
    limit = abs(int(request.args.get('limit', '1000')))

    tag_params = request.args.get('tags')

    query = db.session.query(OptionCandles, CandlePerformance).join(
        CandlePerformance, OptionCandles.candleid == CandlePerformance.candleid
    ).order_by(OptionCandles.time.desc())
    
    if tag_params:
        tags_list = tag_params.split(',')
        for tag in tags_list:
            tag_id = TAG_MAP.get(tag)[0]
            tag_category_str = TAG_MAP.get(tag)[1]

            query = query.filter(OptionCandles.string_to_category(tag_category_str) == tag_id)

    res = query.limit(limit).all()
    option_data = [option_candle_performance_data(option_candle, candle_performance) for option_candle, candle_performance in res]
    return jsonify({'OptionCandles': option_data})