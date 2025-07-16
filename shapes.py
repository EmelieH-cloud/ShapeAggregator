from abc import ABC, abstractmethod
import math

# Internal registry for shape class mappings
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
    """
    Abstract base class for geometric shapes.
    All shapes must implement an area calculation method.
    """

    @abstractmethod
    def area(self) -> float:
        """Calculate and return the area of the shape.

        Returns:
           float: Computed area value.
        """
        pass


@register_shape("circle")
class Circle(Shape):
    """Circle shape defined by its radius."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius**2


@register_shape("rectangle")
class Rectangle(Shape):
    """Rectangle shape defined by width and height."""

    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height


@register_shape("triangle")
class Triangle(Shape):
    """Triangle shape defined by base and height."""

    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def area(self) -> float:
        return 0.5 * self.base * self.height


@register_shape("square")
class Square(Shape):
    """Square shape defined by one side length."""

    def __init__(self, side: float):
        self.side = side

    def area(self) -> float:
        return self.side * self.side
