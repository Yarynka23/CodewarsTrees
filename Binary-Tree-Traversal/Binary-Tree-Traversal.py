class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right

# Pre-order traversal
def pre_order(node):
    final=[]
    if node:
        final.append(node.data)
        final.extend(pre_order(node.left))
        final.extend(pre_order(node.right))
    else:
        return []
    return final

# In-order traversal
def in_order(node):
    final=[]
    if node:
        final.extend(in_order(node.left))
        final.append(node.data)
        final.extend(in_order(node.right))
    else:
        return []
    return final

# Post-order traversal
def post_order(node):
    final=[]
    if node:
        final.extend(post_order(node.left))
        final.extend(post_order(node.right))
        final.append(node.data)
    else:
        return []
    return final
