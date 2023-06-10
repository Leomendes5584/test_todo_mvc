# Automação de Lista de Tarefas

## Projeto
Este projeto consiste em uma automação de teste construído em Python utilizando o Behave e o Selenium para interagir com um aplicativo de lista de tarefas web. 

## Pré-requisitos
### Certifique-se de ter as seguintes dependências instaladas:
Python 3.x <br/>
Behave <br/>
Selenium <br/>

## Instalação
pip install behave selenium <br/>

## Utilização
Execute o arquivo de teste: behave <br/>
Isso executará todos os cenários de teste definidos no arquivo todo.feature <br/>

## Cenários de Teste
Adicionar um item à lista de tarefas e marcá-lo como concluído <br/>

Este cenário automatiza a ação de adicionar itens na lista de tarefas e marcar-los como concluído. <br/>

<b>Dado</b> que estou na página inicial do aplicativo de lista de tarefas <br/>

<b>Quando</b> eu adiciono as tarefas de segunda, terça e quarta <br/>

<b>E</b> eu marco o primeiro item como concluído <br/>

<b>Então</b> o primeiro item na lista deve estar marcado como concluído
