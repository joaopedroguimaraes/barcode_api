# Conversor Código de Barras para Linha Digitável

Construído no intuito de auxiliar automações jurídicas na identificação e leitura de documentos que contivessem
códigos de barras, obtendo deles a linha digitável, este projeto pode ser executado embarcado a um projeto ou executado
como uma API, já com suporte para tal.

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