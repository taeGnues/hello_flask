from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_funct():

        return '<b>'+function()+'</b>'

    return wrapper_funct

def make_emphasis(function):
    def wrapper_funct():

        return '<em>'+function()+'</em>'

    return wrapper_funct


@app.route('/')
@make_bold
@make_emphasis
def hello_world():
    return '<h1 style="text-align: center"> hello world </h1>' \
           '<p1>para</p1>'


if __name__ == "__main__":  # 현재 사용중인 파일에 application code가 있는지 확인함.
    app.run(debug=True)
