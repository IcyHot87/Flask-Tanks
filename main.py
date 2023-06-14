from flask import Flask, render_template, request, make_response, flash, redirect

app = Flask(__name__)


@app.route("/")
def index():
    strng = request.cookies.get('strng')
    if strng is None:
        user = "Новобранец"
    else:
        user = strng
    resp = make_response(render_template('index.html', name=user))
    return resp


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/ending")
def ending():
    return render_template('ending.html', title="Ending")


@app.route("/autors")
def autors():
    return render_template('autors.html', title='Autors')


@app.route('/forma', methods=["POST", "GET"])
def forma():
    if request.method == 'POST' or request.args.get('strng'):
        strng = request.form[
            'strng'] if request.method == 'POST' else request.args.get('strng')
        user = strng
        if request.cookies.get('strng') is None:
            resp = make_response(render_template('forma.html', name=user))
            resp.set_cookie('strng', strng)
            #flash('Я тебя запомнил, брат')
            return resp
        else:
            resp = make_response(render_template('forma.html', name=user))
            resp.set_cookie('strng', strng)
            return resp
    else:
        strng = request.cookies.get('strng')
        if strng is None:
            user = "Новобранец"
        else:
            user = strng
        resp = make_response(render_template('forma.html', name=user))
        resp.set_cookie('strng', strng)
        return resp


@app.route("/T3485")
def T3485():
    return render_template('T3485.html', title='Т-34-85')

@app.route("/КВ2")
def КВ2():
    return render_template('КВ2.html', title='КВ-2')

@app.route("/ИС7")
def ИС7():
    return render_template('ИС7.html', title='ИС-7')

@app.route("/ИСУ152")
def ИСУ152():
    return render_template('ИСУ152.html', title='ИСУ-152')

@app.errorhandler(404)
def page_not(error):
    return render_template('404.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81, debug=True)
