# Baixar PDF Jurisprudêcia

Versão python : 3.10.2

Passos para executar o robô

1 - pip install -r requirements.txt
2 -  url para download do chromeDriver => https://chromedriver.chromium.org/downloads
    2.1 - efetuar download referente a versão do seu navegador chrome
    2.2 - extrair a pasta download
    2.3 - abrir a pasta e copiar o chromedriver.exe e colocar na pasta "web-driver" do projeto
3 - colocar pdf's para raspagem de hiperlink na pasta "documents",o nome dos pdf's não pode conter espaço 
4 - executar arquivo main.py  

OBS:
   no arquivo config.py contém variáveis de execução
     appDir - diretorio root de onde a aplicação de encontrada
     pathChromeDriver - diretorio do chromedriver
     dirDownloads - path da pasta downloads do usuario
     filtroUrls - string que filtra as url raspadas do pdf 
     esperar_range - Range de segundos randômicos que o serviço aguarda para executar a próxima request

