from collections import deque
from inorder_traversal import Solution as InorderTraversal

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def form_tree_from_list(A):
     
    root = TreeNode(A[0])

    Q = deque([root])

    i = 1
    k = len(A)

    while Q:
        temp_Q = deque()
        while Q:
            x = Q.popleft()
            if i >= k: break
            if A[i] is not None:
                x.left = TreeNode(A[i])
                temp_Q.append(x.left)
            i += 1
            if i>=k: break
            if A[i] is not None:
                x.right = TreeNode(A[i])
                temp_Q.append(x.right)
            i += 1
        Q = temp_Q
    
    return root




if __name__ == '__main__':

    print("Checking Inorder Traversal.......")
    test_cases = [[1,None,2,3], [1,3,4,5,None,2,3]]
    results = [[1,3,2], [5,3,1,2,4,3]]
    obj = InorderTraversal()

    for i in range(len(test_cases)):
        root = form_tree_from_list(test_cases[i])
        if obj.inorderTraversal(root) == results[i]:
            print("Test case {} passed".format(i+1))
        else:
            print("Test case {} failed".format(i+1))
