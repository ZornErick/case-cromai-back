# Calculadora
Calculadora capaz de calcular a relação entre os lados de um triângulo retângulo.

## 🚀 Começando
### 📋 Pré-requisitos
* **Python**
* **Docker**

### ⚙️ Executando via Docker
```
docker build -t case-cromai-back .

docker run -d -p 5000:5000 case-cromai-back
```

### ⚙️ Executando via Python
```
pip install flask

pip install flask-restful

pip install flask-cors

python app.py
```

### Endpoint
```
/calcular

Method: POST
Content-Type: application/json

Body
{
    "hipotenusa": 10,
    "cateto_a": 5
}

```

## 🛠️ Construído com
* [Flask](https://flask.palletsprojects.com/en/2.2.x/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

## 🤝 Obrigado
