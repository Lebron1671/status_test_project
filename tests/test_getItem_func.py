import pytest


@pytest.mark.parametrize("data_store, id, expected_result",
                         [('ts', 7, {"id": 7, "parent": 4, "type": None}),
                          ('ds', 7, {"id": 7, "parent": 4, "type": None})])
def test_get_item_positive(data_store, id, expected_result, request):
    ds = request.getfixturevalue(data_store)
    assert ds.getItem(id) == expected_result

@pytest.mark.parametrize("data_store, expected_exception",
                             [('ts', ValueError),
                              ('ds', ValueError)])
def test_get_item_negative(data_store, expected_exception, request):
    ds = request.getfixturevalue(data_store)
    with pytest.raises(expected_exception):
        ds.getAllParents(100)
