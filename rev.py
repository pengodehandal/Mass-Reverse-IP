import requests
import time
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from colorama import Fore, init
import pyfiglet

init(autoreset=True)

def print_ascii_art():
    ascii_banner = pyfiglet.figlet_format("PengodeHandal", font="slant")
    print(Fore.CYAN + ascii_banner)
    print(Fore.YELLOW + "Welcome to Reverse IP Lookup Tool! 🚀")
    print(Fore.GREEN + "Github: https://github.com/pengodehandal/Mass-Reverse-IP/")

def reverse_ip_lookup(ip_or_domain):
    url = f"https://api.webscan.cc/?action=query&ip={ip_or_domain}"
    
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        if response.text.strip() == "":
            print(Fore.RED + f"No data returned for {ip_or_domain}")
            return []

        try:
            data = response.json()
            if data is None:
                print(Fore.RED + f"Invalid response format for {ip_or_domain}")
                return []

        except ValueError as e:
            print(Fore.RED + f"Error parsing JSON response for {ip_or_domain}: {e}")
            return []

        valid_domains = []
        for item in data:
            domain = item.get("domain")
            if domain and domain != "defacer.net":
                if domain.startswith("www."):
                    domain = domain[4:]
                valid_domains.append(domain)
        
        return valid_domains

    except requests.RequestException as e:
        print(Fore.RED + f"Error fetching data for {ip_or_domain}: {e}")
        return []

def process_input_file(input_file, output_file, max_threads=30):
    with open(input_file, 'r') as f:
        ips_or_domains = f.readlines()
    
    total_domains = 0
    total_website_found = 0
    total_items = len(ips_or_domains)
    start_time = time.time()

    processed_domains = set()

    with open(output_file, 'a') as out_file:
        with ThreadPoolExecutor(max_threads) as executor:
            futures = {}
            
            for idx, item in enumerate(ips_or_domains):
                item = item.strip()
                futures[executor.submit(reverse_ip_lookup, item)] = item
            
            for future in as_completed(futures):
                item = futures[future]
                result = future.result()

                if result:
                    total_website_found += len(result)
                    for domain in result:
                        if domain not in processed_domains:
                            processed_domains.add(domain)
                            out_file.write(domain + "\n")
                    print(Fore.GREEN + f"Found {len(result)} websites for {item}")
                else:
                    print(Fore.RED + f"No valid domains found or error for {item}")
                
                time.sleep(0.5)

    remove_duplicates(output_file)

    return total_domains, total_website_found

def remove_duplicates(file_name):
    with open(file_name, "r") as f:
        lines = f.readlines()

    unique_lines = set(line.strip() for line in lines)

    with open(file_name, "w") as f:
        for line in unique_lines:
            f.write(line + "\n")

def main():
    print_ascii_art()

    print(Fore.YELLOW + "=== Reverse IP Lookup ===")
    input_file = input(Fore.YELLOW + " Masukan nama file (berisi IP atau domain): ")
    output_file = "HasilReverseIPS.txt"

    while True:
        try:
            max_threads = int(input(Fore.YELLOW + "Masukkan jumlah thread (maksimal 30): "))
            if max_threads < 1 or max_threads > 30:
                print(Fore.RED + "Jumlah thread harus antara 1 dan 30.")
            else:
                break
        except ValueError:
            print(Fore.RED + "Input tidak valid! Masukkan angka yang benar.")

    total_domains, total_website_found = process_input_file(input_file, output_file, max_threads)
    print(Fore.YELLOW + f"\nTotal website ditemukan dan disimpan: {total_website_found}")

if __name__ == "__main__":
    main()
