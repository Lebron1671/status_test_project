import pytest


@pytest.mark.parametrize("id, expected_result",
                             [(7, [{'id': 7, 'parent': 4, 'type': None},{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]),
                              (1, [{'id': 1, 'parent': 'root'}])])
def test_get_all_parents_positive(ts, id, expected_result):
    assert ts.getAllParents(id) == expected_result

def test_get_all_parents_negative(ts):
    with pytest.raises(ValueError):
        ts.getAllParents(100)
