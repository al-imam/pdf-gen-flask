from datetime import datetime
from io import BytesIO
from flask import Flask, request, Response, jsonify
from jsonschema import ValidationError, validate
from src.generate_visa_pdf import get_visa_html
from src.generate_itenary_pdf import get_itenary_html
from xhtml2pdf import pisa
from src.schema import itenary_schema, visa_schema

app = Flask(__name__)


@app.route("/generate/visa/", methods=["POST"])
def generate_pdf():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return (
                jsonify(
                    {
                        "message": "Request body is not valid JSON!",
                        "code": "invalid-json",
                    }
                ),
                400,
            )

        validate(data, visa_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_visa_html(
                data.get("name"), data.get("passport")
            )
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return (
                jsonify(
                    {
                        "message": f"PDF generation error: {str(e)}",
                        "code": "pdf-gen-error",
                    }
                ),
                500,
            )

        return Response(pdf_buffer, content_type="application/pdf")

    except ValidationError as e:
        return (
            jsonify(
                {
                    "message": "Request doesn't contain valid data!",
                    "error": str(e),
                    "code": "invalid-request",
                }
            ),
            400,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "message": "Internal Server Error",
                    "code": "server-break",
                    "error": str(e),
                }
            ),
            500,
        )


@app.route("/generate/itenary/", methods=["POST"])
def generate_itenary_pdf_route():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return (
                jsonify(
                    {
                        "message": "Request body is not valid JSON!",
                        "code": "invalid-json",
                    }
                ),
                400,
            )

        validate(data, itenary_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_itenary_html(data)
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return (
                jsonify(
                    {
                        "message": "PDF generation valid",
                        "code": "pdf-gen-error",
                        "error": str(e),
                    }
                ),
                500,
            )

        return Response(pdf_buffer, content_type="application/pdf")

    except ValidationError as e:
        return (
            jsonify(
                {
                    "message": "Request doesn't contain valid data!",
                    "error": str(e),
                    "code": "invalid-request",
                }
            ),
            400,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "message": "Internal Server Error",
                    "code": "server-break",
                    "error": str(e),
                }
            ),
            500,
        )


if __name__ == "__main__":
    app.run(debug=True)
