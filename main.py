import os
from pathlib import Path
from configparser import ConfigParser
from src.logs import send_message_info, send_message_error
from src.search_content import ServerInfo


def main():
    send_message_info('Iniciando busca de conteúdo...')

    send_message_info('Lendo configurações...')
    if not Path('config.cfg').exists():
        send_message_error('Arquivo config.cfg não encontrado')

    config = ConfigParser()
    config.read('config.cfg')

    base_directory = config.get('path', 'base_directory')
    if not base_directory:
        send_message_error('Diretório inválido')
        return

    output_excel = config.get('path', 'output_excel')
    if not output_excel:
        send_message_error('Outputu para o resultado inválido')
        return

    send_message_info('Configurações lidas com sucesso')      

    # Parâmetros do config.cfg
    params = {
        'base_directory': base_directory,
        'output_excel': output_excel
    }

    send_message_info('Iterando sobre os conteúdos...')
    ServerInfo.parameters(params=params)
    ServerInfo.run()
    send_message_info('Busca de conteúdo concluída')



if __name__ == '__main__':
    main()
