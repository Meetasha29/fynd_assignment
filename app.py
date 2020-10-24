import newrelic.agent
import os

ENV = os.environ.get('FLASK_ENV', 'development')
newrelic.agent.initialize('newrelic.ini', ENV)

from flask import Flask
from commons.create_app import construct_flask_app
from flask_restplus import Api


app = construct_flask_app()
api = Api(app)

from configurations import settings


# registers all the blueprint and routes of each version of api
from apis.v1 import routes
app = newrelic.agent.wsgi_application()(app)

if __name__ == '__main__':
    app.run(debug=settings.DEBUG)
