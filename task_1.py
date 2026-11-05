"""Завдання 1. Мінімум у двійковому дереві пошуку."""

from bst import Node, build_bst


def find_min(root: Node | None) -> int | None:
    """Повертає найменше значення або None для порожнього дерева."""
    if root is None:
        return None

    node = root
    while node.left is not None:
        node = node.left
    return node.value


if __name__ == "__main__":
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    print(f"Найменше значення в дереві {values} — {find_min(build_bst(values))}")
