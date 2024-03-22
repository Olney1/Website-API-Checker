from seleniumwire import webdriver
from seleniumwire.utils import decode as decodesw
from selenium.webdriver.chrome.options import Options

# The purpose of this script is to extract hidden API URLs from a website for the purposes of scraping data from the website. 
# It saves time checking netowrk requests in the browser's developer tools and shortens the length of some URLs that are too long to be easily readable in the browser.

website_url = "https://thepihut.com/"

def show_request_urls(driver, target_url):
    driver.get(target_url)
    urls = []
    for request in driver.requests:
        if 'api' in request.url:
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
    urls = show_request_urls(driver, target_url)
    for url in urls:
        print(url)
    driver.quit()  # Close the browser after the task is done

if __name__ == "__main__":
    main()
