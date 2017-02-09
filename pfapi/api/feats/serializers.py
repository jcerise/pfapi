from flask_restplus import fields
from pfapi.api.restplus import api

feat = api.model('Feat', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a feat'),
    'feat_name': fields.String(required=True, description='Feat name'),
    'feat_category': fields.String(required=True, description='Feat category'),
    'feat_short_desc': fields.String(required=True, description='Short feat description'),
    'full_description': fields.String(required=True, description='Full feat description'),
    'prereqs': fields.String(required=True, description='Feat pre-requisites'),
    'benefit': fields.String(required=False, description='Feat benefit'),
    'special': fields.String(required=False, description='Feat special text'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_feats = api.inherit('Page of feats', pagination, {
    'items': fields.List(fields.Nested(feat))
})
