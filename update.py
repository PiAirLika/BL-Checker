import requests

def main():
    import_hash()
    import_ip()
    import_domain()
    import_url()

    print(f"# number of entries (Hash): {count_entries('src/hash_bl.txt')}")
    print(f"# number of entries (IP): {count_entries('src/ip_bl.txt')}")
    print(f"# number of entries (Domain): {count_entries('src/domain_bl.txt')}")
    print(f"# number of entries (URL): {count_entries('src/url_bl.txt')}")

def import_hash():
    path = "src/hash_bl.txt"
    hash_list = {
        ('recent malware samples ','https://bazaar.abuse.ch/export/txt/sha256/recent/'),
        ('malicious hash', 'https://github.com/romainmarcoux/malicious-hash/raw/refs/heads/main/full-hash-sha256-aa.txt')
    }
    with open(path, '+w') as updatefile:
        for name,url in hash_list:
            r = requests.get(url)
            if r.status_code == 200:
                updatefile.write(f"$ {name}\n")
                updatefile.write(r.text + "\n")
            else:
                print(f"Error with {name} {url}")
            

def import_ip():
    path = "src/ip_bl.txt"
    ip_list = {
        ('tor exits','https://raw.githubusercontent.com/firehol/blocklist-ipsets/refs/heads/master/tor_exits.ipset'), 
        ('Tracker Botnet C2 IP Blocklist','https://feodotracker.abuse.ch/downloads/ipblocklist_recommended.txt'),
        ('Botnets/Zombies/Scanners in European Cyber Space', 'https://raw.githubusercontent.com/duggytuxy/malicious_ip_addresses/refs/heads/main/botnets_zombies_scanner_spam_ips.txt'),
        ('active compromised IP','https://zonefiles.io/f/compromised/ip/live/'),
        ('Crowdsourced IP feed from ThreatCrowd', 'https://github.com/firehol/blocklist-ipsets/raw/refs/heads/master/threatcrowd.ipset'),
        ('php_harvesters', 'https://github.com/firehol/blocklist-ipsets/raw/refs/heads/master/php_harvesters.ipset')
        # possible de rajouter : https://github.com/romainmarcoux/malicious-ip
    }
    with open(path, '+w') as updatefile:
        for name,url in ip_list:
            r = requests.get(url)
            if r.status_code == 200:
                updatefile.write(f"$ {name}\n")
                updatefile.write(r.text + "\n")
            else:
                print(f"Error with {name} {url}")

def import_domain():
    path = "src/domain_bl.txt"
    domain_list = {
        ('malicious domain used for phising','https://hole.cert.pl/domains/v2/domains.txt'),
        ('active compromised domain', 'https://zonefiles.io/f/compromised/domains/live/'),
        ('malware and phising domain', 'https://github.com/romainmarcoux/malicious-domains/raw/refs/heads/main/full-domains-aa.txt'),
        ('malware and phising domain', 'https://github.com/romainmarcoux/malicious-domains/raw/refs/heads/main/full-domains-aa.txt.txt'),
        ('malware and phising domain', 'https://github.com/romainmarcoux/malicious-domains/raw/refs/heads/main/full-domains-ab.txt'),
        ('malware and phising domain', 'https://github.com/romainmarcoux/malicious-domains/raw/refs/heads/main/full-domains-aa.txt.txt'),
    }
    with open(path, '+w') as updatefile:
        for name,url in domain_list:
            r = requests.get(url)
            if r.status_code == 200:
                updatefile.write(f"$ {name}\n")
                updatefile.write(r.text + "\n")
            else:
                print(f"Error with {name} {url}")

def import_url():
    path = "src/url_bl.txt"
    url_list = {
        ('report malware','http://vxvault.net/URL_List.php'),
        ('malicious URLs used for malware distribution','https://urlhaus.abuse.ch/downloads/text_online/'),
        ('pishing url', 'https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt')
    }
    with open(path, '+w') as updatefile:
        for name,url in url_list:
            r = requests.get(url)
            if r.status_code == 200:
                updatefile.write(f"$ {name}\n")
                updatefile.write(r.text + "\n")
            else:
                print(f"Error with {name} {url}")

def count_entries(path):
    try:
        with open(path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        return 0

if __name__ == '__main__':
    main()