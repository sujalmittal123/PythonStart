menu = ["chowmein","pasta","haaka nodddles","fried rice"]
# emuerate function adds a counter to an iterable and returns it in a form of enumerate object
# which can be directly used in for loops or be converted into a list of tuples using list() method
for idx ,item in enumerate(menu,start=1):# idx is the index of the item and item that present in the list 
    print(f"{idx}. {item} order now") 