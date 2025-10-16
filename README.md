#  Detecção de Dedos com MediaPipe, OpenCV e Arduino

Este projeto utiliza **MediaPipe** e **OpenCV** para detectar qual dedo (indicador, médio ou anelar) está levantado em tempo real.  
Com base nessa detecção, o programa envia um sinal via **Serial** para o **Arduino** (ou **ESP32**), que acende o LED correspondente ao dedo identificado.

---


https://github.com/user-attachments/assets/76f9f3cb-cf49-4fbb-96e9-234d7585ec61


##  Objetivo

Demonstrar a integração entre **visão computacional (Python)** e **hardware (Arduino/ESP32)** para criar um sistema interativo que reconhece gestos de dedos e controla LEDs fisicamente.

---

##  Tecnologias Utilizadas

-  **Python 3**
-  **OpenCV**
-  **MediaPipe**
-  **PySerial**
-  **Arduino UNO / ESP32**

---





##  Como Funciona

1. O programa captura o vídeo da webcam usando o OpenCV.  
2. O **MediaPipe** detecta 21 pontos de referência da mão.  
3. O código verifica a posição dos dedos:
   - Se o **dedo indicador** estiver levantado → envia `1` pela serial.
   - Se o **dedo médio** estiver levantado → envia `2`.
   - Se o **dedo anelar** estiver levantado → envia `3`.
4. O Arduino (ou ESP32) recebe o comando e acende o LED correspondente.

---

##  Exemplo de Funcionamento

| Gesto Detectado | Dado Enviado | LED Ativado |
|------------------|---------------|--------------|
| Dedo Indicador | `1` | LED 1 |
| Dedo Médio | `2` | LED 2 |
| Dedo Anelar | `3` | LED 3 |



