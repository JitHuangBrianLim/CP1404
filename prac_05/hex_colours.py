COLOURS = {"absolutezero": "#0048ba", "acidgreen": "#b0bf1a", "aliceblue": "#f0f8ff",
           "amaranth": "#e52b50", "amber": "#ffbf00", "amethyst": "#9966cc",
           "aqua": "#00ffff", "azure1": "#f0ffff", "beige": "#f5f5dc",
           "black": "#000000"}

chosen_colour = input("Enter a colour: ").lower()
while chosen_colour != "":
    print(f"Colour code for {chosen_colour} is {COLOURS.get(chosen_colour)}")
    chosen_colour = input("Enter a colour: ").lower()