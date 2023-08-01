import pytest


@pytest.mark.parametrize("id, expected_result", [(7, {"id":7,"parent":4,"type":None})])
def test_get_item_positive(ts, id, expected_result):
    assert ts.getItem(id) == expected_result

def test_get_item_negative(ts):
    with pytest.raises(ValueError):
        ts.getAllParents(100)
