#!/usr/bin/env python3
""" Defines a module with a function that returns all students
    sorted by average score
"""


def top_students(mongo_collection):
    """
    mongo_collection will be the pymongo collection object
    The top must be ordered
    The average score must be part of each item returns with key = averageScore
    """
    pipeline = [
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]
    return mongo_collection.aggregate(pipeline)
