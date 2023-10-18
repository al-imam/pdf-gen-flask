import os
from datetime import datetime

from src.util import convert_html_to_pdf

current_directory = os.path.dirname(os.path.abspath(__file__))


def tr(value):
    return f"""
      <tr>
        <td style="font-size: 13px; text-algin: left; padding: 4px 0 0 4px; margin: 0;">{value["sl"]}</td>
        <td style="font-size: 13px; text-algin: left; padding: 4px 0 0 4px; margin: 0;">{value["name"]}</td>
        <td style="font-size: 13px; text-algin: left; padding: 4px 0 0 4px; margin: 0;">{value["number"]}</td>
        <td style="font-size: 13px; text-algin: left; padding: 4px 0 0 4px; margin: 0;">{value["remarks"]}</td>
      </tr>
"""


def generate_html_table(array):
    return "\n".join(map(tr, array))


def get_undertaking_family_html(name, array):
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

    table {{
            border-collapse: collapse;
            width: 100%;
        }}

        table, th, td {{
            border: 1px solid black;
        }}

        th, td {{
            text-align: left;
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
      
    <p class="text">Date: {datetime.today().strftime('%d/%m/%Y')}</p>
    <p class="text"> </p>
    <p class="text">To,</p>
    <p class="text">The Second Secretary (Visa and Consular)</p>
    <p class="text">High Commission of The Republic of Singapore,</p>
    <p class="text">Dhaka, Bangladesh.</p>

    <h3 style="margin-top: 30px; font-size: 20px;">UNDERTAKING</h3>

    <p class="text-li">I am {name}, Proprietor of park view confectionary. My family’s passport details are as follows:</p>

      <table >
        <tr>
          <th style="font-size: 13px; text-algin: left; padding: 4px 0 0 4px; margin: 0;">SL</th>
          <th style="font-size: 13px; text-algin: left; padding: 4px 0 0 4px; margin: 0;">NAME</th>
          <th style="font-size: 13px; text-algin: left; padding: 4px 0 0 4px; margin: 0;">PP NUMBER</th>
          <th style="font-size: 13px; text-algin: left; padding: 4px 0 0 4px; margin: 0;">REMARKS</th>
        </tr>

        {generate_html_table(array)}
      </table>

    <p class="text-li" style="margin: 40px 0 0 0;">I, {name}, applied for Singapore visa and solemnly declare that:</p>

    <div>
        <p class="text-li" style="padding: 0 0 0 20px; margin: 5px;">
         <span style="font-family: monospace; font-weight: 600;">i.</span> I am aware that visa application processing time at the consulate of the Republic of Singapore, Dhaka is minimum 5(Five) working days (Excluding submission Date) to 1(one) month (or more).
        </p>
        <p class="text-li" style="padding: 0 0 0 20px; margin: 5px;">
          <span style="font-family: monospace; font-weight: 600;">ii.</span> 	I agree with all the terms & conditions related to my visa application as well as while I am in Singapore.
        </p>
        
    </div>

    <p class="text-bottom">Thanking you</p>
    <p class="text-bottom">Yours Sincerely,</p>
    <p style="height: 30px;"> </p>

    <p>{"_" * (len(name) + 2) }</p>
    <p class="text-bottom" style="padding-top: -15px">{name}</p>

    </div>
  </body>
</html>
"""


def get_undertaking_family_file_name(code):
    return f"{code}-undertaking_family-application.pdf"


def generate_undertaking_family_pdf(name, array, code="unknown"):
    convert_html_to_pdf(
        get_undertaking_family_html(name, array),
        os.path.normpath(
            os.path.join(
                current_directory,
                "../generated",
                get_undertaking_family_file_name(code),
            )
        ),
    )
