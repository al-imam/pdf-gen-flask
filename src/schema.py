itenary_schema = {
    "type": "object",
    "properties": {
        "guests": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "passport_no": {"anyOf": [{"type": "integer"}, {"type": "string"}]},
                },
                "required": ["name", "passport_no"],
            },
        },
        "itenary": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "date": {"type": "string", "format": "date"},
                    "from": {"type": "string"},
                    "to": {"type": "string"},
                },
                "required": ["date", "from", "to"],
            },
        },
    },
    "required": ["guests", "itenary"],
}
