#By Rees Sweeney-Taylor, Adam Staveski and Leah Nakaima
import csv
import json

#Read vegetables.csv into a variable called vegetables.
with open("vegetables.csv") as f:
	reader=csv.DictReader(f)
	rows=list(reader)
	vegetables = [dict(row) for row in rows]


#Loop through vegetables and filter down to only green vegtables using a whitelist.
whitelist = ["okra", "arugula", "broccoli"]
green_vegetables = []
for vegetable in vegetables:
	if vegetable['name'] in whitelist:
		green_vegetables.append(vegetable)



#Print veggies to the terminal
print(green_vegetables)



#Write the veggies to a json file called greenveggies.json
with open('greenveggies.json', "w") as f:
	json.dump(green_vegetables, f)



#Bonus: Output another csv called green_vegetables.csv.
with open('green_vegetables.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(["name", "color"])
	for veggie in vegetables:
		if veggie['color']=='green':
			writer.writerow([veggie['name'],veggie['color']])
		




