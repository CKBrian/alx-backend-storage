#!/usr/bin/env python3
"""Defines a module that provides some stats
   about Nginx logs stored in MongoDB"""

from pymongo import MongoClient
list_all = __import__('8-all').list_all


def get_stats(nginx_coll):
    """returns stats about Nginx logs stored in MongoDB"""
    stats = ("{} logs\nMethods:\n\t"
             "method GET: {}\n\tmethod POST: {}\n\t"
             "method PUT: {}\n\tmethod PATCH: {}\n\t"
             "method DELETE: {}\n{} status check".format(
               nginx_coll.count_documents({}),
               nginx_coll.count_documents({"method": "GET"}),
               nginx_coll.count_documents({"method": "POST"}),
               nginx_coll.count_documents({"method": "PUT"}),
               nginx_coll.count_documents({"method": "PATCH"}),
               nginx_coll.count_documents({"method": "DELETE"}),
               nginx_coll.count_documents({"method": "GET", 'path': '/status'})
               ))
    return stats


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx
    print(get_stats(nginx_collection))
