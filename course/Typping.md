# Python Type Hints - Introduction

## Overview
Python supports optional **type hints** (also called **type annotations**) that allow you to declare the type of variables. These hints enhance editor support, enable better code understanding, and improve tools' ability to catch errors.

FastAPI relies heavily on type hints, but understanding them is beneficial even if you aren't using FastAPI.

---

## Motivation

### Example: Without Type Hints

```python
# Python 3.8+
def get_full_name(first_name, last_name):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))  # Output: John Doe
```

The function:
1. Accepts `first_name` and `last_name`.
2. Converts the first letter to uppercase.
3. Concatenates them with a space.

Without type hints:
- **Editor autocomplete** doesn't work effectively.
- You might forget method names like `.title()`.

---

### Adding Type Hints

```python
# Python 3.8+
def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + " " + last_name.title()
    return full_name

print(get_full_name("john", "doe"))  # Output: John Doe
```

- **Syntax**: `parameter_name: type`
- **Benefits**:
  - Editors can provide autocompletion.
  - Tools can detect errors in parameter usage.

---

## More Motivations with Type Hints

### Error Detection Example
```python
# Python 3.8+
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + age  # Error
    return name_with_age
```

Without conversion, this throws an error. Type hints help the editor catch it.

**Fixed Version**:
```python
# Python 3.8+
def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age
```

---

## Declaring Types

### Simple Types
You can declare the following standard Python types:
- `str`
- `int`
- `float`
- `bool`
- `bytes`

```python
# Python 3.8+
def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_d, item_e
```

---

### Generic Types with Type Parameters

#### Lists
```python
# Python 3.9+
def process_items(items: list[str]):
    for item in items:
        print(item)
```
- `items` is a `list` of `str`.
- Editors can provide type-specific autocompletion for `item`.

#### Tuples and Sets
```python
# Python 3.9+
def process_items(items_t: tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s
```
- `items_t` is a tuple with types `int`, `int`, `str`.
- `items_s` is a set of `bytes`.

#### Dictionaries
```python
# Python 3.9+
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name, item_price)
```
- `prices` is a dictionary with `str` keys and `float` values.

---

### Union
Declare variables that can have multiple types.

```python
# Python 3.10+
def process_item(item: int | str):
    print(item)
```
- Equivalent to `Union[int, str]`.

---

### Optional
A variable can have a type or `None`.

```python
# Python 3.10+
def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")
```

- `Optional[str]` is a shortcut for `Union[str, None]`.

---

### Classes as Types
You can use a class as a type.

```python
# Python 3.8+
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name
```

---

### Pydantic Models
Pydantic validates and converts data while using type hints.

```python
# Python 3.8+
from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, "2", b"3"],
}
user = User(**external_data)
print(user)
```

---

### Annotated Types
Add metadata using `Annotated`.

```python
# Python 3.9+
from typing import Annotated

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"
```
- Editors ignore metadata, but FastAPI uses it to enhance functionality.

---


# Key Points

## Type Hints Overview
- Python supports **type hints** to declare variable types.
- Type hints improve editor support, enhance code readability, and help detect errors.
- FastAPI relies heavily on type hints for request validation and documentation.

## Benefits of Type Hints
- Enable autocompletion in editors.
- Allow static analysis tools to detect type mismatches.
- Enhance team collaboration by making the code more understandable.

## Common Use Cases
- Declare types for function parameters and return values.
- Use **simple types**: `str`, `int`, `float`, `bool`, `bytes`.
- Use **generic types**: `list`, `tuple`, `set`, `dict` with internal type parameters.
- Combine types using `Union` or `Optional`.

## Advanced Usage
- Use classes as types to ensure variables conform to specific object types.
- Use `Annotated` for adding metadata to type hints.
- Leverage **Pydantic** for data validation and conversion with FastAPI.

---

# Questions and Answers

### **Q1: What are Python type hints?**
**A:** Type hints are a way to declare the type of a variable, function parameter, or return value. They improve code clarity and allow tools to check for type correctness.

---

### **Q2: How do you declare a type hint for a function parameter?**
**A:** Use the colon (`:`) syntax. For example:
```python
def greet(name: str):
    return f"Hello, {name}!"
```

---

### **Q3: What are generic types?**
**A:** Generic types like `list`, `tuple`, `set`, and `dict` can hold elements of specific types. Example:
```python
def process_items(items: list[str]):
    for item in items:
        print(item)
```

---

### **Q4: How do you define a variable that can have multiple types?**
**A:** Use `Union` or the `|` operator (Python 3.10+). Example:
```python
def process_item(item: int | str):
    print(item)
```

---

### **Q5: What is the difference between `Optional` and `Union`?**
**A:** `Optional[Type]` is equivalent to `Union[Type, None]`. Both indicate that a value can either have the specified type or be `None`.

---

### **Q6: How do type hints work with classes?**
**A:** You can specify a class as a type to enforce that a variable is an instance of that class. Example:
```python
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(person: Person):
    return person.name
```

---

### **Q7: What is Pydantic, and how does it relate to type hints?**
**A:** Pydantic is a library for data validation and conversion. It uses type hints in class attributes to validate and structure incoming data.

---

### **Q8: What are the benefits of using `Annotated` in type hints?**
**A:** `Annotated` allows you to add metadata to type hints. While Python itself ignores the metadata, tools like FastAPI use it to provide enhanced functionality.

---

### **Q9: Why is FastAPI built on type hints?**
**A:** FastAPI uses type hints to:
- Validate incoming requests.
- Convert data types.
- Automatically generate API documentation.

---

### **Q10: What happens if you don’t use type hints?**
**A:** Without type hints:
- Editors can’t provide accurate autocompletion.
- Static analysis tools can’t detect type mismatches.
- Code may be harder to understand and debug.


## Summary
Type hints:
1. Improve code readability.
2. Provide better editor and tool support.
3. Help in error detection.
4. Allow FastAPI to validate and document APIs.

FastAPI leverages type hints to streamline request validation, data conversion, and API documentation.