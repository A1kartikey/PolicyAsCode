from fastapi import FastAPI, UploadFile, File
from scanner import scan_code, load_patterns

app = FastAPI(title="Compliance Genie - MVP")

patterns = load_patterns()

@app.post("/scan")
async def scan_python_code(file: UploadFile = File(...)):
    code = (await file.read()).decode("utf-8")
    results = scan_code(code, patterns)
    return {
        "filename": file.filename,
        "issues_found": len(results),
        "results": results
    }
