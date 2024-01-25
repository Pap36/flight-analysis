from google_flight_analysis.scrape import Scrape, ScrapeObjects


result = Scrape("KIX", "OTP", "2024-03-21")
ScrapeObjects(result)
print(result.data)