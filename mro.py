class A:
    def print(self):
        print("A")
class B:
    def print(self):
        print("b")
class C(B,A):
    def feat(self):
        super().print()
        print('c')
a1=C()
a1.feat()
