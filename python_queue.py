from collections import deque

def queu_demo():
    q = deque()
    q.append(3)
    q.append(4)
    q.append(5)
    print(q)
    print(q[0])
    print(q[-1])
    print(q.popleft())
    print(q.pop())
    print(q)

    q.appendleft(10)
    print(q)

    print(q.popleft())

    print(q.pop())
def list_demo():
    l = [1,2,3,4,5,6]
    l2 = [1,2]
    print(l.append(l2))
    print(l)
if __name__ == '__main__':
    list_demo()