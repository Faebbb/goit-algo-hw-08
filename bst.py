"""Двійкове дерево пошуку для завдань 1 і 2."""

from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None


def insert(root: Node | None, value: int) -> Node:
    """Додає вузол і повертає корінь дерева. Дублікати йдуть праворуч."""
    if root is None:
        return Node(value)

    node = root
    while True:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
                return root
            node = node.left
        else:
            if node.right is None:
                node.right = Node(value)
                return root
            node = node.right


def build_bst(values: Iterable[int]) -> Node | None:
    """Будує дерево, вставляючи значення в заданому порядку."""
    root = None
    for value in values:
        root = insert(root, value)
    return root
