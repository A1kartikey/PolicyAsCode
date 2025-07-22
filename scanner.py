import re
import json

def load_patterns(file_path="pattern_library.json"):
    with open(file_path, "r") as f:
        return json.load(f)

def scan_code(code: str, patterns: list) -> list:
    results = []
    lines = code.split("\n") 

    for line_num, line in enumerate(lines, start=1):
        for pattern in patterns:
            regex = re.compile(pattern["regex"], re.IGNORECASE)

            matches = regex.finditer(line)
            for match in matches:
                results.append({
                    "pattern_id": pattern["id"],
                    "name": pattern["name"],
                    "description": pattern["description"],
                    "severity": pattern["severity"],
                    "matched_text": match.group(0),
                    "line": line_num,
                    "position": match.start()
                })
    return results
