#Problem statement: You have a browser of one tab where you start on the homepage and you can visit another url,
#get back in the history number of steps or move forward in the history number of steps.

#The following implementation is using doubly linked lists.
class BrowserHistory:
    class Node:
        def __init__(self, val):
            self.val = val
            self.next = None
            self.prev = None

    def __init__(self, homepage: str):
        self.curr = self.Node(homepage)

    def visit(self, url: str) -> None:
        temp = self.Node(url)
        temp.prev = self.curr
        self.curr.next = temp
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.curr.prev:
            steps -= 1
            self.curr = self.curr.prev
        return self.curr.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.curr.next != None:
            steps -= 1
            self.curr = self.curr.next
        return self.curr.val
    
#The following implementation is using list(array). Next time implement it using self.len and not self.end
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.curr = 0
        self.end = 0

    def visit(self, url: str) -> None:
        if self.curr == self.end:
            if self.end == len(self.history) - 1:
                self.history.append(url)
                self.curr += 1
                self.end += 1
            else:
                self.curr += 1
                self.end += 1
                self.history[self.curr] = url
        else:
            self.curr += 1
            self.end = self.curr
            self.history[self.curr] = url
                
    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps, 0)
        return self.history[self.curr]

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps, self.end)
        return self.history[self.curr]