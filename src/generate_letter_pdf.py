import os
from datetime import datetime

from src.util import convert_html_to_pdf

current_directory = os.path.dirname(os.path.abspath(__file__))


def get_letter_html(name):
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
    
    body {{ zoom: 0.5; }}
    
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
      
    <p class="text">Date: {datetime.today().strftime('%d/%m/%Y')}</p>
    <p class="text"> </p>
    <p class="text">To,</p>
    <p class="text">The Second Secretary (Visa and Consular)</p>
    <p class="text">High Commission of The Republic of Singapore,</p>
    <p class="text">Dhaka, Bangladesh.</p>

    <h3 style="text-align: center; margin-top: 30px; font-size: 20px;">UNDERTAKING</h3>

    <p class="text-li" style="margin-bottom: 0;">I, {name}, applied for Singapore visa and solemnly declare that:</p>

    <ol type="a" style="line-height: 6;">
        <li class="text-li">
            I have submitted all necessary documents required to apply for Singapore visa.
        </li>
        <li class="text-li">
            I am aware that the visa application processing time at the Consulate of the Republic of Singapore,
             Dhaka is minimum 5 (five) working days and more (Excluding Submission Date).
        </li>
        <li class="text-li">
            I agree with all the term & condition related to my visa application as well as while I am in Singapore.
        </li>
    </ol>

    <p class="text-bottom">Thanking you</p>
    <p class="text-bottom">Yours Sincerely,</p>
    <p style="height: 30px;"> </p>

    <p>{"_" * (len(name) + 2) }</p>
    <p class="text-bottom" style="padding-top: -15px">{name}</p>

    </div>
  </body>
</html>
"""


def get_letter_file_name(code):
    return f"{code}-letter-application.pdf"


def generate_letter_pdf(value, code="unknown"):
    convert_html_to_pdf(
        get_letter_html(value),
        os.path.normpath(
            os.path.join(current_directory, "../generated", get_letter_file_name(code))
        ),
    )
