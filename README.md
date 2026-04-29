# 25-26-8640----WEB-SERVICES-AND-APPLICATIONS

Course repository for Web Services and Applications (Higher Diploma in Science in Computing in Data Analytics).

## Repository Layout

- `project/` - Main coursework project (Flask REST API + MySQL)
- `docs/` - Project and API documentation
- `assignments/` - Weekly assignment deliverables
- `labs/` - Lab work and exercises
- `_scratch/` - Personal rough work and experiments

## Main Project

If you are reviewing the core project, start here:

1. `project/src/app.py` - Flask API routes (CRUD endpoints)
2. `project/src/book_dao.py` - Data access layer for MySQL
3. `project/scripts/init_db.py` - Database/table initialization script
4. `docs/api/README.md` - API contract and examples
5. `docs/project/README.md` - Setup, run, and troubleshooting guide

## Notes

- Environment secrets are not committed (`.env` is ignored).
- The project uses the repository-level virtual environment at `.venv`.
