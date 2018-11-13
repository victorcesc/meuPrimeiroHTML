from flask import Flask, render_template
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
    sessionSQL= Session()
    pessoas = sessionSQL.query(Pessoa).all()
    sessionSQL.close()

    return render_template('listar.html',lista_pessoas = pessoas)


@app.route('/index')
@app.route('/')
def hello_world():
    return render_template('index.html',titulo="Inicio")

#@app.route('/listar')
#def listar():
    #return render_template('listar.html',titulo="Listar")


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
