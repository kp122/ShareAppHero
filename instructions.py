class instruction:
    def __init__(self):
        self.text = ""
        self.image = ""
        self.vidlink =""

class _instructions:
    def __init__(self):
        print("Base constructed")
        self.name ="Pasta"
        self.image = ""
        self.instructionList = []
        self.tags = []
        self.summaryvidlink="";
        
        
        
class recipe(_instructions):
    def __init__(self):
        super(recipe,self).__init__()
        print("Child sonstructed")
        self.prep_time=""
        self.number_of_servings=""
        self.cooking_time=""
        

    def printName(self):
        print(self.name)
             

if __name__ == '__main__':
    r = recipe()
    r.printName()
