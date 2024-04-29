#!/usr/bin/env python3
"""Defines a module that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """inserts a new document in a collection based on kwargs"""
    new_doc = kwargs
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
