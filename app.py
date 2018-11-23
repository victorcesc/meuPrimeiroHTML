from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)

SECRET_KEY= "string aleatoria" #protecao contra alguns ataques
app.secret_key = SECRET_KEY

engine = create_engine("sqlite:///lab05-flask.sqlite")
Session = sessionmaker(bind=engine)
session = Session()
Base = automap_base()
Base.prepare(engine, reflect=True)

Pessoa = Base.classes.Pessoa
Telefones = Base.classes.Telefones

# https://github.com/std29006/oo-java-e-python


@app.route('/listar')
def listar_pessoas():
    id = str(request.args.get('id'))
    sessionSQL = Session()

    if id == 'None':
        pessoas = sessionSQL.query(Pessoa).all()
        sessionSQL.close()
        return render_template('listar.html',lista_pessoas = pessoas)
    else:
        pessoa = sessionSQL.query(Pessoa).filter(Pessoa.idPessoa == id).first()
        sessionSQL.delete(pessoa)
        sessionSQL.commit()
        sessionSQL.close()
        return redirect(url_for('listar_pessoas'))


@app.route('/inserir',methods=['GET','POST'])
def inserir():
    if request.method == 'GET':
        return render_template('inserir.html')
    else:
        sessionSQL = Session()
        nome = request.form['nome']

        pessoa = Pessoa()
        pessoa.nome = nome

        sessionSQL.add(pessoa)
        sessionSQL.commit()
        sessionSQL.close()
        return redirect(url_for('listar_pessoas'))

@app.route('/index')
@app.route('/')
def hello_world():
    return render_template('index.html',titulo="Inicio")

#@app.route('/listar')
#def listar():
    #return render_template('listar.html',titulo="Listar")


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
