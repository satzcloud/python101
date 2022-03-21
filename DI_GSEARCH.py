from serpapi import GoogleSearch

search = GoogleSearch({})
location_list = search.get_location("Austin", 3)
print(location_list)