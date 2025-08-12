#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, newline="", encoding="utf-8") as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            # Create a dict where key=index, value=row
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing the page of data indexed by position,
        resilient to deletions in the dataset.

        Args:
            index (int): The start index of the page (default 0)
            page_size (int): The number of items on the page (default 10)

        Returns:
            dict: {
                'index': current start index,
                'next_index': next start index to query,
                'page_size': size of returned data,
                'data': list of dataset rows for the page
            }
        """
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset()), \
            "index out of range"

        indexed_data = self.indexed_dataset()
        data = []
        current_index = index
        collected = 0

        # Keep collecting until we have page_size items or run out of data
        while collected < page_size and current_index < len(indexed_data):
            if current_index in indexed_data:
                data.append(indexed_data[current_index])
                collected += 1
            current_index += 1

        return {
            "index": index,
            "next_index": current_index,
            "page_size": len(data),
            "data": data
        }
