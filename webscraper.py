import requests
import os
from bs4 import BeautifulSoup
def get_product_info(url, output_file):
    # Web sitesinden sayfayı indir
    response = requests.get(url)

    # HTTP yanıt kodunu kontrol et
    if response.status_code == 200:
        # HTML içeriğini BeautifulSoup ile işle
        soup = BeautifulSoup(response.text, 'html.parser')

        # Başlıkları ve ilgili ürünleri bul
        categories = soup.find_all('div', class_='headline')

        # Dosyayı yazma modunda aç
        with open(output_file, 'w', encoding='utf-8') as file:

            # Her bir başlık için ürünleri çek
            for category in categories:
                # Başlık adını çek
                category_name = category.find('h2').text.strip()

                        # Dosya yolunu oluştur
                script_directory = os.path.dirname(os.path.abspath(__file__))
                output_file_path = os.path.join(script_directory, output_file)


                # Başlığı dosyaya yaz
                file.write(f"\n{category_name}\n{'=' * len(category_name)}\n")

                # İlgili ürünleri seç
                product_container = category.find_next('div', class_='slider-product')
                product_tags = product_container.find_all('a', class_='product-box')

                # Her bir ürün için bilgileri dosyaya yaz
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

        print(f"Veriler '{output_file_path}' dosyasına yazıldı.")

    else:
        print(f"Error: {response.status_code}")

# Kategori sayfasının URL'si
category_url = "https://www.pttavm.com/elektronik"

# Dosya adı
output_file = "product_info.txt"

# Fonksiyonu çağır
get_product_info(category_url, output_file)