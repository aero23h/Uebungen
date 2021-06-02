fahrenheit = input("welche Temperatur (in Fahrenheit) möchtest du umrechnen? ")
fahrenheit = int(fahrenheit)
celsius = (fahrenheit - 32) / 1.8
print(fahrenheit, "°F",  "sind umgerechnet", celsius.__round__(2), "°C")