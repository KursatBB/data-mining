import requests
from bs4 import BeautifulSoup

def get_product_info(url, output_file):
    # Web sitesinden sayfayı indir
    response = requests.get(url)

    # HTTP yanıt kodunu kontrol et
    if response.status_code == 200:
        # HTML içeriğini BeautifulSoup ile işle
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ürünlerin bulunduğu etiketleri belirle
        product_tags = soup.find_all('a', class_='product-box')

        # Ürün bilgilerini dosyaya yaz
        with open(output_file, 'w', encoding='utf-8') as file:
            for product_tag in product_tags:
                # Ürün Adı
                product_name_tag = product_tag.find('div', class_='product-box-container-name')
                product_name = product_name_tag.text.strip() if product_name_tag else None

                # Fiyat
                price_tag = product_tag.find('div', class_='price-box-price')
                price = price_tag.text.strip() if price_tag else None

                # Ürün bilgilerini dosyaya yaz
                file.write(f"Ürün Adı: {product_name}\n")
                file.write(f"Fiyat: {price}\n")
                file.write("-" * 30 + "\n")

        print(f"Veriler '{output_file}' dosyasına yazıldı.")

    else:
        print(f"Error: {response.status_code}")

# Kategori sayfasının URL'si
category_url = "https://www.pttavm.com/elektronik"

# Dosya adı
output_file = "product_info.txt"

# Fonksiyonu çağır
get_product_info(category_url, output_file)



""" import requests
from bs4 import BeautifulSoup

def get_product_info(url):
    # Web sitesinden sayfayı indir
    response = requests.get(url)

    # HTTP yanıt kodunu kontrol et
    if response.status_code == 200:
        # HTML içeriğini BeautifulSoup ile işle
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ürünlerin bulunduğu HTML etiketlerini belirle
        product_tags = soup.find_all('div', class_='product')

        # Her bir ürün için bilgileri çek
        for product_tag in product_tags:
            # Ürün Adı
            product_name_tag = product_tag.find('div', class_='product-box-container-name')
            product_name = product_name_tag.text.strip() if product_name_tag else None

            # Fiyat
            price_tag = product_tag.find('div', class_='price-box-price')
            price = price_tag.text.strip() if price_tag else None

            # Ürün bilgilerini yazdır veya başka bir işlem yap
            print(f"Ürün Adı: {product_name}")
            print(f"Fiyat: {price}")
            print("-" * 30)

    else:
        print(f"Error: {response.status_code}")

# Kategori sayfasının URL'si
category_url = "https://www.pttavm.com/elektronik"

# Fonksiyonu çağır
get_product_info(category_url) """










""" import requests
from bs4 import BeautifulSoup

def get_product_info(url):
    # Web sitesinden sayfayı indir
    response = requests.get(url)

    # HTTP yanıt kodunu kontrol et
    if response.status_code == 200:
        # HTML içeriğini BeautifulSoup ile işle
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ürünlerin bulunduğu HTML etiketlerini belirle
        product_tags = soup.find_all('div', class_='product-box p-1')

        # Her bir ürün için bilgileri çek
        for product_tag in product_tags:
            product_name_tag = soup.find('div', class_='product-box-container-name')
            product_name = product_name_tag.text.strip() if product_name_tag else None
            price_tag = soup.find('div', class_='price-box-price')
            price = price_tag.text.strip() if price_tag else None

            # Ürün bilgilerini yazdır veya başka bir işlem yap
            print(f"Ürün Adı: {product_name}")
            print(f"Fiyat: {price}")

            print("-" * 30)

    else:
        print(f"Error: {response.status_code}")

# Kategori sayfasının URL'si
category_url = "https://www.pttavm.com/elektronik"

# Fonksiyonu çağır
get_product_info(category_url) """