class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]



text = input("Enter a word: ")

obj = Reverse(text)


print("Reversed string:", obj.reverse_string())