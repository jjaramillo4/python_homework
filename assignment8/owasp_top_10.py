import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

"""
Task 6 - HTML elements identified in dev tools:

The project page https://owasp.org/www-project-top-ten/ no longer lists the
ten risks itself.  It only links out to the release sites, so the script
starts there, grabs the "OWASP Top Ten 2021" link, and follows it.

On https://owasp.org/Top10/2021/ the list lives in an ordered list that
follows the "The Top 10:2021 List" heading:
- Heading:   h3, id = "the-top-102021-list"
- List:      the first ol after that heading
- Each risk: an a element inside an li of that ol
XPath: //h3[@id='the-top-102021-list']/following-sibling::ol[1]/li/a
"""

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    # start on the project page named in the assignment
    driver.get("https://owasp.org/www-project-top-ten/")
    release_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(@href, 'owasp.org/Top10/2021')]")
        )
    )
    release_url = release_link.get_attribute("href")
    print(f"following link to: {release_url}")

    # follow it to the page that actually holds the list
    driver.get(release_url)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "the-top-102021-list"))
    )

    risk_links = driver.find_elements(
        By.XPATH, "//h3[@id='the-top-102021-list']/following-sibling::ol[1]/li/a"
    )
    print(len(risk_links))

    results = []
    for a in risk_links:
        risk = {"Title": a.text, "Link": a.get_attribute("href")}
        results.append(risk)

    driver.quit()
    print(results)
    owasp_df = pd.DataFrame(results)
    print(owasp_df)

except Exception as e:
    print("couldn't get the web page")
    print(f"Exception: {type(e).__name__} {e}")

owasp_df.to_csv("owasp_top_10.csv", index=False)
