#!/usr/bin/env python3
""" Defines a module with a function that returns
    the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """
        returns the list of school having a specific topic:

        mongo_collection(pymongo.collection.Collection):  pymongo
                                                          collection object
        topics List[str]: list of topics approached in the school
    """
    return mongo_collection.find({"topics": topic})
