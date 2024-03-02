from flask import Blueprint, jsonify
from sqlalchemy import select
from .models import db, UnixValues

unix_values = Blueprint('unix_values', __name__)

@unix_values.route('/unix', methods=['GET'])
def unix_list():
    unix = db.session.execute(select(UnixValues).order_by(UnixValues.time).limit(1000)).scalars()
    return jsonify({'UnixValues': [u.to_dict() for u in unix]})