from fastapi import FastAPI

app = FastAPI()


@app.get ("/")
def home():
    return {"message": "환영"}



@app.get("/users/{name}")
def get_user(name):
    return {"message": f"{name}님, 안녕하세요!"}


@app.get("/members/{member_id}")
def get_member(member_id: int):
    return {
        "member_id": member_id,
        "message": f"{member_id}번 회원을 조회했습니다."
    }

# 연습문제
#
# {
# "product": "사과",
# "message": "사과 상품을 조회했습니다."
# }

@app.get("/products/{apple}")
def get_product(apple: str):
    return {
        "product": apple,
        "message": f"{apple} 상품을 조회했습니다."
    } 

# ------------------------------------------------------

@app.get("/boards/{board_name}/posts/{post_id}")
def get_post(board_name: str, post_id: int):
    return {
        "board": board_name,
        "post_id": post_id
    }

# 연습문제2
#
# {
# "number": 5,
# "double": 10
# }

@app.get("/numbers/{number}")
def get_number(number: int):
    double = number * 2
    return {
        "number": number,
        "double": double
    }
