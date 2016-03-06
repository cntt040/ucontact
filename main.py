import logging

from flask import send_file, jsonify

from appcore import create_app


# Set up log to /leviathan.error.log
# file_handler = logging.FileHandler(filename='logs/leviathan.errors.log')
# file_handler.setLevel(logging.WARNING)

# Create flask uwsgi application
app = create_app()
# app.logger.addHandler(file_handler)


@app.route('/<path:path>')
def static_proxy(path):
    try:
        return send_file('/' + path)
    except Exception as e:
        return jsonify({'status': 'ERROR', 'message': e.message, "errors": e.message}), 400


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=8080)
