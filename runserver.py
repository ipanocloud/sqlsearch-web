import os
from app import create_app
from config import logger

app = create_app(os.getenv('FLASK_ENV') or 'default')

if __name__ == '__main__':
    logger.info("server start...")
    app.run()
