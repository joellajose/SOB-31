# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?: ")) #added missing brackets and quotes, replaced == by single =

if year < 1900: #added colon
    print ("Woah, that's the past!") #corrected quotation error
elif year >= 1900 and year < 2020: #replaced && by and
    print ("That's totally the present!")
else: #replaced elif by else
    print ("Far out, that's the future!!")
