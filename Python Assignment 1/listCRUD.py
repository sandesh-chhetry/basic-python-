##Exercise 5. Create a list of any arbitrary elements. Your code should show the list methods as
##pop, insert and remove.

##list which contain some element
elements = ["1st position", "2nd position", "3rd position", "4th position", "5th position", "6th position"]
print("initial list")
print(elements)
print("list after pop 2nd element " + elements.pop(2))
print(elements)

print("list after insert new value as new element")
print(elements.insert(2, "new element"))
print(elements)

print("list after removing priviously inserted value")
print(elements.remove('new element'))
print(elements)
