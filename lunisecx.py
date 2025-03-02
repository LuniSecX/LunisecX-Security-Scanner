import argparse
import scapy.all as scapy
import requests
import socket
import os

# Port numaraları ve hizmetlerini eşleştiren bir sözlük
port_services = {
    80: "HTTP (Web Server)",
    443: "HTTPS (Secure Web Server)",
    8080: "HTTP (Alternative Web Server)",
    21: "FTP (File Transfer Protocol)",
    22: "SSH (Secure Shell)",
    25: "SMTP (Simple Mail Transfer Protocol)",
    53: "DNS (Domain Name System)",
    110: "POP3 (Post Office Protocol)",
    139: "NetBIOS (Network Basic Input/Output System)",
    445: "SMB (Server Message Block)",
    3306: "MySQL Database",
    5432: "PostgreSQL Database"
}

# URL'yi doğrulama ve eksik protokolü ekleme fonksiyonu
def validate_url(url):
    if not url.startswith("http://") and not url.startswith("https://"):
        url = "http://" + url
    return url

# Ağ taraması fonksiyonu (Port taraması yapar)
def scan_network(target):
    print(f"[LunisecX] Ağ taraması başlatılıyor: {target}")
    
    # Ping ile hedef IP adresinin canlı olup olmadığını kontrol etme
    arp_request = scapy.ARP(pdst=target)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    
    # Yanıtları alıyoruz
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    
    if answered_list:
        print(f"[LunisecX] {target} aktif ve yanıt verdi!")
        for element in answered_list:
            print(f"IP Adresi: {element[1].psrc} - MAC Adresi: {element[1].hwsrc}")
            # Port taraması başlatıyoruz
            open_ports = scan_ports(element[1].psrc)
            if open_ports:
                print(f"[LunisecX] {element[1].psrc} üzerinde açık portlar tespit edildi: {', '.join(map(str, open_ports))}")
            else:
                print(f"[LunisecX] {element[1].psrc} üzerinde açık port bulunamadı.")
    else:
        print(f"[LunisecX] {target} adresine yanıt alınamadı.")

# Web güvenlik taraması ve URL keşfi fonksiyonu
def scan_web(target):
    print(f"[LunisecX] Web güvenlik taraması başlatılıyor: {target}")
    
    # URL'yi doğrulama (Eksik protokol ekleme)
    target = validate_url(target)

    # Hedef siteye basit bir GET isteği gönderme
    try:
        response = requests.get(target)
        if response.status_code == 200:
            print(f"[LunisecX] {target} web sitesi güvenli görünüyor. Yanıt kodu: {response.status_code}")
        else:
            print(f"[LunisecX] {target} web sitesinden beklenmeyen bir yanıt kodu geldi: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"[LunisecX] Web taraması sırasında bir hata oluştu: {e}")

    # URL uzantılarını keşfetme
    print(f"[LunisecX] {target} üzerinde URL keşfi başlatılıyor...")
    discover_urls(target)

# Port tarama fonksiyonu
def scan_ports(target):
    open_ports = []
    common_ports = [80, 443, 8080, 21, 22, 25, 53, 110, 139, 445, 3306, 5432]  # Yaygın portlar
    
    for port in common_ports:
        result = scan_single_port(target, port)
        if result:
            open_ports.append(port)
    
    return open_ports

# Tek bir portu tarama fonksiyonu
def scan_single_port(target, port):
    try:
        # Bağlantıyı kontrol etme
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Timeout süresi 5 saniye
        result = sock.connect_ex((target, port))  # Port bağlantısını kontrol et
        sock.close()
        
        # Eğer bağlantı başarılıysa (0), port açıktır
        if result == 0:
            service = port_services.get(port, "Bilinmeyen Servis")
            print(f"[LunisecX] Port {port} açık. Servis: {service}")
            return True
        return False
    except socket.timeout:
        print(f"[LunisecX] Port {port} zaman aşımına uğradı. Bağlantı kurulamadı.")
        return False
    except socket.error as e:
        print(f"[LunisecX] Port {port} tarama sırasında hata: {e}")
        return False

# URL uzantılarını keşfetme fonksiyonu
def discover_urls(target):
    # Test edilecek yaygın URL uzantıları (dirb tarzı genişletilmiş bir liste)
    extensions = [
        "/", "/config", "/admin", "/login", "/dashboard", "/settings", "/upload", "/index",
        "/test", "/data", "/phpinfo", "/cgi-bin", "/bin", "/private", "/hidden", "/backup",
        "/user", "/home", "/files", "/wp-admin", "/wp-login", "/file", "/scripts", "/css", "/images", "/docs",
        "/.env", "/.git", "/.ssh", "/.idea", "/.vscode", "/robots.txt", "/sitemap.xml", "/admin.php",
        "/login.php", "/admin.html", "/secure", "/error", "/api", "/rest", "/phpmyadmin", "/mysql", "/db",
        "/uploads", "/tmp", "/cgi", "/assets", "/site", "/index.php", "/home.php", "/about", "/contact",
        "/search", "/settings.php", "/admin/config", "/panel", "/portal", "/user/admin", "/secret", "/private_files"
    ]
    
    # Yalnızca başarılı bir şekilde erişilen URL'leri yazdırma
    for ext in extensions:
        url = f"{target}{ext}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"[LunisecX] Keşfedilen URL: {url} (Başarıyla erişildi!)")
        except requests.exceptions.RequestException as e:
            continue  # Başarısız URL'ler için hata mesajı vermeyelim

# Trafik analizi fonksiyonu
def analyze_traffic(port):
    print(f"[LunisecX] Port {port} üzerinde trafik analizi başlatılıyor...")

    # Scapy ile ağ üzerinde belirtilen portu dinleme
    def packet_callback(packet):
        if packet.haslayer(scapy.TCP):
            if packet.sport == port or packet.dport == port:
                print(f"[LunisecX] Paket yakalandı: {packet.summary()}")

    # Port üzerinde paketleri dinlemek için sniffer başlatıyoruz
    scapy.sniff(filter=f"tcp port {port}", prn=packet_callback, store=0)

# Yardım komutları fonksiyonu
def display_help():
    print(""" 
    [LunisecX] Kullanılabilir Komutlar:
    
    -n, --network <TARGET>       Ağ taraması yapar. Hedef IP adresi girilmelidir.
    -w, --web <TARGET>           Web güvenlik taraması yapar. Hedef URL girilmelidir.
    -t, --traffic <PORT>         Trafik analizi yapar. Belirtilen portu izler.
    --manual                     Yardım menüsünü gösterir.
    """)

def main():
    # Komut satırı argümanlarını al
    parser = argparse.ArgumentParser(description="LunisecX Penetration Testing Tool")
    parser.add_argument("-n", "--network", dest="target_network", help="Ağ taraması yapar.")
    parser.add_argument("-w", "--web", dest="target_web", help="Web güvenlik taraması yapar.")
    parser.add_argument("-t", "--traffic", dest="traffic", type=int, help="Trafik analizi yapar. Belirtilen portu izler.")
    parser.add_argument("--manual", dest="manual", action="store_true", help="Yardım menüsünü gösterir.")
    
    args = parser.parse_args()

    if args.manual:
        display_help()
    elif args.target_network:
        scan_network(args.target_network)
    elif args.target_web:
        scan_web(args.target_web)
    elif args.traffic:
        analyze_traffic(args.traffic)
    else:
        display_help()

if __name__ == "__main__":
    main()
