from flask import Flask, render_template

app = Flask('Dashboard', template_folder='scr/front')


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)