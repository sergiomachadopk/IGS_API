# IGS_API

## Dependencias

REST FRAMEWORK:

```sh
pip install djangorestframework
```
```sh
pip install markdown
```

Run server:
python manage.py runserver

Painel Admin:
usuario: djangoadmin
senha:admin
url: http://localhost:8000/admin/

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
Metodo: PUT
URL: http://localhost:8000/employee/{id}/
header: content-type/application/json
body: 
{
    "name": "Exemplo", <string>
    "email": "exemplo@exemplo", <string>
    "department": "Teste" <string>
}

Deletar funcionarios
Metodo: DELETE
URL: http://localhost:8000/employee/{id}/
