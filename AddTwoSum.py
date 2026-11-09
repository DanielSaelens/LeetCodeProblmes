class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoSum(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    carry = 0
    head = None

    while l1 is not None or l2 is not None or carry != 0:
        if l1 is None:
            val_1 = 0
        else:
            val_1 = l1.val
            l1 = l1.next

        if l2 is None:
            val_2 = 0
        else:
            val_2 = l2.val
            l2 = l2.next

        total = val_1 + val_2 + carry
        carry = total // 10
        mod = total % 10
        new_node = ListNode(mod)

        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = current.next

    return head


def build_linked_list(values: list[int]) -> ListNode | None:
    head = None
    for v in values:
        new_node = ListNode(v)
        if head is None:
            head = new_node
            current = head
        else:
            current.next = new_node
            current = current.next
    return head


def to_list(head: ListNode | None) -> list[int]:
    values = []
    current = head
    while current is not None:
        values.append(current.val)
        current = current.next
    return values


if __name__ == "__main__":
    l1 = build_linked_list([9, 9, 9, 9, 9, 9, 9])
    l2 = build_linked_list([9, 9, 9, 9])
    result = addTwoSum(l1, l2)
    print(to_list(result))  