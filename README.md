# 🌌 Star Wars API — PowerOfData Case

API desenvolvida em **Python com Django Rest Framework**, consumindo dados da **SWAPI (Star Wars API)** e disponibilizando endpoints para consulta de **personagens, planetas, naves, veículos e Espécie**, com suporte a **filtros dinâmicos**.

O projeto foi construído seguindo boas práticas de desenvolvimento backend e implantado no **Google Cloud Platform (GCP)** utilizando **Cloud Run**, garantindo reprodutibilidade.

---

## 🚀 Tecnologias Utilizadas

- Python 3.10  
- Django  
- Django Rest Framework (DRF)  
- Gunicorn  
- Docker  
- Google Cloud Run  
- Google Cloud Build  
- SWAPI (https://swapi.dev)

---

## 🏗️ Arquitetura da Solução

Cliente
↓
Cloud Run (GCP)
↓
Django + DRF
↓
SWAPI (API externa)


- Aplicação stateless  
- Sem persistência em banco de dados  
- Consumo de dados em tempo real  
- Infraestrutura serverless com escalabilidade automática  

---

## 🌐 API em Produção

Base URL (Cloud Run):

https://api-starwars-555403443962.europe-west1.run.app/api

---

## 📌 Endpoints Disponíveis

### 👤 Personagens

GET /personagens

Filtros disponíveis:
- name
- gender

Exemplo:

/personagens?name=luke&gender=male

---

### 🪐 Planetas

GET /planetas


Filtros disponíveis:
- name
- climate
- terrain

Exemplo:

/planetas?name=tatooine

---

### 🚀 Naves

GET /naves


Filtros disponíveis:
- name
- model
- manufacturer

---

### 🚗 Veículos

GET /veiculos


Filtros disponíveis:
- name
- model
- manufacturer

---

## 🔎 Funcionalidades Implementadas

- Consumo de API externa (SWAPI)
- Filtros via query params
- Serializers customizados (sem uso de models)
- API RESTful
- Dockerização da aplicação
- Deploy no Google Cloud Platform
- Boas práticas de versionamento com Git

---

## 🔐 Variáveis de Ambiente

As configurações sensíveis são carregadas via variáveis de ambiente e **não são versionadas no repositório**.

Exemplo:

SECRET_KEY=xxxx
DEBUG=False

---

## 🐳 Executando Localmente com Docker

```bash
docker build -t starwars-api .
docker run -p 8080:8080 starwars-api
```

Acesse:
http://localhost:8080

---

📈 Possíveis Evoluções

Autenticação (JWT ou API Key)

Cache de respostas

Paginação

Testes unitários

Expansão de relações entre recursos

Uso de API Gateway / Apigee

---

👨‍💻 Autor

Antonio Gabriel da Silva
Projeto desenvolvido como case técnico para a PowerOfDatas