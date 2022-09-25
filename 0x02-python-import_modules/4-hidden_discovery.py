#!/usr/bin/python3
# 4-hidden_discovery.py
# Haruna Danladi Maina <westamder32@gmail.com>

import hidden_4


def decompile():
    for name in dir(hidden_4):
        if name[0] != '_' and name[1] != '_':
            print(name)


if (__name__ == '__main__'):
    decompile()
