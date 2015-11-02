# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from flask_restful import Resource


class MockResource(Resource):
    def get(self):
        return {'mock': 'me'}


class MockRunnerResource(Resource):
    def put(self, mock_id):
        return {'status': 'OK'}
