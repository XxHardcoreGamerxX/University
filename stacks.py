# Practice 4. Palindromes and Balance
import sys

class Stack:
    def __init__(self):
        self.items = []
    # Checks if stack is empty
    def isEmpty(self):
        return len(self.items) == 0

    # Returns top/last element of the stack
    def top(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.items[-1]
    # Takes x as an argument and appends/inserts x, the new element, to the stack
    def push(self, item):
        self.items.append(item)

    # Pops/Removes the top element from the stack
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        else:
            return self.items.pop()
# Takes string as an argument and returns a boolean based on whether the string is a palindrome or not
def isPalindrome(string):
    # Create instance of a stack
    stack = Stack() #O(1)

    # Ensuring that uppercase and lowercase is not a factor when comparing
    string = string.lower()
    # Runtime: O(n)

    # Push first half of string into the stack
    for i in range(len(string) // 2 ): #O(n)
       stack.push(string[i]) # O(1)
    # 
    # Run time for for-loop: O(n) 


    # Calculate the beginning of the second half of the string
    start = (len(string) // 2) + (len(string) % 2)

    # Compare the 2 halfs of the string by comparing the popped elements from the stack to the second half of the string
    for i in range(start, len(string)): #O(n)
       # If they do not have the same spelling front and back, then it is not palindrome and therefor return false
       if string[i] != stack.pop(): #O(1)
          return False
    # Run time for for-loop: O(n)
    return True # String is palindrome

# Total run time for isPalindrome is: O(n)+O(n)+O(n) = O(3n) = O(n)

# Takes a string and returns a boolean based on whether the string is balanced or not
def balance(string):
    # Create instance of a stack
    stack = Stack() #O(1)
    # We want to identify the opening and closing brackets and create variables for them
    openingBrackets = "([{" # O(1)
    closingBrackets = ")]}" # O(1)

    # We then map the corresponding brackets to each other
    bracketMapping = {')' : '(',']' : '[', '}' : '{'} #O(1)

    # # We then want to transverse the string and check if there are any opening/closing brackets
    for char in string: #O(n)
      if char in openingBrackets: # Check if a character is a opening bracket, if it is then push that character onto the stack
      # O(n)
          stack.push(char) # O(1)
      elif char in closingBrackets: # Check if a character is a closing bracket
         # Two cases: First case; if the stack is empty then there is an imbalance as there is no corresponding opening bracket
         # Second case; We then check if popped first character which should be the corresponding opening bracket matches the closing bracket. 
         # If they don't, then this also means there is an imbalance
      # O(n)
         if stack.isEmpty() or stack.pop() != bracketMapping[char]: # O(n)
            return False # String is imbalanced so we return false
    return stack.isEmpty() # Checks if all brackets have been balanced
    # O(1)

    # The overall time complexity is: O(n)

    

if __name__ == "__main__":
  if len(sys.argv) != 3:
    raise Exception("Correct usage: [program] [input] [output]")
  with open(sys.argv[1], 'r') as inFile:
    lines = inFile.readlines()
  with open(sys.argv[2], 'w') as outFile:
    for line in lines:
      words = line.split()
      op = words[0]
      if op == 'P':
        if len(words) != 2:
          raise Exception("PALINDROME: invalid input")
        ret = "T" if isPalindrome(words[1]) else "F"
        outFile.write(ret+"\n")
      elif op == 'B':
        if len(words) != 2:
          raise Exception("BALANCE: invalid input")
        ret = "T" if balance(words[1]) else "F"
        outFile.write(ret+"\n")
      else:
        raise Exception("Undefined operator")
      
# Alternative solution for isPalindrome:
# def isPalindrome(string):
#    return string == string[::-1]