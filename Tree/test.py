'''
@author: Harsh
'''
from collections import deque


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def form_binary_tree_from_list(A):

    if not A:
        return None

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

    if not A: return None
    root = TreeNode(A[0])
    for x in A[1:]:
        insert_into_bst(root, x)
    return root


def passed(index):
    print("Test case {} passed".format(index))


def failed(index):
    print("Test case {} failed".format(index))


def test_LC94():

    from inorder_traversal_LC94 import Solution
    print("Checking Inorder Traversal of Binary Tree.......")
    test_cases = [[1, None, 2, 3], [1, 3, 4, 5, None, 2, 3]]
    results = [[1, 3, 2], [5, 3, 1, 2, 4, 3]]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.inorderTraversal(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC98():

    from validate_bst_LC98 import Solution
    print("Validating Binary Search Binary Tree.......")
    test_cases = [[10, 5, 15, None, None, 6, 20], [3, 1, 5, 0, 2, 4, 6]]
    results = [False, True]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.isValidBST(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC99():

    from recover_binary_tree_LC99 import Solution
    from inorder_traversal_LC94 import Solution as IT
    print("Validating recovered Binary Tree.......")
    test_cases = [[1,3,None,None,2], [3,1,4,None,None,2]]
    results = [[3,1,None,None,2], [2,1,4,None,None,3]]
    obj = Solution()
    obj2 = IT()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        test = form_binary_tree_from_list(results[i])
        if obj2.inorderTraversal(obj.recoverTree(root)) == obj2.inorderTraversal(test):
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC100():

    from same_tree_LC100 import Solution
    print("Checking Same Binary Tree Algo.......")
    test_cases = [[[1, 2, 3], [1, 2, 3]],
                  [[1, 2, 1], [1, 1, 2]]]
    results = [True, False]
    obj = Solution()

    for i in range(len(test_cases)):
        root1 = form_binary_tree_from_list(test_cases[i][0])
        root2 = form_binary_tree_from_list(test_cases[i][1])
        if obj.isSameTree(root1, root2) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC101():

    from symmetric_tree_LC101 import Solution
    print("Validating Symmetric Binary Tree.......")
    test_cases = [[1, 2, 2, 3, 4, 4, 3], [1, 2, 2, None, 3, None, 3]]
    results = [True, False]
    obj = Solution()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.isSymmetric(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC102():

    from level_order_traversal_LC102 import Solution
    print("Validating Level Order Traversal of Binary Tree.......")
    test_cases = [[3, 9, 20, None, None, 15, 7], [
        3, 9, None, 20, None, None, 15, 7, 28, 19, None]]
    results = [[[3], [9, 20], [15, 7]], [[3], [9], [20], [15], [7, 28], [19]]]
    obj = Solution()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.levelOrder(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC103():

    from zigzag_level_order_traversal_LC103 import Solution
    print("Validating ZigZag Level Order Traversal of Binary Tree.......")
    test_cases = [[3, 9, 20, None, None, 15, 7, None, None, 6, 90], [
        3, 9, 20, None, None, 15, 7, 2, 3, 4, 5, 6, 7, 8, 9]]
    results = [[[3], [20, 9], [15, 7], [90, 6]], [
        [3], [20, 9], [15, 7], [5, 4, 3, 2], [6, 7, 8, 9]]]
    obj = Solution()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.zigzagLevelOrder(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC104():

    from max_depth_LC104 import Solution
    print("Validating Max Depth of Binary Tree.......")
    test_cases = [[3, 9, 20, None, None, 15, 7, None, None, 6, 90], [
        3, 9, 20, None, None, 15, 7, 2, 3, 4, 5, 6, 7, 8, 9]]
    results = [4, 5]
    obj = Solution()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.maxDepth(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC110():

    from balanced_tree_LC110 import Solution
    print("Validating if Binary Tree is Balanced.......")
    test_cases = [[3, 9, 20, None, None, 15, 7], [
        3, 9, 20, None, None, 15, 7, 2, 3, 4, 5, 6, 7, 8, 9]]
    results = [True, False]
    obj = Solution()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.isBalanced(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC112():

    from path_sum_LC112 import Solution
    print("Validating if Binary Tree has Path Sum.......")
    test_cases = [[[1, 2], 1], [
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22]]
    results = [False, True]
    obj = Solution()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i][0])
        if obj.hasPathSum(root, test_cases[i][1]) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC113():

    from path_sum2_LC113 import Solution
    print("Validating Binary Tree Path Sums.......")
    test_cases = [[[0, 1, 1], 1], [
        [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1], 22]]
    results = [[[0, 1], [0, 1]], [[5, 4, 11, 2], [5, 8, 4, 5]]]
    obj = Solution()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i][0])
        if obj.pathSum(root, test_cases[i][1]) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC124():

    from binary_tree_max_path_LC124 import Solution
    print("Validating Binary Tree Path Sums.......")
    test_cases = [[1,2,3], [-10,9,20,None,None,15,7]]
    results = [6, 42]
    obj = Solution()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.maxPathSum(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC114():

    from flatten_binary_tree_to_linked_list_LC114 import Solution
    from inorder_traversal_LC94 import Solution as inorder_traversal
    print("Validating Flattened Binary Tree to Linked List.......")
    test_cases = [[1, 2, 5, 3, 4, None, 6, None, 4, 3, 6, 7, None, None, None, 8, 9, 10, 11],
                  [1, 2, None, 3, None, 4, None]]
    results = [[1, 2, 3, 4, 4, 3, 8, 9, 6, 10, 11, 5, 6, 7],
               [1, 2, 3, 4]]
    obj = Solution()
    obj2 = inorder_traversal()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        test_case = obj2.inorderTraversal(obj.flatten(root))
        if results[i] == test_case:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC144():

    from preorder_traversal_LC144 import Solution
    print("Checking Preorder Traversal of Binary Tree.......")
    test_cases = [[1, None, 2, 3, 4, None, 5, None, 6, 7, 4, 3, None, None, 9, 0],
                  [2, 4, 6, None, 5, None, 6, 7, 8, 9, 0]]
    results = [[1, 2, 3, 5, 7, 9, 4, 0, 4, 6, 3], [2, 4, 5, 7, 8, 6, 6, 9, 0]]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.preorderTraversal(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC145():

    from postorder_traversal_LC145 import Solution
    print("Checking Postorder Traversal of Binary Tree.......")
    test_cases = [[1, None, 2, 3, 4, None, 4, 7, 8, 9, None, None, 10, 11, None, 23],
                  [2, 4, 6, None, 5, None, 6, 7, 8, 9, 0]]
    results = [[23, 9, 4, 3, 10, 7, 11, 8, 4, 2, 1],
               [7, 8, 5, 4, 9, 0, 6, 6, 2]]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.postorderTraversal(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC199():

    from binary_tree_right_side_view_LC199 import Solution
    print("Checking Right Side View of Binary Tree.......")
    test_cases = [[1, 2, 3, None, 5, None, 4, 4, 5, None, None, 5, 6, None, None, 9],
                  [2, 4, 6, None, 5, None, 6, 7, 8, 9, 0, 11]]
    results = [[1, 3, 4, 5, 6, 9], [2, 6, 6, 0, 11]]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.rightSideView(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC222():

    from count_complete_tree_node_LC222 import Solution
    print("Checking count of complete nodes of Binary Tree.......")
    test_cases = [[1, 2, 3, 5, 4, 4, 5, 5, 6, 9], [],
                  [2, 4, 6, 5, 6, 7, 8, 9]]
    results = [10, 0, 8]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.countNodes(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC226():

    from invert_tree_LC226 import Solution
    from preorder_traversal_LC144 import Solution as preorder_traversal
    print("Checking Invert of Binary Tree.......")
    test_cases = [[4, 2, 7, 1, 3, 6, 9, None, None, 4, 3, None, 5, None, 9, 1, 2, 3], [],
                  [2, 4, 6, 5, 6, 7, 8, 9]]
    results = [[4, 7, 2, 9, 6, 3, 1, 9, None, 5, None, 3, 4, None, None, None, None, None, None, None, 3, 2, 1], None,
                [2, 6, 4, 8, 7, 6, 5, None, None, None, None, None, None, None, 9]]
    obj = Solution()
    obj2 = preorder_traversal()

    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        result = form_binary_tree_from_list(results[i])
        if obj2.preorderTraversal(obj.invertTree(root)) == obj2.preorderTraversal(result):
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC230():

    from kth_smallest_element_bst_LC230 import Solution
    print("Checking kth smallest elements in Binary Search Tree.......")
    test_cases = [[[3, 1, 4, None, 2], 2],
                 [[5, 3, 6, 2, 4, None, None, 1], 3]]
    results = [2, 3]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i][0])
        if obj.kthSmallest(root, test_cases[i][1]) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC236():

    from lowest_common_ancestor_LC236 import Solution
    print("Checking lowest common ancestor in Binary Search Tree.......")
    test_cases = [[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1],
                 [[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 6, 4]]
    results = [3, 5]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i][0])
        if obj.lowestCommonAncestor(root, test_cases[i][1], test_cases[i][2]).val == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC297():

    from serilize_deserialize_binary_tree_LC297 import Codec
    from inorder_traversal_LC94 import Solution
    print("Checking serialize deserialize value of Binary Tree.......")
    test_cases = [[1,2,3,None,None,4,5], [], [1], [1,None,2,None,3,4,5,3,None]]
    obj = Codec()
    obj2 = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        test = obj.serialize(root)
        if obj2.inorderTraversal(obj.deserialize(test)) == obj2.inorderTraversal(root):
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC508():

    from most_frequent_subtree_sum_LC508 import Solution
    print("Checking Completeness of Binary Tree.......")
    test_cases = [ 
                    [5,2,-3],
                    [5,2,-3,1,5,4,3,2,6,7,4,3,1,4,5,3,4],
                    [], [1]
                ]
    results = [[2, -3, 4], [4], None, [1]]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.findFrequentTreeSum(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC543():

    from diameter_binary_tree_LC543 import Solution
    print("Validating Diameter of Binary Tree.......")
    test_cases = [ 
                    [3, 5, 1, 6, 2, 0, 8, None , None, 7, 4],
                    [1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2],
                    [], [1]
                ]
    results = [5, 11, 0, 0]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.diameterOfBinaryTree(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC572():

    from is_sub_tree_LC572 import Solution
    print("Checking if one Binary Tree is subtee of another Binary Tree.......")
    test_cases = [ 
                    [[3,4,5,1,2], [4,1,2]],
                    [[1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2],
                    [1,None,1,None,1,None,1,None,1,None,1,2]]
                ]
    results = [True, True]
    obj = Solution()
    for i in range(len(test_cases)):
        root1 = form_binary_tree_from_list(test_cases[i][0])
        root2 = form_binary_tree_from_list(test_cases[i][1])
        if obj.isSubtree(root1, root2) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC814():

    from binary_tree_pruning_LC814 import Solution
    from inorder_traversal_LC94 import Solution as IT
    print("Checking Cameras in Binary Tree.......")
    test_cases = [ 
                    [1,1,0,1,1,0,1,0],
                    [1,0,1,0,0,0,1],
                    [1,None,0,0,1]
                ]
    results = [[1,1,0,1,1,None,1], [1,None,1,None,1], [1,None,0,None,1]]
    obj = Solution()
    obj2 = IT()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        test = form_binary_tree_from_list(results[i])
        if obj2.inorderTraversal(obj.pruneTree(root)) == obj2.inorderTraversal(test):
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC951():

    from flip_equivalent_binary_tree_LC951 import Solution
    print("Checking if one Binary Tree is subtee of another Binary Tree.......")
    test_cases = [ 
                    [   
                        [1,2,3,4,5,6,None,None,None,7,8],
                        [1,3,2,None,6,4,5,None,None,None,None,8,7]
                    ],
                    [   
                        [0,2,1,4,None,3,5,None,None,6,7],
                        [0,2,1,4,None,3,5,None,None,None,6,7]
                    ]
                ]
    results = [True, False]
    obj = Solution()
    for i in range(len(test_cases)):
        root1 = form_binary_tree_from_list(test_cases[i][0])
        root2 = form_binary_tree_from_list(test_cases[i][1])
        if obj.flipEquiv(root1, root2) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC958():

    from check_completeness_binary_tree_LC958 import Solution
    print("Checking Completeness of Binary Tree.......")
    test_cases = [ 
                    [1,2,3,4,5,None,7],
                    [1,2,3,4,5,6],
                    [], [1]
                ]
    results = [False, True, True, True]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.isCompleteTree(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC968():

    from binary_tree_cameras_LC968 import Solution
    print("Checking Cameras in Binary Tree.......")
    test_cases = [ 
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,None,0,None,0,None,0,0,None,None,0,0,0,None,None,0,0,None,None,0],
                    [], [1]
                ]
    results = [4, 5, 0, 1]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.minCameraCover(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


def test_LC1026():

    from max_diff_ancestor_node_LC1026 import Solution
    print("Checking Completeness of Binary Tree.......")
    test_cases = [ 
                    [8,3,10,1,6,None,14,None,None,4,7,13],
                    [1,None,2,None,0,3],
                    [0,None,1], [1]
                ]
    results = [7, 3, 1, 0]
    obj = Solution()
    for i in range(len(test_cases)):
        root = form_binary_tree_from_list(test_cases[i])
        if obj.maxAncestorDiff(root) == results[i]:
            passed(i + 1)
        else:
            failed(i + 1)


if __name__ == '__main__':

    # test_LC94()
    # test_LC98()
    # test_LC99()
    # test_LC100()
    # test_LC101()
    # test_LC102()
    # test_LC103()
    # test_LC104()
    # test_LC110()
    # test_LC112()
    # test_LC113()
    # test_LC114()
    # test_LC124()
    # test_LC144()
    # test_LC145()
    # test_LC199()
    # test_LC222()
    # test_LC226()
    # test_LC230()
    # test_LC236()
    # test_LC297()
    # test_LC508()
    # test_LC543()
    # test_LC572()
    # test_LC814()
    # test_LC951()
    # test_LC958()
    # test_LC968()
    # test_LC1026()