**Java cheat sheet for all 23 GoF design patterns**, mirroring the Python one but in Java syntax. I’ll keep each example **concise and ready to use**.

---

# **Java Design Patterns Cheat Sheet**

## **1. Creational Patterns**

### **1.1 Singleton**

```java
class Singleton {
    private static Singleton instance;
    private Singleton() {}
    public static Singleton getInstance() {
        if (instance == null) instance = new Singleton();
        return instance;
    }
}
```

---

### **1.2 Factory Method**

```java
interface Shape { void draw(); }
class Circle implements Shape { public void draw() { System.out.println("Circle"); } }
class Square implements Shape { public void draw() { System.out.println("Square"); } }

class ShapeFactory {
    public static Shape getShape(String type) {
        if(type.equals("circle")) return new Circle();
        else return new Square();
    }
}

// Usage
Shape s = ShapeFactory.getShape("circle");
s.draw();
```

---

### **1.3 Abstract Factory**

```java
interface Animal { void speak(); }
class Dog implements Animal { public void speak() { System.out.println("Woof"); } }
class Cat implements Animal { public void speak() { System.out.println("Meow"); } }

interface AnimalFactory { Animal createAnimal(); }
class DogFactory implements AnimalFactory { public Animal createAnimal() { return new Dog(); } }
class CatFactory implements AnimalFactory { public Animal createAnimal() { return new Cat(); } }

// Usage
AnimalFactory factory = new DogFactory();
Animal pet = factory.createAnimal();
pet.speak();
```

---

### **1.4 Builder**

```java
class House {
    String walls;
    String roof;
    public void show() { System.out.println("House with " + walls + " and " + roof); }
}

class HouseBuilder {
    House house = new House();
    public HouseBuilder buildWalls(String walls) { house.walls = walls; return this; }
    public HouseBuilder buildRoof(String roof) { house.roof = roof; return this; }
    public House getResult() { return house; }
}

// Usage
House house = new HouseBuilder().buildWalls("Brick").buildRoof("Tile").getResult();
house.show();
```

---

### **1.5 Prototype**

```java
class Prototype implements Cloneable {
    int value;
    Prototype(int v){ value=v; }
    public Prototype clone() throws CloneNotSupportedException { return (Prototype) super.clone(); }
}

// Usage
Prototype p1 = new Prototype(10);
Prototype p2 = p1.clone();
System.out.println(p2.value);
```

---

## **2. Structural Patterns**

### **2.1 Adapter**

```java
class EuropeanPlug { int voltage() { return 220; } }
interface USPlug { int voltage(); }
class Adapter implements USPlug {
    EuropeanPlug plug;
    Adapter(EuropeanPlug plug) { this.plug = plug; }
    public int voltage() { return 110; }
}
```

---

### **2.2 Bridge**

```java
interface DrawingAPI { void drawCircle(double x, double y, double r); }
class API1 implements DrawingAPI {
    public void drawCircle(double x, double y, double r) { System.out.println("API1 circle"); }
}
class Circle {
    double x,y,r; DrawingAPI api;
    Circle(double x,double y,double r,DrawingAPI api){this.x=x;this.y=y;this.r=r;this.api=api;}
    void draw(){ api.drawCircle(x,y,r); }
}
```

---

### **2.3 Composite**

```java
interface Component { void display(); }
class Leaf implements Component {
    String name;
    Leaf(String n){name=n;}
    public void display(){ System.out.println(name); }
}
class Composite implements Component {
    List<Component> children = new ArrayList<>();
    void add(Component c){ children.add(c); }
    public void display(){ for(Component c: children) c.display(); }
}
```

---

### **2.4 Decorator**

```java
interface Component { void operation(); }
class ConcreteComponent implements Component {
    public void operation(){ System.out.println("ConcreteComponent"); }
}
class Decorator implements Component {
    Component comp;
    Decorator(Component c){ this.comp = c; }
    public void operation(){ comp.operation(); System.out.println("Decorated"); }
}
```

---

### **2.5 Facade**

```java
class CPU { void start(){ System.out.println("CPU started"); } }
class Memory { void load(){ System.out.println("Memory loaded"); } }
class Computer {
    CPU cpu = new CPU(); Memory mem = new Memory();
    void start(){ cpu.start(); mem.load(); }
}
```

---

### **2.6 Flyweight**

```java
class Flyweight {
    private String shared;
    Flyweight(String s){ shared=s; }
    void operation(String unique){ System.out.println(shared + " " + unique); }
}
```

---

### **2.7 Proxy**

```java
interface Image { void display(); }
class RealImage implements Image {
    String filename;
    RealImage(String f){ filename=f; load(); }
    void load(){ System.out.println("Loading "+filename); }
    public void display(){ System.out.println("Displaying "+filename); }
}
class ProxyImage implements Image {
    RealImage realImage;
    String filename;
    ProxyImage(String f){ filename=f; }
    public void display(){
        if(realImage==null) realImage=new RealImage(filename);
        realImage.display();
    }
}
```

---

## **3. Behavioral Patterns**

### **3.1 Chain of Responsibility**

```java
abstract class Handler {
    Handler successor;
    void setSuccessor(Handler s){ successor=s; }
    abstract void handle(int request);
}
class ConcreteHandler1 extends Handler {
    void handle(int request){
        if(request<10) System.out.println("Handler1 handled");
        else if(successor!=null) successor.handle(request);
    }
}
class ConcreteHandler2 extends Handler {
    void handle(int request){
        if(request>=10) System.out.println("Handler2 handled");
        else if(successor!=null) successor.handle(request);
    }
}
```

---

### **3.2 Command**

```java
interface Command { void execute(); }
class Light { void on(){System.out.println("Light ON");} }
class LightOnCommand implements Command {
    Light light; LightOnCommand(Light l){light=l;}
    public void execute(){ light.on(); }
}
```

---

### **3.3 Interpreter**

```java
interface Expression { int interpret(); }
class Number implements Expression {
    int number; Number(int n){number=n;}
    public int interpret(){ return number; }
}
class Add implements Expression {
    Expression left,right;
    Add(Expression l, Expression r){ left=l; right=r; }
    public int interpret(){ return left.interpret() + right.interpret(); }
}
```

---

### **3.4 Iterator**

```java
List<Integer> list = Arrays.asList(1,2,3);
Iterator<Integer> it = list.iterator();
while(it.hasNext()){ System.out.println(it.next()); }
```

---

### **3.5 Mediator**

```java
class Mediator {
    void notify(Component sender, String event){}
}
class Component {
    Mediator mediator;
    Component(Mediator m){ mediator=m; }
}
```

---

### **3.6 Memento**

```java
class Memento { String state; Memento(String s){state=s;} }
class Originator {
    String state;
    Memento save(){ return new Memento(state); }
    void restore(Memento m){ state=m.state; }
}
```

---

### **3.7 Observer**

```java
interface Observer { void update(String msg); }
class Subject {
    List<Observer> observers = new ArrayList<>();
    void attach(Observer o){ observers.add(o); }
    void notifyObservers(String msg){ for(Observer o: observers) o.update(msg); }
}
```

---

### **3.8 State**

```java
interface State { void handle(); }
class ConcreteStateA implements State { public void handle(){ System.out.println("A"); } }
class ConcreteStateB implements State { public void handle(){ System.out.println("B"); } }
class Context {
    State state;
    Context(State s){ state=s; }
    void request(){ state.handle(); }
}
```

---

### **3.9 Strategy**

```java
interface Strategy { int doOperation(int a,int b); }
class Add implements Strategy { public int doOperation(int a,int b){ return a+b; } }
class Multiply implements Strategy { public int doOperation(int a,int b){ return a*b; } }
class Context {
    Strategy strategy; Context(Strategy s){ strategy=s; }
    int execute(int a,int b){ return strategy.doOperation(a,b); }
}
```

---

### **3.10 Template Method**

```java
abstract class Game {
    void play(){ start(); playGame(); end(); }
    abstract void start(); abstract void playGame(); abstract void end();
}
class Football extends Game {
    void start(){ System.out.println("Football started"); }
    void playGame(){ System.out.println("Playing"); }
    void end(){ System.out.println("Football ended"); }
}
```

---

### **3.11 Visitor**

```java
interface Visitor { void visit(Element e); }
interface Element { void accept(Visitor v); }
class ConcreteElement implements Element {
    public void accept(Visitor v){ v.visit(this); }
    void operation(){ System.out.println("Element op"); }
}
class ConcreteVisitor implements Visitor {
    public void visit(Element e){ ((ConcreteElement)e).operation(); }
}
```

---

This gives a **ready-to-use Java reference** for all 23 patterns, similar to the Python cheat sheet.

