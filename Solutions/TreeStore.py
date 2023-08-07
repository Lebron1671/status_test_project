from collections import deque

from Solutions.IDataStore import IDataStore


class Node:
    def __init__(self, id: int, parent=None, type=None):
        self.id = id
        self.parent = parent
        self.type = type
        self.children = []


class TreeStore(IDataStore):
    def __init__(self, data: list):
        self.data = self._build_tree(data)

    def getAll(self):
        result = []
        queue = deque([self.data])

        while queue:
            current_node = queue.popleft()
            result.append({"id": current_node.id, "parent": current_node.parent}) if current_node.parent == 'root' \
                else result.append({"id": current_node.id, "parent": current_node.parent, "type": current_node.type})
            queue.extend(current_node.children)

        return result

    def getItem(self, id: int):
        node = self._findItem(id)
        if node is None:
            raise ValueError(f'Element with id {id} does not exist in TreeStore')
        return {'id': node.id, 'parent': node.parent} if node.parent == 'root' \
            else {'id': node.id, 'parent': node.parent, 'type': node.type}

    def getChildren(self, id: int):
        node = self._findItem(id)
        if node is None:
            raise ValueError(f'Element with id {id} does not exist in TreeStore')
        return self._get_all_children(node)

    def getAllParents(self, id: int):
        node = self._findItem(id)
        if node is None:
            raise ValueError(f'Element with id {id} does not exist in TreeStore')
        return self._get_all_parents(node)

    def _build_tree(self, items: list):
        nodes = {}
        root = None

        for item in items:
            node = Node(item["id"], parent=item.get("parent"), type=item.get("type"))
            nodes[node.id] = node

            if node.parent == 'root':
                root = node
            else:
                parent_node = nodes.get(node.parent)
                if parent_node:
                    parent_node.children.append(node)

        return root

    def _findItem(self, id: int):
        return self._find_item_recursive(self.data, id)

    def _find_item_recursive(self, current_node: Node, id: int):
        if current_node.id == id:
            return current_node

        for child in current_node.children:
            result = self._find_item_recursive(child, id)
            if result:
                return result

        return None

    def _get_all_children(self, current_node: Node):
        children = []

        for child in current_node.children:
            children.append({'id': child.id, 'parent': child.parent, 'type': child.type})
            children.extend(self._get_all_children(child))

        return children

    def _get_all_parents(self, current_node: Node):
        parents = []
        while current_node:
            parents.append({"id": current_node.id, "parent": current_node.parent}) if current_node.parent == 'root' \
                else parents.append({"id": current_node.id, "parent": current_node.parent, "type": current_node.type})
            current_node = self._findItem(current_node.parent)

        return parents
