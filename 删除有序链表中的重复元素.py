# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
# 示例 1:
#
# 输入: 1->1->2
# 输出: 1->2
# 示例 2:
#
# 输入: 1->1->2->3->3
# 输出: 1->2->3


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        cur = head
        while cur != None and cur.next != None:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
class Solution:
    def maxSubArray(self, nums):
        sum = 0  # 阶段性和
        max_sub_sum = nums[0]  # 最终结果
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0
        return max_sub_sum
