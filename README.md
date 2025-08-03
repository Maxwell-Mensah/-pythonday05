## -pythonday05
## 🐍 Python Lab – Classes, Inheritance & Special Methods
## 📌 Objective
This lab aims to explore the fundamental concepts of **Object-Oriented Programming (OOP)** in Python through:

- the use of inheritance,

- class methods (@classmethod),

- static methods (@staticmethod)

## 🧱 Class Structure
🔹 Base Class
A base class, such as Animal, includes:

- attributes (e.g., name, legs, species_type)

- a constructor __init__

- public methods like get_name() or get_legs()

## 🔁 Inheritance
🔸 Child Class
A child class, like Cat, inherits from the Animal class:

- it reuses the parent’s methods using super()

- it can add new attributes (e.g., color)

- it can override existing methods (called overriding)

To call a method from the parent class that has been overridden:
**super().method_name()**

## ⚙️ Special Methods
__init__: Automatically called constructor when the object is created

## 🏷️ Class Methods
Declared with **@classmethod**
They take **cls** as the first parameter (representing the class itself).

## ✅ Use Case:
To get class-wide information (e.g., number of instances)

To define alternative constructors

## 📦 Static Methods
Declared with **@staticmethod**
They take neither self nor **cls**.

## ✅ Use Case:
To create utility methods related to the class, but independent of both the class and its instances

## ✅ Conclusion
The use of inheritance, class/static methods, and modular structure enables writing code that is:

- more modular

- more reusable

- more organized

These principles are essential for progressing toward more advanced and professional Python projects.