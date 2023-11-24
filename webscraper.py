import os
from bs4 import BeautifulSoup
import requests



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
        with open(output_file, 'a', encoding='utf-8') as file:
            file.write(f"\n{url}\n{'*=' * len(url)}"+"*\n")
            # Her bir başlık için ürünleri çek
            for category in categories:
                # Başlık adını çek
                category_name = category.find('h2').text.strip()



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

            print(f"{url} urlindeki veriler 'product_info.txt' dosyasına yazıldı.")

    else:
        print(f"Error: {response.status_code}")

def process_urls_from_file(file_path):
    # Dosyadaki URL'leri oku
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_directory, file_path)
    with open(file_path, 'r', encoding='utf-8') as url_file:
        
        # Her bir URL için get_product_info fonksiyonunu çağır
        for url in url_file:
            # Satırdaki boşlukları temizle
            url = url.strip()
            
            # get_product_info fonksiyonunu çağır
            get_product_info(url, output_file_path)

# Dosya adı
output_file = "product_info.txt"
# Dosya yolunu oluştur
script_directory = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_directory, output_file)
# URL'leri içeren dosyanın adı
url_file_path = "url_list.txt"

# URL'leri işle
process_urls_from_file(url_file_path)
