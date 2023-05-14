#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        raise ValueError("sentence cannot be empty")
    length = len(sentence)
    first_character = sentence[0] if length > 0 else None
    return (length, first_character)
