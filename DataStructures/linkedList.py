import sys
ADD = 'A'
DELETE = 'D'
FIND = 'F'

class Student:
  def __init__(self, i, n, p=None):
    self.i = i
    self.n = n
    self.p = p

class Course:
  def __init__(self):
    self.head = None

  def __len__(self):
    return self.size

  def isEmpty(self):
    return self.size == 0

  # Insert function
  def addStudent(self, newID, newName):
    newStudent = Student(newID, newName)
    # Insert at beginning
    if self.head is None or newStudent.i < self.head.i:
        newStudent.p = self.head
        self.head = newStudent
        return True

    elif newStudent.i == self.head.i:
        return False

    else:
        temp = self.head
        while temp.p is not None and temp.p.i < newStudent.i:
            if temp.p.i == newStudent.i:
                return False
            temp = temp.p
        if temp.p is not None and temp.p.i == newStudent.i:
            return False
        newStudent.p = temp.p
        temp.p = newStudent
        return True

  # Delete function
  def deleteStudent(self, queryID):
    # If ID to be deleted is not in the list
    if self.head is None:
        return False
    # If ID to be deleted is the first node
    if self.head.i == queryID:
        self.head = self.head.p
        return True
       
    # If ID to be deleted is an intermediate node
    temp = self.head
    while temp.p is not None:
        if temp.p.i == queryID:
            temp.p = temp.p.p
            return True
        temp = temp.p
    # Check if last node is the Node to be deleted
    if temp.p == queryID:
       self.head = None
       return True
    return False
  
  # Search function
  def find(self, queryID):
    temp = self.head
    while temp is not None and temp.i != queryID:
        temp = temp.p
    return temp

  def write(self, outFile):
    temp = self.head
    while temp:
        outFile.write(f"{temp.i} {temp.n}\n")
        temp = temp.p

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  
  course = Course()
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == ADD:
        if len(words) != 3:
          raise Exception("ADD: invalid input")
        i, n = int(words[1]), words[2]
        if course.addStudent(i, n):
          course.write(outFile)
        else:
          outFile.write("Addition failed\n")
      elif op == DELETE:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        if course.deleteStudent(i):
          course.write(outFile)
        else:
          outFile.write("Deletion failed\n")
      elif op == FIND:
        if len(words) != 2:
          raise Exception("DELETE: invalid input")
        i = int(words[1])
        found = course.find(i)
        if not found:
          outFile.write("Search failed\n")
        else:
          outFile.write(str(found.i) + " " + found.n + "\n")
      else:
        raise Exception("Undefined operator")
        
