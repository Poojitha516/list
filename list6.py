Write a Python Program to find the smallest number in a list
Input & Output Format:
Input consists of one list and one integer.
First input consists of a size of a list.
Second inputs corresponds to the size of the list.
Output consists of the largest element.
Sample Input:
5
1
2
3
6
5
Sample Output:
1
# Function to find the smallest number in a list
def find_smallest(elements):
    return min(elements)

# Main function to take input and display output
def main():
    # Input the size of the list
    size = int(input("Enter the size of the list: "))
    
    elements = []
    
    print("Enter the elements:")
    for _ in range(size):
        elements.append(int(input()))
    
    # Find the smallest number
    smallest_number = find_smallest(elements)
    
    # Print the result
    print(smallest_number)

# Run the program
if __name__ == "__main__":
    main()
