# Step 1: Create a list of 10 integers
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Initial List:", my_list)

# Append an element to the list
my_list.append(110)
print("After appending 110:", my_list)

#  Insert an element at a specific position (e.g., index 2)
my_list.insert(2, 25)
print("After inserting 25 at index 2:", my_list)

# Remove an element from the list (e.g., value 60)
my_list.remove(60)
print("After removing 60:", my_list)

# Pop an element from a specific position (e.g., index 4)
popped_element = my_list.pop(4)
print(f"After popping element at index 4 ({popped_element}):", my_list)
