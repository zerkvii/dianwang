from flask import jsonify, render_template, request, Response,request
from app.models import Record, Notice
from . import api


@api.route('/notice', methods=['GET', 'POST'])
def notice():
    # if request.method=='POST':

    notices = Notice.query.filter_by(is_checked=0).all()
    time_lists = [x.time for x in notices]
    data = {
        'notices': time_lists
    }
    return jsonify(data), 200
