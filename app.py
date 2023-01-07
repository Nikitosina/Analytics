from flask import Flask
from argparse import ArgumentParser

def create_app() -> Flask:
    app = Flask(__name__)

    with app.app_context():
        from api.route.event import blueprint as analytics_api
        app.config["SQLALCHEMY_DATABASE_URI"] = "clickhouse://default:@localhost/default"
        app.register_blueprint(analytics_api, url_prefix="/analytics")

    return app


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-p', '--port', default=5000, type=int, help='port to listen on')
    args = parser.parse_args()
    port = args.port

    app = create_app()

    app.run(host='0.0.0.0', port=port)
