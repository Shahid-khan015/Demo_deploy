from main import app

# This is required for Vercel's serverless functions
def handler(request, response):
    return app(request, response)