# api/v1/views/index.py

#!/usr/bin/python3

from flask import jsonify
from api.v1.views import app_views

@app_views.route('/status', methods=['GET'])
def status():
    """Return status OK"""
    return jsonify({"status": "OK"})
