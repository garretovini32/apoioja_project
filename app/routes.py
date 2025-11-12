from flask import Blueprint, render_template, request, jsonify
from .models import Report
from . import db
from datetime import datetime

bp = Blueprint('routes', __name__)

# Página inicial
@bp.route('/')
def index():
    return render_template('index.html')

# Página de denúncia
@bp.route('/denuncia')
def denuncia():
    return render_template('denuncia.html')

# API: Receber denúncias (POST)
@bp.route('/api/reports', methods=['POST'])
def create_report():
    data = request.get_json() or request.form

    category = data.get('category')
    location = data.get('location')
    description = data.get('description')

    if not all([category, location, description]):
        return jsonify({'error': 'Preencha todos os campos.'}), 400

    report = Report(
        category=category,
        location=location,
        description=description,
        created_at=datetime.utcnow()
    )
    db.session.add(report)
    db.session.commit()

    return jsonify({'message': 'Denúncia registrada com sucesso!'}), 201

# API: Visualizar todas as denúncias (GET)
@bp.route('/api/reports', methods=['GET'])
def get_reports():
    reports = Report.query.order_by(Report.created_at.desc()).all()
    return jsonify([
        {
            'id': r.id,
            'category': r.category,
            'location': r.location,
            'description': r.description,
            'created_at': r.created_at.isoformat()
        }
        for r in reports
    ])
