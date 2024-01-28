class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self,num):
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            p1_evaluated = self.p1.evaluate(num)
        else:
            if isinstance(self.p1,X):
                if (num<0):
                    p1_evaluated = Int(f"({num})")
                else:
                    p1_evaluated = Int(num)
            else:
                p1_evaluated = self.p1

        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_evaluated = self.p2.evaluate(num)
        else:
            if isinstance(self.p2,X):
                if (num<0):
                    p2_evaluated = Int(f"({num})")
                else:
                    p2_evaluated = Int(num)
            else:
                p2_evaluated = self.p2

        return Add(p1_evaluated, p2_evaluated)
       

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)
    def evaluate(self,num):
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            p1_evaluated = self.p1.evaluate(num)
        else:
            if isinstance(self.p1,X):
                if (num<0):
                    p1_evaluated = Int(f"({num})")
                else:
                    p1_evaluated = Int(num)
            else:
                p1_evaluated = self.p1

        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_evaluated = self.p2.evaluate(num)
        else:
            if isinstance(self.p2,X):
                if (num<0):
                    p2_evaluated = Int(f"({num})")
                else:
                    p2_evaluated = Int(num)
            else:
                p2_evaluated = self.p2

        return Sub(p1_evaluated, p2_evaluated)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
                 return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

    def evaluate(self,num):
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            p1_evaluated = self.p1.evaluate(num)
        else:
            if isinstance(self.p1,X):
                if (num<0):
                    p1_evaluated = Int(f"({num})")
                else:
                    p1_evaluated = Int(num)
            else:
                p1_evaluated = self.p1

        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_evaluated = self.p2.evaluate(num)
        else:
            if isinstance(self.p2,X):
                if (num<0):
                    p2_evaluated = Int(f"({num})")
                else:
                    p2_evaluated = Int(num)
            else:
                p2_evaluated = self.p2

        return Mul(p1_evaluated, p2_evaluated)
       
        

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add) or isinstance(self.p1, Sub):
            if isinstance(self.p2, Add) or isinstance(self.p1, Sub):
                 return "( " + repr(self.p1) + " ) / ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) / " + repr(self.p2)
        if isinstance(self.p2, Add) or isinstance(self.p2, Sub):
            return repr(self.p1) + " / ( " + repr(self.p2) + " )"
        return repr(self.p1) + " / " + repr(self.p2)
    
    def evaluate(self,num):
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            p1_evaluated = self.p1.evaluate(num)
        else:
            if isinstance(self.p1,X):
                if (num<0):
                    p1_evaluated = Int(f"({num})")
                else:
                    p1_evaluated = Int(num)
            else:
                p1_evaluated = self.p1

        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_evaluated = self.p2.evaluate(num)
        else:
            if isinstance(self.p2,X):
                if (num<0):
                    p2_evaluated = Int(f"({num})")
                else:
                    p2_evaluated = Int(num)
            else:
                p2_evaluated = self.p2

        return Div(p1_evaluated, p2_evaluated)


poly = Add( Add( Int(4), Int(3)), Add( X(), Mul( Int(1), Add( Mul(X(), X()), Int(1)))))
print(poly)
print(poly.evaluate(-1))
poly1 = Mul(X(), Add(Int(1),Int(3)))


print(poly1)
print(poly1.evaluate(-2))