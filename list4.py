Write a Python Program to put the even and odd elements in a list into two different lists.
Input format:
Input consists of one integer and one list.
First input consists of the size of the list.
Second input consists of the elements based on the size.
Output format:
Output consists of two lists.
First list consists of all the even numbers in the list.
Second list consists of all the odd numbers in the list.
Sample Input:
5
1
2
3
6
5
Sample Output:
The even list [2, 6]
The odd list [1, 3, 5]
def separate_even_odd(size, elements):
    even_list = []
    odd_list = []
    
    for number in elements:
        if number % 2 == 0:
            even_list.append(number)
        else:
            odd_list.append(number)
    
    return even_list, odd_list

# Main function to take input and display output
def main():
    size = int(input("Enter the size of the list: "))
    elements = []
    
    print("Enter the elements:")
    for _ in range(size):
        elements.append(int(input()))
    
    even_list, odd_list = separate_even_odd(size, elements)
    
    print("The even list", even_list)
    print("The odd list", odd_list)

# Run the program
if __name__ == "__main__":
    main()
