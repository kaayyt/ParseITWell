import yaml
import requests
import json
CONFIG_PATH = r"config.yaml"
api_key = None
with open(CONFIG_PATH) as file:
    data = yaml.load(file, Loader=yaml.FullLoader)
    api_key = data['GROQ_API_KEY']
def ats_extractor(resume_data):
    prompt = '''
    You are an AI bot designed to act as a professional for parsing resumes. You are given with resume and your job is to extract the following information from the resume:
    1. Full Name
    2. Email id
    3. Github portfolio
    4. Linkedin id
    5. Education 
    6. Employment details
    7. Technical skills
    8. Soft skills
    9. Certifications
    Give the extracted information in json format only
    '''
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": resume_data}
    ]
    
    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": messages,
        "temperature": 0.0,
        "max_tokens": 1500,
        "response_format": {"type": "json_object"}  # Request JSON object response
    }
    
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()  # Raise error for bad HTTP status
        
        data = response.json()
         # Extract the content from the response
        extracted_info = data['choices'][0]['message']['content']
        
        
        if isinstance(extracted_info, dict):
            return extracted_info
        
        
        return json.loads(extracted_info)
        
    except requests.exceptions.RequestException as e:
        print(f"API Request Error: {e}")
        return {"error": f"API request failed: {str(e)}"}
    
    except KeyError as e:
        print(f"KeyError in response: {e}")
        print(f"Full response: {response.text}")
        return {"error": "Unexpected API response format"}
    
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Raw content: {extracted_info}")
        return {"error": "Failed to parse JSON response"}
    
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {"error": f"Unexpected error: {str(e)}"}