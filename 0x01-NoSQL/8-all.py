#!/usr/bin/env python3
"""Defines a module with a function that lists all
    documents in a collection in MongoDb"""

from typing import List


def list_all(mongo_collection: pymongo.collection.Collection) -> List[dict]:
    """lists all documents in a collection in MongoDb"""
    cursor = mongo_collection.find({})
    all_docs = [doc for doc in cursor]
    return all_docs if all_docs else []
