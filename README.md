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

## Kurulum

1. **Gerekli kütüphaneleri yükleyin:**

   ```bash
   pip install scapy requests mitmproxy

2. **LunisecX aracını indirin:**

   ```bash
    git clone https://github.com/kullanici_adi/lunisecx.git

 3. **Aracı Çalıştırın:**
   ```bash
    python3 lunisecx.py -n <TARGET_NETWORK>
    python3 lunisecx.py -w <TARGET_URL>
    python3 lunisecx.py -t
    python3 lunisecx.py --manual
