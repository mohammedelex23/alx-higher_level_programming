#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or len(sentence) == 0:
        return tuple((0, None))
    return (len(sentence),sentence[0])
