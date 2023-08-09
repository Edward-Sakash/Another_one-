global_var = "This is a global variable"  # Define a global variable

def outer_function():
    outer_var = "This is an outer variable"  # Define a variable in outer_function's scope
    
    def inner_function():
        inner_var = "This is an inner variable"  # Define a variable in inner_function's scope
        print("Inside inner_function:")
        print("global_var:", global_var)  # Access the global variable
        print("outer_var:", outer_var)    # Access the outer variable
        print("inner_var:", inner_var)    # Access the inner variable
    
    print("Inside outer_function:")
    print("global_var:", global_var)  # Access the global variable
    print("outer_var:", outer_var)    # Access the outer variable
    inner_function()                  # Call the inner_function

# Print the values of variables in global scope
print("In global scope:")
print("global_var:", global_var)

# Call the outer_function to start the scope exploration
outer_function()
