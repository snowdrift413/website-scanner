from domain_name import *
from general import *
from ip_address import *
from nmap import *
from robots_txt import *
from whois import *
import time

ROOT_DIR = 'websites'
create_dir(ROOT_DIR)


def gather_info(name, url):
    domain_name = get_domain_name(url)
    robots_txt = get_robots_txt(url)
    whois = get_whois(domain_name)
    ip_address = str(get_ip_address(domain_name))
    nmap = get_nmap('-F', ip_address)
    create_report(name, url, domain_name, nmap, robots_txt, whois)


def create_report(name, full_url, domain_name, nmap, robots_txt, whois):
    project_dir = ROOT_DIR + '/' + name
    create_dir(project_dir)
    write_file(project_dir + '/full_url.txt', full_url)
    write_file(project_dir + '/domain_name.txt', domain_name)
    write_file(project_dir + '/nmap.txt', nmap)
    write_file(project_dir + '/robots_txt.txt', robots_txt)
    write_file(project_dir + '/whois.txt', whois)


if __name__ == '__main__':
    website_name = input('\nEnter the name of website to scan: ')
    website_url = input('\nEnter the full url of the website: ')

    print('\nGetting all things clear...')
    time.sleep(2)
    print(f'\nGetting full url of {website_name}...')
    time.sleep(1)
    print(f'\nGetting IP addresses of {website_name}...')
    time.sleep(1)
    print(f'\nGetting top level domain of {website_name}...')
    time.sleep(1)
    print(f'\nRunning nmap on {website_url}...')
    time.sleep(1)
    print('\nGetting all the robots.txt files...')
    time.sleep(1)
    print(f'\nPerforming whois lookup on {website_url}...')
    time.sleep(1)

    gather_info(website_name, website_url)
    time.sleep(2)

    print(f'\nGenerating report for {website_name}...')
    time.sleep(1)
    print('\nDone everything! Thanks for using me.')
