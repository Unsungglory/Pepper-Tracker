from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from pepper_tracker.models import User
from pepper_tracker import db, login_manager

auth_bp = Blueprint('auth', __name__, template_folder='templates')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        # For simplicity, we're comparing plaintext. In production, hash your passwords!
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@login_manager.user_loader
def load_user(user_id):
    from pepper_tracker.models import User
    return User.query.get(int(user_id))
