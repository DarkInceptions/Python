d = u"\u00B0"

print "This Python Script will convert " + d + "Fahrenheit to " + d + "Celsius."
print ("Please enter a temperature in " + d  + "Fahrenheit.")
F = raw_input()
cTemp = (float(F) - 32) * (5.0/9)
C = round(float(cTemp), 2)
print float(F), d + "Fahrenheit is equal to", float(C), d + "Celsius."
raw_input()
