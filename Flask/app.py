from flask import Flask,request,render_template,make_response,session

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



### 쿠키
# 쿠키생성
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('쿠키 설정 완료')
    resp.set_cookie('my_cookie', 'value123')  # 쿠키 설정
    return resp


# 쿠키 읽기
@app.route('/get_cookie')
def get_cookie():
    cookie_value = request.cookies.get('my_cookie')  # 쿠키 값 가져오기
    return f'쿠키 값: {cookie_value}'





app.secret_key = 'testkey'

# 세션 생성
@app.route('/set_session')
def set_session():
    session['user_id'] = 1  # 세션에 사용자 ID 설정
    return '세션 설정 완료'


# 세션 읽기
@app.route('/get_session')
def get_session():
    user_id = session.get('user_id')  # 세션 값 가져오기
    return f'세션 값: {user_id}'


# 세션 제거
@app.route('/clear_session')
def clear_session():
    session.pop('user_id', None)  # 세션 값 삭제
    return '세션 제거 완료'

if __name__ == '__main__':
    app.run()  # Flask 앱 실행