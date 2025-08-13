#!/usr/bin/env python3
""" Lists all documents in a collection """


def list_all(mongo_collection):
    """
    Returns all documents in a PyMongo collection.
    If no documents exist, returns an empty list.

    Args:
        mongo_collection (Collection): PyMongo collection object.

    Returns:
        list: List of all documents in the collection.
    """
    return list(mongo_collection.find())
