'''
Write a Python program to find validity of a string of parentheses, 
'(',')', '{', '}', '[' and ']. 

These brackets must be close in the correct order, 
for example "()" and "()[]{}" are valid but "[)", "({[)]" and
"{{{" are invalid.
'''


# My Solution:
class CheckBrackets():

    mydict = {'[':']','(':')','{':'}'}
    mylist = ['[',']','(',')','{','}']

    def check(self, mystr):


        new_list = []

        for i in mystr:
            if i in self.mylist:
                new_list.append(i)

        index1 = 0 
        index2 = 1


        while len(new_list) > 1 :
            print(new_list)
            i = new_list[index1]
            if i not in self.mydict:
                return False
            j = self.mydict[i]
            if new_list[index2] == j:
                new_list.pop(index2)
                new_list.pop(index1)
                index1 = 0 
                index2 = 1
            else:
                index1 += 1
                index2 += 1
                if index2 == len(new_list):
                    break


        return len(new_list) == 0 
            

  


# ______________________________________________________________________
# Given solution:

class py_solution:
   def is_valid_parenthese(self, str1):
        pchar = {"(": ")", "{": "}", "[": "]"}

        stack = []

        for parenthese in str1:
            if parenthese in pchar:
                stack.append(parenthese)
            elif len(stack) == 0 or pchar[stack.pop()] != parenthese:
                return False
        return len(stack) == 0


# ______________________________________________________________________

     

'''

('{}[]{}')            true
('({}[])')            true
('({}[])()')          true
('{[}]')              false
('(()[{}{}[]]())')    true
('((()[{}{}[]]())')   false
('((()[{}{}[]]([)')   false
('][')                false
('[')                 false

'''

