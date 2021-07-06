# Как будет выглядеть список после выполнения последовательности операций?
# Найдите размер списка

from node import Node
from linkedList import LinkedList

LL = LinkedList()

LL.pushright(1)
LL.pushleft(2)
LL.pushright(3)
LL.popright()
LL.pushleft(4)
LL.pushright(5)
LL.popleft()

print(LL)

print(LL.__len__())