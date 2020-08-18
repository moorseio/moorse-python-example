<p align="center">
    <strong><font size="+2">Usando Whatsapp API com Python</font></strong>
    <br/>
    <strong><font size="+1" align="center">
      <a href="https://moorse.io/">Nosso Site</a>
      <span> · </span>
      <a href="https://moorse.readme.io/">Readme IO</a>
    </font></strong>
</p>

Este é um exemplo simples da utilização da API do [Moorse](https://github.com/moorseio) para envio de mensgagens utilizando python.


## Instalação
1. Clone o repositorio:
```bash
$ git clone https://github.com/moorseio/moorse-python-example.git
```
2. Instale as dependências:

```bash
$ cd moorse-python-example
$ pip install -r requirements.txt 
```
OBS:(Se possível utilze um ambiente virtal env)

3. Abra `const.py` e adicione suas informações configurações.
E configure as variáveis abaixo com suas informações.

```python
YOUR_TRIAL_NUMBER = 551199999999
DESTINATION_NUMBER = 551199999999
USER = 'moorseexample@moorse.com'
PASSWORD= '123456'
```

YOUR_TRIAL_NUMBER numero de sua integração.
DESTINATION_NUMBER numero informado na hora de cadastro na ferramenta.
USER email utilizado no cadastro 
PASSWORD senha utilizada no cadastro

Se houver criado um novo grupo na ferramenta, configurar o GROUPID.

```python
GROUPID = 'Grupo id que é disponibilizado dentro da ferramenta'
```

4. Execute o examplo:
```bash
python main.py
```
5. Ao executar o comando anterior, você deve receber as mensagens tanto no grupo cadastrado quanto no número informado.

### :mag: Veja também

Além do Python, nós temos exemplos nas mais variadas linguagens utilizadas no momento. Veja abaixo todas as opções que temos disponíveis:

- [Javascript](https://github.com/moorseio/moorse-node-example)
- [Typescript](https://github.com/moorseio/moorse-typescript-example)

<a id="structure"></a>
