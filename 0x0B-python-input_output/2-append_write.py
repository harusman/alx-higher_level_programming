#!/usr/bin/python3
# 2-append_write.py
# Haruna Danladi Maina <westamder32@gmail.com>
"""
Module 4-append_write
Contains function that appends to text file and returns num chars added
"""


def append_write(filename="", text=""):
    """appends to text file and returns num chars added"""
    with open(filename, mode="a", encoding="utf-8") as f:
        return(f.write(text))
