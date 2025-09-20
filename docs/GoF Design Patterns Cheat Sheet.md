
# **Python Design Patterns Cheat Sheet**

## **1. Creational Patterns**

### **1.1 Singleton**

```python
class Singleton:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = Singleton()
s2 = Singleton()
print(s1 is s2)  # True
```

---

### **1.2 Factory Method**

```python
class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing Circle")

class Square(Shape):
    def draw(self):
        print("Drawing Square")

def shape_factory(shape_type):
    if shape_type == "circle":
        return Circle()
    elif shape_type == "square":
        return Square()
    return None

shape = shape_factory("circle")
shape.draw()  # Drawing Circle
```

---

### **1.3 Abstract Factory**

```python
class Dog:
    def speak(self): return "Woof"

class Cat:
    def speak(self): return "Meow"

class DogFactory:
    def create_pet(self): return Dog()

class CatFactory:
    def create_pet(self): return Cat()

def get_factory(animal):
    return DogFactory() if animal == "dog" else CatFactory()

factory = get_factory("cat")
pet = factory.create_pet()
print(pet.speak())  # Meow
```

---

### **1.4 Builder**

```python
class House:
    def __init__(self):
        self.parts = []

    def show(self):
        print("House parts:", ", ".join(self.parts))

class HouseBuilder:
    def __init__(self):
        self.house = House()

    def build_walls(self):
        self.house.parts.append("Walls")
        return self

    def build_roof(self):
        self.house.parts.append("Roof")
        return self

    def get_result(self):
        return self.house

builder = HouseBuilder()
house = builder.build_walls().build_roof().get_result()
house.show()  # House parts: Walls, Roof
```

---

### **1.5 Prototype**

```python
import copy

class Prototype:
    def __init__(self, value):
        self.value = value

    def clone(self):
        return copy.deepcopy(self)

obj1 = Prototype([1, 2, 3])
obj2 = obj1.clone()
obj2.value.append(4)
print(obj1.value)  # [1, 2, 3]
print(obj2.value)  # [1, 2, 3, 4]
```

---

## **2. Structural Patterns**

### **2.1 Adapter**

```python
class EuropeanPlug:
    def voltage(self): return 220

class USPlug:
    def voltage(self): return 110

class Adapter:
    def __init__(self, european_plug):
        self.plug = european_plug

    def voltage(self):
        return 110  # adapt to US voltage

plug = Adapter(EuropeanPlug())
print(plug.voltage())  # 110
```

---

### **2.2 Bridge**

```python
class DrawingAPI:
    def draw_circle(self, x, y, r):
        pass

class API1(DrawingAPI):
    def draw_circle(self, x, y, r):
        print(f"API1 circle at ({x},{y}) radius {r}")

class Circle:
    def __init__(self, x, y, r, api):
        self.x, self.y, self.r, self.api = x, y, r, api

    def draw(self):
        self.api.draw_circle(self.x, self.y, self.r)

circle = Circle(1, 2, 3, API1())
circle.draw()  # API1 circle at (1,2) radius 3
```

---

### **2.3 Composite**

```python
class Component:
    def display(self): pass

class Leaf(Component):
    def __init__(self, name): self.name = name
    def display(self): print(self.name)

class Composite(Component):
    def __init__(self): self.children = []
    def add(self, child): self.children.append(child)
    def display(self):
        for child in self.children: child.display()

leaf1 = Leaf("Leaf1")
leaf2 = Leaf("Leaf2")
comp = Composite()
comp.add(leaf1)
comp.add(leaf2)
comp.display()
```

---

### **2.4 Decorator**

```python
def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

@make_bold
def greet(): return "Hello!"

print(greet())  # <b>Hello!</b>
```

---

### **2.5 Facade**

```python
class CPU:
    def start(self): print("CPU started")

class Memory:
    def load(self): print("Memory loaded")

class Computer:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
    def start(self):
        self.cpu.start()
        self.memory.load()

computer = Computer()
computer.start()
```

---

### **2.6 Flyweight**

```python
class Flyweight:
    def __init__(self, shared_state):
        self.shared_state = shared_state

    def operation(self, unique_state):
        print(f"Shared: {self.shared_state}, Unique: {unique_state}")

fw = Flyweight("Tree")
fw.operation("Oak")
fw.operation("Pine")
```

---

### **2.7 Proxy**

```python
class RealImage:
    def __init__(self, filename):
        self.filename = filename
        self.load()

    def load(self):
        print(f"Loading {self.filename}")

    def display(self):
        print(f"Displaying {self.filename}")

class ProxyImage:
    def __init__(self, filename):
        self.real_image = None
        self.filename = filename

    def display(self):
        if not self.real_image:
            self.real_image = RealImage(self.filename)
        self.real_image.display()

img = ProxyImage("photo.jpg")
img.display()  # Loads and displays
img.display()  # Only displays
```

---

## **3. Behavioral Patterns**

### **3.1 Chain of Responsibility**

```python
class Handler:
    def __init__(self, successor=None): self.successor = successor
    def handle(self, request):
        if self.successor: self.successor.handle(request)

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request < 10:
            print("Handler1 handled", request)
        else:
            super().handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request >= 10:
            print("Handler2 handled", request)
        else:
            super().handle(request)

h1 = ConcreteHandler1(ConcreteHandler2())
h1.handle(5)
h1.handle(15)
```

---

### **3.2 Command**

```python
class Command:
    def execute(self): pass

class Light:
    def on(self): print("Light ON")
    def off(self): print("Light OFF")

class LightOnCommand(Command):
    def __init__(self, light): self.light = light
    def execute(self): self.light.on()

light = Light()
cmd = LightOnCommand(light)
cmd.execute()  # Light ON
```

---

### **3.3 Interpreter**

```python
class Expression:
    def interpret(self, context): pass

class Number(Expression):
    def __init__(self, number): self.number = number
    def interpret(self, context): return self.number

class Add(Expression):
    def __init__(self, left, right):
        self.left, self.right = left, right
    def interpret(self, context):
        return self.left.interpret(context) + self.right.interpret(context)

expr = Add(Number(5), Number(3))
print(expr.interpret(None))  # 8
```

---

### **3.4 Iterator**

```python
class MyCollection:
    def __init__(self, items): self.items = items
    def __iter__(self): return iter(self.items)

for item in MyCollection([1,2,3]):
    print(item)
```

---

### **3.5 Mediator**

```python
class Mediator:
    def notify(self, sender, event): pass

class ConcreteMediator(Mediator):
    def __init__(self, component1, component2):
        self.component1, self.component2 = component1, component2
        component1.mediator = self
        component2.mediator = self
    def notify(self, sender, event):
        if sender == self.component1 and event == "A":
            print("Mediator reacts to A")
            self.component2.do_B()

class Component:
    def __init__(self): self.mediator = None

class Component1(Component):
    def do_A(self): self.mediator.notify(self, "A")

class Component2(Component):
    def do_B(self): print("Component2 does B")

c1, c2 = Component1(), Component2()
mediator = ConcreteMediator(c1, c2)
c1.do_A()
```

---

### **3.6 Memento**

```python
class Memento:
    def __init__(self, state): self.state = state

class Originator:
    def __init__(self, state): self.state = state
    def save(self): return Memento(self.state)
    def restore(self, memento): self.state = memento.state

origin = Originator("State1")
memento = origin.save()
origin.state = "State2"
origin.restore(memento)
print(origin.state)  # State1
```

---

### **3.7 Observer**

```python
class Subject:
    def __init__(self): self._observers = []
    def attach(self, observer): self._observers.append(observer)
    def notify(self, msg):
        for obs in self._observers: obs.update(msg)

class Observer:
    def __init__(self, name): self.name = name
    def update(self, msg): print(f"{self.name} got {msg}")

sub = Subject()
o1, o2 = Observer("A"), Observer("B")
sub.attach(o1); sub.attach(o2)
sub.notify("Hello")  # A got Hello, B got Hello
```

---

### **3.8 State**

```python
class State:
    def handle(self): pass

class ConcreteStateA(State):
    def handle(self): print("State A handling")

class ConcreteStateB(State):
    def handle(self): print("State B handling")

class Context:
    def __init__(self, state): self.state = state
    def request(self): self.state.handle()

context = Context(ConcreteStateA())
context.request()  # State A handling
context.state = ConcreteStateB()
context.request()  # State B handling
```

---

### **3.9 Strategy**

```python
class Strategy:
    def do_operation(self, a, b): pass

class Add(Strategy):
    def do_operation(self, a, b): return a + b

class Multiply(Strategy):
    def do_operation(self, a, b): return a * b

class Context:
    def __init__(self, strategy): self.strategy = strategy
    def execute(self, a, b): return self.strategy.do_operation(a, b)

context = Context(Add())
print(context.execute(3,4))  # 7
context.strategy = Multiply()
print(context.execute(3,4))  # 12
```

---

### **3.10 Template Method**

```python
from abc import ABC, abstractmethod

class Game(ABC):
    def play(self):
        self.start()
        self.play_game()
        self.end()

    @abstractmethod
    def start(self): pass
    @abstractmethod
    def play_game(self): pass
    @abstractmethod
    def end(self): pass

class Football(Game):
    def start(self): print("Football started")
    def play_game(self): print("Playing football")
    def end(self): print("Football ended")

game = Football()
game.play()
```

---

### **3.11 Visitor**

```python
class Visitor:
    def visit(self, element): pass

class Element:
    def accept(self, visitor): visitor.visit(self)

class ConcreteElement(Element):
    def operation(self): print("Element operation")

class ConcreteVisitor(Visitor):
    def visit(self, element): element.operation()

element = ConcreteElement()
visitor = ConcreteVisitor()
element.accept(visitor)  # Element operation
```

This gives you **all 23 GoF patterns in Python**, each with a **short, functional example**.


---

# **Design Patterns Mind Map**

### **Center Node:** **Design Patterns**

---

## **1. Creational Patterns**

**Goal:** Object creation control & flexibility

* **Singleton** – Only one instance
* **Factory Method** – Subclass decides which class to instantiate
* **Abstract Factory** – Creates families of related objects
* **Builder** – Step-by-step object construction
* **Prototype** – Clone existing objects

---

## **2. Structural Patterns**

**Goal:** Object composition and relationships

* **Adapter** – Converts interface to expected form
* **Bridge** – Decouple abstraction from implementation
* **Composite** – Part-whole hierarchy
* **Decorator** – Add behavior dynamically
* **Facade** – Simplified interface to complex subsystem
* **Flyweight** – Share objects for efficiency
* **Proxy** – Control access to objects

---

## **3. Behavioral Patterns**

**Goal:** Object communication and responsibility

* **Chain of Responsibility** – Pass requests along a chain
* **Command** – Encapsulate requests as objects
* **Interpreter** – Grammar & expression evaluation
* **Iterator** – Sequential access without exposing internals
* **Mediator** – Centralized communication between objects
* **Memento** – Capture and restore object state
* **Observer** – Notify dependents of state changes
* **State** – Change behavior when internal state changes
* **Strategy** – Encapsulate interchangeable algorithms
* **Template Method** – Skeleton algorithm with overridable steps
* **Visitor** – Define operations on object structure elements

---

### **Visual Layout Suggestion:**

1. **Center:** "Design Patterns"
2. **First Layer (Branches):** Creational, Structural, Behavioral
3. **Second Layer (Sub-branches):** Each pattern name
4. **Optional:** Small note or symbol per pattern (e.g., ⚡ for Singleton, 🔧 for Builder)

---



