n = int(input())
node = {}

for _ in range(n):
    key, value1, value2 = map(str, input().split())
    node[key] = (value1, value2)
# print(node)

def preorder(nd):
    print(nd, end='')
    if node[nd][0] != '.':
        preorder(node[nd][0])
    if node[nd][1] != '.':
        preorder(node[nd][1])

def inorder(nd):
    if node[nd][0] != '.':
        inorder(node[nd][0])
    print(nd, end='')
    if node[nd][1] != '.':
        inorder(node[nd][1])

def postorder(nd):
    if node[nd][0] != '.':
        postorder(node[nd][0])
    if node[nd][1] != '.':
        postorder(node[nd][1])
    print(nd, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')