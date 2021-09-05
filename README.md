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
Usuario: djangoadmin

Senha: admin

URL: http://localhost:8000/admin/

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

header: content-type/application/json

body:
```sh
{
    "name": "Exemplo", <string>   
    "email": "exemplo@exemplo", <string>    
    "department": "Teste" <string>   
}
```

Atualizar Funcionario:

Metodo: PUT
```sh
http://localhost:8000/employee/{id}/
```
header: content-type/application/json

body:
```sh
{
    "name": "Exemplo", <string>
    "email": "exemplo@exemplo", <string>
    "department": "Teste" <string>
}
```
Deletar funcionario:

Metodo: DELETE
```sh
http://localhost:8000/employee/{id}/
```
