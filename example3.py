# Example dictionary
author = {"name": "Hank", "color": "green", "shape": "circle"}

# A list of colors
colors = ["blue", "green", "red"]

# A list of dictionaries 
favorite_colors = [
                        {
                            "student": "Mary",
                            "color": "red"
                        },
                        {
                            "student": "John",
                            "color": "blue"
                        }
]

# Entry point for program
if __name__ == "__main__":
    print("The author name is {}.".format(author["name"]))
    print("His favorite color is {}.".format(author["color"]))
    print("His favorite shape is {}.".format(author["shape"]))
    print("")

print("The current colors are")
for color in colors:
    print(color)
print("")

# Ask user for favorite color and compare to the author's
new_color = input("What is your favorite color? ")
if new_color == author["color"]:
    print("You have the same favorite color as {}.".format(author["name"]))
else: 
    print("Your favorite color is different from {}'s".format(author["name"]))    
    print("")

# See if this is a new color for the list 
if new_color not in colors:
    print("That is a new colors, adding it to the list!")
    colors.append(new_color)
    # Print update message about the new colors list
    message = ("There are now {} colors in the list. ".format(len(colors)))
    message += "The color you added was {}.".format(colors[3])
    print(message)
else:
    pass