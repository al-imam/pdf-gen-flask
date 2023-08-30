from src.generate_itenary_pdf import generate_itenary_pdf
from src.generate_visa_pdf import generate_visa_pdf
from datetime import datetime

if __name__ == "__main__":
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

    generate_visa_pdf("Al-imm", "345345345345")
