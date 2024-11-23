from website import create_app

app = create_app()
app.secret_key = '12@#!_#SD'  # Better to use environment variable

# This is important! Vercel needs the app variable exposed
application = app

if __name__ == '__main__':
    app.run()