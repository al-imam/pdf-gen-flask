import os
from src.util import convert_html_to_pdf
from src.images import banner

current_directory = os.path.dirname(os.path.abspath(__file__))


def tr(value):
    return f"""
      <tr>
        <td>{value["date"]}</td>
        <td>{value["from"]}</td>
        <td>{value["to"]}</td>
      </tr>
"""


def generate_html_table(array):
    return "\n".join(map(tr, array))


def get_itenary_html(dictionary):
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

    .table-container {{
      font-family: sans-serif;
      padding: 0 20px;
      margin: auto;
    }}


    .logo-img {{
      margin: 10px auto;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 35px;
    }}

    table {{
      width: 100%;
      border-collapse: collapse;
    }}

    td, th {{
      font-size: 16px;
      padding: 5px 15px;
      text-align: center;
    }}

    .heading {{
      text-align: center;
      text-decoration: underline;
      font-weight: 700;
      font-size: 25px;
    }}

  </style>
  <body style="font-family: 'Roboto', sans-serif;">
    <div class="table-container">
      <img class="logo-img" src="{banner}" alt="logo" />

      <h1 style="font-weight: 700" class="heading">TOUR ITENARY</h1>

      <div class="name-container">
        <p style="font-size: 22px; text-decoration: underline">
          {", ".join(map(lambda guest: f"{guest['name']} - {guest['passport_no']}", dictionary["guests"]))}
        </p>
      </div>

      <table border="1">
        <tr>
          <th>Date</th>
          <th>From</th>
          <th>To</th>
        </tr>

        {generate_html_table(dictionary["itenary"])}
      </table>
    </div>
  </body>
</html>
"""


def get_itenary_file_name(code):
    return f"{code}-itenary-application.pdf"


def generate_itenary_pdf(value, code="unknown"):
    convert_html_to_pdf(
        get_itenary_html(value),
        os.path.normpath(
            os.path.join(current_directory, "../generated", get_itenary_file_name(code))
        ),
    )
