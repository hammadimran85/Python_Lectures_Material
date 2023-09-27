# from abc import ABC, abstractmethod
#
#
# class Animal(ABC):  # Base Class
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     @abstractmethod
#     def speak(self):
#         pass
#
#
# class Lion(Animal):  # Derived Classes
#     def speak(self):
#         return f'{self.name} the {self.species} says Roar!'
#
#
# class Elephant(Animal):
#     def speak(self):
#         return f'{self.name} the {self.species} says Trumpet!'
#
#
# class Monkey(Animal):
#     def speak(self):
#         return f'{self.name} the {self.species} says Chatter!'
#
#
# # Polymorphism in action
# def animal_activity(animal):
#     print(animal.speak())
#
#
# class Zoo:
#     def __init__(self):
#         self.__animals = []  # Encapsulating private variable
#
#     def add_animal(self, animal):
#         self.__animals.append(animal)
#
#     def get_animal(self):
#         return self.__animals
#
#     def display_animal_names(self):
#         print('Animals in Zoo')
#         for animal in self.__animals:
#             print(animal.name)
#
#
# # abstraction
# def add_animal(zoo):
#     name = input(f'Enter the animal\'s name: ')
#     species = input(f'Enter the animal\'s species: ')
#     animal_type = input(f'Enter the animal\'s type (Lion, Elephant, Monkey): ').capitalize()
#
#     if animal_type == 'Lion':
#         animal = Lion(name, species)
#     elif animal_type == 'Elephant':
#         animal = Elephant(name, species)
#     elif animal_type == 'Monkey':
#         animal = Monkey(name, species)
#     else:
#         print('Invalid Animal Type')
#         return
#
#     zoo.add_animal(animal)
#     print(f'{name} the {species} has been added to the zoo')
#
#
# def main():
#     zoo = Zoo()
#
#     while True:
#         print('Zoo Management System Menu')
#         print('Press 1 to Add Animal')
#         print('Press 2 to Display Animal Names')
#         print('Press 3 to showcase Animal')
#         print('Press 4 to List All Animals')
#         print('Press 5 to Exit')
#
#         choice = int(input('Enter your choice: '))
#
#         if choice == 1:
#             add_animal(zoo)
#         elif choice == 2:
#             zoo.display_animal_names()
#         elif choice == 3:
#             name = input('Enter the animal\'s name')
#             for animal in zoo.get_animal():
#                 if animal.name == name:
#                     animal_activity(animal)
#                     break
#         elif choice == 4:
#             animals = zoo.get_animal()
#             if animals:
#                 print('All animals in Zoo')
#                 for animal in animals:
#                     print(f'{animal.name} the {animal.species}')
#             else:
#                 print('We have no animals in the Zoo')
#         elif choice == 5:
#             print('Thanks for using Zoo management System')
#             break
#         else:
#             print('Invalid Choice')
#
# if __name__ == '__main__':
#     main()
import sys

a = 10
b = 2598968736831244545367345
print(sys.getrefcount(a))
print(sys.getrefcount(b))