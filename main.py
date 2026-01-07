from scanner import QRScanner
from parser import URLParser

scanner = QRScanner() 
url = scanner.start()  # Start scanning and get the URL from the QR code

if url:  # If a URL is successfully scanned
    parser = URLParser()
    data = parser.parse(url)
    print("Extracted Data:", data)
