#!/usr/bin/python3
# 3-to_json_string.py
# Haruna Danladi Maina <westamder32@gmail.com>
"""
Module 5-to_json_string
Contains function that returns JSON representation of obj (string)
"""


def to_json_string(my_obj):
    """Returns JSON representation of obj (string)
    Args:
        my_obj: python object
    Return:
        json string representation
    """
    import json

    return json.dumps(my_obj)
