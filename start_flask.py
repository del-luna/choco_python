from flask_deep import app

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'
# 127.0.0.1(localhost)
app.run(host='0.0.0.0', port=5002, debug=False)