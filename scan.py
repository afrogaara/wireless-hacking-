import requests 
import socket  
import re 

portas = [80, 21, 22]
list_ip = list() 

def ippublico():
    try:
        ip = requests.get('https://api.ipify.org/').text
        return ip
    except:
        print('site fora do ar')

def enum(ip):
    print(f"ip found - > {ip}")
    try:  
        n = re.findall(r"\d{1,3}.\d{1,3}.\d{1,3}.", ip)
        for c in n:
            return c 
    except:
        print('nenhum ip encontrado')

def lista(ip):
    for n in range(0, 255+1, +1):
        conca = ip + str(n)
        list_ip.append(conca) 
    return list_ip

def scan(list_ip, portas):
    for i in list_ip:
        print(f'scan no ip {i}')
        for p in portas:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.settimeout(1.0)
            request = cliente.connect_ex((i, 80))
            if request == 0:
                print(f"{i} - > [+] {p} Open port")
   


if __name__ == "__main__":
    ip = ippublico()
    c = enum(ip)
    list_ip = lista(c)
    scan(list_ip, portas)
    
