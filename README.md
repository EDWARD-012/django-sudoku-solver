# Django Sudoku Solver

Live Demo: https://django-sudoku-solver-z3uo.vercel.app/

A simple Django-based Sudoku solver web application with a clean input form and results page. Users can enter 9x9 Sudoku puzzles, submit, and receive up to 10 valid solved grids.

## 🚀 Features

- 9x9 Sudoku grid input UI
- Solver based on backtracking with row/column/3x3 constraint checks
- Multiple solutions support (up to 10 results per request)
- Handles empty cells gracefully and ignores invalid digits
- Rendered via templates `index.html` and `result.html`
- Deployed on Vercel using Django + Gunicorn + Whitenoise static support

## 🧩 Project Structure

- `manage.py` - Django CLI utility
- `sudoku/` - Django project settings and WSGI/asgi
- `sudokuapp/` - Sudoku app routes and logic
  - `views.py` - solving logic, home and solve views
  - `urls.py` - local routing
- `templates/` - HTML templates
  - `index.html` - input form
  - `result.html` - solutions display
- `staticfiles/` - admin and assets (auto-collected assets)

## ⚙️ Requirements

- Python 3.11+ (tested with Python 3.12 available in container)
- `pip`
- `virtualenv` (recommended)

## 📦 Install locally

1. Clone repository

```bash
git clone https://github.com/EDWARD-012/django-sudoku-solver.git
cd django-sudoku-solver
```

2. Create and activate environment

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Apply migrations (no custom models required, but Django expects migrations)

```bash
python manage.py migrate
```

5. Run development server

```bash
python manage.py runserver
```

6. Open http://127.0.0.1:8000/

## 🧠 Sudoku solver details

Solver uses `sudokuapp/views.py` functions:

- `is_valid(board, row, col, ch)` - checks row, column, and 3x3 block constraints
- `solve_sudoku(board, solutions, row=0, col=0, limit=10)` - recursive backtracking
- `solve` view builds board from POST fields `cell{i}{j}` and returns solutions

If no valid solution exists, output board is unchanged and `solutions` is empty.

## 🧪 Testing

No dedicated tests included yet. Basic manual validation flow:

1. Enter a known Sudoku puzzle on the home page
2. Click solve
3. Verify output in the result table

## 🌐 Vercel deployment

- `vercel.json` controls the deployment. Example anticipates Django WSGI with `gunicorn` and static file support.
- Production command (from Vercel settings): `gunicorn sudoku.wsgi`

## 🛠️ Optional improvements

- Add Django form validation for 9x9 and numeric constraints
- Add test coverage with Django `TestCase` for `is_valid` and `solve_sudoku`
- Add frontend input UX (cell highlighting, keyboard navigation)

## 🤝 Contributing

1. Fork repository
2. Create feature branch
3. Send pull request

## 📄 License

MIT-style license (add or replace with your preferred terms as needed).