#http://www.cs.cmu.edu/~jiweil/html/hotel-review.html
# in reviews.txt we have hotels review information

import json
import csv

user_id = []
offering_id = []
service_rating = []
cleanliness_rating = []
overall_rating = []
value_rating = []
location_rating = []
sleep_quality_rating = []
rooms_rating = []


with open("review.txt") as f:
    for line in f:
        d = json.loads(line)
	# add user_id
	if "author" in d.keys():
	    user_id.append(d["author"]["id"])
	else:
	    user_id.append("NA")

	# add rated_hotel_id
	if "offering_id" in d.keys():
	    offering_id.append(d["offering_id"])
	else:
	    offering_id.append("NA")
	
	# get ratings from review:
        if "ratings" in d.keys():
	    ratings = d["ratings"]
	    
	    if "service" in ratings.keys():
                service_rating.append(ratings["service"])
	    else:
	        service_rating.append("NA")

	    if "cleanliness" in ratings.keys():
		cleanliness_rating.append(ratings["cleanliness"])
	    else:
		cleanliness_rating.append("NA")
		
	    if "overall" in ratings.keys():
		overall_rating.append(ratings["overall"])
	    else:
		overall_rating.append("NA")

	    if "location" in ratings.keys():
		location_rating.append(ratings["location"])
	    else:
		location_rating.append("NA")

	    if "value" in ratings.keys():
		value_rating.append(ratings["value"])
	    else:
		value_rating.append("NA")

	    if "sleep_quality" in ratings.keys():
		sleep_quality_rating.append(ratings["sleep_quality"])
	    else:
		sleep_quality_rating.append("NA")

	    if "rooms" in ratings.keys():
		rooms_rating.append(ratings["rooms"])
	    else:
		rooms_rating.append("NA")


        else:
            service_rating.append("NA")
	    cleanliness_rating.append("NA")
	    overall_rating.append("NA")
	    location_rating.append("NA")
	    value_rating.append("NA")
	    sleep_quality_rating.append("NA")
	    rooms_rating.append("NA")

		
	
	

f.close()

with open('review.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(["user_id", "hotel_id", "service", "cleanliness", "overall", "location", "value", "sleep_quality", "rooms"])
    for i in range(len(user_id)):
        writer.writerow([user_id[i], offering_id[i], service_rating[i], cleanliness_rating[i], overall_rating[i], location_rating[i], value_rating[i], sleep_quality_rating[i], rooms_rating[i]])
	print (user_id[i], offering_id[i], service_rating[i], cleanliness_rating[i], overall_rating[i], location_rating[i], value_rating[i], sleep_quality_rating[i], rooms_rating[i])
	
f.close()	
