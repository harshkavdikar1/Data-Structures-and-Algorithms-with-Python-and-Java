from collections import deque
from inorder_traversal_LC94 import Solution as LC94
from validate_bst_LC98 import Solution as LC98
from same_tree_LC100 import Solution as LC100


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def form_binary_tree_from_list(A):

    root = TreeNode(A[0])

    Q = deque([root])

    i = 1
    k = len(A)

    while Q:
        temp_Q = deque()
        while Q:
            x = Q.popleft()
            if i >= k:
                break
            if A[i] is not None:
                x.left = TreeNode(A[i])
                temp_Q.append(x.left)
            i += 1
            if i >= k:
                break
            if A[i] is not None:
                x.right = TreeNode(A[i])
                temp_Q.append(x.right)
            i += 1
        Q = temp_Q

    return root


def insert_into_bst(root, x):
    if x > root.val:
        if root.right is not None:
            insert_into_bst(root.right, x)
        else:
            root.right = TreeNode(x)
    else:
        if root.left is not None:
            insert_into_bst(root.left, x)
        else:
            root.left = TreeNode(x)


def form_binary_search_tree_from_list(A):

    root = TreeNode(A[0])

    for x in A[1:]:
        insert_into_bst(root, x)

    return root


if __name__ == '__main__':

    print("Checking Inorder Traversal.......")
    test_cases = [[1, None, 2, 3], [1, 3, 4, 5, None, 2, 3]]
    results = [[1, 3, 2], [5, 3, 1, 2, 4, 3]]
    obj = LC94()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.inorderTraversal(root) == results[i]:
            print("Test case {} passed".format(i+1))
        else:
            print("Test case {} failed".format(i+1))

    print("Validating Binary Search Tree.......")
    test_cases = [[10, 5, 15, None, None, 6, 20], [3, 1, 5, 0, 2, 4, 6]]
    results = [False, True]
    obj = LC98()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.isValidBST(root) == results[i]:
            print("Test case {} passed".format(i+1))
        else:
            print("Test case {} failed".format(i+1))

    print("Checking Same Tree Algo.......")
    test_cases = [[[1, 2, 3], [1, 2, 3]],
                  [[1, 2, 1], [1, 1, 2]]]
    results = [True, False]
    obj = LC100()

    for i in range(len(test_cases)):
        root1 = form_binary_tree_from_list(test_cases[i][0])
        root2 = form_binary_tree_from_list(test_cases[i][1])
        if obj.isSameTree(root1, root2) == results[i]:
            print("Test case {} passed".format(i+1))
        else:
            print("Test case {} failed".format(i+1))
