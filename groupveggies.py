#By Rees Sweeney-Taylor, Adam Staveski and Leah Nakaima

import csv
import json
from pprint import pprint

#Read vegtables.csv into a variable called vegtables.
with open("vegetables.csv") as f:
	reader=csv.DictReader(f)
	vegetables=list(reader)
	vegetables=[dict(vegetables) for vegetables in vegetables]




#Group vegtables by color as a variable vegtables_by_color.
vegetables_by_color = {}
for vegetable in vegetables:
	color=vegetable["color"]
	if color in vegetables_by_color:
		vegetables_by_color[color].append(vegetable)
	else:
		vegetables_by_color[color] = [vegetable]

pprint(vegetables_by_color)



#Output vegtables_by_color into a json called vegtables_by_color.json.


