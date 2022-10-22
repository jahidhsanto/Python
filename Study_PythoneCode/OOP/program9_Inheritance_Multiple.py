class A:
    def display1(self):
        print("I am inside A  class")


class B:
    def display2(self):
        print("I am inside B class")


class C(A, B):
    # display1
    # display2
    def display3(self):
        super().display1()
        super().display2()
        print("I am inside C class")


ob1 = C()
ob1.display1()
ob1.display2()
ob1.display3()
