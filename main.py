from scanner import QRScanner
from parser import URLParser

scanner = QRScanner()
url = scanner.start()

if url:
    parser = URLParser()
    data = parser.parse(url)
    print("Extracted Data:", data)
