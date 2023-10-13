import os
from datetime import datetime

from src.util import convert_html_to_pdf

current_directory = os.path.dirname(os.path.abspath(__file__))


def get_authorize_html(value = {}):
    return f"""
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>itenary</title>
  </head>
  <style>
    * {{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
    }}
    
    .container {{
      font-family: sans-serif;
      padding: 0 40px;
      margin: auto;
    }}
    
    .text {{
        font-size: 14px;
        line-height: 1.5;
        margin: 0;
    }}
    
    .text-li {{
        font-size: 14px;
    }}
    
    .text-bottom {{
        font-size: 14px;
    }}
    

  </style>
  <body style="font-family: 'Roboto', sans-serif;">
    <div class="container">
      
      <h1 style="text-align: center; margin-top: 30px; font-size: 20px;">AUTHORISATION LETTER</h1>
      <p> I, {value.get("name")} (Name of applicant), holder of Passport type & number/Identity Card No. A03181341_, hereby authorise {value.get("representative_name")} (Name of the applicant’s representative), who is my {value.get("relationship")}(state relationship, e.g. Father, mother, sibling, friend, business associate, etc), holder of Passport type & number /Identity Card number {value.get("number")}, and email/contact number {value.get("contact")} to submit my visa application and all necessary documents and, if necessary, collect my passport and/or other personal documents on my behalf.</p>

      <p>To: {value.get("name_ava")} (name of AVA)</p>
      <p>To: {value.get("address_ava")} (address of AVA)</p>

    </div>
  </body>
</html>
"""


def get_authorize_file_name(code):
    return f"{code}-authorize-application.pdf"


def generate_authorize_pdf(value, code="unknown"):
    convert_html_to_pdf(
        get_authorize_html(value),
        os.path.normpath(
            os.path.join(current_directory, "../generated", get_authorize_file_name(code))
        ),
    )
