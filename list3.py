Write a Python Program to find the largest number in a list
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
6
size = int(input("Enter the size of the list: "))

# Initialize an empty list
elements = []

# Get the elements of the list from the user
for _ in range(size):
    element = int(input("Enter an element: "))
    elements.append(element)

# Find the largest element in the list
largest_element = max(elements)

# Print the largest element
print(largest_element)
