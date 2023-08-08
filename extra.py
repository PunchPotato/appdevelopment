class ClassA:
    def __init__(self, value):
        self.value = value

    def print_value(self):
        print(f"Value in ClassA: {self.value}")

class ClassB:
    def __init__(self, obj_a):
        self.obj_a = obj_a

    def add_attribute(self, attribute_name, attribute_value):
        setattr(self.obj_a, attribute_name, attribute_value)


# Create an instance of ClassA
obj_a = ClassA(42)

# Create an instance of ClassB and add an attribute to ClassA
obj_b = ClassB(obj_a)
obj_b.add_attribute("new_attribute", "Hello, I'm a new attribute!")

# Access the new attribute in ClassA
print(obj_a.new_attribute)  # Output: Hello, I'm a new attribute!