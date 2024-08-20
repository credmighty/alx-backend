#!/usr/bin/env python3
""" Simple helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function that takes two int as it argument and returns turple of size two
    start index and end index
    param:
       page -> int
       page_size -> int
    return:
        turple(int, int)
    """
    first_ind = (page - 1) * page_size
    end_ind = first_ind + page_size
    return first_ind, end_ind
