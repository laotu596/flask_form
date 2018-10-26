from flask import Flask
from flask import render_template,request
import configs
#from flask_wtf import Form
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import  Required
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config.from_object(configs)


class NameForm(FlaskForm):
    name = StringField('What is your name?',validators=[Required()])
    submit = SubmitField('Submit')

@app.route('/',methods=['GET','POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html',form=form,name=name)
#    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)
