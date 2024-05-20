#!/usr/bin/env python3
"""Module for task 0"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    """function index_range that takes two integer arguments.

    Args:
        page (int): page index
        page_size (int): description

    Returns:
        Tuple: of size two containing a start index and an end
        index corresponding to the range of indexes
    """
    end_index = page * page_size
    return ((end_index - page_size, end_index))
