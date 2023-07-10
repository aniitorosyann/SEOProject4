import requests,json;
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/';
post_fields = {'format': 'json', 'data':'3GNDA13D76S000000;5XYKT3A12CG000000'};
r = requests.post(url, data=post_fields);
print(r.text);	
