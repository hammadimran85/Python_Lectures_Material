class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.__age = age
        self.__grade = grade

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def display_student_info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.__age}')
        print(f'Grade: {self.__grade}')

    def is_passing(self):
        return self.__grade >= 40

    def promote(self):
        if self.__grade < 100:
            self.__grade += 10
            print(f'{self.name} has been promoted to the next grade')
        else:
            print(f'{self.name} has already reached the highest grade')

student1 = Student('Mohtashim', 19, 75)
student2 = Student('Abubaker', 22, 100)

student2.name = 'Hammad'
# print(student2.get_age())
student2.set_age(21)

print('Student 2 Information')
student2.display_student_info()

print('Student 2 is Passing?', student2.is_passing())

student2.promote()