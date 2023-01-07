import config
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
    parser.add_argument('-p', '--port', default=5001, type=int, help='port to listen on')
    parser.add_argument('-s', '--setup', default='local', type=str, help='use local or remote db')
    args = parser.parse_args()
    port = args.port
    if args.setup == 'remote':
        config.current_config = config.Remote()
    elif args.setup == 'local':
        config.current_config = config.Local()
    else:
        raise ValueError("Wrong app setup type")

    app = create_app()

    app.run(host='0.0.0.0', port=port)
