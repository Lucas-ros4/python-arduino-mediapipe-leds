import cv2
from detecter_maos import DetectorMaos

def main():
    cap = cv2.VideoCapture(0)
    detector = DetectorMaos()  #cria uma instancia de detector de mãos

    while True:
        _, frame = cap.read() #frame é a imagem atual do video
        frame = detector.encontrar_maos(frame)

        todos_pontos = []  #lista para armazenas as posicões dos 21 pontos da mão

        #coleta todos os 21 pontos da mão cada um com usa posicao (id, x, y)
        for ponto_id in range(21): #loop de 0 até 20 representando os 21 pontos de referência para poder confirmar que é uma mao
            ponto = detector.encontrar_pontos(frame, ponto_detectado=ponto_id, desenho=False) #para cada ponto chama o medodo encontrar_pontos para ober a posicao deles(false pq não denha o ponto ainda)
            if ponto:#se o ponto voi encontrado ele é adicionado a lista
                todos_pontos.append(ponto[0])  # [id, x, y]

        if len(todos_pontos) == 21: #so entra no if se ele detectar os 21 pontos corretamente
            # ponto 8 e a ponta do dedo indicador
            # ponto 6 e a junta do dedo indicador
            y_dedo_indicador = todos_pontos[8][2]
            y_junta_inferior = todos_pontos[6][2]

            if y_dedo_indicador < y_junta_inferior: #se a ponta do dedo for maior que a base
                cv2.putText(frame, "1", (50, 100), cv2.FONT_HERSHEY_SIMPLEX,#texto, posicao do texto, tamanho da vonte, cor do texto e espessura da fonte
                            3, (0, 255, 0), 5)
                print(f"Posição do dedo indicador: x={todos_pontos[8][1]}, y={y_dedo_indicador}") #exibe as coordenadas do dedo indicador

        cv2.imshow("Deteccao de dedo Indicador", frame) #mostra o video na tela

        if cv2.waitKey(1) & 0xFF == ord('q'): #condição para sair do loop
            break

    cap.release() #termina o uso de webcam
    cv2.destroyAllWindows() #fecha todas as janelas do opencv que foram abertas

if __name__ == "__main__":
    main()
