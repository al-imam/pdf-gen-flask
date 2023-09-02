from datetime import datetime
from io import BytesIO
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, StreamingResponse
from jsonschema import ValidationError, validate
from src.generate_visa_pdf import generate_visa_pdf, get_visa_html
from src.generate_itenary_pdf import generate_itenary_pdf, get_itenary_html
from xhtml2pdf import pisa
from src.schema import itenary_schema

app = FastAPI()


@app.post("/generate/visa/")
async def generate_pdf(request: Request):
    try:
        data = await request.json()

        if not (isinstance(data, dict) and data.get("name") and data.get("passport")):
            return JSONResponse(
                status_code=400,
                content={
                    "message": "'name' and 'passport' are required!",
                    "code": "invalid-req",
                },
            )

        pdf_buffer = BytesIO()

        try:
            content = get_visa_html(data.get("name"), data.get("passport"))
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={
                    "message": f"PDF generation error: {str(e)}",
                    "code": "pdf-gen-error",
                },
            )

        return StreamingResponse(pdf_buffer, media_type="application/pdf")

    except ValueError:
        return JSONResponse(
            status_code=400,
            content={
                "message": "Request body is not valid JSON!",
                "code": "invalid-json",
            },
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Internal Server Error",
                "code": "server-break",
            },
        )


@app.post("/generate/itenary/")
async def generate_pdf(request: Request):
    try:
        data = await request.json()

        validate(data, itenary_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_itenary_html(data)
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={
                    "message": f"PDF generation error: {str(e)}",
                    "code": "pdf-gen-error",
                },
            )

        return StreamingResponse(pdf_buffer, media_type="application/pdf")

    except ValueError:
        return JSONResponse(
            status_code=400,
            content={
                "message": "Request body is not valid JSON!",
                "code": "invalid-json",
            },
        )

    except ValidationError as e:
        return JSONResponse(
            status_code=400,
            content={
                "message": "Request doesn't contain valid data!",
                "expected-shape": {
                    "guests": [{"name": "string", "passport_no": "string"}],
                    "itenary": [
                        {"date": "2023-09-01", "from": "string", "to": "string"}
                    ],
                },
                "provided": data,
                "code": "invalid-request",
            },
        )

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": "Internal Server Error",
                "code": "server-break",
            },
        )


@app.get("/generate/visa-itenary-test")
async def generate_pdf():
    generate_itenary_pdf(
        {
            "guests": [
                {"name": "Al-imam", "passport_no": 43534},
            ],
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

    generate_visa_pdf("Al-Imam", "345D42343")

    return {"success": True}
