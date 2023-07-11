<<<<<<< HEAD
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
=======
import requests,json;
url = 'https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVINValuesBatch/';
post_fields = {'format': 'json', 'data':'3GNDA13D76S000000;5XYKT3A12CG000000'};
r = requests.post(url, data=post_fields);
print(r.text);	
>>>>>>> e16b086caa495538678987e7f4bb7ea4656571c1
