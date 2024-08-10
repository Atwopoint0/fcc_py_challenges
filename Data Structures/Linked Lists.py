class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def trasversal(head):
    current = head
    while current is not None:
        print(current.data)
        current = current.next

def search(head, target):
    while head is not None:
        if head.data == target:
            return head
        head = head.next
    return "Target not found"

def length(head):
    current = head
    length = 0
    while current is not None:
        length += 1
        current = current.next
    return length

def insert_at_start(head, value):
    new_node = Node(value)
    new_node.next = head
    head = new_node
    return head

def insert_at_end(head, value):
    new_node = Node(value)
    if head is None:
        return new_node
    current = head
    while current is not None:
        current = current.next
    current.next = new_node
    return head

def insert_at_position(head, position, value):
    if position == 1:
        insert_at_start(head, value)
    current = head
    for _ in range(1, position - 1):
        if current is None:
            break
        current = current.next
    if current is None:
        return head
    new_node = Node(value)
    new_node.next = current.next
    current.next = new_node
    return head

def delete_at_start(head):
    if not head:
        return None
    temp = head
    head = head.next
    temp = None
    return head

def delete_at_end(head):
    if not head or not head.next:
        return None
    second_last = head
    while second_last.next.next:
        second_last = second_last.next
    second_last.next = None
    return head

def print_list(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")

def deleteNode(head, position):
    if head is None or position < 1:
        return head
    if position == 1:
        delete_at_start(head)

    current = head
    for i in range(1, position - 1):
        if current is not None:
            current = current.next

    if current is None or current.next is None:
        return head
    temp = current.next
    current.next = current.next.next
    temp = None
    return head