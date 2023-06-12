#!/usr/bin/python3
"""defining integer"""


class MyInt(int):
    """Class  that inherits from integer"""

    def __eq__(self, other):
        """Swap logic with __ne__"""
        return super().__ne__(other)

    def __ne__(self, other):
        """Swap logic __eq__"""
        return super().__eq__(other)
