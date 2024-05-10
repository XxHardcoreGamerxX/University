# Practice 9. Max Heap
import sys
INSERT = 'I'
DELETE = 'D'
MAXIMUM = 'M'
MAX_CAPACITY = 1000
INT_MIN = -sys.maxsize

class MaxHeap:
  def __init__(self, num=MAX_CAPACITY):
    self.elements = [0] * num
    self.count = 0
    self.capacity = num

  """
  Given the index i of element, return the index of that element's parent in the heap

  Parameters:
  - i: index of element

  Returns:
  - Parent of the element

  Time complexity: O(1)
  """
  def parent(self, i):
    return (i - 1) // 2 # O(1)


  """
  Given the index i of element, return the index of that element's left child in the heap

  Parameters:
  - i: index of element

  Returns:
  - Left child of the element
  
  Time complexity: O(1)
  """
  def left(self, i):
    left_child = 2 * i + 1 # O(1)
    return left_child # O(1)
  
  """
   Given the index i of element, return the index of that element's right child in the heap

  Parameters:
  - i: index of element

  Returns:
  - Right child of the element
  
  Time complexity: O(1)
  """
  def right(self, i):
    right_child = 2 * i + 2 # O(1)
    return right_child # O(1)

  """
  Inserts a given element, elem, into the heap. 
  If the insertion fails, then the program is immedaitely terminated with an appropriate error message

  Parameters:
  - elem: element to be inserted

  Time complexity: O(logn)
  """
  def insertElement(self, elem):
    if self.count < self.capacity: 
      self.elements[self.count] = elem 
    else:
      self.elements.append(elem)
    
    i = self.count 
    p = self.parent(i) 

    while i > 0 and self.elements[p] < elem:
      self.elements[i] = self.elements[p] 
      i = p
      p = self.parent(i)
    self.elements[i] = elem
    self.count += 1


  """
  Returns the maximum of the heap if it exists

  Time complexity: O(1)
  """
  def maximum(self):
    return self.elements[0]

  """
  MaxHeapiy has the responsibility of maintaining the heap structure. We maintain the heap structure using recursion.

  Time complexity: O(log n)
  """
  def maxHeapify(self, i):
    largest = i
    left_child = self.left(i)
    right_child = self.right(i)
    if left_child != self.count and self.elements[left_child] > self.elements[largest]:
      largest = left_child

    if right_child != self.count and self.elements[right_child] > self.elements[largest]:
      largest = right_child

    if largest != i:
      self.elements[i], self.elements[largest] = self.elements[largest], self.elements[i]
      self.maxHeapify(largest)

  """
  Deletes the maximum from the heap and returns the maximum.
  If the deletion fails, then the program will terminate with an error

  Returns:
  - The maximum after deletion of previous maximum

  Time complexity: O(log n)
  """
  def deleteMaximum(self):
    if self.count < 1:
      raise Exception("Heap underflow")
    largest = self.elements[0]
    self.elements[0] = self.elements[self.count - 1]
    self.count -= 1
    self.maxHeapify(0)
    return largest

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  h = MaxHeap()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == INSERT:
        if len(words) != 2:
          raise Exception("INSERT: invalid input")
        i = int(words[1])
        h.insertElement(i)
        outFile.write(' '.join(map(str, h.elements[:h.count]))+ '\n')
        # If the insertion succeeds, write every element in the array into output file.
      elif op == DELETE:
        max_element = h.deleteMaximum()
        outFile.write(' '.join(map(str, h.elements[:h.count]))+ '\n')
        # If the deletion succeeds, write every element in the array into output file.
      elif op == MAXIMUM:
        max_element = h.maximum()
        outFile.write(str(max_element) + '\n')
        # If getting the maximum succeeds, write the maximum into output file.
      else:
        raise Exception("Undefined operator")
        

