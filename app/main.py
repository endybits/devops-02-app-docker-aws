import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello_devops():
    return {
        'msg': "Hello, this is an Application Running on AWS",
        'project': "devops-02-app-docker-aws",
        'devops_engineer': "Endy B!"
    }


if __name__ == "__main__":
    uvicorn.run(app=app, host="0.0.0.0", port=80)