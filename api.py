from seleniumwire import webdriver
from seleniumwire.utils import decode as decodesw
from selenium.webdriver.chrome.options import Options

# The purpose of this script is to extract hidden API URLs from a website for the purposes of scraping data from the website.
# It saves time checking network requests in the browser's developer tools and shortens the length of some URLs that are too long to be easily readable in the browser.

# Define our target website
website_url = "Website URL here"

# Define the keywords to search for in the URLs
keywords = ['api', 'product']  # Define the keywords to search for in the URLs. This can be adjusted to suit your scraping needs.

def show_request_urls(driver, target_url, keywords):
    driver.get(target_url)
    urls = []
    for request in driver.requests:
        if any(keyword in request.url for keyword in keywords):
            url = request.url
            if len(url) > 100:
                url = url[:100] + "..."
            urls.append(url)
    return urls

def main():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=chrome_options, seleniumwire_options={"disable_encoding": True})
    target_url = website_url
    urls = show_request_urls(driver, target_url, keywords)
    for url in urls:
        print(url)
    driver.quit()  # Close the browser after the task is done

if __name__ == "__main__":
    main()
