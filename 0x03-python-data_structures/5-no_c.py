#!/usr/bin/python3
# 5-no_c.py
# Haruna Danladi Maina <westamder32@gmail.com>



def no_c(my_string):
    return ("".join(c for c in my_string if c not in "Cc"))
