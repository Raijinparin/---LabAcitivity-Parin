def tower_of_hanoi(n, source, target, auxiliary):
    """Recursive solution for Tower of Hanoi."""
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, target, source)

# Main program
def main():
    try:
        n = int(input("Enter number of disks: "))

        if n <= 0:
            print("Error: Please enter a positive integer only.")
            return

        print(f"\nTower of Hanoi solution for {n} disks:\n")
        tower_of_hanoi(n, 'A', 'C', 'B')
    except ValueError:
        print("Error: Invalid input. Please enter an integer only.")

if __name__ == "__main__":
    main()
