reviews <- read.csv("review.csv")
hotels <- read.csv("offering.csv")

reviews$user_id <- as.character(reviews$user_id)
reviews <- reviews[reviews$user_id != "", ]


hotel_reviews <- merge(hotels, reviews, by.x = "id", by.y = "hotel_id")
full_reviews <- hotel_reviews[complete.cases(hotel_reviews), ]

str(full_reviews)

get_users_hotels <- function(hotelID){
  items <- full_reviews$user_id[full_reviews$id == hotelID]
  return(items)
}

tanimoto_similarity <- function(user1_ratings, user2_ratings){  
  common_items <- length(intersect(user1_ratings, user2_ratings))
  all_items <- length(union(user1_ratings, user2_ratings))
  similarity <- 0
  if (all_items > 0){
    similarity <- common_items/all_items
  }  
  return(similarity)
}

hotels_list <- unique(full_reviews$id)
ratings_hotels <- sapply(hotels_list, get_users_hotels)
names(ratings_hotels) <- hotels_list

get_NN_hotel <- function(hotelID, ratings_hotels, similarity_function, neighbours){
  hotelID <- as.character(hotelID)
  current_ratings_hotels <- ratings_hotels[[hotelID]]
  hotels_similarity <- sapply(ratings_hotels, similarity_function, user2_ratings = current_ratings_hotels)
  return(sort(hotels_similarity, decreasing=T)[2:(neighbours+1)])  
}

get_NN_hotel("1592809", ratings_hotels, tanimoto_similarity, 5)
