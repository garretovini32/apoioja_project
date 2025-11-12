from app import create_app, db
from app.models import Report

app = create_app()

# Cria o banco na primeira execução
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
