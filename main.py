# var for while loop condition. While loop will run until running != True
running = True

while(running == True):

    # Copied function from provided lab code
    # Added correct conversion F -> C
    """
    def fahrenheit_to_celsius(t):
        t_celsius = (t - 32) * 5/9
        return t_celsius
    """
    
    ## Convert C -> F function
    def celsius_to_fahrenheit(t):
        t_fahrenheit = (t * 9/5) + 32
        return t_fahrenheit

    """
    svar = input('Ange en temperatur i Fahrenheit: ')
    t_fahrenheit = float(svar)
    t = fahrenheit_to_celsius(t_fahrenheit)
    print("Celcius: ", t)
    """

    svar = input('Ange en temperatur i Celsius: ')
    t_celsius = float(svar)
    t = celsius_to_fahrenheit(t_celsius)
    print("Fahrenheit: ", t)

    # Stop while loop, hardcoded until correctly implemented
    running = False
