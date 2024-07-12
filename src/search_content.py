import os
import json
import pandas as pd
from src.lists import services_list
from src.logs import send_message_info, send_message_error

class ServerInfo:
    base_directory: str = ''
    output_excel: str = ''

    def parameters(self, params: dict = None) -> None:
        """Configurar os parâmetros da aplicação

        :param params: Dicionário contendo os parâmetros
        :return:
        """
        self.base_directory = params['base_directory']
        self.output_excel = params['output_excel']

    def buscar_jsons_e_extrair_info(self):
        """
        Fazer a leitura dos arquivos JSON e extrair as informações relevantes
        
        params: diretorios (list): Lista de diretorios a serem verificados
        """
        dados = []
        diretorios = [os.path.join(self.base_directory, service["name"].replace('/', os.sep) + '.' + service["type"]) for service in services_list]
        for diretorio in diretorios:
            json_filename = os.path.basename(diretorio) + '.json'
            json_path = os.path.join(diretorio, json_filename)
            send_message_info(f"Verificando o caminho: {json_path}")
            if os.path.isfile(json_path):
                send_message_info(f"Encontrado JSON: {json_path}")
                with open(json_path, 'r', encoding='utf-8') as f:
                    try:
                        conteudo = json.load(f)
                        name = conteudo.get('serviceName')
                        min_instancias = conteudo.get('minInstancesPerNode')
                        max_instancias = conteudo.get('maxInstancesPerNode')
                        percontainer_instancias = conteudo.get('instancesPerContainer')
                        max_wait_time = conteudo.get('maxWaitTime')
                        max_idle_time = conteudo.get('maxIdleTime')
                        max_usage_time = conteudo.get('maxUsageTime')
                        keep_alive_interval = conteudo.get('keepAliveInterval')
                        state = conteudo.get('configuredState')

                        
                        if name and min_instancias is not None and state:
                            dados.append({
                                'name': name,
                                'state': state,
                                'min_instancia': min_instancias,
                                'max_instancia': max_instancias,
                                'percontainer_instancia': percontainer_instancias,
                                'max_wait_time': max_wait_time,
                                'max_idle_time': max_idle_time,
                                'max_usage_time': max_usage_time,
                                'keep_alive_interval': keep_alive_interval
                            })
                        else:
                            send_message_error(f"Campos ausentes para o JSON: {json_path}") 
                    except json.JSONDecodeError:
                        send_message_error(f"Erro ao ler o arquivo {json_path}")
            else:
                send_message_error(f"Arquivo não encontrado: {json_path}")
        return dados

    def salvar_em_excel(self, dados):
        """
        Salvar os dados em um arquivo Excel

        :param dados: Dados a serem salvos
        :param caminho_arquivo: Caminho para o arquivo
        """
        try:
            df = pd.DataFrame(dados)
            df.to_excel(self.output_excel, index=False)
            send_message_info(f"Arquivo salvo em: {self.output_excel}")
        except Exception as e:
            send_message_error(f"Erro ao salvar os dados em Excel: {e}")    

    def run(self):
        """
        Executar a aplicação
        """
        
        dados = self.buscar_jsons_e_extrair_info()
        self.salvar_em_excel(dados)


ServerInfo = ServerInfo()