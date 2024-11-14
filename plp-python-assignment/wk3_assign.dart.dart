
// Class with encapsulation
class Person {
  final String name;
  final int age;
  String _address;

  Person(this.name, this.age, this._address); // Removed redundant assignment

  String get address => _address;

  void setAddress(String newAddress) {
    _address = newAddress;
  }

  void displayInfo() {
    print('Name: $name, Age: $age, Address: $_address');
  }
}

// Inheritance
class Student extends Person {
  final String studentId;

  Student(String name, int age, String address, this.studentId) : super(name, age, address);

  void study() {
    print('$name is studying.');
  }

  @override
  void displayInfo() {
    super.displayInfo(); // Call the parent method
    print('Student ID: $studentId');
  }
}

// Polymorphism
abstract class Shape {
  double area();
}

class Circle extends Shape {
  final double radius;

  Circle(this.radius);

  @override
  double area() {
    return 3.14 * radius * radius; // Corrected to 3.14
  }
}

class Rectangle extends Shape {
  final double width;
  final double height;

  Rectangle(this.width, this.height);

  @override
  double area() {
    return width * height;
  }
}

// Abstraction
abstract class Animal {
  void makeSound();
}

class Dog extends Animal {
  @override
  void makeSound() {
    print('Woof!');
  }
}

class Cat extends Animal {
  @override
  void makeSound() {
    print('Meow!');
  }
}

// Main function to demonstrate the functionality
void main() {
  // Creating Person and Student
  Person person = Person("Alice", 30, "123 Main St");
  person.displayInfo();

  Student student = Student("Bob", 20, "456 College Ave", "S12345");
  student.displayInfo();
  student.study();

  // Demonstrating polymorphism with shapes
  List<Shape> shapes = [Circle(5), Rectangle(4, 6)];
  for (var shape in shapes) {
    print('Area: ${shape.area()}');
  }

  // Demonstrating abstraction with animals
  List<Animal> animals = [Dog(), Cat()];
  for (var animal in animals) {
    animal.makeSound();
  }
}