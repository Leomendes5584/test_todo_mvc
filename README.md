<h1 align="center"> Lista de itens Automatizada  </h1>

Este projeto consiste em uma automação de teste utilizando o Behave e o Selenium para interagir com um aplicativo de lista de tarefas web.

Pré-requisitos
Certifique-se de ter as seguintes dependências instaladas:

Python 3.x
Behave
Selenium
Instalação
Clone este repositório em sua máquina local.
Instale as dependências necessárias:
bash
Copy code
pip install behave selenium
Utilização
Execute o arquivo de teste:
bash
Copy code
behave
Isso executará todos os cenários de teste definidos no arquivo de recursos nome_do_arquivo.feature.

Cenários de Teste
Adicionar um item à lista de tarefas e marcá-lo como concluído
Este cenário automatiza a ação de adicionar um novo item à lista de tarefas e marcar o primeiro item como concluído.

Dado que estou na página inicial do aplicativo de lista de tarefas
Quando eu adiciono as tarefas de segunda, terça e quarta
E eu marco o primeiro item como concluído
Então o primeiro item na lista deve estar marcado como concluído
