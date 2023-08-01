from TreeStore import TreeStore

if __name__ == '__main__':
    pass
    # Create data
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

    # Create TreeStore
    ts = TreeStore(items)

    # Example # 1
    print(ts.getAll()) # Return -> [{"id":1,"parent":"root"},{"id":2,"parent":1,"type":"test"},{"id":3,"parent":1,"type":"test"},{"id":4,"parent":2,"type":"test"},{"id":5,"parent":2,"type":"test"},{"id":6,"parent":2,"type":"test"},{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]

    # Example # 2
    print(ts.getItem(7)) # Return -> {"id":7,"parent":4,"type":None}

    # Example # 3
    print(ts.getChildren(4)) # Return -> [{"id":7,"parent":4,"type":None},{"id":8,"parent":4,"type":None}]

    # Example # 4
    print(ts.getChildren(5)) # Return -> []

    # Example # 5
    print(ts.getAllParents(7)) # Return -> [{'id': 7, 'parent': 4, 'type': None},{"id":4,"parent":2,"type":"test"},{"id":2,"parent":1,"type":"test"},{"id":1,"parent":"root"}]
