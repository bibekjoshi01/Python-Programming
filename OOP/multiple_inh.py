class A:
    def show(self):
        return "A"

class B(A):
    def show(self):
        return super().show() + " -> B"

class C(A):
    def show(self):
        return super().show() + " -> C"

class D(B, C):  # Inherits from B first, then C
    def show(self):
        return super().show() + " -> D"

obj = D()
print(obj.show())  # Output: A -> C -> B -> D
print(D.mro())  # Order: D → B → C → A → object

print(isinstance(4, int))