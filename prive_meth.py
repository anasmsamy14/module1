class myclass:
    __privatevar=27;

    def __privmeth(self):
        print("I'm inside my class")
    
    def hello(self):
        print('private variable value: ',myclass.__privatevar)

foo = myclass()
foo.hello()
foo.__privmeth