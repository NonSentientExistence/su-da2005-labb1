# var for while loop condition. While loop will run until running != True
running = True

# Validates user input for temprature unit. Takes temp unit
def conv_units_are_valid(u):
    if u == "c":
        return True
    elif u == "f":
        return True
    elif u == "k":
        return True
    else:
        return False

# Used to convert all tempratures to kelvin. Takes degrees and unit
def temp_to_kelvin(t,tf):
    if tf == "k":
        return t
    elif tf == "c":
        temp_kelvin = t + 273.15
        return temp_kelvin
    elif tf == "f":
        temp_kelvin = (t - 32) * 5/9 + 273.15
        return temp_kelvin

# Converts kelvin to celsius and farhenheit since all input tempratures are converted to kelvin. Takes degrees and unit
def kelvin_to_temp(t,tt):
    if tt == "k":
        return t
    elif tt == "c":
        temp_celsius = t - 273.15
        return temp_celsius
    elif tt == "f":
        temp_farenheit = (t - 273.15) * 9/5 + 32
        return temp_farenheit

#While loop for program. If bool !true then stop loop
while(running == True):
    #user input, choose unit to convert from. q will stop loop (quit)
    print("Celsius (c) | Farenheit (f) | Kelvin (k) | Avsluta (q)")
    conv_from_unit = str(input('Vilken temperatur enhet vill du konvertera från?: '))

    # set while condition to false if user input is q (quit)
    if conv_from_unit == "q":
        running = False
        continue
    # Runs unit validation on user input. If not true, print msg and await user input. Then restart loop.
    if not conv_units_are_valid(conv_from_unit):
        input("Ogiltig enhet, vänligen ange igen. Tryck enter för att fortsätta")
        continue

    # user input, how many degrees of chosen unit
    temp_deg = float(input('Ange antal grader: '))

    # user input, unit to convert to. q will stop loop (quit)
    print("Celsius (c) | Farenheit (f) | Kelvin (k) | Avsluta (q)")
    conv_to_unit = str(input('Vilken temperatur enhet vill du konvertera till?: '))
    # set while condition to false if user input is q (quit)
    if conv_to_unit == "q":
        running = False
        continue
    # Run unit validation on user input. If not true, print msg and await user input. Then restart loop.
    if not conv_units_are_valid(conv_to_unit):
        input("Ogiltig enhet, vänligen ange igen. Tryck enter för att fortsätta")
        continue
    
    # Run temp conversion to kelvin on user input. 
    conv_to_kelvin = temp_to_kelvin(temp_deg, conv_from_unit)
    # Run kelvin conversion to desired output unit 
    conv_to_user_unit = kelvin_to_temp(conv_to_kelvin, conv_to_unit)

    # Prints degrees input, the unit to convert from, 
    # the degrees calculated in convert from kelvin rounded to 2 decimals and convert to unit.
    print(f'\n{temp_deg}{conv_from_unit}° motsvarar {conv_to_user_unit}{conv_to_unit}°\n')

# Copied function from provided lab code
# Added correct conversion F -> C
# left below code as correcting the conversion calculation is part of the assignment
"""
def fahrenheit_to_celsius(t):
    t_celsius = (t - 32) * 5/9
    return t_celsius


## Convert C -> F function
def celsius_to_fahrenheit(t):
    t_fahrenheit = (t * 9/5) + 32
    return t_fahrenheit

svar = input('Ange en temperatur i Fahrenheit: ')
t_fahrenheit = float(svar)
t = fahrenheit_to_celsius(t_fahrenheit)
print("Celcius: ", t)

svar = input('Ange en temperatur i Celsius: ')
t_celsius = float(svar)
t = celsius_to_fahrenheit(t_celsius)
print("Fahrenheit: ", t)
"""



