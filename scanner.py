import re
import json

def load_patterns(file_path="pattern_library.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def scan_code(code: str, patterns: list) -> list:
    results = []
    for pattern in patterns:
        matches = re.finditer(pattern["regex"], code)
        for match in matches:
            results.append({
                "pattern_id": pattern["id"],
                "name": pattern["name"],
                "description": pattern["description"],
                "severity": pattern["severity"],
                "matched_text": match.group(0),
                "position": match.start()
            })
    return results
