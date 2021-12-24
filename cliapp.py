import requests
import json
import argparse
import csv

parser= argparse.ArgumentParser()
parser.add_argument('getcve')
args=parser.parse_args()

url1="https://services.nvd.nist.gov/rest/json/cves/1.0/"
url2='https://services.nvd.nist.gov/rest/json/cves/1.0/?startIndex=1'
r1=requests.get(url1)
r2=requests.get(url2)
data1=json.loads(r1.text)
data2=json.loads(r2.text)

def get():
    
    with open('cves.csv','w',newline='') as f:
        writer=csv.writer(f)
        for i in range(20):
            writer.writerow([ data1['result']['CVE_Items'][i]['cve']['CVE_data_meta']['ID'],data1['result']['CVE_Items'][i]['publishedDate'],data1['result']['CVE_Items'][i]['cve']['references']['reference_data'][0]['url'],data1['result']['CVE_Items'][i]['cve']['description']['description_data'][0]['value']])

        for i in range(20):
            writer.writerow([ data2['result']['CVE_Items'][i]['cve']['CVE_data_meta']['ID'],data2['result']['CVE_Items'][i]['publishedDate'],data2['result']['CVE_Items'][i]['cve']['references']['reference_data'][0]['url'],data2['result']['CVE_Items'][i]['cve']['description']['description_data'][0]['value']])
    
get()
