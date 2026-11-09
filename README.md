# PlantPulse
An industrial machine monitoring platform, developed incrementally with
FastAPI and, in later phases, React and TypeScript.
## Current scope
Phase 2 foundation: a FastAPI service with a liveness endpoint and generated
API documentation. Machine simulation, the frontend, WebSockets, and database
integration will be added in later phases.
## Windows development setup
Run these PowerShell commands from the repository root. Python 3.14 is the
current development interpreter.
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r backend/requirements.txt
```
If `.venv` already exists, skip creating it. The requirements file pins the
direct dependencies; it is not a complete dependency lock file.
## Run the API locally
With the virtual environment active, run from the repository root:
```powershell
python -m uvicorn app.main:app --app-dir backend --reload
```
The server binds to localhost at `http://127.0.0.1:8000` by default.
`--reload` restarts it when Python files change and is for local development.
Stop the server with Ctrl+C.
- Health: <http://127.0.0.1:8000/health>
- Interactive API documentation: <http://127.0.0.1:8000/docs>
- OpenAPI schema: <http://127.0.0.1:8000/openapi.json>
From a second PowerShell terminal:
```powershell
Invoke-RestMethod http://127.0.0.1:8000/health
```
Expected JSON response: `{"status":"ok"}`. This checks API liveness only;
it does not check machines, hardware, or database connectivity.
## Structure
```text
backend/
  app/
    __init__.py
    main.py          # FastAPI application and health response model
  requirements.txt   # Direct backend dependency versions
```
Local environments, logs, secrets, and databases are excluded by `.gitignore`.
