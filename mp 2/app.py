from flask import Flask,render_template,redirect,flash,session,url_for
app=Flask(__name__)
app.secret_key="abc123"
@app.route('/')
def home():
    return render_template('home.html')
if __name__=='__main__':
    app.run(debug=True,port=5002)