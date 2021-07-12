from test.entity.Student import Student

lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.get_name(), lisa.get_grade())
print(bart.get_name(), bart.get_grade())
print(lisa.name)
print(Student.name)
lisa.name="Michael"
print(lisa.name)
print(Student.name)
del lisa.name
print(lisa.name)
print(Student.name)