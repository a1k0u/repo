"""
Server configuration run
"""

import sys
import stud_api.uploader.upload as uploader
import uvicorn

if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("Choose start mode: upload, server ...")

    _, command = sys.argv

    if command == "--upload":
        from stud_api.db.engine import engine
        import stud_api.db.models as models

        models.Base.metadata.create_all(bind=engine)

        uploader.upload()
    elif command == "--server":
        uvicorn.run(
            "stud_api.api.application:app",
            host="127.0.0.1",
            port=5000,
            reload=True,
            workers=4,
        )
    else:
        exit("Choose between upload and server...")
