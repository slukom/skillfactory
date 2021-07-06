class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.left_child = self.left_child
            self.left_child = new_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BinaryTree(next_value)
        else:
            new_child = BinaryTree(next_value)
            new_child.right_child = self.right_child
            self.right_child = new_child
        return self

    def pre_order(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию

    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки


    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию