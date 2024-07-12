
# SEARCH CONTENT SERVER

Script criado para extrair os serviços existente no ArcGIS Server. A busca pode ser alterada facilmente para buscar outros tipos de conteú dentro do server, não só os do exemplo do código, apenas deve conter o arquivo JSON na pasta.

## Estrutura necessária para o código:

```path
search_content_portal/
│
├── logs/         
│   └── arquivo.txt   
│
├── src/    
│   ├── list.py
│   ├── logs.py
│   └── search_content.py
│        
├── .gitignore
├── config-example.cfg
├── main.py
└── README.md
```

## Arquivo de configuração:

No arquivo config-example.cfg contém o necessário para que o código possa ser executado, tendo isso, altere o nome desse arquivo para "config.cfg" e preencha as configurações como indicado.

```
[path]
base_directory = CAMINHO ONDE FICAM SEUS SERVICOS PUBLICADOS NO ARCGIS SERVER
output_excel = logs\dados_extraidos.xlsx

```

## Alteração do tipo buscado:
Para alterar o tipo de contúdo buscado pelo script dentro do seu server, basta alterar o tipo no trecho que está no arquivo **lists.py**.

Lemabrando que você pode fazer uma lista com todos os tipos, sem a necessidade de criar listas por tipo de item, mas isso é opcional.

Segue exemplo da alteração:

```py
services_list = [
    {
        "name": "PASTA_a/Servico_Teste_1",
        "type": "FeatureServer" <--- Alterar o tipo aqui 
    },
```


## Execução do código:

A execução do código é realizada através do arquivo **main.py**. 

No *cmd*, basta acessar a pasta do projeto e executar o comando exibido abaixo e o script será executado.

Comando:

```cmd
python main.py
```

## Logs 

A cada execução será criado um arquivo de log dentro da pasta *logs*, o que é util para o acompanhmento do processo e também na correção de bug's.