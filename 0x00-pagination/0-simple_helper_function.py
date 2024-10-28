#!/usr/bin/env python3
"""
Contains definition of index_range helper function
"""


def index_range(page, page_size):
    """
    Takes 2 integer arguments and returns a tuple of size two
    containing the start and end index corresponding to the range of
    indexes to return in a list for those pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
