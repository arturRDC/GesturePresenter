# GesturePresenter

GesturePresenter is a Python project that controls presentation slides using finger gestures.

## Features

- Move to the next slide by connecting your thumb with your middle finger (simulates pressing the right arrow key).
- Move to the previous slide by connecting your thumb with your index finger (simulates pressing the left arrow key).
- Optional flag to show camera output for visual feedback.
- Optional flag to invert controls, which might be preferable for left-handed users.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyAutoGUI

## Installation

1. Clone this repository:

   ```sh
   git clone https://github.com/arturRDC/GesturePresenter.git
   cd GesturePresenter
   ```

2. Install the required packages:

   ```sh
   pip install mediapipe opencv-python pyautogui
   ```

## Usage

1. Run the script with desired options:

   ```sh
   python app.py [--show-output] [--invert-controls]
   ```

   - Use `--show-output` to display the camera feed with visual indicators.
   - Use `--invert-controls` to swap the functions of index and middle fingers. This might be more comfortable for left-handed users.

2. Switch windows to the slides presentation.

3. Position your hand in front of the camera and use the following gestures:
   - Connect your thumb with your middle finger to move to the next slide (or previous slide if controls are inverted).
   - Connect your thumb with your index finger to move to the previous slide (or next slide if controls are inverted).

## Command-line Options

- `--show-output`: Shows the camera output with visual indicators for debugging or learning the gestures.
- `--invert-controls`: Inverts the controls, making the index finger control the right arrow and the middle finger control the left arrow. This might be more intuitive for left-handed users.

Examples:

```sh
python app.py --show-output  # Run with camera output
python app.py --invert-controls  # Run with inverted controls
python app.py --show-output --invert-controls  # Run with both options
```

## Português

# GesturePresenter

GesturePresenter é um projeto em Python que controla slides de apresentação usando gestos com os dedos.

## Funcionalidades

- Mover para o próximo slide conectando o polegar com o dedo médio (simula pressionar a tecla de seta para a direita).
- Mover para o slide anterior conectando o polegar com o dedo indicador (simula pressionar a tecla de seta para a esquerda).
- Flag opcional para mostrar a saída da câmera para feedback visual.
- Flag opcional para inverter os controles, o que pode ser preferível para usuários canhotos.

## Requisitos

- Python 3.x
- MediaPipe
- OpenCV
- PyAutoGUI

## Instalação

1. Clone este repositório:

   ```sh
   git clone https://github.com/arturRDC/GesturePresenter.git
   cd GesturePresenter
   ```

2. Instale os pacotes necessários:

   ```sh
   pip install mediapipe opencv-python pyautogui
   ```

## Uso

1. Execute o script com as opções desejadas:

   ```sh
   python app.py [--show-output] [--invert-controls]
   ```

   - Use `--show-output` para exibir o feed da câmera com indicadores visuais.
   - Use `--invert-controls` para trocar as funções dos dedos indicador e médio. Isso pode ser mais confortável para usuários canhotos.

2. Troque a janela para a apresentação de slides.

3. Posicione sua mão em frente à câmera e use os seguintes gestos:
   - Conecte o polegar com o dedo médio para mover para o próximo slide (ou slide anterior se os controles estiverem invertidos).
   - Conecte o polegar com o dedo indicador para mover para o slide anterior (ou próximo slide se os controles estiverem invertidos).

## Opções de Linha de Comando

- `--show-output`: Mostra a saída da câmera com indicadores visuais para depuração ou aprendizado dos gestos.
- `--invert-controls`: Inverte os controles, fazendo o dedo indicador controlar a seta direita e o dedo médio controlar a seta esquerda. Isso pode ser mais intuitivo para usuários canhotos.

Exemplos:

```sh
python app.py --show-output  # Executar com saída da câmera
python app.py --invert-controls  # Executar com controles invertidos
python app.py --show-output --invert-controls  # Executar com ambas as opções
```
