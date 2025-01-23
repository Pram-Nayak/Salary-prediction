#import glassdoor_scraper as gs  # Import the web_glassdoor_scraper module
import glassdoor_scrapercopy as gs
import pandas as pd

# Specify the correct path to your ChromeDriver executable
path = "D:/web tech project/ds_salary_proj"  # Update with your actual path to chromedriver

# Call the function with all required arguments
df = gs.get_jobs("data scientist", 15, False, path, 15)

df