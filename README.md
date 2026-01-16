# Hand Tracking Module

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![MediaPipe](https://img.shields.io/badge/MediaPipe-Google-orange)
![OpenCV](https://img.shields.io/badge/OpenCV-Computer_Vision-green)

O objetivo principal deste projeto é realizar a detecção e rastreamento de mãos em tempo real utilizando a webcam. O código foi estruturado em Classes para facilitar a reutilização em outros projetos de Visão Computacional.

> Projeto desenvolvido com o intuito de pôr em prática os conhecimentos das bibliotecas OpenCV* e MediaPipe.

## Arquivos do Projeto

O código principal funciona tanto como um módulo importável quanto como um script executável:

| Arquivo | Descrição |
| :--- | :--- |
| **`hand_detector.py`** | Contém a classe `Detector` que encapsula a lógica do MediaPipe e desenha os pontos de referência na mão. |

## Funcionalidades
- **Detecção em Tempo Real:** Captura e processa vídeo diretamente da webcam.
- **Rastreamento Multi-Mão:** Configurado por padrão para detectar até 2 mãos simultaneamente.
- **Visualização de Landmarks:** Desenha as conexões e articulações da mão na tela.
- **Código Modular:** Estrutura de Classe (`Detector`) pronta para ser importada em outros scripts.

## Tecnologias Utilizadas
- **Linguagem:** Python.
- **Bibliotecas:**
    - MediaPipe.
    - OpenCV.
    - NumPy.

## Como Rodar o Programa

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/caio-alm/mediapipe-hand-wrapper.git](https://github.com/caio-alm/mediapipe-hand-wrapper.git)
   ```
2. **Entre na pasta:**
  ```bash
  cd nome-da-pasta
  ```
3. **Instale o requirements.txt:**
  ```bash
  pip install -r requirements.txt
  ```
4. **Execute o processamento: Navegue até a pasta de projetos e rode o script:**
  ```bash
  cd Agriculture_Projects
  python seu_arquivo.py
  ```
  
