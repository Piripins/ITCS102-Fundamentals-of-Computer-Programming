temp = eval(input("Enter temperature here --> "))

if temp <= 0:
	print("The temperature is BELOW FREEZING POINT")
if temp >= 1 and temp <= 15:
	print("The temperature is EXTREMELY COLD")
if temp >= 16 and temp <= 30:
	print("The temperature is COLD")
if temp >= 31 and temp <= 38:
	print("The temperature is LUKEWARM")
if temp >= 39 and temp <= 42:
	print("The temperature is WARM")
if temp >= 43 and temp <= 50:
	print("The temperature is HOT")
if temp >= 51 and temp <= 60:
	print("The temperature is EXTREMELY HOT")
if temp >= 61:
	print("The temperature is BURNING")
