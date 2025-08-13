#!/usr/bin/env python3
""" Returns the list of schools having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """
    Finds all schools in the collection that have a specific topic.

    Args:
        mongo_collection (Collection): PyMongo collection object.
        topic (str): The topic to search for.

    Returns:
        list: List of school documents matching the topic.
    """
    return list(mongo_collection.find({"topics": topic}))
