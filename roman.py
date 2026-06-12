class RomanConverter:
    def int_to_roman(self, num):
        
        mapping = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        
        result = ""
        for value, symbol in mapping:
            
            while num >= value:
                result += symbol
                num -= value
                
        return result



user_num = int(input("Enter an integer: "))

converter = RomanConverter()


print("Roman value:", converter.int_to_roman(user_num))