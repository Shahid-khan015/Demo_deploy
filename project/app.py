from website import create_app

app = create_app()
app.secret_key = '12@#!_#SD'

# Expose the app for Vercel
application = app

# For local testing
if __name__ == '__main__':
    app.run(debug=True)
