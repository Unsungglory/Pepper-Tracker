# pepper_tracker/main.py
from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required
from pepper_tracker.models import PepperPlant
from pepper_tracker import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    # Fetch all pepper plant records
    peppers = PepperPlant.query.all()
    
    # Calculate totals
    totals = {
        "seeds": sum(p.seeds for p in peppers),
        "germinated": sum(p.germinated for p in peppers),
        "seedlings": sum(p.seedlings for p in peppers),
        "hardening": sum(p.hardening for p in peppers),
        "plants": sum(p.plants for p in peppers)
    }
    totals["germination_percentage"] = (
        round((totals["germinated"] / totals["seeds"]) * 100, 2)
        if totals["seeds"] > 0
        else 0
    )
    
    return render_template('index.html', peppers=peppers, totals=totals)


@main_bp.route('/update/<int:plant_id>', methods=['POST'])
@login_required
def update_plant(plant_id):
    plant = PepperPlant.query.get_or_404(plant_id)
    try:
        plant.seeds = int(request.form.get('seeds', plant.seeds))
        plant.germinated = int(request.form.get('germinated', plant.germinated))
        plant.seedlings = int(request.form.get('seedlings', plant.seedlings))
        plant.hardening = int(request.form.get('hardening', plant.hardening))
        plant.plants = int(request.form.get('plants', plant.plants))
        plant.dead = int(request.form.get('dead', plant.dead))
        plant.fruits = int(request.form.get('fruits', plant.fruits))
    except Exception as e:
        flash(f"Error updating record: {e}", "danger")
        return redirect(url_for('main.index'))
    
    db.session.commit()
    flash('Plant record updated!', 'success')
    return redirect(url_for('main.index'))
