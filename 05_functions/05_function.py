#nonlocal bean from inside to inside function we are just targeting outside function
def update_kitchen():
    spice_type ="chilli"
    def new_kitechen ():
        nonlocal spice_type
        spice_type ="cumin"
    new_kitechen()
    print(f"spice type inside kitchen is {spice_type}")
update_kitchen()
