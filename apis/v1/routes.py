"""
This module is responsible for adding resources of the APIs to the blueprint.
"""

from . import api, resources


# Movies CRUD

api.add_resource(resources.MovieCreation, '/movie-creation',
                 endpoint='v1_movie', methods=['POST'])

api.add_resource(resources.MovieListing, '/movie-listing',
                 endpoint='v1_movie_listing', methods=['GET'])

api.add_resource(resources.MovieDetail, '/movie/<int:movie_id>',
                 endpoint='v1_movie_detail', methods=['PUT', 'DELETE'])
