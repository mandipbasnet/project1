
import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://nmap.com"

# Sending HTTP request
response = requests.get(url)

# Parsing HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Extracting data
titles = soup.find_all("h2")  # Example: finding all <h2> tags (titles)
paragraph = soup.find_all("p")  # Example: finding all <h2> tags (titles)
links = soup.find_all("a")
images = soup.find_all("img")

for title in titles:
    print(title.get_text())  # Printing the text inside each <h2> tag


# Print each link's href attribute
for link in links:
    href = link.get("href")
    if href:
        print(href)

# Print the 'src' attribute of each image
for img in images:
    img_src = img.get("src")
    if img_src:
        print(img_src)

# Print the text inside each paragraph
import csv

# Save the extracted headlines to a CSV file
with open("headlines.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Headline"])
    for headline in headlines:
        writer.writerow([headline.get_text()])
"""	
Some websites load content dynamically using JavaScript. 
For these websites, a simple requests and BeautifulSoup approach 
might not work. You can use Selenium to interact with JavaScript-
heavy pages.
"""	
from selenium import webdriver
from selenium.webdriver.common.by import By

# Set up the web driver (make sure the correct driver is installed and set in your PATH)
driver = webdriver.Chrome(executable_path="/path/to/chromedriver")

# Open a page
driver.get("https://example.com")

# Wait for the page to load
driver.implicitly_wait(5)  # Waits for up to 5 seconds for the page to load

# Extract data
page_content = driver.page_source

# Use BeautifulSoup to parse the page content
soup = BeautifulSoup(page_content, "lxml")
print(soup.prettify())

# Close the browser
driver.quit()
