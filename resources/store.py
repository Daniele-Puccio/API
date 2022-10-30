import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from schema import StoreSchema

blp = Blueprint("stores", __name__, description="Operations on stores")

@blp.route("/store/<string:store_id>")
class Store(MethodView):
    @blp.response(200, StoreSchema)
    def get(self, store_id):
        try:
            return stores[store_id]
        except KeyError:
            abort(404, message="Store not found!")

    def delete(self, store_id):
        try:
            del stores[store_id]
            return {"message": "Store deleted."}
        except KeyError():
            abort(404, message="Store not found!")
    def put(self, store_id):
        store_data=request.get_json()
        if (
            "name" not in store_data or
            store_data['name'] == ""
        ):
            abort(499, message="Bad request. Ensure 'name' are included correctly in the JSON payload.")
        try:
            store=stores[store_id]
            store |= store_data
            return store
        except KeyError:
            abort(404, message="Store not found.")

@blp.route("/store")
class Store(MethodView):
    @blp.response(200,StoreSchema(many=True))
    def get(self):
        return stores.values()
    @blp.response(201,StoreSchema)
    @blp.arguments(StoreSchema)
    def post(self,store_data):
        for store in stores.values():
            if(store['name']==store_data['name']):
                abort(400,message="Store already exists.")
            if(store_data['name'] == ""):
                abort(400,message="Store must have a name.")
        store_id = uuid.uuid4().hex
        store = {**store_data, "id":store_id}
        stores[store_id] = store
        return store, 201