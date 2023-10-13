import os
from datetime import datetime

from src.util import convert_html_to_pdf

current_directory = os.path.dirname(os.path.abspath(__file__))


def get_authorize_html(value={}):
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
      padding: 0 60px;
      margin: auto;
    }}

    tr {{
      margin: 20px 0;
    }}
    


  </style>
  <body style="font-family: 'Roboto', sans-serif; font-size: 16px;">
    <div class="container">
      
      <h1 style="text-align: center; margin-top: 30px; font-size: 20px; padding-top: 40px; text-decoration: underline;">AUTHORISATION LETTER</h1>
      <p> I, {value.get("client")} (Name of applicant), holder of Passport type & number/Identity Card No. {value.get("client_passport_number")}, hereby authorise {value.get("authorizer")} (Name of the applicant’s representative), who is my {value.get("relationship")}(state relationship, e.g. Father, mother, sibling, friend, business associate, etc), holder of Passport type & number/Identity Card number {value.get("authorizer_passport_number")}, and email/contact number {value.get("contact")} to submit my visa application and all necessary documents and, if necessary, collect my passport and/or other personal documents on my behalf.</p>

      <p style="padding-top: 30px;">To: {value.get("name_ava")} (name of AVA)</p>
      <p>At: {value.get("address_ava")} (address of AVA)</p>

      <table style="margin-top: 60px;">
        <tr>
          <td>__________________</td>
          <td>{getCurDate()}</td>
        </tr>
        <tr>
          <td>Signature of applicant</td>
          <td>Date</td>
        </tr>
        <tr>
          <td><p style="padding: 50px 0;">Accepted by AVA :</p></td>
        </tr>
        <tr>
          <td>________________</td>
          <td>{getCurDate()}</td>
        </tr>
        <tr>
          <td>Signature of AVA</td>
          <td>Date</td>
        </tr>
      </table>

    </div>
  </body>
</html>
"""


def getCurDate():
    return datetime.now().strftime("%d %b %y").upper()


def get_authorize_file_name(code):
    return f"{code}-authorize-application.pdf"


def generate_authorize_pdf(value, code="unknown"):
    convert_html_to_pdf(
        get_authorize_html(value),
        os.path.normpath(
            os.path.join(
                current_directory, "../generated", get_authorize_file_name(code)
            )
        ),
    )
