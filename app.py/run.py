from todo import create_app, db

# create the Flask app with config, database, and routes
app = create_app()

with app.app_context():
    db.create_all()  # create database tables if they don't exist

if __name__ == "__main__":
    app.run(debug=True)  # start the Flask server
