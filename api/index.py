from website import create_app

app = create_app()
app.secret_key = '12@#!_#SD'  # Better to use environment variable

# Add a test route to verify deployment
@app.route('/test')
def test():
    return {'status': 'working'}

# This is important! Vercel needs the app variable exposed
application = app