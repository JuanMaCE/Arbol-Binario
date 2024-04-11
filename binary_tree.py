from typing import Optional, TypeVar
from node import Node

T = TypeVar('T')


class BinaryTree:
    def __init__(self, data: T):
        self.__root: Node[T] | None = Node(data)

    def insert_left(self, data: T, ref: T):
        node = self.__search(ref)
        if node is not None:
            new_node = Node(data)
            if node.left is None:
                node.left = new_node
            else:
                raise Exception("The left side isn't empty")
        else:
            raise Exception("The reference doesn't exist")

    def insert_right(self, data: T, ref: T):
        node = self.__search(ref)
        if node is not None:
            new_node = Node(data)
            if node.right is None:
                node.right = new_node
            else:
                raise Exception("The right side isn't empty")
        else:
            raise Exception("The reference doesn't exist")

    def depth(self, ref: T, *args) -> int:
        node = self.__root if len(args) == 0 else args[0]
        if node is None:
            return -1
        elif node.data == ref:
            return 0
        else:
            # Retornar a 27
            left = self.depth(ref, node.left)
            right = self.depth(ref, node.right)
            if left == -1 and right == -1:
                # No existe en ningún lado
                return -1
            else:
                # Existe en algún lado
                return max(left, right) + 1

    def __search(self, ref: T, *args) -> Optional[Node]:
        node = self.__root if len(args) == 0 else args[0]
        if node is not None:
            if node.data == ref:
                return node
            else:
                result = self.__search(ref, node.left)
                if result is None:
                    result = self.__search(ref, node.right)
                    return result
                else:
                    return result
        else:
            return None

    def height(self, *args):
        node = self.__root if len(args) == 0 else args[0]
        if node is None:
            return 0
        else:
            altura = max(self.height(node.left), self.height(node.right)) + 1
            return altura
