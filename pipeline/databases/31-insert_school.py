#!/usr/bin/env python3
"""Documentation"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document into the collection
    based on kwargs and returns the new _id."""
    return mongo_collection.insert_one(kwargs).inserted_id
