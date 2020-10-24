import logging
from flask_restplus import Resource

from activities.movie_activities import MovieCreationActivity, MovieListingActivity, MovieUpdationActivity, MovieDeletionActivity
from apis.v1 import api
from apis.v1.request_schema import HeaderMap, MovieRequestSchema, movie_map_parser
from utils import parse_response

logger = logging.getLogger(__name__)


@api.doc(parser=HeaderMap.USER_MAP)
class MovieCreation(Resource):
    """
    Exposes APIs for Movie creation
    """

    @api.expect(MovieRequestSchema.MovieCreate, validate=True)
    @parse_response
    def post(self):

        payload = self.api.payload
        headers = HeaderMap.USER_MAP.parse_args()
        auth_token = headers.get('Authorization')

        response = MovieCreationActivity().execute(payload, auth_token=auth_token, permission_code='movie_create')

        return response


class MovieListing(Resource):
    """
    API for movie listin
    """
    @api.expect(movie_map_parser, validate=True)
    @parse_response
    def get(self):
        payload = movie_map_parser.parse_args()

        response = MovieListingActivity().execute(payload)

        return response


@api.doc(parser=HeaderMap.USER_MAP)
class MovieDetail(Resource):
    """
    Expose API for movie Updation and Deletion
    """

    @api.expect(MovieRequestSchema.MovieCreate, validate=True)
    @parse_response
    def put(self, movie_id):
        payload = self.api.payload
        headers = HeaderMap.USER_MAP.parse_args()
        auth_token = headers.get('Authorization')

        response = MovieUpdationActivity().execute(payload, auth_token=auth_token, movie_id=movie_id, permission_code='movie_update')

        return response

    @parse_response
    def delete(self, movie_id):
        headers = HeaderMap.USER_MAP.parse_args()
        auth_token = headers.get('Authorization')

        response = MovieDeletionActivity().execute(auth_token=auth_token, movie_id=movie_id, permission_code='movie_delete')

        return response
