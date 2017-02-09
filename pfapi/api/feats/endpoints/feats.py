import string

from flask import logging
from flask import request
from flask_restplus import Resource

from pfapi.api.feats.parsers import pagination_arguments
from pfapi.api.feats.serializers import feat, page_of_feats
from pfapi.api.restplus import api
from pfapi.database.models import Feat

log = logging.getLogger(__name__)

ns = api.namespace('data/feats', description='Operations related to Feats.')

@ns.route('/<int:id>')
@api.response(404, 'Feat not found.')
class FeatItem(Resource):
    @api.marshal_with(feat)
    def get(self, id):
        """
        Returns a single feat.
        """
        return Feat.query.filter(Feat.id == id).one()

@ns.route('/category/<string:category>')
@api.response(404, 'Feat category not found')
class FeatCategoryCollection(Resource):
    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_feats)
    def get(self, category):
        """
        Returns a list of feats within the provided category
        """

        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        # Capitalize each word, to better match the DB values
        category = string.capwords(category)

        feat_query = Feat.query.filter(Feat.feat_category == category)

        feats_page = feat_query.paginate(page, per_page, error_out=False)

        return feats_page

@ns.route('/name/<string:name_search>')
@ns.route('/name/<string:name_search>/<string:category>')
@api.response(404, 'No feat found for that criteria')
class FeatNameCollection(Resource):
    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_feats)
    def get(self, name_search, category=None):
        """
        Returns a list of feats whose name matches the provided string
        """

        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        # Capitalize each word, to better match the DB values
        name_search = string.capwords(name_search)
        category = string.capwords(category)

        feat_query = Feat.query.filter(Feat.feat_name.contains(name_search)).filter(Feat.feat_category == category)

        feats_page = feat_query.paginate(page, per_page, error_out=False)

        return feats_page
