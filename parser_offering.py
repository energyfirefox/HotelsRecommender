# in offering.txt we have information about hotels in json format

import json
import csv

hotel_class = []
hotel_id = []
hotel_name = []
hotel_region_id = []
hotel_region = []
hotel_locality = []

with open("offering.txt") as f:
    for line in f:
        d = json.loads(line)
	# add hotel_id
	if "id" in d.keys():
	    hotel_id.append(d["id"])
	else:
	    hotel_id.append("NA")

	# add hotel_name
	if "name" in d.keys():
	    hotel_name.append(d["name"])
	else:
	    hotel_name.append("NA")
	
	# add hotel class
        if "hotel_class" in d.keys():
            hotel_class.append(d["hotel_class"])
        else:
            hotel_class.append("NA")

	# add region _id
	if "region_id" in d.keys():
            hotel_region_id.append(d["region_id"])
        else:
            hotel_region_id.append("NA")
	# add region
	if "address" in d.keys():
            hotel_region.append(d["address"]["region"])
        else:
            hotel_region.append("NA")

	# add locality
	if "address" in d.keys():
            hotel_locality.append(d["address"]["locality"])
        else:
            hotel_locality.append("NA")

f.close()

with open('offering.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["id", "name", "class", "region_id", "region", "locality"])
    for i in range(len(hotel_id)):
        writer.writerow([hotel_id[i], hotel_name[i], hotel_class[i], hotel_region_id[i], hotel_region[i], hotel_locality[i]])
	print(hotel_id[i], hotel_name[i], hotel_class[i], hotel_region_id[i], hotel_region[i], hotel_locality[i])
f.close()	
