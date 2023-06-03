#language: pt

Funcionalidade: Automatizar a adição de um item em uma lista de tarefas

Cenário: Adicionar um item à lista de tarefas e marcá-lo como concluído
    Dado que estou na página inicial do aplicativo de lista de tarefas
    Quando eu adiciono um novo item com o texto "Essa é minha primeira lista"
    E eu marco o primeiro item como concluído
    Então o primeiro item na lista deve estar marcado como concluído