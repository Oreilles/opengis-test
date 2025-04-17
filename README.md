# How to test

```sh
# Start database
docker compose up

# Setup python environment
uv venv
source .venv/bin/activate
uv sync

# Run migrations and start backend
python manage.py migrate
python manage.py runserver

# Start frontend
cd frontend
npm i
npm run dev
```
