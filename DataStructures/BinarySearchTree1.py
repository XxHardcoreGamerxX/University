# Practice 5. Binary Search Tree
import sys
from collections import deque
BUILD = 'B'
FIND_MIN = 'm'
FIND_MAX = 'M'

# Node implementation
class TreeNode:
  def __init__(self, key):
    self.key = key
    self.right = None
    self.left = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  # Return True if tree is empty; False otherwise
  def isEmpty(self):
    return self.root is None

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

  Time complexity: O(n)
  """
  def arrayToBST(self, arr, l, r):
    if l > r:
      return None
    mid = (l + r) // 2
    node = TreeNode(arr[mid])
    node.left = self.arrayToBST(arr, l, mid-1)
    node.right = self.arrayToBST(arr, mid+1, r)
    return node
  
  """
  Goes through the trees and looks for the lowest value in the tree

  Returns: Node with the minimum value

  Time complexity: O(n)
  """
  def findMin(self):
    if self.root is None:
      return None
    current = self.root
    while current.left is not None:
      current = current.left
    return current

  """
  Goes through tree to find the maximum value in the tree

  Returns: Node with the maximum value

  Time complexity: O(n)
  """
  def findMax(self):
    if self.root is None:
      return None
    current = self.root
    while current.right is not None:
      current = current.right
    return current

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
      else:
        raise Exception("Undefined operator")
        
