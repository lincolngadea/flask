## CHANGELOGS

### PREPARAÇÃO DO AMBIENTE

- Criação do ambiente Virtual: _"python -m env ./env"_
- Ativação do ambiente Virtual: _"source ./env/bin/activate"_
- Instalação do Flask: _"pip install flask"_
- Criação do requiriments.txt: _"pip freeze > requiriments.txt"_

### IMPLEMENTAÇÕES INICIAIS

- Criação da primeira rota e execução do servidor para teste
- Comandos no terminal para subir o servidor:
  - _set FLASK_APP = app.py_
  - _flask run_

### CRIAÇÃO DE TEMPLATES

- Criação e execução do primeiro template
- Criação de templates dinânmigos como query params e jimja

### Renderização de formulários

- Instalação da dependencia Flask-WTF:
  - _pip install flask-wtf_
- Criação de classe de formulários
- Renderização do formulário
- Tratamento dos dados recebidos no formulário via template