#!/usr/bin/env python3
"""Defines a module with a function that lists all
    documents in a collection in MongoDb"""


def list_all(mongo_collection):
    """lists all documents in a collection in MongoDb"""
    return mongo_collection.find({})
