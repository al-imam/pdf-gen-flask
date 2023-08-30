from xhtml2pdf import pisa
import requests


def convert_url_to_pdf(url, output_path):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        with open(output_path, 'wb') as pdf_file:
            pisa.CreatePDF(html_content, dest=pdf_file)
            print(f'PDF created at: {output_path}')
    else:
        print(f"Failed to retrieve HTML content from URL: {url}")


def convert_html_to_pdf(html_text, output_path):
    with open(output_path, 'wb') as pdf_file:
        pisa.CreatePDF(html_text, dest=pdf_file)
        print(f'PDF created at - {output_path}')

def underline_and_space(value):
    return f"""<span style="text-decoration: underline; text-decoration-color: black;"><span class='underline-hide'>____</span>{value}<span class='underline-hide'>____</span></span>"""
