from fastapi import FastAPI
from fastapi import APIRouter

app = FastAPI(
    title="Learning demo", description="Learning fastapi", version="0.0.1", debug=False
)


@app.get("/", tags=["示例"])
@app.get("/index")
@app.get("/app/hello", tags=["示例"])
def app_hello():
    return "Hello world"


# 动态路由
@app.get("/login/{userid}")
async def login(userid: str):
    return {"hello": "dynamic"}


# 静态路由
@app.get("/login/userid")
async def login():
    return {"hello": "static"}


router_user = APIRouter(prefix="/user", tags=["用户"])
router_pay = APIRouter(prefix="/pay", tags=["支付"])


@router_user.get("/login")
def user_login():
    return {"hello": "user"}


@router_pay.get("/order")
def pay_order():
    return {"hello": "pay"}


app.include_router(router_user)
app.include_router(router_pay)
