# Sample taken from pyStrich GitHub repository
# https://github.com/mmulqueen/pyStrich
import  time, netifaces, os

id = 0

def get_ips():
    """load ip addresses with netifaces"""
    local_ips = []
    public_ips = []
    
    # list of iface names, 'lo0', 'eth0', etc.
    for iface in netifaces.interfaces():
        # list of ipv4 addrinfo dicts
        ipv4s = netifaces.ifaddresses(iface).get(netifaces.AF_INET, [])
        for entry in ipv4s:
            addr = entry.get('addr')
            #print("addr: " + addr)
            if not addr:
                continue
            if not (iface.startswith('lo') or addr.startswith('127.')):
                public_ips.append(addr)
            else:
                local_ips.append(addr)        
    return public_ips

def write_file(text):
	if os.path.exists(filename):
		append_write = 'a' # append if already exists
	else:
		append_write = 'w' # make a new file if not
	file = open(filename,append_write)
	file.write(str(text) + '\n')
	file.close()

filename = str(get_ips()[0]) + str(time.time())
filename = "/mydata/" + filename.replace(".","_")  +".log" 
print(filename)
while(1):
	print(id)
	id = id+1
	write_file(id)
	time.sleep(1)