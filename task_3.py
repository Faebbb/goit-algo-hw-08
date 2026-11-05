"""Завдання 3. З'єднання кабелів із мінімальними витратами."""

from collections.abc import Iterable
from heapq import heapify, heappop, heappush


def min_connection_cost(
    lengths: Iterable[int],
) -> tuple[int, list[tuple[int, int, int]]]:
    """Повертає мінімальні витрати та кроки (перша, друга, об'єднана довжина)."""
    heap = list(lengths)
    if any(length < 0 for length in heap):
        raise ValueError("Довжини кабелів мають бути невід’ємними")
    heapify(heap)

    total_cost = 0
    merges = []
    while len(heap) > 1:
        first = heappop(heap)
        second = heappop(heap)
        merged = first + second
        total_cost += merged
        merges.append((first, second, merged))
        heappush(heap, merged)

    return total_cost, merges


if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    total_cost, merges = min_connection_cost(cables)
    print(f"Довжини кабелів — {cables}")
    for step, (first, second, merged) in enumerate(merges, start=1):
        print(f"Крок {step}. {first} + {second} = {merged}")
    print(f"Мінімальні загальні витрати — {total_cost}")
