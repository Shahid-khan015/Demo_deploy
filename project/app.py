from website import create_app

# Create the Flask app
app = create_app()
app.secret_key = '12@#!_#SD'

# Expose the app for deployment platforms like Vercel
application = app

# Add a default route to confirm the app is working
@app.route('/')
def home():
    return "Welcome to the Flask App!"

# For local development/testing
if __name__ == '__main__':
    app.run(debug=True)
