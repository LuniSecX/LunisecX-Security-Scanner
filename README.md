# LunisecX - Penetration Testing Tool

**LunisecX**, ağ taraması, web güvenlik taraması, port taraması ve trafik analizi yapmak için geliştirilmiş bir Python tabanlı güvenlik aracıdır. Bu araç, penetration testing (sızma testi) sürecinde kullanıcıya yardımcı olmak için çeşitli özellikler sunar.

## Özellikler

- **Ağ Taraması** (`-n` komutu): Hedef ağdaki aktif cihazları tespit eder ve IP/MAC adreslerini listeler.
- **Web Güvenlik Taraması** (`-w` komutu): Hedef web sitesinin güvenliğini kontrol eder, HTTP yanıtlarını analiz eder ve yaygın URL uzantılarını tarar.
- **Port Taraması**: Yaygın portları tarar ve açık portları tespit eder.
- **Trafik Analizi** (`-t` komutu): Mitmproxy kullanarak belirli portlarda trafik analizi yapar.
- **URL Keşfi**: Web güvenlik taraması sırasında, belirli URL uzantılarını test eder.

## Gereksinimler

- Python 3.x
- `scapy` (Ağ taraması için)
- `requests` (Web güvenlik taraması için)
- `mitmproxy` (Trafik analizi için)
- `socket` (Port taraması için)

## Kurulumd

1. **Gerekli kütüphaneleri yükleyin:**

   ```bash
   pip install scapy requests mitmproxy

2. **LunisecX aracını indirin:**

   ```bash
    git clone https://github.com/kullanici_adi/lunisecx.git

3. **Trafik Analizi Taraması Kullanım:**
    Trafik Analizi (-t komutu)
Trafik analizi, belirli portlarda ağ trafiğini analiz etmek için mitmproxy kullanır. Bu analiz, şüpheli trafiği ve veri sızıntılarını tespit etmek için faydalıdır.
   ```bash
    python3 lunisecx.py -t
   
4. **Web Güvenlik Taraması Kullanım:**
    Web Güvenlik Taraması (-w komutu)
Web güvenlik taraması, belirtilen hedef URL'yi analiz eder. Bu tarama HTTP yanıtları ve URL keşfi içerir.
   ```bash
    python3 lunisecx.py -w http://example.com
   
5. **Ağ taraması Kullanım:**
    Ağ Taraması (-n komutu)
Ağ taraması, belirli bir IP aralığındaki cihazları tespit etmek için kullanılır. Bu, hedef ağdaki aktif cihazları ve IP/MAC adreslerini listelemek için faydalıdır.
   ```bash
    python3 lunisecx.py -n 192.168.1.0/24

6. **Aracı Çalıştırın:**
   ```bash
    python3 lunisecx.py -n <TARGET_NETWORK>
    python3 lunisecx.py -w <TARGET_URL>
    python3 lunisecx.py -t
    python3 lunisecx.py --manual

6. **İçerik:**
   ```bash
    ### İçeriği Açıklamalar:

- **Proje Tanıtımı ve Özellikler**: Projenin ne amaçla kullanıldığını ve sunduğu başlıca özellikleri açıklıyor.
- **Gereksinimler**: Projeyi çalıştırabilmek için hangi Python kütüphanelerine ihtiyacınız olduğunu belirtiyor.
- **Kurulum**: Projenin nasıl kurulacağı ve çalıştırılacağı hakkında detaylı bilgiler veriyor.
- **Kullanım**: Aracın nasıl kullanılacağına dair örnek komutlar içeriyor.
- **Lisans**: Projenin lisans bilgilerini içeriyor. Burada MIT lisansını kullandık, fakat bunu değiştirebilirsiniz.
- **Katkı**: Katkı sağlamak isteyen kullanıcılar için GitHub üzerinden nasıl katkı yapabileceklerini anlatıyor.
   
 6. **Lisans:**
   ```bash
    Bu proje, MIT Lisansı altında lisanslanmıştır. Lisansı inceleyebilirsiniz.


