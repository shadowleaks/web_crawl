import requests

def request(url):
	try:
		return requests.get("https://" + url)
	except requests.exceptions.ConnectionError:
		pass


target_url = ""

with open("/root/Downloads/web_crawl/subdomains.list", "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		test_url = word + "." + target_url
		response = request(test_url)
		if response:
			print("[+] Discovered subdomain --> " + test_url)
