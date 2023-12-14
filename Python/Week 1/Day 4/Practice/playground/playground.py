from flask import Flask , render_template
app = Flask(__name__)
@app.route('/play/<int:x>/<string:color>')
def playing(x ,color ):
    
    return render_template('play_ground.html' , x=x  , color=color)




if __name__=="__main__":
    app.run(debug=True)