import geocoder
import folium
from requests import get

ip = get('https://api.ipify.org').text


g = geocoder.ip(ip)
my_address = g.latlng
my_map = folium.Map(location=my_address,
                    zoom_start=120)
folium.CircleMarker(location=my_address,radius=50,popup="yorkshire").add_to(my_map)
my_map.save("mymap1.html")
## importing socket module
import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")

import socket    
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)    
print("Your Computer Name is:" + hostname)    
print("Your Computer IP Address is:" + IPAddr) 
#How to get the IP address of a client using socket