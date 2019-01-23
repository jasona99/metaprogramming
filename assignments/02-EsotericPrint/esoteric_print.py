import builtins, random, string

class print:
    def __init__(self):
        self.count = 0
        self.prev_string = None
        self.file = open("file.txt")
        self.lines = self.file.readlines()
    def __call__(self, s):

        if self.prev_string != None and self.prev_string == s:
            self.count += 1

            if self.count == 3:
                #Thanks, StackOverflow!
                builtins.print(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(len(s))))
            elif self.count == 5:
                builtins.print(hex(id(s)))
            elif self.count == 7:
                builtins.print("Oi, I'm walkin' 'ere!'")
            elif self.count >= 9 and self.count < 1984:
                #You asked for it...
                builtins.print(self.lines[self.count-9])
            else:
                builtins.print(s)


        elif s == "Hello, world!":
            builtins.print("Hello, noob!")

        else:
            self.prev_string = s
            self.count = 1
            builtins.print(s)
###
p = print()
for i in range(0,2000):
    p("Hello there!")
###


#Old code.
"""
count = 0
prev_string = ""
class print:
    def __init__(self, s):
        global prev_string
        global count

        file = open("file.txt")
        lines = file.readlines()

        if prev_string != None and prev_string == s:
            count += 1

            if count == 2:
                #Thanks, StackOverflow!
                builtins.print(''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits) for _ in range(len(s))))
            elif count == 4:
                builtins.print(hex(id(s)))
            elif count == 6:
                builtins.print("Oi, I'm walkin' 'ere!'")
            elif count >= 8 and count < 1983:
                #You asked for it...
                builtins.print(lines[count-8])
            else:
                builtins.print(s)

        elif s == "Hello, world!":
            builtins.print("Hello, noob!")

        else:
            prev_string = s
            count = 0
            builtins.print(s)
for i in range(0,2000):
    print("Hello!")
"""
