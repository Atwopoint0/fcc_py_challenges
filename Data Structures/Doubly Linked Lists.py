class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

def forward_traverse(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next

def backward_traverse(tail):
    current = tail
    while current is not None:
        print(current.data, end=" ")
        current = current.prev

def forward_search(head, target):
    while head is not None:
        if head.data == target:
            return head
        head = head.next
    return "Target not found"

def backward_search(tail, target):
    while tail is not None:
        if tail.data == target:
            return tail
        tail = tail.prev
    return "Target not found"

def length(head):
    count = 0
    current = head
    while current is not None:
        count += 1
        current = current.next
    return count

def insert_at_start(head, data):
    new_node = Node(data)
    new_node.next = head
    if head is not None:
        head.prev = new_node
    return new_node

def insert_at_end(head, data):
    new_node = Node(data)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
    return head

def insert_at_position(head, pos, new_data):
    new_node = Node(new_data)
    if pos == 1:
        new_node.next = head
        if head is not None:
            head.prev = new_node
        head = new_node
        return head
    
    curr = head
    for _ in range(1, pos - 1):
        if curr is None:
            print("Position is out of bounds.")
            return head
        curr = curr.next

    if curr is None:
        print("Position is out of bounds.")
        return head

    new_node.prev = curr
    new_node.next = curr.next
    curr.next = new_node
    if new_node.next is not None:
        new_node.next.prev = new_node
    return head

def delete_at_start(head):
    if head is None:
        return None
    temp = head
    head = head.next
    if head is not None:
        head.prev = None
    return head

def del_last(head):
    if not head or not head.next:
        return None
    curr = head
    while curr.next is not None:
        curr = curr.next
    if curr.prev is not None:
        curr.prev.next = None
    return head

def del_pos(head, pos):
    if head is None:
        return head

    curr = head
    for i in range(1, pos):
        if curr is None:
            return head

        curr = curr.next
    if curr is None:
        return head
    if curr.prev is not None:
        curr.prev.next = curr.next
    if curr.next is not None:
        curr.next.prev = curr.prev
    if head == curr:
        head = curr.next
    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next