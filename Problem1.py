def gcd(a, b):

    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def lcm(a, b):

    return (a * b) // gcd(a, b)

# Main program
def main():
    try:
        x = int(input("Enter a value for x: "))
        y = int(input("Enter a value for y: "))

        if x <= 0 or y <= 0:
            print("Error: Please enter positive integers only.")
            return

        print(f"The LCM of {x} and {y} is = {lcm(x, y)}")
    except ValueError:
        print("Error: Invalid input. Please enter integers only.")

if __name__ == "__main__":
    main()
