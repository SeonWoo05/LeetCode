# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        # 두 포인터를 각각 headA와 headB로 설정
        pointerA = headA
        pointerB = headB
        
        # 두 포인터가 서로 만나기 전까지 순회
        while pointerA != pointerB:
            # pointerA가 끝에 도달하면 headB로 이동
            pointerA = pointerA.next if pointerA else headB
            # pointerB가 끝에 도달하면 headA로 이동
            pointerB = pointerB.next if pointerB else headA
        
        # pointerA와 pointerB가 만나는 노드를 반환 (교차점)
        # 또는 교차점이 없으면 None이 반환
        return pointerA