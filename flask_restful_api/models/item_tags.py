from flask_restful_api.db import db


class ItemsTags(db.Model):
    __tablename__ = "items_tag"

    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey("items.id"))
    tag_id = db.Column(db.Integer, db.ForeignKey("tags.id"))