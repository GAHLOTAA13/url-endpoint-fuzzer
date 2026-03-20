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


def generate_urls(base_url, endpoints):
    """Generate full URLs by appending endpoints to base URL"""
    urls = []
    for endpoint in endpoints:
        full_url = base_url + endpoint
        urls.append(full_url)
    return urls


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
    
    # Get base URL from user
    base_url = input("\nEnter the target URL (e.g., google.com): ").strip()
    
    if not base_url:
        print("[!] Error: URL cannot be empty")
        return
    
    # Normalize the URL
    base_url = normalize_url(base_url)
    print(f"\n[+] Base URL: {base_url}")
    print(f"[+] Generating {len(ENDPOINTS)} endpoint variations...\n")
    print("[*] Including: .git, .svn, .bzr, .hg, _darcs, .env, admin panels, API endpoints, backups, etc.\n")
    
    # Generate URLs
    generated_urls = generate_urls(base_url, ENDPOINTS)
    
    # Display results
    print("-" * 60)
    for url in generated_urls:
        print(url)
    print("-" * 60)
    
    # Ask if user wants to save to file
    save_choice = input("\nSave to file? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter filename (default: fuzzing_urls.txt): ").strip()
        if not filename:
            filename = 'fuzzing_urls.txt'
        save_to_file(generated_urls, filename)
    
    print(f"\n[+] Total URLs generated: {len(generated_urls)}")
    print("[+] Done!")


if __name__ == "__main__":
    main()
