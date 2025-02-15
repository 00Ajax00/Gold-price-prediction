import uvicorn
import os
from backend.api.predict import app

if __name__ == "__main__":
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", 8000))

    try:
        uvicorn.run(app, host=host, port=port, reload=True)
    except Exception as e:
        print(f"Error starting the server: {e}")
