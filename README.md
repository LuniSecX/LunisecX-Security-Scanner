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
