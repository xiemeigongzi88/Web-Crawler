import requests

# http://www.ip138.com/ips138.asp?ip=100.00.38.006&action=2
# IP address format: http://www.ip138.com/ips138.asp?ip= ipaddress

url='http://www.ip138.com/ips138.asp?ip='

r=requests.get(url+'202.204.80.112')
r.status_code

print(r.text[-500:])