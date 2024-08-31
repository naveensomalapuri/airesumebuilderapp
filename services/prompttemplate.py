from langchain.prompts import PromptTemplate
"""
# Define the user inputs
bio = "Somalapuri Naveen is a seasoned software engineer with 8 years of experience in full-stack development, holding a B.Sc. in Computer Science from State University, proficient in JavaScript, Python, React, Docker, and experienced in leading projects and mentoring developers. Future Tech Solutions is seeking a Senior Software Engineer with expertise in JavaScript, Python, React, Docker, and AWS to lead and develop scalable web applications, mentor junior developers, and stay current with industry trends."
job_description = "Job Title: Senior Software Engineer | Company: Future Tech Solutions | Location: San Francisco, CA | Job Description: Future Tech Solutions seeks a Senior Software Engineer with a robust background in full-stack development to lead and develop scalable, high-performance web applications, collaborate with cross-functional teams, mentor junior developers, and stay current with industry trends and emerging technologies. Required Skills: Proficiency in JavaScript, Python, React, Docker, and experience with AWS or Azure. Preferred Qualifications: Agile development experience and an advanced degree in Computer Science. Benefits: Competitive salary, health insurance, flexible work hours, and professional development opportunities."
"""

def promtfun(bio, job_description):
  # Define the prompt template
  prompt_template = PromptTemplate(
    input_variables=["bio", "job_description"],
    template="""
    Bio: {bio}

    Job Description: {job_description}

    Task:
    1. Analyze the provided bio to extract all relevant information, including name, contact details, professional experience, skills, education, certifications, projects, awards, volunteer work, publications, and other relevant details.
    2. Cross-reference the extracted information with the job description to ensure alignment between the candidate's qualifications and the job requirements.
    3. Correct any grammatical errors in the bio, enhance the language for clarity and impact, and structure the bio to make it compelling for the specific job role.
    4. Generate a detailed and well-structured resume in BSON format based on the provided bio and job description. The BSON output must strictly adhere to proper syntax without any errors.
    5. Ensure that the BSON output does not contain newline characters or `\\n` in any part of the response.
    Ensure that the following sections are included in the BSON format:

{{
  "name": "Extracted name here",
  "contact_information": {{
    "phone_number": "Extracted phone number",
    "email_address": "Extracted email address",
    "linkedin_profile": "Extracted LinkedIn profile",
    "physical_address": "Extracted physical address"
  }},
  "objective_or_summary": {{
    "career_objective": "Generated career objective based on bio and job description"
  }},
  "work_experience": [
    {{
      "company_name": "Extracted company name",
      "job_title": "Extracted job title",
      "employment_dates": "Extracted employment dates",
      "key_responsibilities": [
        "Extracted key responsibility 1",
        "Extracted key responsibility 2"
      ],
      "achievements": [
        "Extracted achievement 1",
        "Extracted achievement 2"
      ]
    }}
  ],
  "education": [
    {{
      "school_name": "Extracted school name",
      "degree": "Extracted degree",
      "graduation_date": "Extracted graduation date",
      "relevant_coursework": [
        "Extracted coursework 1",
        "Extracted coursework 2"
      ]
    }}
  ],
  "skills": {{
    "technical_skills": [
      "Extracted technical skill 1",
      "Extracted technical skill 2"
    ],
    "soft_skills": [
      "Extracted soft skill 1",
      "Extracted soft skill 2"
    ],
    "languages": [
      "Extracted language 1",
      "Extracted language 2"
    ]
  }},
  "projects": [
    {{
      "project_name": "Extracted project name",
      "description": "Extracted project description",
      "technologies_used": [
        "Extracted technology 1",
        "Extracted technology 2"
      ],
      "project_link": "Extracted project link"
    }}
  ],
  "hobbies_and_interests": [
    "Extracted hobby or interest 1",
    "Extracted hobby or interest 2"
  ],
  "languages": [
    {{
      "language_name": "Extracted language name",
      "proficiency_level": "Extracted proficiency level"
    }}
  ]
}}

    """
)
  return prompt_template

