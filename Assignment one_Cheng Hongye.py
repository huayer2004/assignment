import os
import sys
import subprocess

# Auto-install and import ColabTurtlePlus for Colab environment or turtle for py
try:
    import google.colab
    IS_COLAB = True
except ImportError:
    IS_COLAB = False

if IS_COLAB:
    try:
        import ColabTurtlePlus.Turtle as turtle
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "ColabTurtlePlus"])
        import ColabTurtlePlus.Turtle as turtle
else:
    import turtle

def clear_screen():
    """Clear terminal or Colab notebook output."""
    if IS_COLAB:
        from google.colab import output
        output.clear()
    else:
        cmd = 'cls' if os.name == 'nt' else 'clear'
        subprocess.run(cmd, shell=True)

# ================================================================
# Task 1: Calculator
# ================================================================

def get_number(prompt):
    """Prompt user for a valid numerical input."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number!")

def get_operator():
    """Prompt user for a valid arithmetic operator."""
    operators = ['+', '-', '*', '/']
    while True:
        op = input("Operator (+, -, *, /): ").strip()
        if op in operators:
            return op
        print("Invalid operator!")

def calculate(num1, num2, operator):
    """Perform basic arithmetic operations."""
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return "Error: Div by zero!" if num2 == 0 else num1 / num2

def run_calculator():
    """Main execution loop for calculator."""
    while True:
        clear_screen()
        print("=== CALCULATOR ===")
        
        num1 = get_number("Num 1: ")
        num2 = get_number("Num 2: ")
        op = get_operator()

        res = calculate(num1, num2, op)
        print(f"\nResult: {num1} {op} {num2} = {res}")

        print("\n1. Calculate Again")
        print("2. Back to Main Menu")
        choice = input("Choice (1-2): ").strip()
        
        if choice == '2':
            break

# ================================================================
# Task 2: QA Bot
# ================================================================

def run_qa_bot():
    """Main execution loop for QA Bot."""
    while True:
        clear_screen()
        print("=== QA BOT ===")
        print('Ask for: "hello", "python", "jetson", "ai", "name"')
        print("1. hello")
        print("2. python")
        print("3. jetson")
        print("4. ai")
        print("5. name")
        print("6. Back to Main Menu")

        choice = input("\nChoice (1-6): ").strip()

        if choice == '1':
            print("\nA: Hello! How can I help?")
        elif choice == '2':
            print("\nA: Python is a popular programming language.")
        elif choice == '3':
            print("\nA: NVIDIA Jetson is an embedded AI platform.")
        elif choice == '4':
            print("\nA: AI simulates human intelligence in machines.")
        elif choice == '5':
            print("\nA: I'm Q-Bot!")
        elif choice == '6':
            break
        else:
            print("\nInvalid choice!")

        input("\nPress ENTER to continue...")

# ================================================================
# Task 3: Turtle Drawing 
# ================================================================

def run_turtle_drawing():
    """Main execution loop for Turtle graphics with enhanced drawing logic."""
    
    def draw_square(length=100, color="cyan"):
        turtle.color(color)
        turtle.penup()
        turtle.goto(-length / 2, length / 2)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(length)
            turtle.right(90)
        turtle.end_fill()

    def draw_triangle(length=120, color="yellow"):
        turtle.color(color)
        turtle.penup()
        turtle.goto(-length / 2, -length / 3)
        turtle.pendown()
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(length)
            turtle.left(120)
        turtle.end_fill()

    def draw_star(r=80, color="magenta"):
        import math
        turtle.color(color)
        turtle.penup()
        # Calculate 10 points (5 outer vertices, 5 inner vertices)
        r_inner = r * 0.382
        points = []
        for i in range(10):
            radius = r if i % 2 == 0 else r_inner
            angle = math.radians(90 - i * 36)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            points.append((x, y))
            
        turtle.goto(points[0])
        turtle.pendown()
        turtle.begin_fill()
        for pt in points[1:]:
            turtle.goto(pt)
        turtle.goto(points[0])
        turtle.end_fill()

    def draw_color_spiral(turns=60):
        """Draws a multi-colored spiral expanding in length."""
        colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "magenta"]
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        for i in range(turns):
            turtle.color(colors[i % len(colors)])
            turtle.forward(i * 3)
            turtle.right(59)

    def draw_flower(petals=6, radius=70):
        """Draws a realistic flower with dual-arc petals and a central core."""
        colors = ["red", "orange", "pink", "magenta", "purple", "cyan"]
        
        # 1. Draw Petals
        for i in range(petals):
            turtle.color(colors[i % len(colors)])
            turtle.penup()
            turtle.goto(0, 0)
            turtle.setheading(i * (360 / petals))
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(radius, 60)
            turtle.left(120)
            turtle.circle(radius, 60)
            turtle.end_fill()
            
        # 2. Draw Yellow Flower Center
        turtle.penup()
        turtle.goto(0, -15)
        turtle.setheading(0)
        turtle.color("yellow")
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(15)
        turtle.end_fill()

    while True:
        clear_screen()
        print("=== TURTLE DRAWING ===")
        print("1. Square")
        print("2. Triangle")
        print("3. Star")
        print("4. Color Spiral")
        print("5. Flower")
        print("6. Back to Main Menu")
        
        choice = input("\nChoice (1-6): ").strip()

        if choice == '6':
            break

        # Canvas Initialization
        if IS_COLAB:
            turtle.clearscreen()
            turtle.initializeTurtle(window=(400, 400))
            turtle.speed(10)
        else:
            try:
                turtle.clearscreen()
            except turtle.Terminator:
                turtle.TurtleScreen._RUNNING = True
                turtle.resetscreen()
            turtle.speed(0)
            
        turtle.pensize(2)
        turtle.hideturtle()

        if choice == '1':
            draw_square()
        elif choice == '2':
            draw_triangle()
        elif choice == '3':
            draw_star()
        elif choice == '4':
            draw_color_spiral()
        elif choice == '5':
            draw_flower()
        else:
            print("Invalid choice!")
            input("\nPress ENTER to continue...")
            continue

        input("\nPress ENTER to continue...")

# ================================================================
# Main Menu
# ================================================================

def main_menu():
    """Main program navigation menu."""
    while True:
        clear_screen()
        print("=== MAIN MENU ===")
        print("1. Calculator")
        print("2. QA Bot")
        print("3. Turtle Drawing")
        print("4. Exit")
        
        choice = input("\nChoice (1-4): ").strip()

        if choice == '1':
            run_calculator()
        elif choice == '2':
            run_qa_bot()
        elif choice == '3':
            run_turtle_drawing()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")
            input("\nPress ENTER to continue...")

# ================================================================
# Entry Point
# ================================================================

if __name__ == "__main__":
    main_menu()
