from Solutions.IDataStore import IDataStore


class DictStore(IDataStore):
    def __init__(self, data):
        self.data = {node.get('id'): node for node in data}

    def getAll(self) -> list:
        """
            Return the original array of elements.

            :return: list of dict, a list of dictionaries representing the element objects.
        """
        return list(self.data.values())

    def getItem(self, id: int) -> dict:
        """
            Accepts the element id and returns the element object itself.

            :param id: int, the unique identifier of the element to be retrieved.
            :return: dict, the dictionary representing the element object
            :raises ValueError: If the element with the given id does not exist in the TreeStore.
        """
        if id in self.data:
            return self.data.get(id)
        else:
            raise ValueError(f'Element with id {id} does not exist in DictStore')

    def getChildren(self, id: int):
        """
            Accepts the element id and returns an array of elements that are children of this element,
            whose id is received in the argument. If the element has no children, then an empty array should
            be returned

            :param id: int, the unique identifier of the element whose children are to be retrieved.
            :return: list of dict, a list of dictionaries representing the element objects.
            :raises ValueError: If the element with the given id does not exist in the TreeStore.
        """
        if id in self.data:
            children = []

            for node in self.data.values():
                if node.get('parent') == id:
                    children.append(node)
                    children.extend(self.getChildren(node.get('id')))
            return children
        else:
            raise ValueError(f'Element with id {id} does not exist in DictStore')

    def getAllParents(self, id: int):
        """
            Takes the id of the element and returns an array from the chain of parent elements, starting
            from the element itself, whose id was passed in the argument and up to the root element,
            i.e. the path of the element to the top of the tree through the chain of parents to the root
            of the tree should be obtained.

            :param id: int, the unique identifier of the element whose chain of parent elements is to be retrieved.
            :return: list of dict, a list of dictionaries representing the element objects forming the chain of parents.
            :raises ValueError: If the element with the given id does not exist in the TreeStore.
        """
        if id in self.data:
            itself_and_parents = []

            for node in self.data.values():
                if node.get('id') == id:
                    itself_and_parents.append(node)
                    if node.get('parent') != 'root':
                        itself_and_parents.extend(self.getAllParents(node.get('parent')))
                    else:
                        break
            return itself_and_parents
        else:
            raise ValueError(f'Element with id {id} does not exist in DictStore')
