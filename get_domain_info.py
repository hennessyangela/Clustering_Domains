from time import sleep
import sys, argparse, requests, json

# url to search crt.sh
BASE_URL = "https://crt.sh/?q={}&output=json"
def crtsh(domain):
#Look up given domain in crt.sh
#(certificate transparency logs)
    print('Looking up {}'.format(domain))
    try:
        response = requests.get(BASE_URL.format(domain), timeout=5)
        if response.ok:
            
            content = response.content.decode('UTF-8')
            jsondata = json.loads(content)
            resp_domains=[]
            for i in range(len(jsondata)):
                name_value = jsondata[i]['name_value']
                resp_domains.append(name_value)

            return resp_domains
    except:
        return None
domains= set()

# Read in domains from block list
for line in open('bad_domains_all.txt','r'):
    domains.add(line.strip())

print(domains)

# open output file
with open('output.txt','w') as fout:
    for domain in domains:
        sleep(10)
# write the output of crt.sh lookup to output file
        fout.write(domain)
        fout.write('\n')
        fout.write(str((crtsh(domain))))
        fout.write('\n')
fout.close()
