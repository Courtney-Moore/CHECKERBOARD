from flask import Flask, render_template
app = Flask(__name__)

# This route is to display an eight by eight board.
@app.route('/')
def eight_by_eight():
     return render_template('eighties.html')
 
@app.route('/4')
def four_by_eight():
    return render_template('four.html')

@app.route('/<int:x>/<int:y>')
def user_choose(x,y):
    return render_template('userchoose.html', x = x, y = y)



if __name__=="__main__":
    app.run(debug=True)