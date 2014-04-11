reviews <- read.csv("review.csv")
hotels <- read.csv("offering.csv")

reviews$user_id <- as.character(reviews$user_id)
reviews <- reviews[reviews$user_id != "", ]


hotel_reviews <- merge(hotels, reviews, by.x = "id", by.y = "hotel_id")
full_reviews <- hotel_reviews[complete.cases(hotel_reviews), ]


get_users_regions <- function(regionID){
  users <- full_reviews$user_id[full_reviews$region_id == regionID]
  return(users)
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

# region test:
ratings1 <- get_users_regions("60768")
ratings2 <- get_users_regions("55711")

tanimoto_similarity(ratings1, ratings2)

# build regions similarity tables:

region_list <- unique(full_reviews$region_id)

ratings_regions <- sapply(region_list, get_users_regions)
names(ratings_regions) <- region_list 

head(ratings_regions)

get_NN_region <- function(regionID, ratings_regions, similarity_function, neighbours){
  regionID <- as.character(regionID)
  current_ratings_regions <- ratings_regions[[regionID]]
  regions_similarity <- sapply(ratings_regions, similarity_function, user2_ratings = current_ratings_regions)
  return(sort(regions_similarity, decreasing=T)[2:(neighbours+1)])  
}

get_NN_region("60878", ratings_regions, tanimoto_similarity, neighbours = 3)

hotels$locality[hotels$region_id == 60878][1]
hotels$locality[hotels$region_id == 60713][1]
hotels$locality[hotels$region_id == 32655][1]
