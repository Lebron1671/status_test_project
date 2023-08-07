import pytest


@pytest.mark.parametrize("data_store, id, expected_result",
                             [('ts', 4, [{"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}]),
                              ('ds', 4, [{"id": 7, "parent": 4, "type": None}, {"id": 8, "parent": 4, "type": None}]),
                              ('ts', 5, []),
                              ('ds', 5, [])])
def test_get_children_positive(data_store, id, expected_result, request):
    ds = request.getfixturevalue(data_store)
    assert ds.getChildren(id) == expected_result

@pytest.mark.parametrize("data_store, expected_exception",
                             [('ts', ValueError),
                              ('ds', ValueError)])
def test_get_children_negative(data_store, expected_exception, request):
    ds = request.getfixturevalue(data_store)
    with pytest.raises(expected_exception):
        ds.getAllParents(100)