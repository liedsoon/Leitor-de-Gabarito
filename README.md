# 📷 Leitor de Gabarito com OpenCV

Este projeto utiliza **OpenCV** para capturar frames da webcam ou de um vídeo, identificar o maior contorno (gabarito de respostas), segmentar os campos de alternativas, e validar as respostas marcadas com base em um gabarito pré-definido.

## ✨ Funcionalidades

- Leitura da da webcam ou vídeo.
- Identificação automática do gabarito por contorno
- Segmentação dos campos de respostas
- Cálculo de preenchimento para identificar a alternativa marcada
- Validação de respostas e exibição da pontuação
- Interface visual com realce em:
  - ✅ Verde para respostas corretas
  - ❌ Vermelho para respostas erradas
  - 🔲 Azul para marcações de campo

## 🧠 Como Funciona

1. O script captura frame a frame do vídeo.
2. Detecta o maior contorno presente no frame (suposto gabarito).
3. Segmenta o gabarito em uma matriz 5x4 de campos.
4. Aplica limiarização (binarização) para detectar preenchimento.
5. Compara as respostas detectadas com as respostas corretas.
6. Exibe os resultados na tela com nota e feedback visual.

## 📁 Estrutura dos Campos e Alternativas

Os campos são definidos manualmente com suas posições (x, y, w, h), representando 20 áreas de marcação, que seguem este mapeamento:

```python
1-A, 1-B, 1-C, 1-D
2-A, 2-B, 2-C, 2-D
3-A, 3-B, 3-C, 3-D
4-A, 4-B, 4-C, 4-D
5-A, 5-B, 5-C, 5-D
```

## ✅ Gabarito de Respostas

```python
respostasCorretas = ["1-A", "2-D", "3-B", "4-C", "5-A"]
```

## 🛠️ Requisitos

- Python 3.13
- OpenCV
- NumPy

## ▶️ Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/liedsoon/Leitor-de-Gabarito.git
```

2. Crie e ative um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
./venv/scripts/activate # Windows
```

3. Instale as dependências com:

```bash
pip install -r requirements.txt
```

4. Execute com:

```bash
python Main.py
```

5. Pressione `ESC` para sair da visualização.

## 🖼️ Exibição

São exibidas três janelas:

- **WebCam**: Visualização geral do frame
- **Gabarito**: Recorte com feedback das respostas
- **Binarização**: Visualização em preto e branco do preenchimento

<div align="center">
<img src="https://github.com/user-attachments/assets/cac6ba2d-05fb-45a1-bc96-cae97a335161" width="1000px" />
</div>

