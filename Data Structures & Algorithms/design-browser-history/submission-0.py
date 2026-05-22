class ListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.currIndex = 0

    def visit(self, url: str) -> None:
        self.history = self.history[:self.currIndex + 1]

        self.history.append(url)

        self.currIndex += 1

    def back(self, steps: int) -> str:
        self.currIndex = max(0, self.currIndex - steps)

        return self.history[self.currIndex]

    def forward(self, steps: int) -> str:
        self.currIndex = min(len(self.history) - 1, self.currIndex + steps)

        return self.history[self.currIndex]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)