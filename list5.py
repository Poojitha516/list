Write a program to find the sum of the elements in the array. 
Input Format: 
Input consists of n+1 integers where n corresponds to the number of elements in the array.
The first integer corresponds to n and the next n integers correspond to the elements in the array.
Assume that the maximum number of elements in the array is 20. 
Output Format: 
Output consists of a double value which corresponds to the mean of the array.
Refer sample input and output for formatting specifications.
Sample Input: 
5
2
4
1
3
1
Sample Output:
11
def sum_of_array(size, elements):
    return sum(elements)

# Main function to take input and display output
def main():
    # Input the number of elements
    n = int(input("Enter the number of elements in the array: "))
    
    # Ensure the number of elements does not exceed 20
    if n > 20:
        print("The maximum number of elements is 20.")
        return
    
    elements = []
    
    print("Enter the elements:")
    for _ in range(n):
        elements.append(int(input()))
    
    # Calculate the sum of the array
    total_sum = sum_of_array(n, elements)
    
    # Print the result
    print(total_sum)

# Run the program
if __name__ == "__main__":
    main()
