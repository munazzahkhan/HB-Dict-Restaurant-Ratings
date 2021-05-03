def restaurant_ratings(file_name):
    """Restaurant rating lister."""

    file = open(file_name)
    rest_ratings = {}

    for line in file:
        line = line.replace("\n","")
        restaurant_info = line.split(":")
        rest_ratings[restaurant_info[0]] = restaurant_info[1]
        
            
    return rest_ratings


print(restaurant_ratings("scores.txt"))