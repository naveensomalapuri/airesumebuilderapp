import re
import json

def extractjson(content):
    content = str(content)
    
    # Define the pattern to match the content between content=' and response_metadata=
    pattern = r"content='(.*?)' response_metadata="
    
    # Use re.DOTALL to ensure the dot matches newlines
    match = re.search(pattern, content, re.DOTALL)
    
    if match:
        json_string = match.group(1)
        
        # Replace \n with a space
        json_string = json_string.replace("\\n", " ")
        
        # Remove multiple spaces, leaving only single spaces
        json_string = re.sub(r'\s+', ' ', json_string)
        
        # Convert the JSON string to a Python dictionary
        json_string = json.loads(json_string)
        return json_string
    else:
        return "No JSON content found."
