from config import configuration
from src.initialize import init_app

configuration = configuration['development']

if __name__ == 'main':
    init_app(configuration).run(host='0.0.0.0', port='8081')