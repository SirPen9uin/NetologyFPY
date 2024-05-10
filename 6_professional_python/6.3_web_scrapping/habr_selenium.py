from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


def wait_element(browser, delay_seconds=1, by=By.TAG_NAME, value=None):
    return WebDriverWait(browser, delay_seconds).until(
        expected_conditions.presence_of_element_located((by, value))
    )


chrome_driver_path = ChromeDriverManager().install()
browser_servise = Service(executable_path=chrome_driver_path)
browser = Chrome(service=browser_servise)

browser.get("https://habr.com/ru/articles/")

parsed_articles = []
articles_tag = wait_element(browser, 1, By.CLASS_NAME, "tm-articles-list")

for article_tag in articles_tag.find_elements(By.TAG_NAME, "article"):
    h2_tag = wait_element(article_tag, 1, By.TAG_NAME, "h2")
    a_tag = h2_tag.find_element(By.TAG_NAME, "a")
    time_tag = article_tag.find_element(By.TAG_NAME, "time")

    header = h2_tag.text
    link_absolute = a_tag.get_attribute("href")
    publish_time = time_tag.get_attribute("datetime")

    parsed_articles.append(
        {
            "header": header,
            "link": link_absolute,
            "publish_time": publish_time,
            "text": None,
        }
    )

for parsed_article in parsed_articles:
    browser.get(parsed_article["link"])
    article_tag = wait_element(browser, 1, By.ID, "post-content-body")
    article_text = article_tag.text
    parsed_article["text"] = article_text[:100]
