# in this we going to discuss nestes scopes of variable and global scopes

def chai_order():
    chai_name ="gingerchai"#enclosing
    def print_order():
        chai_name ="masala chai"

        print(f"order for {chai_name} is ready")
    print_order()
    print(f"order for {chai_name} is ready")

chai_name ="black chai"
chai_order()
print(f"order for{chai_name} is ready")