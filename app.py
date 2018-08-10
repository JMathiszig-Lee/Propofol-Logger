from connexion.resolver import RestyResolver
import connexion


if __name__ == '__main__':
    app = connexion.FlaskApp(__name__, specification_dir='swagger/')
    app.add_api('api.yaml', resolver=RestyResolver('api'))
    app.run(host='127.0.0.1', port=9090)
