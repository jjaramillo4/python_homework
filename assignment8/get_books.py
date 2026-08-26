import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""
Task 1 - robots.txt compliance:
AI agents and crawlers are disallowed. 

Task 2 - HTML elements identified in dev tools:
 Single result:  li,   class = "cp-search-result-item"
- Title:          span, class = "title-content"
- Author:         a,    class = "author-link"
- Format/Year:    span class = "display-info-primary", inside div class = "cp-format-info"
"""

# Task 3

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")
    WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "cp-search-result-item"))
    )

    li_elements = driver.find_elements(By.CLASS_NAME, "cp-search-result-item")
    print(len(li_elements))

    results = []
    for li in li_elements:
        title = li.find_element(By.CLASS_NAME, "title-content").text
        author_list = li.find_elements(By.CSS_SELECTOR, "a.author-link")
        authors = ";".join([a.text for a in author_list])
        format_div = li.find_element(By.CLASS_NAME, "cp-format-info")
        format_year = format_div.find_element(By.CLASS_NAME, "display-info-primary").text
        book = {"Title": title, "Author": authors, "Format-Year": format_year}
        results.append(book)
    
    book_df = pd.DataFrame(results)
    print(book_df)

    # Task 4
    book_df.to_csv("get_books.csv", index=False)

    with open("get_books.json", "w") as f:
        json.dump(results, f, indent=4)

except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")

finally:
    driver.quit()