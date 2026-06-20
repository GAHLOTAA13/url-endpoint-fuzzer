#!/usr/bin/env python3
"""
URL Endpoint Fuzzer for Bug Bounty
Appends common security testing endpoints to a base URL
"""

# Common bug bounty endpoints
ENDPOINTS = [
    # Git version control
    '/.git',
    '/.git/config',
    '/.git/HEAD',
    
    # Other version control systems
    '/.svn',
    '/.svn/entries',
    '/.bzr',
    '/.hg',
    '/_darcs',
    
    # Environment files
    '/.env',
    '/.env.backup',
    '/.env.old',
    '/.env.production',
    
    # Admin panels
    '/admin',
    '/admin/login',
    '/administrator',
    '/phpmyadmin',
    
    # Common files
    '/phpinfo.php',
    '/wp-admin',
    '/wp-login.php',
    
    # Backup files
    '/backup',
    '/backup.sql',
    '/backup.zip',
    '/backup.tar.gz',
    
    # Config files
    '/config',
    '/config.php',
    '/wp-config.php',
    '/web.config',
    
    # Database dumps
    '/database.sql',
    '/db_backup.sql',
    
    # Standard files
    '/robots.txt',
    '/sitemap.xml',
    
    # API endpoints
    '/api',
    '/api/v1',
    '/api/swagger',
    '/swagger.json',
    '/graphql',
    
    # System files
    '/.DS_Store',
    '/.htaccess',
    
    # Debug/test endpoints
    '/debug',
    '/test',
    '/dev',
    '/server-status',
    '/console',
    
    # Authentication
    '/login',
    
    # Well-known URIs
    '/.well-known/',
    
    # Temp directories
    '/tmp/',
    '/temp/',
    
    # SSH keys
    '/.ssh/',
    '/id_rsa',
]


def normalize_url(url):
    """Normalize URL by adding protocol if missing and removing trailing slash"""
    url = url.strip()
    
    # Add https:// if no protocol specified
    if not url.startswith(('http://', 'https://')):
        url = 'https://' + url
    
    # Remove trailing slash
    if url.endswith('/'):
        url = url[:-1]
    
    return url


def parse_multi_urls(raw_input):
    """
    Parse multiple URLs from a single input string.
    Accepts comma-separated or newline-separated values, ignores blanks/duplicates.
    """
    # Support both comma-separated and newline-separated entries
    raw_input = raw_input.replace('\n', ',')
    candidates = [u.strip() for u in raw_input.split(',')]
    
    seen = set()
    urls = []
    for candidate in candidates:
        if not candidate:
            continue
        normalized = normalize_url(candidate)
        if normalized not in seen:
            seen.add(normalized)
            urls.append(normalized)
    return urls


def load_urls_from_file(filepath):
    """Load target URLs from a text file, one URL per line"""
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    return parse_multi_urls('\n'.join(lines))


def generate_urls(base_url, endpoints):
    """Generate full URLs by appending endpoints to a single base URL"""
    urls = []
    for endpoint in endpoints:
        full_url = base_url + endpoint
        urls.append(full_url)
    return urls


def generate_urls_multi(base_urls, endpoints):
    """
    Generate full URLs for MULTIPLE base URLs at once (batch/multi-URL mode).
    Returns a dict: {base_url: [list of generated urls]}
    """
    results = {}
    for base_url in base_urls:
        results[base_url] = generate_urls(base_url, endpoints)
    return results


def save_to_file(urls, filename='fuzzing_urls.txt'):
    """Save generated URLs to a file"""
    with open(filename, 'w') as f:
        for url in urls:
            f.write(url + '\n')
    print(f"\n[+] URLs saved to {filename}")


def main():
    print("=" * 60)
    print("URL Endpoint Fuzzer for Bug Bounty")
    print("=" * 60)
    
    print("\nSelect mode:")
    print("  1. Single URL")
    print("  2. Multiple URLs (comma-separated, batch mode)")
    print("  3. Load URLs from a file (one URL per line)")
    mode = input("\nEnter choice (1/2/3): ").strip()
    
    if mode == '3':
        filepath = input("Enter path to URL list file: ").strip()
        try:
            base_urls = load_urls_from_file(filepath)
        except FileNotFoundError:
            print(f"[!] Error: File '{filepath}' not found")
            return
    elif mode == '2':
        raw_input_urls = input("\nEnter target URLs (comma-separated, e.g. google.com,example.com): ").strip()
        base_urls = parse_multi_urls(raw_input_urls)
    else:
        single_url = input("\nEnter the target URL (e.g., google.com): ").strip()
        base_urls = parse_multi_urls(single_url)
    
    if not base_urls:
        print("[!] Error: No valid URL(s) provided")
        return
    
    print(f"\n[+] Targets loaded: {len(base_urls)}")
    print(f"[+] Generating {len(ENDPOINTS)} endpoint variations per target...")
    print(f"[+] Total URLs to be generated: {len(base_urls) * len(ENDPOINTS)}")
    print("[*] Including: .git, .svn, .bzr, .hg, _darcs, .env, admin panels, API endpoints, backups, etc.\n")
    
    # Generate URLs for all targets (multi-URL batch mode)
    results = generate_urls_multi(base_urls, ENDPOINTS)
    
    # Display results grouped by target
    all_urls = []
    for base_url, generated_urls in results.items():
        print("-" * 60)
        print(f"Target: {base_url}")
        print("-" * 60)
        for url in generated_urls:
            print(url)
            all_urls.append(url)
    print("-" * 60)
    
    # Ask if user wants to save to file
    save_choice = input("\nSave all results to file? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter filename (default: fuzzing_urls.txt): ").strip()
        if not filename:
            filename = 'fuzzing_urls.txt'
        save_to_file(all_urls, filename)
    
    print(f"\n[+] Targets processed: {len(base_urls)}")
    print(f"[+] Total URLs generated: {len(all_urls)}")
    print("[+] Done!")


if __name__ == "__main__":
    main()
