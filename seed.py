import os
from datetime import datetime
from pepper_tracker import create_app, db
from pepper_tracker.models import PepperPlant
from data.plants import plants  

app = create_app()

with app.app_context():
    for plant_data in plants:
        # Parse the sowing date from string to a date object.
        sowing_date = datetime.strptime(plant_data["sowing_date"], "%Y-%m-%d").date()
        
        new_plant = PepperPlant(
            plant_type = plant_data["type"],
            sowing_date = sowing_date,
            seeds = plant_data["seeds"],
            germinated = plant_data["germinated"],
            seedlings = plant_data["seedlings"],
            hardening = plant_data["hardening"],
            plants = plant_data["plants"],
            year = plant_data["year"],
            dead = plant_data.get("dead", False),
            fruits = plant_data.get("fruits", 0)  # Default to 0 if not provided
        )

        db.session.add(new_plant)
    
    db.session.commit()
    print("Database seeded successfully!")
