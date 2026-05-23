## Setup

# 1. Create a virtual environment and install deps:
python -m venv .venv
.venv\Scripts\activate            # Windows PowerShell
pip install -r requirements.txt

# 2. Run the app:
python app.py
# Open http://localhost:5000


## Repo layout
app.py                  Flask entry point (single-file app for now)
templates/              Jinja templates
CLAUDE.md               project context Claude Code reads automatically
requirements.txt        Python dependencies

## Ground rules
- Don't paste secrets, API keys, or personal credentials anywhere.
