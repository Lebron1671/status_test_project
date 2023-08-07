import pytest

@pytest.mark.parametrize("data_store, expected_result",
                             [('ts', [{'id': 1, 'parent': 'root'}, {'id': 2, 'parent': 1, 'type': 'test'}, {'id': 3, 'parent': 1, 'type': 'test'}, {'id': 4, 'parent': 2, 'type': 'test'}, {'id': 5, 'parent': 2, 'type': 'test'}, {'id': 6, 'parent': 2, 'type': 'test'}, {'id': 7, 'parent': 4, 'type': None}, {'id': 8, 'parent': 4, 'type': None}]),
                              ('ds', [{'id': 1, 'parent': 'root'}, {'id': 2, 'parent': 1, 'type': 'test'}, {'id': 3, 'parent': 1, 'type': 'test'}, {'id': 4, 'parent': 2, 'type': 'test'}, {'id': 5, 'parent': 2, 'type': 'test'}, {'id': 6, 'parent': 2, 'type': 'test'}, {'id': 7, 'parent': 4, 'type': None}, {'id': 8, 'parent': 4, 'type': None}])])
def test_get_all_positive(data_store, expected_result, request):
    ds = request.getfixturevalue(data_store)
    assert ds.getAll() == expected_result
