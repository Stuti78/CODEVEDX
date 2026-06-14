import requests

print("====================================")
print(" Web Application Security Scanner ")
print("====================================")

url = input("Enter Website URL (e.g., https://example.com): ")

try:
    response = requests.get(url, timeout=10)

    print("\nWebsite Status Code:", response.status_code)

    headers = response.headers

    print("\nChecking Security Headers...\n")

    security_headers = [
        "Content-Security-Policy",
        "X-Frame-Options",
        "Strict-Transport-Security",
        "X-XSS-Protection",
        "X-Content-Type-Options"
    ]

    for header in security_headers:
        if header in headers:
            print(f"[✓] {header} Found")
        else:
            print(f"[✗] {header} Missing")

    print("\nServer Information:")
    print(headers.get("Server", "Not Disclosed"))

    if url.startswith("https://"):
        print("\n[✓] HTTPS Enabled")
    else:
        print("\n[✗] HTTPS Not Enabled")

except requests.exceptions.RequestException as e:
    print("\nError:", e)