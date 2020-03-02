from Student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 3.8, True)

print(student1)
print(student2.name)

print(student1.on_honor_roll())
print(student2.on_honor_roll())
