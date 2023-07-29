from flask import Flask, request, jsonify


def create_app():
    
 app = Flask(__name__)

 @app.route('/process', methods=['POST'])
 def process():
     try:
         data = request.get_json()
         text = data['string']
         if not isinstance(text, int) and not text.isdigit():
             switched_text = text.swapcase()
             return jsonify({'string': switched_text}), 200
         else:
             return jsonify({'error': 'Please use letters and words'}), 400
     except Exception as e:
         return jsonify({'error': str(e)}), 500

 if __name__ == '__main__':
     app.run()
 return app    