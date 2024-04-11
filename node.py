from __future__ import annotations
from typing import TypeVar, Generic

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, data: T):
        self.data = data
        self.left: Node[T] | None = None
        self.right: Node[T] | None = None

    def is_leaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        return str(self.data)
