
name = "laiba"
print( "My name is " + name )
print( "My name is {}".format (name) )
print( f"My name is {name}" )




user_name = input("What's your name ? ")
user_age = int(input( "What's your age ? " ))
print(f"Hello, {user_name}! You are {user_age} years old.")



print("Welcome to Madlibs! Fill in the blanks to create your own story. 😊")
noun1 = input("Enter a noun: ")
verb_past = input("Enter a verb (past tense): ")
adjective = input("Enter an adjective: ")
place = input("Enter a place: ")
noun2 = input("Enter another noun: ")
story = f"""
One day, a {adjective} {noun1} went to {place}. 
It {verb_past} all the way there and found a mysterious {noun2}. 
What happened next? Only you can imagine!
"""

print("\nHere's your story:")
print(story)
