import pytest
import os
import sys

from Solutions.TreeStore import TreeStore
from Solutions.DictStore import DictStore
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@pytest.fixture()
def get_data():
    return [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]



@pytest.fixture(name='ds')
def dict_store_fixture(get_data):
    return DictStore(get_data)

@pytest.fixture(name='ts')
def tree_store_fixture(get_data):
    return TreeStore(get_data)
