#!/usr/bin/env python3
"""Defines a module that provides some stats
   about Nginx logs stored in MongoDB"""

from pymongo import MongoClient
get_stats = __import__('12-log_stats').get_stats


def get_ip_stats(nginx_coll):
    """returns stats about Nginx logs stored in MongoDB"""
    pipeline = [
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        },
        {
            "$limit": 10
        }
    ]
    cursor = nginx_coll.aggregate(pipeline)
    return "\n".join(f"\t{doc.get('_id')}: {doc.get('count')}"
                     for doc in cursor)


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print(get_stats(nginx_collection))
    print("IPs:")
    print(get_ip_stats(nginx_collection))
