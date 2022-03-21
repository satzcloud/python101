from serpapi import GoogleSearch


params = {
  "api_key": "a77e9903d4232268b11baf15e20895fe111c3101b9edb04e04c3ddae1b864c03",
  "engine": "google",
  "q": "driving insights, driving school, Chennai",
  "location": "Austin, Texas, United States",
  "google_domain": "google.com",
  "gl": "us",
  "hl": "en"
}

search = GoogleSearch(params)
results = search.get_dict()
print(results)
