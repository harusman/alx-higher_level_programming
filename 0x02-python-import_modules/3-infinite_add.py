#!/usr/bin/python3
# 3-infinite_add.py
# Haruna Danladi Maina <westamder32@gmail.com>

if __name__ == "__main__":
    from sys import argv
    add = 0
    for s in argv[1:]:
        add += int(s)
    print("{:d}".format(add))
