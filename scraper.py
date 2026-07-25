import requests
from bs4 import BeautifulSoup

search_term = "external harddrive"

url = "https://mdcomputers.in/index.php"
params = {
    "route": "product/search",
    "search": search_term
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, params=params, headers=headers)
response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

products = soup.select(".product-layout")

if not products:
    print("No products found.")
else:
    for i, product in enumerate(products, 1):
        name = product.select_one(".caption h4")
        price = product.select_one(".price")
        link = product.select_one(".caption h4 a")

        print(f"Product {i}")
        print("Name :", name.get_text(strip=True) if name else "N/A")
        print("Price:", price.get_text(" ", strip=True) if price else "N/A")
        print("Link :", link["href"] if link else "N/A")
        print("-" * 50)
