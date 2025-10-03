def serve_chai():
    chai_type = "Masala" ## local scope
    print(f"Inside function {chai_type}")

chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}")
