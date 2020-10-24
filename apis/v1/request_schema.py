from jsonschema import Draft4Validator
from jsonschema.exceptions import ValidationError
from flask_restplus._http import HTTPStatus
from flask_restplus import fields, reqparse
from flask_restplus.model import ModelBase, RE_REQUIRED
from flask_restplus.errors import abort
from commons.error_codes import PayloadValidationErrorCodes
from . import api


class CustomRequestParser(reqparse.RequestParser):

    def __init__(self):
        super(CustomRequestParser, self).__init__()

    def parse_args(self, req=None, strict=False):
        try:
            return super(CustomRequestParser, self).parse_args()
        except Exception as e:
            errors = []
            parse_errors = e.data['errors']
            for key, value in parse_errors.items():
                errors.append({
                    "error_message": "{} - {}".format(key, value),
                    "error_code": "INVAILD_REQUEST_ARGS"
                })
            abort(
                HTTPStatus.BAD_REQUEST,
                _metadata={},
                message='Input payload validation failed',
                success=False,
                errors=errors)


def validate(self, data, resolver=None, format_checker=None):
    validator = Draft4Validator(self.__schema__, resolver=resolver, format_checker=format_checker)
    try:
        validator.validate(data)
    except ValidationError:
        abort(HTTPStatus.BAD_REQUEST,
              success=False,
              data=[],
              _metadata={},
              message='Input payload validation failed',
              errors=list(format_error(e) for e in validator.iter_errors(data)))


def format_error(error):
    path = list(error.path)
    if error.validator == 'required':
        name = RE_REQUIRED.match(error.message).group('name')
        path.append(name)
    field = '.'.join(str(p) for p in path)
    validator = error.validator
    value = error.validator_value
    error_data = PayloadValidationErrorCodes[validator].value
    error_message = error_data['error_message'].format(**{
        'field': field,
        'value': value
    })
    error_code = error_data['error_code']
    return {
        'error_code': error_code,
        'error_message': error_message
    }


ModelBase.validate = validate


class MovieRequestSchema:

    MovieCreate = api.model('MovieCreate', {
        'name': fields.String(desciption='movie name', required=True),
        'director': fields.String(desciption='movie_director', required=True),
        'imdb_score': fields.Integer(desciption='imdb score'),
        'popularity_99': fields.Integer(description='popularity_99'),
        'genre': fields.List(fields.String, description='list of genre')
    })


movie_map_parser = api.parser()
movie_map_parser.add_argument('name', type=str, help='name of the movie')
movie_map_parser.add_argument('director', type=str, help='name of the director')


class HeaderMap:
    USER_MAP = reqparse.RequestParser()
    USER_MAP.add_argument("Authorization", type=str, required=True, location='headers', help="User's Auth token")

