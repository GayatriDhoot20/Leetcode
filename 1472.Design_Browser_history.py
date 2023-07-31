class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.cur = ListNode(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
obj = BrowserHistory("leetcode.com")
obj.visit("google.com")
obj.visit("facebook.com")
obj.visit("youtube.com")
print(obj.back(1))
print(obj.back(1))
print(obj.forward(1))
obj.visit("linkedin.com")
print(obj.forward(2))
print(obj.back(2))
print(obj.back(7))
