from fastapi import APIRouter, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, FileResponse
from services.resume_service import generate_resume, save_resume, get_all_resumes, view_resume
from models.resume_model import Resume
from pdfcrowd import HtmlToPdfClient
import os

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/create_resume")
async def show_form(request: Request):
    return templates.TemplateResponse("resume_form.html", {"request": request})

@router.post("/generate_resume")
async def create_resume(name: str = Form(...), bio: str = Form(...), job_description: str = Form(...)):
    generated_resume = generate_resume(bio, job_description)
    
    # Create a Resume instance
    resume = Resume(name=name, bio=bio, job_description=job_description, generated_resume=generated_resume)
    
    # Convert the Pydantic model instance to a dictionary
    resume_dict = resume.dict()
    
    # Save the resume to the database
    resume_id = save_resume(resume_dict)
    
    if resume_id:
        # Redirect to the resume list page
        return RedirectResponse(url="/", status_code=303)
    else:
        raise HTTPException(status_code=500, detail="Failed to save resume")

@router.get("/")
async def list_resumes(request: Request):
    resumes = get_all_resumes()
    return templates.TemplateResponse("resume_list.html", {"request": request, "resumes": resumes})

@router.get("/resume_view/{resume_name}")
async def view(resume_name: str, request: Request):
    # Call the synchronous function to retrieve the resume data
    resume = view_resume(resume_name)
    if resume and 'name' in resume:
        return templates.TemplateResponse("resume_detail.html", {"request": request, "resume": resume})
    else:
        raise HTTPException(status_code=404, detail="Resume not found")

@router.get("/resume_download/{resume_name}")
async def download_pdf(resume_name: str, request: Request):
    # Call the synchronous function to retrieve the resume data
    resume = view_resume(resume_name)
    if resume and 'name' in resume:
        # Render the HTML content from the template
        html_content = templates.get_template("resume_detail.html").render(request=request, resume=resume)
    else:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    pdf_file_path = f"resume_{resume_name}.pdf"
    client = HtmlToPdfClient("venkat913355","63a3da52797edd89f83eb4792651123a")  # Replace with your actual username and API key
    try:
        client.convertStringToFile(html_content, pdf_file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"PDF generation failed: {str(e)}")
    
    return FileResponse(path=pdf_file_path, filename=f"resume_{resume_name}.pdf", media_type="application/pdf")
