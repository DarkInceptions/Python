d = u"\u00B0"

forc = raw_input("Convert from Fahrenheit to Celsius [1] or Celsius to Fahrenheit [2]: ")
if forc == "1":
	print "This Python Script will convert " + d + "Fahrenheit to " + d + "Celsius."
	print ("Please enter a temperature in " + d  + "Fahrenheit.")
	F = raw_input()
	cTemp = (float(F) - 32) * (5.0/9)
	C = round(float(cTemp), 2)
	print float(F), d + "Fahrenheit is equal to", float(C), d + "Celsius."
else:
		print "This Python Script will convert " + d + "Celsius to " + d + "Fahrenheit."
		print ("Please enter a temperature in " + d  + "Celsius.")
		C = raw_input()
		fTemp = (float(C) * (9.0/5) + 32)
		F = round(float(fTemp), 2)
		print float(C), d + "Celsius is equal to", float(F), d + "Fahrenheit."
raw_input()
