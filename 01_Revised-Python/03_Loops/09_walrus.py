value = 13

if (remainder := value %5):
    print(f"Not divisible, remainder is {remainder}")


available_sizes = ["small", "medium", "large"]

if(requested_size := input("Enter your chai cup size: ")) in available_sizes:
    print(f"Serving {requested_size}")
else:
    print(f"Size is unavailabel - {requested_size}")

flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors)

while (flavor :=input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available.")
print(f"YOu choose {flavor} chai!")