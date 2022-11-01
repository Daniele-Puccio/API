from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from db import db
from flask_jwt_extended import jwt_required
from models import TagModel, StoreModel
from flask_smorest import Blueprint, abort
from models.item import ItemModel
from schema import TagSchema, TagAndItemSchema

blp = Blueprint("Tags", "tags", description="Operations on tags")

@blp.route("/store/<int:store_id>/tag")
class TagsInStore(MethodView):

    @jwt_required()
    @blp.response(200, TagSchema(many=True))
    def get(self,store_id):
        store = StoreModel.query.get_or_404(store_id)
        return store.tags.all()

    @jwt_required()
    @blp.arguments(TagSchema)
    @blp.response(201,TagSchema)
    def post(self, tag_data,store_id):
        tag = TagModel(**tag_data,store_id=store_id)
        try:
            db.session.add(tag)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500,message=str(e))
        return tag

@blp.route("/item/<int:item_id>/tag/<int:tag_id>")
class LinkTagsToItem(MethodView):

    @jwt_required()
    @blp.response(201,TagSchema)
    def post(self,item_id,tag_id):
        item=ItemModel.query.get_or_404(item_id)
        tag=TagModel.query.get_or_404(tag_id)
        item.tags.append(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500,message="An error occurred while inserting the tag.")
        return tag

    @jwt_required()
    @blp.response(200, TagAndItemSchema)
    def delete(self, item_id, tag_id):
        item=ItemModel.query.get_or_404(item_id)
        tag=TagModel.query.get_or_404(tag_id)
        item.tags.remove(tag)
        try:
            db.session.add(item)
            db.session.commit()
        except SQLAlchemyError as e:
            abort(500,message="An error occurred while inserting the tag.")
        return {"message":"Item removed from tag", "item": item, "tag":tag}


@blp.route("/tag/<int:tag_id>")
class Tag(MethodView):

    @jwt_required()
    @blp.response(200, TagSchema)
    def get(self,tag_id):
        tag = StoreModel.query.get_or_404(tag_id)
        return tag

    @jwt_required()
    @blp.response(202,example={"message": "Tag deleted."})
    @blp.response(404, description="Tag not found.")
    @blp.response(400,description="Returnet if the tag is assigned to one or more items. In this case the tag is not deleted.")
    def delete(self,tag_id):
        tag = TagModel.sql.query_or_404(tag_id)
        if not tag.items:
            db.session.delete(tag)
            db.session.commit()
            return {"message":"Tag deleted."}
        else:
            abort(400, message="Could not delete tag. Make sure tag is not associated with any items, then try again.")
            