# Реализуйте структуру дерева при помощи класса BinaryTree.

from binaryTree import BinaryTree

node_root = BinaryTree('2').insert_left('7').insert_right('5')
node_7 = node_root.left_child.insert_left('3').insert_right('6')
node_6 = node_7.right_child.insert_left('8').insert_right('11')

node_5 = node_root.right_child.insert_right('9')
node_9 = node_5.right_child.insert_left('4')

print('per_order')
node_root.pre_order()

# Для рассматриваемого примера напишите значения узлов (через запятую и пробел) в порядке постфиксного обхода
print('post_order')
node_root.post_order()


print('in_order')
node_root.in_order()
