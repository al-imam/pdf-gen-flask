from datetime import datetime
import os
from src.util import convert_html_to_pdf, underline_and_space
from src.images import signature, stamp

current_directory = os.path.dirname(os.path.abspath(__file__))


def get_visa_html(name: str, passport: str):
    return f"""
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
    <style>

      * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
      }}

      .element {{
        background: #F0F8FF;
      }}

      .main-container {{
        padding: 5px 50px;
        margin: 50px auto;
        font-size: 14px;
      }}

      h4 {{
        font-weight: 300;
        text-align: justify;
      }}
      
      .down-border {{
        text-decoration: underline;
        font-family: monospace;
      }}

      .underline {{
        text-decoration: underline;
      }}

      .up-border {{
        border-top: 2px solid black;
      }}

      .full-width-table {{
        width: 100%; 
        table-layout: fixed; 
      }}

      .style-tr {{
        display: block; 
        width: 100%;
      }}

      .style-td {{
        width: 42.5%; 
        padding: 2px 0 10px;
      }}

      .style-td-gap {{
        width: 15%;
        padding: 2px 0 20px;
      }}

      .style-td-down {{
        width: 42.5%; 
        padding: 2px 0 5px;
      }}


      .style-td-gap-down {{
        width: 15%;
        padding: 2px 0 5px;
      }}
      
      .description {{ 
        margin-bottom: 20px; 
        line-height: 1.6; 
        text-align: justify;
      }}

    </style>
  </head>
  
  <body style="font-family: 'Roboto', sans-serif;">
    <div class="main-container">
      <table class="full-width-table">
        <tr class="style-tr">
          <td style="width: 50%; text-align: left;">Controller of Immigration<br /> Singapore </td>
          <td style="width: 50%; text-align: right;">Date: <span class="underline">{underline_and_space(datetime.today().strftime('%Y-%m-%d'))}</span></td>
        </tr>
      </table>

      <h4 style="margin: 16px 0;">Dear Sir</h4>

      <h4 style="text-align: center; margin-bottom: 24px;">
        LETTER OF INTRODUCTION FOR VISA APPLICATION
      </h4>

      <p class="description"> The applicant for the visa, {underline_and_space(str.upper(name))} ( name of applicant ) of {underline_and_space("BANGLADESH")} ( country/place ), holder of passport/travel document no. {underline_and_space(str.upper(passport))} is coming to Singapore from {underline_and_space("BANGLADESH")} ( country/place of embarkation ) for the purpose of {underline_and_space("HOLIDAY")} ( e.g., holiday, transit, business, meeting, exhibition, visiting friends & relatives, employment, education for others, please specify ). The applicant is my {underline_and_space("CLIENT")} ( e.g., father, mother, brother, sister, son, daughter, spouse, business partner; for others, please specify ). </p>

      <h4 style="margin: 20px 0;">
        Yours faithfully
      </h4>

      <h4 class="underline" style="padding-bottom: 10px; font-weight: bolder;">Only for application where Local Contact is an individual:</h4>

      <table class="full-width-table">

        <tr>
          <td class="style-td"><input /></td>
          <td class="style-td-gap"></td>
          <td class="element style-td"></td>
        </tr>
        <tr class="style-tr">
          <td class="up-border style-td">Signature of Local Contact</td>
          <td class="style-td-gap"></td>
          <td class="up-border style-td">NRIC (Pink / Blue) No</td>
        </tr>
        <tr>
          <td class="style-td element"></td>
          <td class="style-td-gap"></td>
          <td class="element style-td"></td>
        </tr>
        <tr class="style-tr">
          <td class="up-border style-td">Name of Local Contact</td>
          <td class="style-td-gap"></td>
          <td class="up-border style-td">Contact Number</td>
        </tr>
        <tr>
          <td class="style-td element"></td>
          <td class="style-td-gap"></td>
          <td class="element style-td"></td>
        </tr>
        <tr class="style-tr">
          <td class="up-border style-td-down">Address of Local Contact</td>
          <td class="style-td-gap-down"></td>
          <td class="up-border style-td-down">Email Address</td>
        </tr>
      </table>

      <img style="display: block;" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABT4AAAALCAYAAABWIZIYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAH/SURBVHhe7dohT2tBEIDRKQqHw1XhcHU4HA5Xh8LhcHU4HA6HQ+FwOFxdHa6uqq4OhwLmdTch7fyC+85JNjThg7T37o646ej7VwAAAAAADMhB+wkAAAAAMBgefAIAAAAAg+PBJwAAAAAwOAej0Sh211+Hh4d7v8/19fXVioijo6Oy+fz8bEXE8fFx2Ww2m1ZEjMfjslmv162IODk5KZvVatWKiNPT07JZLpetiJhMJmXz8fHRioizs7OyWSwWrYg4Pz8vm/l83oqIi4uLsnl/f29FxOXlZdm8vb21ImI6nZbN6+trKyKurq7K5uXlpRUR19fXZfP8/NyKiJubm7J5enpqRcTt7W3ZPD4+tiJiNpuVzcPDQysi7u7uyub+/r4V8e911eTfdvk/qybfQ5fvrWrys3T5Gasmr0mX16pq8tp2ec2rJu9Rl/euavJed7kHqib3TJd7qWpy73W5J6sm93CXe7tq8ix0eUaqJs9Ul2etavJsdnlmqybPeJdnv2pyVnQ5Q6omZ06Xs6hqcnZ1OdOqJmfgX1WT6y9zc78xN7fMzf3G3NwyN83N3WVubpmb+425uWVumpu7y9zcMjf3G3Nz63+dm77xCQAAAAAMjgefAAAAAMDgjL5/tdcAAAAAAIPgG58AAAAAwOB48AkAAAAADI4HnwAAAADAwET8AGrIwpPRd1H+AAAAAElFTkSuQmCC" alt="" />


      <h4 class="underline" style="font-weight: bolder;">Only for application where Local Contact is a company:</h4>

      <table class="full-width-table" style="margin-bottom: 50px:">
        <tr class="style-tr" >
           <td style="text-align: center;"><img style="width: 64px;" src={signature} alt="signature"></td>
          <td></td>
          <td ><img style="width: 64px; padding-left: 160px;  display: block;padding-bottom: -45px;" src="{stamp}" alt="img"><span>&nbsp;&nbsp;&nbsp;</span><p class="element-down" style="font-weight: bold; ">201727755Z</p></td>
        </tr>
        <tr class="style-tr">
          <td class="up-border style-td-down">Signature of person acting on behalf of the Company/Firm</td>
          <td class="style-td-gap-down"></td>
          <td class="up-border style-td-down">Unique Entity Number (UEN) of the Company/Firm
        </tr>
        <tr class="style-tr">
          <td class="element-down">SHAIKH MD SHAH JALAL, S7567880J, Director</td>
          <td ></td>
          <td class="element-down">+65 98570429</td>
        </tr>
        <tr class="style-tr gap-top">
          <td class="up-border style-td-down">Name, NRIC No. and Designation/Capacity</td>
          <td class="style-td-gap-down"></td>
          <td class="up-border style-td-down">Contact Number</td>
        </tr>
        <tr class="style-tr">
          <td class="element-down">Flyasia Travel Pte Ltd. 92B sSyed Alwi Road (level 3),Singapore 207668</td>
          <td ></td>
          <td class="element-down" style="padding-top: 10px;">sgflyasia@gmail.com</td>
        </tr>
        <tr class="style-tr gap-top">
          <td class="up-border style-td-down">Company Name and Address</td>
          <td class="style-td-gap-down"></td>
          <td class="up-border style-td-down">Email Address</td>
        </tr>
      </table>

      <p style="font-size: 14px;">
        V39A
      </p>
    </div>
  </body>
</html>
"""


def get_visa_file_name(code):
    return f"{code}-visa-application.pdf"


def generate_visa_pdf(name, passport, code="unknown"):
    convert_html_to_pdf(
        get_visa_html(name, passport),
        os.path.normpath(
            os.path.join(current_directory, "../generated", get_visa_file_name(code))
        ),
    )
