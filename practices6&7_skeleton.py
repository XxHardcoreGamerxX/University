# Practices 6&7. Binary Search Tree Operations
import sys
from collections import deque
BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'
SEARCH = 'S'
INSERT = 'I'
DELETE = 'D'
INORDER = 'N'
PREORDER = 'R'
POSTORDER = 'O'

# Node implementation
class TreeNode:
  def __init__(self, k, l=None, r=None):
    self.key = k
    self.left = l
    self.right = r

class BinarySearchTree:
  def __init__(self):
    self.root = None

  # Return True if tree is empty; False otherwise
  def isEmpty(self):
    return self.root == None

  """
  Given a sorted array of integers with start first index l and last index r. 
  Based on that, a binary search tree is then built containing the elements of the index.
  We start by selecting the middle element as the root, and then there is generated new sub-arrays which we then use the same logic for
  the left and right children of the middle element. 

  Parameters:
  arr (list[int]): Array
  l (int): First index
  r (int): Last index

  Returns:
  The root node of the constructed tree

  Time complexity: O(n) as the function is executed for each element in the given array, therefore the complexity is O(n) despite the operations
  being constant time
  """
  def arrayToBST(self, arr, l, r):
    if l > r: # O(1)
      return None
    mid = (l + r) // 2 # O(1)
    node = TreeNode(arr[mid])
    node.left = self.arrayToBST(arr, l, mid-1)
    node.right = self.arrayToBST(arr, mid+1, r)
    return node # O(1)
  
  """
  Goes through the trees and looks for the lowest value in the tree

  Returns: Node with the minimum value

  Time complexity: O(n)
  """
  def findMin(self, node=None):
    if self.root is None: # O(1)
      return None
    current = node # O(1)
    while current.left is not None: # O(n)
      current = current.left
    return current # O(1)
  """
  Goes through tree to find the maximum value in the tree

  Returns: Node with the maximum value

  Time complexity: O(n)
  """
  def findMax(self):
    if self.root is None: # O(1)
      return None
    current = self.root # O(1)
    while current.right is not None: # O(n)
      current = current.right
    return current # O(1)

  def _getHeight(self, curr):
    if not curr:
      return 0
    return 1 + max(self._getHeight(curr.left), self._getHeight(curr.right))

  def _printSpaces(self, n, curr):
    for i in range(int(n)):
      print("  ", end="")
    if not curr:
      print(" ", end="")
    else:
      print(str(curr.key), end="")

  def printTree(self):
    if not self.root:
      return 
    q = deque()
    q.append(self.root)
    temp = deque()
    cnt = 0
    height = self._getHeight(self.root) - 1
    nMaxNodes = 2**(height + 1) - 1
    while cnt <= height:
      curr = q.popleft()
      if len(temp) == 0:
        self._printSpaces(nMaxNodes / (2**(cnt+1)), curr)
      else:
        self._printSpaces(nMaxNodes / (2**cnt), curr)
      if not curr:
        temp.append(None)
        temp.append(None)
      else:
        temp.append(curr.left)
        temp.append(curr.right)
      if len(q) == 0:
        print("\n")
        q = temp
        temp = deque()
        cnt += 1

  """
  Given a query, searches for the node whose key is equal to the query.

  Parameters:
  - Query: The desired node to be found

  Returns:
  - If the node exists, then it returns the key of the desired node. If not, then it returns none/null

  Time complexity: O(n)
  """
  def search(self, query):
    current = self.root # O(1)
    while current is not None: # O(n)
      if query == current.key: # O(1)
        return current
      elif query < current.key: # O(1)
        current = current.left
      else:
        current = current.right
    return None
      
  """
  Given an output file, it writes the keys of all the nodes visited inorder

  Parameters:
  - outFile: File to be written to
  - Node: The starting node for the inorder traversal. If None, the traversal
  starts from the root of the tree.

  Time complexity: This function uses recursion and is called each time a node is to be written to an output file
  making the time complexity O(n)

  """
  def writeInorder(self, outFile, node=None):
    # Practice 6
    if node is None: # Base case ... O(1)
      return # terminate
    if node is not None: # Recursive case ... O(1)
      self.writeInorder(outFile, node.left)
      outFile.write(f"{node.key} ")
      self.writeInorder(outFile, node.right)

  # Given an output file, write the keys of all the nodes 
  # visited in preorder traversal
  """
  Given an output file, writes the keys of all the nodes visited in preorder transversal

  Parameters:
  - outFile: File to be written to
  - Node: The starting node for the preorder transversal. If None, the traversal
  starts from the root of the tree.

  Time complexity: O(n)
  """
  def writePreorder(self, outFile, node=None):
    if node is None: # Base case
      if self.root is None: # O(1)
        return # Terminate
      node = self.root
    outFile.write(f"{node.key} ")
    if node.left is not None: # O(1)
      self.writePreorder(outFile, node.left)
    if node.right is not None: # O(1)
      self.writePreorder(outFile, node.right)


  
  # Given an output file, write the keys of all the nodes 
  # visited in postorder traversal
  """
  Given an output file, write the keys of all the nodes visited in postorder transversal

  Parameters:
  - outFile: File to be written to
  - Node: The starting node for the postorder transversal. If None, the traversal
  starts from the root of the tree.

  Time complexity: O(n)
  """
  def writePostorder(self, outFile, node=None):
    # Practice 6
    if node is None: # Base case
      return # Terminate
    if node is not None: # Recursive case
      self.writePostorder(outFile, node.left)
      self.writePostorder(outFile, node.right)
      outFile.write(f"{node.key} ")

  # If node with key k alreay exists in the tree, do nothing
  # Otherwise, insert new node with key k 
  """
  Inserts a node with key k in a tree. If the key already exists then it does nothing. 
  Otherwise, k is inserted

  Parameters:
  - k: key to be inserted

  Time complexity: O(n)
  """
  def insertNode(self, k):
    # Practice 7
    if self.root is None: # O(1)
      self.root = TreeNode(k)
      return
    else:
      current = self.root
      while True: # O(n) - it depends on the depth of the tree
        if k < current.key:
          if current.left is None: # O(1)
            current.left = TreeNode(k)
            break
          else:
            current = current.left
        elif k > current.key: # O(1)
          if current.right is None:
            current.right = TreeNode(k)
            break
          else:
            current = current.right
      
  # If deletion fails, immediately terminate the program
  # Otherwise, delete the node with key k
  """
  Deletes a node with key k

  Parameters:
  - k: key of the node to be deleted

  Time complexity: O(n)
  """
  def deleteNode(self, k, node=None):
    if node is None: # Base case O(1)
        node = self.root

    if node is None: # Base case O(1)
        return node

    if k < node.key: # Recursive case O(n) - depends on height of tree
        node.left = self.deleteNode(k, node.left)
    elif k > node.key:
        node.right = self.deleteNode(k, node.right)
    else:
        # Node with only one child or no child
        if node.left is None:
            temp = node.right # Set temp ot point to the node to be deleted's right child
            node = None # Deletion of node
            return temp # Make the temp take the place of the deleted node
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        # Node with two children, get the inorder successor (smallest in the right subtree)
        temp = self.findMin(node.right)
        node.key = temp.key
        node.right = self.deleteNode(temp.key, node.right)

    return node

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  tree = BinarySearchTree()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == BUILD:
        data = [int(s) for s in words[1:]]
        tree.root = tree.arrayToBST(data, 0, len(data) - 1)
        if tree.root:
          outFile.write(BUILD + "\n")
          tree.printTree()
        else:
          raise Exception("BUILD: invalid input")
      elif op == FIND_MIN:
        found = tree.findMin()
        if not found:
          raise Exception("FindMin failed")
        else:
          outFile.write(str(found.key) + "\n")
      elif op == FIND_MAX:
        found = tree.findMax()
        if not found:
          raise Exception("FindMax failed")
        else:
          outFile.write(str(found.key) + "\n")
      elif op == SEARCH:
        if len(words) != 2:
          raise Exception("SEARCH: invalid input")
        k = int(words[1])
        # Practice 6. Call the function for search
        found = tree.search(k)
        if not found:
          raise Exception("SEARCH: Failed")
        else:
          outFile.write(str(found.key) + "\n")
      elif op == INORDER:
        output = []
          # Practice 6. Call the function for inorder traversal   
        tree.writeInorder(outFile, tree.root)
        outFile.write('\n')
      elif op == PREORDER:
          # Practice 6. Call the function for preorder traversal
        output = []
        tree.writePreorder(outFile, tree.root)
        outFile.write('\n')
      elif op == POSTORDER:
          # Practice 6. Call the function for postorder traversal
        output = []
        tree.writePostorder(outFile, tree.root)
        outFile.write('\n')
      elif op == INSERT:
        if len(words) != 2:
          raise Exception("INSERT: invalid input")
        ret = "I "
        k = int(words[1])
        tree.insertNode(k)
        outFile.write(f"I{k}\n")
      elif op == DELETE:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        k = int(words[1])
        tree.root = tree.deleteNode(k)
        outFile.write(f"D{k}\n")
      else:
        raise Exception("Undefined operator")
        
