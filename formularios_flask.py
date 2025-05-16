from flask import Flask, request, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, EqualTo, Email

# Criando a aplicação Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123'

class RegisterForm(FlaskForm):
    first_name= StringField('Primeiro Nome', validators=[DataRequired()])
    last_name= StringField('Sobrenome')
    email= StringField('Email', validators=[Email(message='E-mail inválido!')])
    password= PasswordField('Senha', validators=[InputRequired(), EqualTo('confirm', message='As senhas não conferem!')])
    confirm= PasswordField('Confirme a senha')
    submit= SubmitField('CADASTRAR')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        return redirect('/template')
    
    return render_template('register.html', form=form)


@app.route('/template')
def template():
    return render_template('index.html', name='Flask Developer') 

# Executando o servidor
if __name__ == '__main__':
    app.run(debug=True, port=5152)