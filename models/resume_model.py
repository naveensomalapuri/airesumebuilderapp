from pydantic import BaseModel

class Resume(BaseModel):
    name: str
    bio: str
    job_description: str
    generated_resume: dict
