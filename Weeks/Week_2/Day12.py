#Local and Global Scopes
enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function:{enemies}")

increase_enemies()
print(f"enemies outside funftion: {enemies}")

# Local scopes exist within the function.
# Global scopes exist outide the function.

# Modifying Global Scopes
enemies = 1

def increase_enemies():
    global enemies # Explicitly define that there is a global variable
    enemies += 1
    print(f"enemies inside function:{enemies}")

increase_enemies()
print(f"enemies outside funftion: {enemies}")

# You capitalise the name of the variables that you are NEVER going to change e.g pi = 3.14159
