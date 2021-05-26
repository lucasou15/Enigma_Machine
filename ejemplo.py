class Triangle:

    def __init__(self, b, h):
        self.height = h
        self.base = b

    
    def __repr__(self):
        return "base is " + str(self.base) + " height is " + str(self.height)


    def area(self):
        return "Area is " + str(self.base*self.height*0.5)

    def set_base(self, b):
        if b <= 0:
            raise Exception("base must be greater than 0!")
        if isinstance(b, float):
            raise Exception("base must be an integer value!")
        
        self.base = b

    def get_base(self):
        return self.base

        
