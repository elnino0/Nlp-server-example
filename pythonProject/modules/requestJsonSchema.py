analyzeJsonSchema = {
    "type": "object",
    "properties": {
        "text": {"type": "string"},
        "method": {"type": "string"}
    },
    "additionalProperties": False,
    "required": [
        "text",
        "method"
    ]
}

sentimentJsonSchema = {
    "type": "object",
    "properties": {
        "text": {"type": "string"}
    },
    "additionalProperties": False,
    "required": [
        "text",
    ]
}
