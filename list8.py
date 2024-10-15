Write a program to count the number of times the given value is repeated.
Input Format:
First line of input consists of our list elements.
Second line of input consists of value to count.
Output Format:
Print thr number of times the given value is repeated in the list.
Sample Input:
10 20 10 40 10
10
Sample Output:
3
def count_occurrences(elements, target):
    return elements.count(target)

# Main function to take input and display output
def main():
    # Input the list elements
    elements = list(map(int, input("Enter the list elements separated by space: ").split()))
    
    # Input the value to count
    target = int(input("Enter the value to count: "))
    
    # Count occurrences
    count = count_occurrences(elements, target)
    
    # Print the result
    print(count)

# Run the program
if __name__ == "__main__":
    main()
