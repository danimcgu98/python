from sys import argv, exit
from nmap import *
import re
from os import path
from socket import getfqdn, herror
import subprocess

GEO_URL = 'ipinfo.io/'
RANGE_MODE = '--cidr'
IPS_MODE = '--ips' 
HELP_MODE = '--help'

def main():
    
    if not validate_arg_num():
        output_help()
        exit(2)
     
    mode=argv[1]    
    if mode == RANGE_MODE:
        
        if not is_range(argv[2]):
            output_help()
            exit(3)
            
        scanner = PortScanner()    
        results = scanner.scan(hosts=argv[2], arguments='-sn')
        
        host_list = get_active_hosts(scanner, results)
        print('Host(s): ',end='')
        output_items(host_list)
        print('\n')
        
        
        for host in host_list:
            print(f'---{host}---')
            print(f'Host Name: {get_dns(host)}')
            output_geolocation(host)
            print('Open Port(s): ',end='')
            ports_list = get_open_ports(scanner, host_list)
            output_items(ports_list)
            print('\n')
            
    elif mode == IPS_MODE:
        
        scanner = PortScanner()
        
        ip_list = get_arguments()

        for i, ip in enumerate(ip_list):
            if is_ip(ip):
                print(f'---{ip}---')
                print(f'Host Name: {get_dns(ip)}')
                output_geolocation(ip)
                port_list = get_open_ports(scanner, ip_list)
                print('Open Port(s): ',end='')
                output_items(port_list)
            else:
                print(f'Argument {i+1} is not a valid ip address')
            print('\n')
    
    elif mode == HELP_MODE:
        output_help()
                     
    else:
        output_help()
        exit(4)
                      

def execute_curl_command(curl_command):
    try:
        result = subprocess.run(curl_command, capture_output=True, text=True)
        if result.returncode == 0:
            return result.stdout
        else:
            return None
    except subprocess.CalledProcessError:
        return None

  
def get_active_hosts(scanner, results):
    
    ip_list = []
    if 'scan' in results:
        for host in scanner.all_hosts():
            if scanner[host].state() == 'up':
                ip_list.append(host)
                
    return ip_list       


def get_arguments():
    
    args = []
    for i, arg in enumerate(argv):
        
        if i == 0 or i == 1:
                continue
        else:
            args.append(arg)
    
    return args


def get_dns(ip):
    
    try:
        domain_name = getfqdn(ip)
        return domain_name
    except herror:
        return "DNS lookup failed"


def get_open_ports(scanner, ip_list):
    
    ports_list = []        
    for target in ip_list:
        results = scanner.scan(target, arguments="-p 0-1023")
        if 'scan' in results:
            for port in scanner[target]['tcp']:
                if scanner[target]['tcp'][port]['state'] == 'open':
                    ports_list.append(port)
                    
    return ports_list


def is_ip(ip):
    
    ip_pattern = r"^\b(25[0-5]|2[0-4]\d|[01]?\d{1,2})\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})\b$"
    
    if re.match(ip_pattern, ip):
        return True
    
    return False


def is_range(ip):
    range_pattern = r"^\b(25[0-5]|2[0-4]\d|[01]?\d{1,2})\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})\.(25[0-5]|2[0-4]\d|[01]?\d{1,2})\/\d{1,2}$"

    if re.match(range_pattern, ip):
        return True

    return False


def output_geolocation(ip):
    
    url = GEO_URL + ip
    org_url = url + '/org'
    country_url = url + '/country'
    region_url = url + '/region'
    city_url = url + '/city'
    loc_url = url + '/loc'
    timezone_url = url + '/timezone'
    print(f'Owner: {execute_curl_command(["curl", org_url])}',end='')
    print(f'Country: {execute_curl_command(["curl", country_url])}',end='')
    print(f'Province/State: {execute_curl_command(["curl", region_url])}',end='')
    print(f'City: {execute_curl_command(["curl", city_url])}',end='')
    print(f'Long/Lat: {execute_curl_command(["curl", loc_url])}',end='')
    print(f'Time Zone: {execute_curl_command(["curl", timezone_url])}',end='')


def output_items(list):
    
    is_first=True
    for item in list:
        if is_first:
            print(f"{item}",end='')
            is_first=False
        else:
            print(', ',end='')
            print(f"{item}",end='')


def output_help():
    
    file_name = path.basename(__file__)
    print('Usages:')
    print(f'1. python {file_name} --help')
    print(f'2. python {file_name} --cidr ip_range_CIDR')
    print(f'3. python {file_name} --cidr address1 address2 address3 ...')


def validate_arg_num():
    
    min_arg = 2
    argc = len(argv) - 1;

    if argc < min_arg:
        return False
    
    return True


if __name__ == '__main__':    
    main()