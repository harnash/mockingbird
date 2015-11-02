from flask import Flask

from flask_restful import Api
from mocks.resources import MockResource, MockRunnerResource

app = Flask(__name__)
api = Api(app)

api.add_resource(MockResource, '/mocks/')
api.add_resource(MockRunnerResource, '/mocks/run/<string:mock_id>', endpoint='put')

if __name__ == '__main__':
    app.run()
