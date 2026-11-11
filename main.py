from fastapi import FastAPI,Request,Response

app=FastAPI()
@app.get("/")
def home(req:Request):
    username=req.cookies.get("username")
    
    expiry=req.cookies.get("expiry")
    httponly=req.cookies.get("httponly")
    samesite=req.cookies.get("samesite")

    print(f"""
        username : {username},
    
        expiry : {expiry},
        httponly : {httponly},
        samesites : {samesite}

    """)
    return {"username": username
        }
@app.get("/set_preference")
def set_preference(res:Response):
    res.set_cookie(
        key="username",
        value="Rudra",
        max_age=60 * 60 * 24,
        httponly=True,
        samesite="lax")
    return {"message": "Cookie created"}
    