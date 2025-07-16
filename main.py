import argparse
import json
import sys
from collections import Counter

from shapes import shape_factory


def main():
    """
    Entry point for the shape aggregator CLI.

    Parses JSON input from a file, creates shape objects,
    computes total area, and prints the result to stdout and area.txt.
    Also outputs the count of each shape type.

    Exits on file or JSON errors.
    """
    parser = argparse.ArgumentParser(description="Calculate total area of shapes.")
    parser.add_argument("--file", required=True, help="Path to input JSON file.")
    args = parser.parse_args()

    try:
        with open(args.file, "r") as f:
            shape_data = json.load(f)
    except FileNotFoundError:
        print("Error: File not found.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.", file=sys.stderr)
        sys.exit(1)

    shapes = []
    for item in shape_data:
        try:
            shape = shape_factory(item)
            shapes.append(shape)
        except Exception as e:
            print(f"Skipping invalid shape: {e}", file=sys.stderr)

    total_area = sum(shape.area() for shape in shapes)
    formatted = f"Total area: {total_area:.1f}"

    print(formatted)
    with open("area.txt", "w") as f:
        f.write(formatted + "\n")

    shape_types = [type(shape).__name__ for shape in shapes]
    counts = Counter(shape_types)
    for shape_name, count in counts.items():
        print(f"{shape_name}: {count}")


if __name__ == "__main__":
    main()
