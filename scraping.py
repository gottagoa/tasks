"""
Scrape the website bazar.kg
https://www.bazar.kg/kyrgyzstan/elektronika/kompyutery/noutbuki
It is necessary to scrape all laptops.
Scrape:

Title
Laptop model
Description
Price in dollars and in soms
Also, retrieve all additional descriptions from the list.
Link to the laptop's page.
"""

from bs4 import BeautifulSoup
import requests

def get_html(url):
    page = requests.get(url)
    html = page.text
    return html

def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    main = soup.find("div", {"class": "main-content"})
    listing = main.find("div", {"class": "listings-wrapper"})
    posts = listing.find_all("div", {"class": "listing"})
    links = []
    for post in posts:
        pre_link = post.find('div', {'class': "left-image"})
        link = pre_link.find('a').get('href')
        full_link = "https://www.bazar.kg" + link
        links.append(full_link)
    return links

def get_page_data(html, link):
    soup = BeautifulSoup(html, "html.parser")
    info = soup.find("div", {"class": "content-wrapper padding-top-0"})
    top = info.find("div", {"class": "block-main details"})
    pre_title = top.find("div", {"class": "left"})
    title = pre_title.find("h1").text.strip()
    pre_description = pre_title.find("div", {"class": "details-info"})
    if pre_description is not None:
        description = pre_description.find('p', {'class': "description"}).text.strip()
        price_som = pre_description.find("span", {"class": "main"}).text
        price_dollar = pre_description.find("span", {"class": "sub"}).text
        ad_info = pre_description.find_all('div', {'class': 'info-row'})
        additional_info = []
        for ad in ad_info:
            label = ad.find('div', {'class': 'label'}).text
            if label == 'Views':
                info = ad.find('div', {'class': 'info'}).text.strip()
            additional_info.append(info)
      
        print("Title:", title)
        print("Link:", link)
        print("Description:", description)
        print("Views:", ad.text.strip())
        print("Price (in soms):", price_som)
        print("Price (in dollars):", price_dollar)
        print("----------------------")
    else:
        print('Product information was not specified')

def main():
    URL = "https://www.bazar.kg/kyrgyzstan/elektronika/kompyutery/noutbuki"
    html = get_html(URL)
    post_links = get_links(html)
    for link in post_links:
        post_html = get_html(link)
        data = get_page_data(post_html, link)

if __name__ == "__main__":
    main()
