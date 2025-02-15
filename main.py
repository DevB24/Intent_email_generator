from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
from database import search_case_studies
from retrival import extract_intent, generate_email
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
@app.get("/", response_class=HTMLResponse)
async def serve_homepage(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Define input model
class UserRequest(BaseModel):
    name: str
    email: str
    message: str
    visited_pages: list[str]


def extract_content(url):
    """Scrape page content from the given URL."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return ' '.join([p.text for p in soup.find_all('p')])
    except Exception as e:
        return f"Error fetching {url}: {e}"



@app.post("/analyze-urls")
def analyze_urls(request: UserRequest):
    """Process user request, determine intent, extract case study info, and generate email."""
    

    extracted_info = "\n".join([extract_content(url) for url in request.visited_pages])
    intent = extract_intent(request,extracted_info)
    
    case_studies = search_case_studies(intent, request.visited_pages)
    
    
    case_study_text = "\n".join([f"tittle : {cs['title']}: \n Content : {cs['description']} Description: {cs['content']}" for cs in case_studies])

    
    email_content = generate_email(request.name, intent, extracted_info ,case_study_text)
    # returns the generated email
    return {
        "intent": intent,
        "extracted_info": extracted_info,
        "generated_email": email_content
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
