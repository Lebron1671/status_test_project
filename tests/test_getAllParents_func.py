import pytest


@pytest.mark.parametrize("data_store, id, expected_result",
                             [('ts', 7, [{'id': 7, 'parent': 4, 'type': None}, {"id": 4, "parent": 2, "type": "test"},{"id": 2, "parent": 1, "type": "test"}, {"id": 1, "parent": "root"}]),
                              ('ds', 7, [{'id': 7, 'parent': 4, 'type': None}, {"id": 4, "parent": 2, "type": "test"},{"id": 2, "parent": 1, "type": "test"}, {"id": 1, "parent": "root"}]),
                              ('ts', 1, [{'id': 1, 'parent': 'root'}]),
                              ('ds', 1, [{'id': 1, 'parent': 'root'}])])
def test_get_all_parents_positive(data_store, id, expected_result, request):
    ds = request.getfixturevalue(data_store)
    assert ds.getAllParents(id) == expected_result

@pytest.mark.parametrize("data_store, expected_exception",
                             [('ts', ValueError),
                              ('ds', ValueError)])
def test_get_all_parents_negative(data_store, expected_exception, request):
    ds = request.getfixturevalue(data_store)
    with pytest.raises(expected_exception):
        ds.getAllParents(100)
