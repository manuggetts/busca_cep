# Buscador de CEP com Python 🤖🔎

<div align="middle">
<img src="https://github.com/manuggetts/busca_cep/assets/141872152/719e71ba-04e5-42fa-a0be-cef94b7f57ac" width="800">
</div>

>Este projeto foi originalmente criado como parte de um processo seletivo, onde o desafio era desenvolver um script de Automação de Processos Robóticos (RPA) usando AutoHotkey.
Depois de concluir o desafio, decidi recriar o projeto usando Python.
>A transição de AutoHotkey para Python também me permitiu explorar diferentes bibliotecas e técnicas, e acredito que o projeto final é mais fácil de usar como resultado.
>Estou compartilhando este projeto na esperança de que ele possa ser útil para outras pessoas que estão aprendendo sobre RPA ou que precisam buscar informações de CEPs de uma forma automatizada.

## Descrição do Projeto 📝
Este projeto utiliza Python para buscar informações de CEPs a partir da API ViaCEP. O script lê uma lista de CEPs de uma planilha Excel, busca as informações de cada CEP usando a API ViaCEP, e então adiciona essas informações de volta à planilha original.
É um exemplo simples de um projeto de Automação de Processos Robóticos (RPA) que pode ser útil para quem precisa buscar informações de vários CEPs de uma vez.

## Como usar 🚀
1. Certifique-se de que você tem Python instalado em seu computador. Este script foi testado com Python 3.8, mas deve funcionar com outras versões também.
2. Instale as bibliotecas necessárias executando o seguinte comando no seu terminal:
```
pip install requests pandas
```
3. Coloque a planilha com os CEPs que você deseja buscar no mesmo diretório do script. A planilha deve ter uma coluna chamada 'CEP' que contém os CEPs. Deixei [esta](https://github.com/manuggetts/busca_cep/files/15097573/ceps.xlsx) planilha de exemplo com 3 CEPS.
4. Execute o script com o seguinte comando no seu terminal:
```
python app.py
```
5. O script irá adicionar as informações de cada CEP à planilha original e salvar a planilha.

## Contribuições 👥
Contribuições são sempre bem-vindas! Sinta-se à vontade para abrir uma [issue](https://github.com/manuggetts/busca_cep/issues) ou enviar um [pull request.](https://github.com/manuggetts/busca_cep/pulls)
