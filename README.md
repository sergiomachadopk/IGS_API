# IGS_API

## Dependencias

REST FRAMEWORK:

```sh
pip install djangorestframework
```
```sh
pip install markdown
```

Executando:

python manage.py runserver

## Painel Admin:
usuario: djangoadmin

senha:admin

url: http://localhost:8000/admin/

## API:

Listar Funcionarios:

Metodo: GET
```sh
http://localhost:8000/employee/
```

Cadastrar Funcionario:

Metodo: POST
```sh
http://localhost:8000/employee/
```
Exemplo:

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
