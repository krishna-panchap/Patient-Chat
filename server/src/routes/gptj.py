import os
from dotenv import load_dotenv
from pydantic import BaseModel
import requests
import json
import openai


load_dotenv()


class GPT:
    def __init__(self, name, age, sex, PMS, SH, CM, PP):
        openai.api_key = os.environ.get('OPEN_API_KEY');
        self.name = name
        self.age = age
        self.sex = sex
        self.PMS = PMS
        self.SH = SH
        self.CM = CM
        self.PP = PP



    def query(self, input: str) -> list:
      response = openai.Completion.create(
        model="text-davinci-003",

        prompt = 
        f"""
        Patient information:
        - Name: {self.name}
        - Age: {self.age}
        - Sex: {self.sex}
        - Past Medical History: {self.PMS}
        - Social History: {self.SH}
        - Current Medications: {self.CM}
        - Scheduled Procedures: {self.PP}
        
        
        Please answer concisely and do not congratulate them (keep it professional), and make sure to explain possible concerns/ things to know about with regard to their Past Medical History
        and Current  Medications. Please explain explicitly each medical history in the list and
        how it might impact their question. Also explain explicitly how each medicine in their list
        impacts their upcoming surgery. After addressing their question, mention things they can do to 
        have a complication-free experience after surgery. Close off with your name, MediAI.

        Patient Question: {input}
        """,
        temperature=0.72,
        max_tokens=724,
        top_p=1,
        frequency_penalty=0.22,
        presence_penalty=0.14
      )
      text = response['choices'][0]['text']
      return text

# if __name__ == "__main__":
#     instance = GPT(name = "John Phillips", age = 65, sex = 'male', PMS=['Type 2 Diabetes', 'hypoglycemia', 'hypothyroidism', 'High blood pressure'], 
#     CM = ['Metformin 500 mg 2 tablets twice daily', 'Glimepiride 1 mg daily', 'Lisinopril 20 mg daily', 'Atorvastatin 20 mg daily', 'Levothyroxine 88 mcg daily', 'Aspirin 81 mg daily', 'Coenzyme q10 200 mg daily', 'Vitamin D 2000 IU daily'],
#     PP = " The patient has a knee arthroplasty scheduled 2 days from now.", SH = ['Smoker', 'Light Drinker'] 
#     )
    
    
#     print(instance.query("Hello, my name is John and I am scheduled f  or Knee Replacement Surgery. I am feeling a little concerned, what can I expect of this procedure for myself"))