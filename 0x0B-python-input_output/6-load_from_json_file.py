#!/usr/bin/python3
# 6-load_from_json_file.py
# Haruna Danladi Maina <westamder32@gmail.com>
"""
Module 8-load_from_json_file
Contains function that creates a Python obj from JSON file
"""


def load_from_json_file(filename):
    """Creates a Python obj from JSON file
    Args:
        filename: file
    """
    import json

    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
