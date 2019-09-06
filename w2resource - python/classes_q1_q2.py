"""1. Write a Python class to convert an integer to a roman numeral"""

"""2. Write a Python class to convert a roman numeral to an integer."""

class Convertion:
 
    values = [
        ('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
        ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), 
        ('V', 5), ('IV', 4), ('I', 1)
    ]    

    def num_to_roman(self, num):
        '''this function convert an int to roman characters.'''
        if not isinstance(num, int):
            raise ValueError 
        elif num <= 0:
            raise ValueError
        else:
            roman_num = ''
                       
            values = self.values[:]
            
            while num != 0:                
                tuples = values.pop(0)
                factor = num // tuples[1]
                roman_num += (tuples[0]*factor)
                num -= tuples[1] * factor
        return roman_num

    def roman_to_num(self, roman):
        '''this function convert roman characters to an int.'''
        _dict= {} 

        for tuple in self.values:
            _dict.update({tuple[0]: tuple[1]})
        
        number = 0

        roman_list = [r for r in roman] 
        roman_list.append('Z')
        

        while roman_list[0] != 'Z':
            # c is for current letter
            # n is for next letter 

            c = roman_list[0]
            
            n = roman_list[1]
            c = _dict.get(c)
            n = _dict.get(n, 0) 
            
            if c >= n:
                number += c 
            else:
                number -= c  

            roman_list.pop(0)

        return number


        

