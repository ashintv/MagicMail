import google.generativeai as genai
import os

#genai.configure(api_key=os.environ["API_KEY"])

def api_call_mail(user):
    print(user)
    prom = f'create an email from {user['Name']} ,recipient name is {user['Reciever']},data {user} in the form of {user['Type']} send back the email only with given information'
    my_api_key = 'AIzaSyA6CioVC1OUvPnljiaAywUnRvPNJDtSIzY'
    genai.configure(api_key=my_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    result = model.generate_content(prom)
    print(result.text)
    return result.text



def api_call_bot(mse):
    my_api_key = 'AIzaSyA6CioVC1OUvPnljiaAywUnRvPNJDtSIzY'
    genai.configure(api_key=my_api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    chat = model.start_chat(
        history=[
        ]
    )
    response = chat.send_message(mse)
    print(response.text)
    return response.text

