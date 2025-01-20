from flask import Flask, request, jsonify

app = Flask(__name__)

# 기본 API 루트
@app.route('/')
def index():
    return "Welcome to REST API!"


@app.route('/api/resource', methods=['POST'])
def create_resource():
    data = request.json  # 클라이언트에서 JSON 형식으로 전달된 데이터
    return jsonify(data), 201  # 201 Created 상태 코드와 함께 응답

@app.route('/api/resource/<int:id>', methods=['GET'])
def get_resource(id):
    # 데이터 조회 로직 (가정)
    data = {'id': id, 'name': 'Sample Resource'}
    return jsonify(data)

@app.route('/api/resource/<int:id>', methods=['PUT'])
def update_resource(id):
    data = request.json  # 클라이언트에서 JSON 형식으로 전달된 데이터
    # 데이터 업데이트 로직 (가정)
    return jsonify({'id': id, 'updated': data}), 200  # 200 OK 상태 코드와 함께 응답


@app.route('/api/resource/<int:id>', methods=['DELETE'])
def delete_resource(id):
    # 데이터 삭제 로직 (가정)
    return '', 204  # 204 No Content 상태 코드 반환

if __name__ == '__main__':
    app.run(debug=True)
