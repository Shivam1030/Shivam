class Node:
    def __init__(self, data):
        self.data=data
        self.next=None
head=Node(1)
head.next=Node(2)
head.next.next=Node(3)
head.next.next.next=Node(4)
head.next.next.next.next=Node(5)
head.next.next.next.next.next=Node(6)
head.next.next.next.next.next.next=Node(7)

prev=None
curr=head

while curr:
    temp=curr.next
    curr.next=prev
    prev=curr
    curr=temp

head=prev

while head:
    print(head.data, end=" -> ")
    head=head.next