from abc import ABC, abstractmethod
import math

_shape_registry = {}

def register_shape(name):
    """Decorator to register a shape class with a given name."""
    def decorator(cls):
        _shape_registry[name] = cls
        return cls
    return decorator

def shape_factory(data: dict):
    """Create a Shape instance from dict, based on registered shapes.

    Args:
        data (dict): Dict with 'type' and shape parameters.

    Returns:
        Shape: Instance of a registered shape class.

    Raises:
        ValueError: If shape type is unknown.
    """
    shape_type = data.get("type")
    cls = _shape_registry.get(shape_type)
    if cls is None:
        raise ValueError(f"Unknown shape type: {shape_type}")
    params = {k: v for k, v in data.items() if k != "type"}
    return cls(**params)

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape."""
        pass

@register_shape("circle")
class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2

@register_shape("rectangle")
class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

@register_shape("triangle")
class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height

@register_shape("square")
class Square(Shape):
    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side
