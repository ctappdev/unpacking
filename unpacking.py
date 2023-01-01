from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    job: str


def parameter_calculate_number(a: int, b: int) -> int:
    return int(a + b)


def args_calculate_number(*args) -> int:
    result: int = 0
    for x in args:
        result += x
    return result


def kwargs_calculate_number(**kwargs) -> int:
    result: int = 0
    for x in kwargs.values():
        result += x
    return result


def unpack_calculate_number(a: int, b: int, c: int, d: int = 0) -> int:
    return a + b + c + d


# Function call with standard parameters
print(f"Parameter Calculated Number {parameter_calculate_number(3, 4)}")

# Function call with *args parameters
print(f"Args Calculated Number {args_calculate_number(3, 4, 5)}")

# Function call with *kwargs parameters
print(f"Kwargs Calculated Number {kwargs_calculate_number(a = 3, b = 4, c = 5)}")

# Function to unpack parameters from a dict
adict: dict = {"a": 1, "b": 2, "c": 3}
print(f"Unpack dict Calculated Number {unpack_calculate_number(**adict)}")

# Function to unpack parameters from a list
alist: list = [1, 2, 3, 4]
print(f"Unpack list Calculated Number {unpack_calculate_number(*alist)}")

# Function to unpack parameters from a tuple
atuple: tuple = (1, 2, 3)
print(f"Unpack tuple Calculated Number {unpack_calculate_number(*atuple)}")

person1 = Person("Leon", 53, "Programmer")
print(f"Unpack Dataclass person one {person1}")

dict_person2 = {"name": "Elzahn", "age": 32, "job": "Coach"}
person2 = Person(**dict_person2)
print(f"Unpack dict person two {person2}")

list_person3 = ["Elzahn", 32, "Coach"]
person3 = Person(*list_person3)
print(f"Unpack list person two {person3}")

tuple_person4 = ("Elzahn", 32, "Coach")
person4 = Person(*tuple_person4)
print(f"Unpack tuple person two {person4}")
