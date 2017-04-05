# coding: utf-8
from . import api
from . import opt_db
from flask import jsonify


@api.route('/diligent')
def diligent():
    start_time = opt_db.Select().select_start_time
    end_time = opt_db.Select().select_end_time

    return jsonify(result={'s_time': start_time, 'e_time': end_time})