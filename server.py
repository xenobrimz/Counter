from flask import Flask, render_template, request, session, redirect
app = Flask(__name__)
app.secret_key = 'fsgsdgshjjgj'

@app.route('/', methods=['GET', 'POST'])
def incrimate_counter():
    if 'count' in session:
     session['count'] += 1
     return render_template('index.html', count = session['count'])
    else:
        session['count'] = 0
        return render_template('index.html', count = session['count'])
 
@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/')	
   
if __name__=="__main__":   
    app.run(debug=True)
