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
    "properties": {"name": {"type": "string"}, "passport": {"type": "string"}},
    "required": ["name", "passport"],
}
