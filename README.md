# LunisecX - Penetration Testing Tool

**LunisecX**, ağ taraması, web güvenlik taraması, port taraması ve trafik analizi yapmak için geliştirilmiş bir Python tabanlı güvenlik aracıdır. Penetration testing sürecinde kullanıcıya yardımcı olmak için aşağıdaki özellikleri sunar:

## Özellikler

- **Ağ Taraması**: Hedef ağdaki aktif cihazları tespit eder ve IP/MAC adreslerini listeler.
- **Web Güvenlik Taraması**: Hedef web sitesinin güvenliğini kontrol eder, HTTP yanıtlarını analiz eder ve yaygın URL uzantılarını tarar.
- **Port Taraması**: Yaygın portları tarar ve açık portları tespit eder.
- **Trafik Analizi**: Mitmproxy kullanarak belirli portlarda trafik analizi yapar.
- **URL Keşfi**: Web güvenlik taraması sırasında belirli URL uzantılarını test eder.

## Gereksinimler

- Python 3.x
- `scapy`, `requests`, `mitmproxy`, `socket`

## Kurulum

1. **Gerekli kütüphaneleri yükleyin:**
   ```bash
   pip install scapy requests mitmproxy

2. **LunisecX'i indirin::**
   ```bash
   git clone https://github.com/kullanici_adi/lunisecx.git

3. **Aracı çalıştırın::**
   ```bash
   Ağ taraması: python lunisecx.py -n <TARGET_NETWORK>
   Web güvenlik taraması: python lunisecx.py -w <TARGET_URL>
   Trafik analizi: python lunisecx.py -t
   Yardım menüsü: python lunisecx.py --manual

Lisans
MIT Lisansı altında lisanslanmıştır.
