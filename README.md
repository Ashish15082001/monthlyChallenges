# monthlyChallenges

A Django project I'm building while learning Django.

Built with Django 6.1.1 on Python 3.14.

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate   # Windows (Git Bash)
# .venv\Scripts\activate        # Windows (PowerShell)
# source .venv/bin/activate     # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# then generate a secret key and paste it into .env:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# 4. Apply migrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
```

The app is then served at http://127.0.0.1:8000/.

## Notes

`SECRET_KEY` and `DEBUG` are read from environment variables in
`monthlyChallenges/settings.py`. The `.env` file holds the local values and is
gitignored — never commit it. `settings.py` falls back to a throwaway
development key so `runserver` works without any setup, but that fallback must
never be used in production.
