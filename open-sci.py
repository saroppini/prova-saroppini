# aprire json -> contare la lunghezza del valore della chiave invalid che è una delle due chiavi del dizionario che è il valore di citations. quindi aggiungiamo un'altra chiave al json, total_num_of_invalid_citations

import json


with open("output_read_only.json", errors='ignore', encoding='utf-8') as inputjson:
    data = json.load(inputjson)

data['total_num_of_invalid_citations'] = len(data["citations"]["invalid"])

with open('output_read_only_new.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, indent=2)
