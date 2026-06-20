
# Copied function from provided lab code
# Added correct conversion F -> C
def fahrenheit_to_celsius(t):
    t_celsius = (t - 32) * 5/9
    return t_celsius

svar = input('Ange en temperatur i Fahrenheit: ')
t_fahrenheit = float(svar)
t = fahrenheit_to_celsius(t_fahrenheit)
print("Celcius: ", t)

