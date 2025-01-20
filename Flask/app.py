from flask import Flask,request,render_template

# Flask 객체 생성
app = Flask(__name__)  

# 기본 라우트 설정
@app.route('/')  
def home():
    return 'Hello, Flask!'  



# 쿼리파라미터
@app.route('/search')
def search():
    keyword = request.args.get('keyword')  # 쿼리 파라미터 처리
    return f'검색: {keyword}'

# 변수파라미터
@app.route('/user/<username>')
def user(username):
    return f'Welcome, {username}!'


# 복합 변수 파라미터
@app.route('/post/<int:post_id>/<string:comment>')
def post(post_id, comment):
    return f'Post ID: {post_id}, Comment: {comment}'

# 데이터 처리
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']  # 폼 데이터 처리
    return f'Hello, {name}!'


# 템플릿 사용
@app.route('/test')
def test():
    return render_template('test.html')  # 템플릿





if __name__ == '__main__':
    app.run()  # Flask 앱 실행