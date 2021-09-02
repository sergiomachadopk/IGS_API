# IGS_API

Dependencias:
pip install djangorestframework
pip install markdown

Listar Funcionarios:
Metodo: GET
URL: http://localhost:8000/employee/

Cadastrar Funcionario:
Metodo: POST
URL: http://localhost:8000/employee/
header: content-type/application/json
body: 
{
    "name": "Exemplo", <string>
    "email": "exemplo@exemplo", <string>
    "department": "Teste" <string>
}

Atualizar Funcionario:
Metodo: POST
URL: http://localhost:8000/employee/{id}/
header: content-type/application/json
body: 
{
    "name": "Exemplo", <string>
    "email": "exemplo@exemplo", <string>
    "department": "Teste" <string>
}

Deletar funcionarios
Metodo: Delete
URL: http://localhost:8000/employee/{id}/
