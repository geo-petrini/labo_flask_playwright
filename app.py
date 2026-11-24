from flask import Flask
from routes.default import app as d_bp
app = Flask(__name__)

app.register_blueprint(d_bp)


if __name__ == '__main__':
    app.run(debug=True)