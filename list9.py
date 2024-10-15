Write a program to print the given list in reverse order.
Sample Input:
10 20 30 40 50
Sample Output:
50 40 30 20 10 
10)Write a program to sort the given list and print it.
Sample Input:
30 20 10 50 40
Sample Output:
10 20 30 40 50 
def print_reverse(elements):
    reversed_list = elements[::-1]
    print(" ".join(map(str, reversed_list)))

# Main function to take input
def main():
    # Input the list elements
    elements = list(map(int, input("Enter the list elements separated by space: ").split()))
    
    # Print the list in reverse order
    print_reverse(elements)

# Run the program
if __name__ == "__main__":
    main()

