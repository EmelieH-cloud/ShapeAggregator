import math
import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from shapes import Circle, Rectangle, Triangle, Square, shape_factory

def test_circle_area():
    c = Circle(radius=1)
    assert math.isclose(c.area(), math.pi)

def test_rectangle_area():
    r = Rectangle(width=2, height=3)
    assert r.area() == 6

def test_triangle_area():
    t = Triangle(base=4, height=5)
    assert t.area() == 10

def test_square_area():
    s = Square(side=4)
    assert s.area() == 16

def test_shape_factory_circle():
    data = {"type": "circle", "radius": 3}
    shape = shape_factory(data)
    assert isinstance(shape, Circle)
    assert math.isclose(shape.area(), math.pi * 9)

def test_shape_factory_unknown():
    data = {"type": "hexagon", "side": 2}
    with pytest.raises(ValueError):
        shape_factory(data)
