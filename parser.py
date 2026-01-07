from urllib.parse import urlparse, parse_qs

class URLParser:
    def parse(self, url):
        parsed = urlparse(url)
        params = parse_qs(parsed.query)
        return {
            "patient_id": params.get("patientId", [""])[0],
            "hospital_id": params.get("hospitalId", [""])[0]
        }
