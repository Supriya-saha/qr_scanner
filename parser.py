from urllib.parse import urlparse, parse_qs

class URLParser:
    def parse(self, url):
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
   
        extracted = {}
        for key, value_list in params.items():
            extracted[key] = value_list[0] if value_list else ""
        
        return extracted
