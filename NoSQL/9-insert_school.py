#!/usr/bin/env python3
""" Inserts a new document in a collection based on kwargs """


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a PyMongo collection using kwargs.

    Args:
        mongo_collection (Collection): PyMongo collection object.
        **kwargs: Key-value pairs of the document to insert.

    Returns:
        ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
