#!/usr/bin/env python3
"""
Function that returns all students sorted by average score
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    - mongo_collection: pymongo collection object
    """
    return mongo_collection.aggregate([
        {
            "$addFields": {
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ])
