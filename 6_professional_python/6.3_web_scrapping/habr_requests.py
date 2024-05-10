"""
div class="tm-articles-list
article
<time datetime="2023-10-26T16:04:51.000Z" title="2023-10-26, 19:04">58 минут назад</time>
h2 class="tm-title tm-title_h2"
a href
span
post-content-body
"""

from urllib.parse import urljoin

import bs4
import fake_headers
import requests

headers_gen = fake_headers.Headers(os="win", browser="chrome")

response = requests.get("https://habr.com/ru/articles/", headers=headers_gen.generate())
main_html_data = response.text
main_soup = bs4.BeautifulSoup(main_html_data, "lxml")

articles_list_tag = main_soup.find("div", class_="tm-articles-list")

articles_tags = articles_list_tag.find_all("article")
articles_data = []

for article_tag in articles_tags:
    time_tag = article_tag.find("time")
    pub_time = time_tag["datetime"]

    h2_tag = article_tag.find("h2", class_="tm-title")
    span_tag = h2_tag.find("span")

    header = span_tag.text.strip()

    a_tag = h2_tag.find("a")
    link_relative = a_tag["href"]

    link_absolute = urljoin("https://habr.com/", link_relative)

    response = requests.get(link_absolute, headers=headers_gen.generate())
    article_html_data = response.text
    article_soup = bs4.BeautifulSoup(article_html_data, "lxml")

    article_body_tag = article_soup.find("div", id="post-content-body").text

    articles_data.append(
        {
            "header": header,
            "link": link_absolute,
            "pub_time": pub_time,
            "text": article_body_tag[:100],
        }
    )


print(len(articles_data))
