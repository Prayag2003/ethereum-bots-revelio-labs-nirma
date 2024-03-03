import requests
import json
import re

def generate_response_mistral(section):
    API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
    headers = {"Authorization": "Bearer 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"}
    
    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    output = query({"inputs": section})
    
    api_response_text = output[0]['generated_text']
    parts = api_response_text.split('\n\n[')
    final_response = parts[-1].replace('\n','').replace('\\','').strip()[0:-1].replace('  ','')
    
    result = re.findall(r'{[^{}]*}', final_response[1:])
    
    list_of_dicts = [json.loads(json_str) for json_str in result[1:]]
    
    return json.dumps(list_of_dicts)
