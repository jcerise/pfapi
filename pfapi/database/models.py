from datetime import datetime

from . import db


class Feat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow())
    date_updated = db.Column(db.DateTime, default=datetime.utcnow())
    feat_name = db.Column(db.String(80))
    feat_category = db.Column(db.String(32))
    feat_short_desc = db.Column(db.String(256))
    full_description = db.Column(db.String(2048))
    prereqs = db.Column(db.String(512))
    benefit = db.Column(db.String(2048))
    special = db.Column(db.String(2048))

    def __init__(self, name, category, short_desc, full_desc, pre_reqs, benefit, special, date_created=None,
                 date_updated = None):
        if date_created is None:
            date_created = datetime.utcnow()
        self.date_created = date_created
        if date_updated is None:
            date_updated = datetime.utcnow()
        self.date_updated = date_updated
        self.name = name
        self.category = category
        self.short_desc = short_desc
        self.full_desc = full_desc
        self.pre_reqs = pre_reqs
        self.benefit = benefit
        self. special = special

    def __repr__(self):
        return '<Feat {}>'.format(self.nam)
