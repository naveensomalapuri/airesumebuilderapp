from services.extract_json import extractjson
from services.model import openmodle
from services.prompttemplate import promtfun
import os
import json
import uuid

# Define the directory where JSON files will be stored
RESUME_DIR = 'resumes_data'

# Ensure the directory exists
os.makedirs(RESUME_DIR, exist_ok=True)

def generate_resume(bio: str, job_description: str) -> dict:
    # Generate the prompt using the promtfun
    prompt_template = promtfun(bio, job_description)

    # Render the prompt by formatting the template
    prompt = prompt_template.format(bio=bio, job_description=job_description)
    
    # Pass the rendered prompt string to openmodle
    response = openmodle(prompt=prompt)

    # Debugging: Print the response
    print(f"Response from openmodle: {response}")

    # Handle None response
    if response is None:
        print("Error: No response received from openmodle.")
        return {}  # Return an empty dictionary or handle as needed
    print("#" * 10, "Before extracting", "#" * 10)
    print(response)

    # Extract JSON from the response
    result = extractjson(response)
    print(f"Extracted JSON: {result}")

    # Convert result from JSON string to dict if needed
    return result

def save_resume(resume_data: dict) -> str:
    try:
        # Generate a unique ID for the resume
        resume_id = str(uuid.uuid4())
        file_name = f'{resume_id}.json'
        file_path = os.path.join(RESUME_DIR, file_name)
        
        # Save the resume data as a JSON file
        with open(file_path, 'w') as file:
            json.dump(resume_data, file, indent=4)
        
        return resume_id
    except Exception as e:
        print(f"Error saving resume to file: {e}")
        return None

def get_all_resumes() -> list:
    resumes = []
    try:
        # Load all resumes from the directory
        for file_name in os.listdir(RESUME_DIR):
            file_path = os.path.join(RESUME_DIR, file_name)
            with open(file_path, 'r') as file:
                resume_data = json.load(file)
                resumes.append(resume_data)
    except Exception as e:
        print(f"Error reading resumes from file: {e}")
    return resumes

def delete_resume(resume_id: str) -> bool:
    try:
        file_name = f'{resume_id}.json'
        file_path = os.path.join(RESUME_DIR, file_name)
        
        # Check if the file exists
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        else:
            print(f"Error: Resume file {file_name} does not exist.")
            return False
    except Exception as e:
        print(f"Error deleting resume file: {e}")
        return False
    


import os
import json

RESUME_DIR = 'resumes_data'

import os
import json

def view_resume(resume_name: str) -> dict:
    try:
        for file_name in os.listdir(RESUME_DIR):
            file_path = os.path.join(RESUME_DIR, file_name)
            with open(file_path, 'r') as file:
                resume_data = json.load(file)
                # Check if the 'name' field matches the resume_name
                if resume_data.get('name') == resume_name:
                    return resume_data
        # Return a message if no matching resume is found
        return {'error': 'Resume not found'}
    except Exception as e:
        print(f"Error reading resume file: {e}")
        return {'error': str(e)}

if __name__ == "__main__":
    sample_bio = "Somalapuri Naveen is a seasoned software engineer with 8 years of experience in full-stack development..."
    sample_job_description = "Job Title: Senior Software Engineer | Company: Future Tech Solutions..."

    test_resume = generate_resume(sample_bio, sample_job_description)
    print("Generated Resume:", test_resume)
