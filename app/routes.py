from flask import Blueprint, jsonify, request
from sqlalchemy import select
from .models import db, UnixValues, UnderlyingCandles, OptionCandles
from .tagmapping import TAG_MAP

unix_values = Blueprint('unix_values', __name__)
underlying_candles = Blueprint('underlying_candles', __name__)
option_candles = Blueprint('option_candles', __name__)

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
    timeframe_str = request.args.get('timeframe')
    optiontype_str = request.args.get('type')
    limit = abs(int(request.args.get('limit', '1000')))

    query = select(OptionCandles).order_by(OptionCandles.time.desc())

    if timeframe_str:
        timeframe_value = TAG_MAP.get(timeframe_str)
        if timeframe_value is not None:
            query = query.filter(OptionCandles.timeframe == timeframe_value)
        else:
            # Handle the case where the timeframe string is not recognized
            return jsonify({'error': 'Invalid timeframe provided'}), 400

    if optiontype_str:
        optiontype_value = TAG_MAP.get(optiontype_str)
        if optiontype_value is not None:
            query = query.filter(OptionCandles.optiontype == optiontype_value)
        else:
            return jsonify({'error': 'Invalid option type provided'}), 400

    optiondata = db.session.execute(query.limit(limit)).scalars()
    return jsonify({'OptionCandles': [c.to_dict() for c in optiondata]})