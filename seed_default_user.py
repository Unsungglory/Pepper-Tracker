# seed_default_user.py
from pepper_tracker import create_app, db
from pepper_tracker.models import User

app = create_app()

with app.app_context():
    if not User.query.filter_by(username='admin').first():
        # Create the default user (ensure you change the password to something secure)
        default_user = User(username='nick', password='password')
        db.session.add(default_user)
        db.session.commit()
        print("Default user created.")
    else:
        print("Default user already exists.")
