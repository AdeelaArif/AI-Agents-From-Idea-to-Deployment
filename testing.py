"""
Testing file for Git version control practice
"""

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Add two numbers"""
    return a + b

def main():
    print("Testing Git Version Control")
    print("-" * 40)
    
    # Test greeting
    message = greet("Adeela")
    print(message)
    
    # Test addition
    result = add_numbers(5, 3)
    print(f"5 + 3 = {result}")
    
    print("\nThis is version 1 of the testing file")

if __name__ == "__main__":
    main()
