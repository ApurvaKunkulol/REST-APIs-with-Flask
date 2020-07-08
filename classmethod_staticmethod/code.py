class ClassTest:
    def instance_method(self):
        print(f"Called instance method of {self}.")

    def __str__(self):
        return  "Classtest"

    def __repr__(self):
        return  "Classtest"

    @classmethod
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("Called the static method!")

test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)
ClassTest.class_method()
ClassTest.static_method()
