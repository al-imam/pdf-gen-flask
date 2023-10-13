from datetime import datetime
from io import BytesIO
from flask import Flask, request, Response, jsonify
from jsonschema import ValidationError, validate
from src.generate_visa_pdf import get_visa_html, generate_visa_pdf
from src.generate_itenary_pdf import get_itenary_html, generate_itenary_pdf
from src.generate_letter_pdf import get_letter_html, generate_letter_pdf
from xhtml2pdf import pisa
from src.schema import itenary_schema, visa_schema, letter_schema

app = Flask(__name__)


@app.route("/generate/visa/", methods=["POST"])
def generate_visa_pdf_route():
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
                data.get("name"), data.get("passport"), data.get("purpose")
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


@app.route("/generate/letter/", methods=["POST"])
def generate_letter_pdf_route():
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

        validate(data, letter_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_letter_html(data.get("name"))
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


@app.route("/generate/test/", methods=["GET"])
def test():
    generate_itenary_pdf(
        {
            "guest": {"name": "Al-imam", "passport": 43534, "family": 4},
            "itenary": [
                {
                    "date": datetime.today().strftime("%Y-%m-%d"),
                    "from": "AirPost",
                    "to": "Hotel valentilo",
                },
                {
                    "date": datetime.today().strftime("%Y-%m-%d"),
                    "from": "AirPost",
                    "to": "Hotel valentilo",
                },
            ],
        },
    )

    generate_visa_pdf("HelloLUEHUIG", "A3485G45", "visitingfrien")

    generate_letter_pdf("Nirob")

    return (
        jsonify({"success": True}),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
