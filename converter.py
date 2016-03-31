print ""
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print ""
print "Hello and welcome to Fiona's Fabulous Converter!"
print ""
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print ""
print "This converter can perform the following functions:"
print ""
print "0. I changed my mind. I don't want to convert anything"
print ""
print "1. Convert something from units per day to units per second"
print ""
print "2. Convert milliarcseconds per day to kilometers per second"
print ""
print "3. Convert milliarcseconds per day squared to kilometers per second squared"
print ""
print "-1. I want to know more about Fiona's Fabulous Converter"
print ""
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print ""

function = int(input("Which one do you want?   "))
print ""
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print ""

# anything/day to anything/sec

if function == 0:
	print "That's ok! When you figure out what you want to convert, Fiona's Fabulous converter will be here for you"

elif function == 1:

	per_day = float(input("Enter the quantity in units/day:    "))
	print ""

	per_second = per_day/86400.0
	
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print ""
	print "quantity in units/second = ",per_second
	print ""
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"


# mas/day to km/s

elif function == 2:
	
	mas_per_day = float(input("Enter the velocity in mas/day:   "))
	print ""
	distance_kpc = float(input("Enter the distance to the source (in kpc):   "))
	print ""	
	
	mas_per_second = mas_per_day/86400
	
	rad_per_second = mas_per_second*4.848e-9
	
	distance_km = distance_kpc*3.086e16
	
	km_per_second = rad_per_second*distance_km
	
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print ""
	print "velocity in km/s = ",km_per_second
	print ""
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
elif function == 3:
	
	mas_day_squared = float(input("Enter the acceleration in mas/day/day:   "))
	print ""
	distance_kpc = float(input("Enter the distance to the source (in kpc):   "))
	print ""
	
	mas_second_squared = mas_day_squared/(86400^2)
	
	rad_second_squared = mas_second_squared*4.848e-9
	
	distance_km = distance_kpc*3.086e16
	
	km_second_squared = rad_second_squared*distance_km
	
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print ""
	print "acceleration in km/s/s = ",km_second_squared
	print ""
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
elif function == -1:
	print "Thank you for choosing to use Fiona's Fabulous Converter!"
	print ""
	print "You may find some of the functions listed here oddly specific."
	print "This is because Fiona wrote her Fabulous Converter as she went along,"
	print "adding any calculation she needed to do during her Ph.D. She has done her"
	print "best to ensure that all the calculations included here are correct. If you"
	print "spot a mistake, please let her know, and feel free to correct it! Please"
	print "also feel free to add any functions that you need, or any functions that"
	print "you don't necessarily need but feel are important."
	print ""
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	
else:
	print "Unfortunately, Fiona's Fabulous Converter doesn't understand that."
	print ""
	print "To select a function, simply type the corresponding number from the list above."
	print ""


print ""	
print "Thank you for using Fiona's Fabulous Converter! <3 <3 <3"
print ""