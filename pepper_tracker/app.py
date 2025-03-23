# pepper_tracker/app.py
from pepper_tracker import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
