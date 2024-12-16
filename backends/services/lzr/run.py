"""
Author: RookieNoob
"""
from flask_cors import CORS

from backends.services.lzr.app import app


if __name__ == '__main__':
    CORS(app)
    app.run(host='0.0.0.0', port=3456, debug=True)
    