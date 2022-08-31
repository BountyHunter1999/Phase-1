#!/bin/python3


def pos(text):
    d = {}
    for i, v in enumerate(text):
        d[v] = d.get(v, []) + [i]
    return d

# print(pos("Hello"))

