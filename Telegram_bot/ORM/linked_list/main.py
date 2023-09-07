a = range(1, 6)


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


head = Node(0)
tmp = head
for i in a:
    tmp.next = Node(i)
    tmp = tmp.next

# node1 = Node(1)
# node2 = Node(2)
# node3 = Node(3)
# node4 = Node(4)
# node5 = Node(5)
#
# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

tmp = head.next
while tmp:
    print(tmp.val)
    if not tmp.next:
        break
    tmp = tmp.next.next

