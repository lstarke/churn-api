# Deploy de um modelo de Machine Learning

Neste projeto utilizei o modelo vencedor treinado [neste projeto](https://github.com/lstarke/churn_prediction) e fiz o deploy do modelo criando uma API Rest em [Flask](https://flask.palletsprojects.com/en/3.0.x/).

Etapas que são executadas na API para fazer as predições:

### 1. Transformação das features:

Optei por transformar os valores das features na própria API, para isso tive que treinar um "transformer" novamente somente com as features selecionadas pelo pipeline na fase de treinamento.
Assim, o usuário utiliza os valores nativos do dataset utilizado e a API cuida de entregar as features transformadas para o modelo.

### 2. Recuperação das features transformadas:

O "transformer" retorna uma quantidade maior de features pois foi treinado com o dataset completo. Precisamos utilizar somente a features selecionadas pelo pipeline.

### 3. Predição utilizando o modelo importado

Nesta etapa o modelo é simplesmente carregado e chamado o método ```predict()```.

# Teste da API com Postman

Podemos ver abaixo um teste realizado com a API e logo abaixo o resultado, neste caso o modelo classificou o cliente como sendo um possível candidato a canelamento de sua assinatura (Churn = True). 

![](https://i.imgur.com/OiwfU6N.png)
