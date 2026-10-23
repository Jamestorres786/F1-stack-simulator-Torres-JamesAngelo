from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'demo123key'

@app.route('/')
def index():
    if 'stack' not in session:
        session['stack'] = []
    return render_template('index.html', stack=session['stack'], count=len(session['stack']))

@app.route('/stack', methods=['POST'])
def stack_action():
    action = request.form.get('action')
    value = request.form.get('value', '').strip()
    if 'stack' not in session:
        session['stack'] = []
    stack = session['stack']
    if action == 'push' and value:
        stack.append(value)
    elif action == 'pop' and stack:
        stack.pop()
    elif action == 'clear':
        stack = []
    session['stack'] = stack
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
