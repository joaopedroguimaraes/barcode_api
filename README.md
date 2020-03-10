# Conversor Código de Barras para Linha Digitável

Construído no intuito de auxiliar automações jurídicas na identificação e leitura de documentos que contivessem
códigos de barras, obtendo deles a linha digitável, este projeto pode ser executado embarcado a um projeto ou executado
como uma API, já com suporte para tal.

### Especificações

O projeto utiliza o **Python 3.8.+**, e as bibliotecas utilizadas estão listadas no arquivo `requirements.txt`, 
podendo ser instaladas da seguinte forma:

`pip install -r requirements.txt`

> Lembrando: é altamente recomendável utilizar um ambiente virtual para o projeto. Para saber mais, consulte 
[venv — Creation of virtual environments](https://docs.python.org/3/library/venv.html).

## #1 Utilizando como API

### Requisição

- **URL**

`/barcode`

- **Método**

`POST`

- **Parâmetro multipart**

`arquivo`, que deve ser PDF ou imagem.

---

### Resposta

- **Sucesso**

```
Code: 200
Content: { 'linhadigitavel': resultado } 
```

- **Erro**

Requisição realizada sem o arquivo.

```
Code: 422
Content: { 'linhadigitavel': 'Envie o arquivo junto à requisição HTTP POST } 
```

## #2 Utilizando os métodos

> Ainda é necessário descrever aqui.

## Referências utilizadas

- [An OpenCV barcode and QR code scanner with ZBar](https://www.pyimagesearch.com/2018/05/21/an-opencv-barcode-and-qr-code-scanner-with-zbar/)
- [Python | Reading contents of PDF using OCR (Optical Character Recognition)](https://www.geeksforgeeks.org/python-reading-contents-of-pdf-using-ocr-optical-character-recognition/)