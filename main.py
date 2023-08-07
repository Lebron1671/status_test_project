from Solutions.DictStore import DictStore
from Solutions.TreeStore import TreeStore

if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    data_store_objects = [DictStore(items), TreeStore(items)]

    for i in range(2):
        print(f"Work of {type(data_store_objects[i])}")
        print("getAll method work")
        print(data_store_objects[i].getAll()) # Return -> [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
        print("getItem method work")
        print(data_store_objects[i].getItem(7)) # Return -> {"id":7,"parent":4,"type":None}
        print("getChildren method work")
        print(data_store_objects[i].getChildren(1)) # Return -> [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]
        print("getChildren method work")
        print(data_store_objects[i].getChildren(5)) # Return -> []
        print("getAllParents method work")
        print(data_store_objects[i].getAllParents(7)) # Return -> [{'id': 7, 'parent': 4, 'type': None},{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]
        print("")
