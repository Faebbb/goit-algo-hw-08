"""Завдання 2. Сума значень у двійковому дереві пошуку."""

from bst import Node, build_bst


def sum_values(root: Node | None) -> int:
    """Повертає суму значень усіх вузлів. Для порожнього дерева сума дорівнює 0."""
    if root is None:
        return 0

    total = 0
    stack = [root]
    while stack:
        node = stack.pop()
        total += node.value
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return total


if __name__ == "__main__":
    values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
    print(f"Сума значень у дереві {values} — {sum_values(build_bst(values))}")
