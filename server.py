from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    with open('index.html', 'r') as file:
        return file.read()

@app.route('/run-script-GOOD', methods=['GET'])
def run_script_good():
    # 이곳에서 원하는 Python 연산을 수행합니다.
    result = 'aCVZVVk7YvE'
    return result

@app.route('/run-script-BAD', methods=['GET'])
def run_script_bad():
    # 이곳에서 원하는 Python 연산을 수행합니다.
    result = 'hZe5K1DN4ec'
    return result
if __name__ == '__main__':
    app.run()