class Node:
    def __init__(self, L, R, n):
        self.left = L
        self.right = R
        self.value = n

def tree_by_levels(node):
    final=[]
    queue=[node]
    while queue:
        node=queue.pop(0)
        if not node:
            return []
        final.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return final
