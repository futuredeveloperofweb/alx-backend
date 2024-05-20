#!/usr/bin/env python3
"""Module for task 3"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """get_hyper_index method with two integer arguments: index
        with a None default value and page_size with default
        value of 10

        Args:
            index (int): current index of the page
            page_size (int): the current size of the page with Defaults to 10

        Returns: dict
        """
        max_index = len(self.dataset())
        assert type(index) is int and index < max_index
        gap = 0

        for idx in range(index, max_index):
            if self.indexed_dataset().get(idx):
                break
            gap += 1

        next_index = idx + page_size
        data = self.dataset()[idx:next_index]

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
