#!/usr/bin/env python3
""" Defines a module with a function that updates a MongoDB document"""


def update_topics(mongo_collection, name, topics):
    """
        changes all topics of a school document based on the name:

        mongo_collection(pymongo.collection.Collection):  pymongo
                                                          collection object
        name (string) : the school name to update
        topics List[str]: list of topics approached in the school
    """
    mongo_collection.update_many(
            {'name': name},
            {'$set': {'topics': topics}}
            )
