class Organization:
    def __init__(self):
        self.name = "Tech Corp"
        self.inner1 = self.Department1()
        self.inner2 = self.Department2()

    def show(self):
        print("This is an organization.", self.name)

    class Department1:
        def __init__(self):
            self.name = "HR"

        def show(self):
            print(f"Department Name: {self.name}")

    class Department2:
        def __init__(self):
            self.name = "Finance"

        def show(self):
            print(f"Department Name: {self.name}")


org = Organization()

org.show()

org.inner1.show()
org.inner2.show()
