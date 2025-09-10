ingredient = ["water", "milk", "tea leaves", "sugar", "ginger"]
ingredient.append("cup")
print(F"the ingredient are {ingredient}")
ingredient.remove("sugar")
print(F"the ingredient are {ingredient}")

subject = ["maths", "science", "english", "hindi", "history"]
marks = [90, 80, 70, 60, 50]

subject.extend(marks)
print(f"the subject and marks are {subject}")

subject.reverse()
print(f"the subject and marks are {subject}")