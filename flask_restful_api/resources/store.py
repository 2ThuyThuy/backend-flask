# from flask_restful import Resource
# from sqlalchemy.exc import SQLAlchemyError
# from flask_restful_api.models import StoreModel
#
#
# class Store(Resource):
#     @classmethod
#     def get(cls, name):
#         store = StoreModel.find_by_name(name)
#         if store:
#             return store.json()
#         return {"message": "Store not found"}, 404
#
#     @classmethod
#     def post(cls, name):
#         if StoreModel.find_by_name(name):
#             return {
#                 "message": "A store with name '{}' already exists.".format(name)
#             }, 400
#         store = StoreModel(name=name)
#         try:
#             store.save_to_db()
#         except SQLAlchemyError:
#             return {"message": "An error occurred creating the store."}, 500
#
#         return store.json(), 201
#
#     @classmethod
#     def delete(cls, name):
#         store = StoreModel.find_by_name(name)
#         if store:
#             store.delete_from_db()
#             return {"message": "Store deleted"}, 200
#         return {"message": "Store note found"}, 404
#
#
# class StoreList(Resource):
#     @classmethod
#     def get(cls):
#         return {"store":[store.json() for store in StoreModel.find_all()]}
#
