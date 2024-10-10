#!/usr/bin/python3
'''
Determines if all the boxes can be opened
'''


def canUnlockAll(boxes):
    '''Checks if all the boxes in a list of boxes containing the keys
    (indices) to other boxes can be unlocked given that the first
    box is unlocked.

    Args:
    - boxes: Each box is represented as a list of positive integers.
      A key with the same number as a box opens that box.

    Returns:
    - bool: True if all boxes can be opened, False otherwise.
    '''
    total_boxes = len(boxes)

    # Initialize seen_boxes with the first box
    visited_boxes = set([0])

    # Initialize unvisited_boxes with keys from the first box excluding 0
    unvisited_boxes = set(boxes[0]).difference(set([0]))

    # Explore the boxes
    while len(unvisited_boxes) > 0:
        current_box = unvisited_boxes.pop()

        # Skip invalid box indices
        if not (0 <= current_box < total_boxes):
            continue

        # Add unvisited boxes to the set and mark the current box as visited
        if current_box not in visited_boxes:
            unvisited_boxes = unvisited_boxes.union(boxes[current_box])
            visited_boxes.add(current_box)

    # Check if all boxes are visited
    return total_boxes == len(visited_boxes)
