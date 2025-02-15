import os

from groq import Groq
    
client = Groq(
    # This is the default and can be omitted
    api_key="grooq_api",
)
def generate_email(name, intent, extracted_info,case_study):
    
    """Generate email based on user intent,visited website and extracted case studies."""

    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful and Professional Email writer assistant, Your task is to write a very professional email maintaining the syntax on the basis of the intent and the last visited websites of the user that it matches the case studies of what company does. Write an email on the basis of what the user wants which matches our companies domain and what services the company provides to that intention."
                },
                {
                    "role": "user",
                    "content": (f"Generate a professional email for {name} based on their intention : {intent} "
                f"Based on the provided company case study:  {case_study}, gather relevant portfolio or application URLs designed by the company. Include these links in the email under an appropriate information heading derived from the case study. Present each breif description  explaining what the URL showcases in a structured new line along with a url link at end. This is the websites the user visited: {extracted_info}. Write a sophasticated well structured like professional email to the user from the company provided case study, and remember no placeholders just write on the basis of company user visited. The name of the user is : {name}, And donot give placeholders. Just generate the mail in your response nothing else"),
                }
            ],
            model="llama-3.3-70b-versatile",
            max_tokens=1024,
        )
        
        
        return chat_completion.choices[0].message.content


    except:
        return "Please input only one Link inside the chatbot/ or try after 1 min."



def extract_intent(request,info):
    
    "Extract the intentions of the user from the messages"
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "you are a helpful assistant, Your task is to give the users intention on the basis of message or he/she written or the webpages the user has visited recently."
                },
                {
                    "role": "user",
                    "content": f"Determine the intent from this message: {request.message} and this is the last visited websites by the user websites: {info}. Remeber Give your intention in short about what user wants to do."
                }
            ],
            model="llama-3.3-70b-versatile",
            max_tokens=1024,
        )
        
        
        
        return chat_completion.choices[0].message.content    
    except:
        return "Please input only one Link inside the chatbot/ or try after 1 min."
    
    
    
    
    
    
    

