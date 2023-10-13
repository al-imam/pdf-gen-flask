itenary_schema = {
    "type": "object",
    "properties": {
        "guest": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "passport": {"anyOf": [{"type": "integer"}, {"type": "string"}]},
                "family": {"type": "string"},
            },
            "required": ["name", "passport", "family"],
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
    "required": ["guest", "itenary"],
}


visa_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "passport": {"type": "string"},
        "purpose": {"type": "string"},
    },
    "required": ["name", "passport", "purpose"],
}

letter_schema = {
    "type": "object",
    "properties": {"name": {"type": "string"}},
    "required": ["name"],
}

authorize_schema = {
    "type": "object",
    "properties": {
        "client": {"type": "string"},
        "client_passport_number": {"type": "string"},
        "authorizer": {"type": "string"},
        "relationship": {"type": "string"},
        "authorizer_passport_number": {"type": "string"},
        "contact": {"type": "string"},
        "name_ava": {"type": "string"},
        "address_ava": {"type": "string"},
    },
    "required": [
        "client",
        "client_passport_number",
        "authorizer",
        "relationship",
        "authorizer_passport_number",
        "contact",
        "name_ava",
        "address_ava",
    ],
}
