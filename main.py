from typing import Optional
from fastapi import FastAPI
import random  # randomライブラリを追加
from fastapi.responses import HTMLResponse #インポート

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉",
        "中吉",
        "小吉",
        "吉",
        "半吉",
        "末吉",
        "末小吉",
        "凶",
        "小凶",
        "大凶"
    ]

    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <meta charset = "utf-8">
            <title>diary</title>
        </head>
        <body>
            <h1>日記20240618</h1>
            <p>毎日Obsidianでつけている日記の一部を載せておきます。</p>
            <p> 日記 20240618 やったこと ES2枚提出 インターン内定+1 月曜火曜課題 <br> 
            やること ソフでICPC勉強会予定 AtCoderすすめて 研究室探しもそろそろ <br>
            雑多 久々に河川敷を走った, もう夏だなあ 森永ラムネの炭酸味が美味しすぎる, 食べ過ぎちゃうから良くないね～ </p> 
            
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)
