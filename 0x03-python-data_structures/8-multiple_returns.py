#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        raise ValueError("sentence cannot be empty")
    length = len(sentence)
    first = sentence[0] if sentence else None
    return (length, first)
