#!/usr/bin/env python3
""" Updates all topics of a school document based on the name """


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field of all documents with the given school name.

    Args:
        mongo_collection (Collection): PyMongo collection object.
        name (str): The name of the school to update.
        topics (list): List of topics to set for the school.

    Returns:
        dict: The result of the update operation.
    """
    return mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
