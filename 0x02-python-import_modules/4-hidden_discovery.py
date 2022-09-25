#!/usr/bin/python3
# 4-hidden_discovery.py
# Haruna Danladi Maina <westamder32@gmail.com>

if __name__ == "__main__":
    import hidden_4
    defs = dir(hidden_4)
    for i in range(0, len(defs)):
        if defs[i][0] != '_' and defs[i][1] != '_':
            print(defs[i])
