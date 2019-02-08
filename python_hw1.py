from flask import Flask,render_template,request, redirect, url_for
app = Flask(__name__,template_folder='templates')

@app.route("/")
def hello():
         return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      prnum = request.form['n1']
      return redirect(url_for('prime', p = prnum))
   else:
      prnum = request.args.get('n1')
      return redirect(url_for('prime', p = prnum))



@app.route('/prime/<p>')
def prime(p):
	n = int(p)
  if (n <= 1) :
        final="The number should be greater than 1"
        return redirect(url_for('final',final))
  for i in range(2,n/2):
        if (n%i ==0) :
		final="The number is not prime. "+ i +" times "+ n/i+" is equal to "+ n
		return redirect(url_for('final',final)
  final="The number is prime"
  return redirect(url_for('final',final)

@app.route('/final/<final>')
def final(final):
                return render_template("final.html",final)




if __name__ == "__main__":
        app.debug= True
        app.run(debug = True)
