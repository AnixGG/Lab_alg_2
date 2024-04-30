import time


class Node:
    def __init__(self):
        self.left_child = None
        self.right_child = None
        self.count_rect = 0
        self.right_boundary_index = 0
        self.left_boundary_index = 0

    def copy(self):
        new_node = Node()
        new_node.right_boundary_index = self.right_boundary_index
        new_node.left_boundary_index = self.left_boundary_index
        new_node.count_rect = self.count_rect
        return new_node

    def copy_with_children(self):
        new_node = self.copy()
        new_node.left_child = self.left_child
        new_node.right_child = self.right_child
        return new_node


class Tree:
    ind_leaves = 0
    y_cords = []

    @classmethod
    def set_data(cls, y_cords):
        cls.y_cords = y_cords.copy()

    @classmethod
    def create_tree(cls, count_leaves, k=1):
        if count_leaves * 2 - 1 < k:
            return
        root = Node()
        left_child = Tree.create_tree(count_leaves, k * 2)
        right_child = Tree.create_tree(count_leaves, k * 2)
        root.left_child = left_child
        root.right_child = right_child
        if right_child is None:
            root.left_boundary_index = Tree.ind_leaves
            root.right_boundary_index = Tree.ind_leaves + 1
            Tree.ind_leaves += 1
            return root
        root.right_boundary_index = Tree.ind_leaves
        root.left_boundary_index = left_child.left_boundary_index
        root.right_boundary_index = right_child.right_boundary_index
        return root

    @classmethod
    def update(cls, root, v_l, v_r, diff):
        if root.left_boundary_index >= len(cls.y_cords):
            return root
        if v_l <= cls.y_cords[root.left_boundary_index] and root.right_boundary_index < len(cls.y_cords) and \
                cls.y_cords[root.right_boundary_index] <= v_r:
            new_node = root.copy_with_children()
            new_node.count_rect += diff
            return new_node
        if root.right_boundary_index < len(cls.y_cords) and v_l >= cls.y_cords[root.right_boundary_index]:
            return root
        if v_r <= cls.y_cords[root.left_boundary_index]:
            return root
        new_node = root.copy()
        new_node.left_child = cls.update(root.left_child, v_l, v_r, diff)
        new_node.right_child = cls.update(root.right_child, v_l, v_r, diff)
        return new_node


def tree_alg():
    rect_file = "data/rects_session.txt"
    points_file = "data/points_session.txt"
    x_changes_y = []
    x_cords = set()
    y_cords = set()
    n = 0  # на вход не поддается количество прямоугольников - считаю сам
    start_time_prep = time.time()
    with open(rect_file) as f:
        for line in f:
            x1, y1, x2, y2 = tuple(map(int, line.split()))
            x_cords.add(x1)
            x_cords.add(x2)
            y_cords.add(y1)
            y_cords.add(y2)
            x_changes_y.append((x1, y1, y2, 1))
            x_changes_y.append((x2, y1, y2, -1))
            n += 1
    x_cords = sorted(list(x_cords))
    y_cords = sorted(list(y_cords))
    x_changes_y = sorted(x_changes_y)
    trees = []
    Tree.set_data(y_cords)
    tree = Tree.create_tree(len(y_cords))
    last_change = None
    if n != 0:
        last_change = x_changes_y[0][0]
    for change in x_changes_y:
        if last_change != change[0]:
            trees.append(tree)
        tree = Tree.update(tree, change[1], change[2], change[3])
        last_change = change[0]
    trees.append(tree)
    end_time_prep = time.time()

    answ = []

    start_time_alg = time.time()
    with open(points_file) as f:
        for line in f:
            x, y = map(float, line.split())
            counter = 0
            if n == 0 or x >= x_cords[-1] or y >= y_cords[-1] or x < x_cords[0] or y < y_cords[0]:
                answ.append(0)
                continue
            l_ = 0
            r_ = len(x_cords)
            while l_ < r_:
                m_ = (l_ + r_) // 2
                if x_cords[m_] < x:
                    l_ = m_ + 1
                elif x_cords[m_] == x:
                    l_ = m_ + 1
                    break
                else:
                    r_ = m_
            x_ind = l_ - 1

            l_ = 0
            r_ = len(y_cords)
            while l_ < r_:
                m_ = (l_ + r_) // 2
                if y_cords[m_] < y:
                    l_ = m_ + 1
                elif y_cords[m_] == y:
                    l_ = m_ + 1
                    break
                else:
                    r_ = m_
            y_ind = l_ - 1

            root = trees[x_ind]
            while root.right_child and root.left_child:
                counter += root.count_rect
                if y_ind < root.left_child.right_boundary_index:
                    root = root.left_child
                else:
                    root = root.right_child
            counter += root.count_rect
            answ.append(counter)
    end_time_alg = time.time()
    # print(*answ)
    return end_time_prep - start_time_prep, end_time_alg - start_time_alg
