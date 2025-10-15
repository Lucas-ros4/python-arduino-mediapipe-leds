import cv2
import mediapipe as mp


class DetectorMaos:
    def __init__(self, modo=False, max_maos=2, deteccao_confianca=0.5,
                 rastreio_confianca=0.5, cor_pontos=(0, 0, 255), cor_conexoes=(255, 255, 255)):
        """
        modo: True ele detecta e rastreia o tempo TODO, deixa a parada toda travada.
              False, não fica rastreando e detectando o tempo todo, pode perder anguns instantes de marcaçao mas não trava
        max_maos: qtd maxima de maos que podem ser detectadas
        deteccao_confianca: percentualo da taxa de deteccao da mão. se for menor que o limite, a deteccao não ocorre
        astreio_confianca: mesma coisa mas com o rastreio
        cor_pontos: cor dos pontos na tela
        or_conexoes: cor das conexoes
        """
        #inicializando os parametros
        self.modo = modo
        self.max_maos = max_maos
        self.deteccao_confianca = deteccao_confianca
        self.rastreio_confianca = rastreio_confianca
        self.cor_pontos = cor_pontos
        self.cor_conexoes = cor_conexoes

        #inicializando os modulos de deteccao das maos
        self.maos_mp = mp.solutions.hands
        self.maos = self.maos_mp.Hands(
            self.modo,
            self.max_maos,
            1,
            self.deteccao_confianca,
            self.rastreio_confianca
        )

        self.desenho_mp = mp.solutions.drawing_utils #desenho maos

        self.desenho_config_pontos = self.desenho_mp.DrawingSpec(color=self.cor_pontos) #desenhos pontos

        self.desenho_config_conexoes = self.desenho_mp.DrawingSpec(color=self.cor_conexoes) #desenho conexao

    def encontrar_maos(self, imagem, desenho=True):
        """
        imagem: imagem capturada
        desenho: desenha os pontos/conexoes das maos
        """

        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)#converte de bgr para rgb

        self.resultado = self.maos.process(imagem_rgb)

        #verifica se alguma mao foi detectada
        if self.resultado.multi_hand_landmarks: #landmarks são os pontos
            for pontos in self.resultado.multi_hand_landmarks:
                if desenho:
                    self.desenho_mp.draw_landmarks(
                        imagem,  # imagem de captura
                        pontos,  # pontos da mao
                        self.maos_mp.HAND_CONNECTIONS,
                        self.desenho_config_pontos,  #cor dos pontos
                        self.desenho_config_conexoes  #cor da conexao
                    )

        return imagem

    def encontrar_pontos(self, imagem, mao_num=0, desenho=True, cor=(255, 0, 255), raio=7, ponto_detectado=0):
        """
        #funcao para encontrar a posicao dos potnos na mao
        imagem: Imagem capturada.
        mao_num: numero de maos detectadas
        desenho: desenha o ponto encontrado
        cor: cor(bgr)
        raio: raio do circulo
        ponto_detectado: ponto que vai ser detectado
        retorna uma uma lista com os pontos detectados
        """

        lista_pontos = []

       #verifica
        if self.resultado.multi_hand_landmarks:
            mao = self.resultado.multi_hand_landmarks[mao_num]

            for id, ponto in enumerate(mao.landmark):
                if id == ponto_detectado:

                    altura, largura, _ = imagem.shape#largura e altura da imagem

                    centro_x, centro_y = int(ponto.x * largura), int(ponto.y * altura)

                    lista_pontos.append([id, centro_x, centro_y]) #adiciona os pontos a lista

                    if desenho:
                        cv2.circle(
                            imagem,  # imagem da captura
                            (centro_x, centro_y),  # centro do círculo
                            raio,  # raio do círculo
                            cor,  # cor do círculo
                            cv2.FILLED  # espessura
                        )

        return lista_pontos


def main():
    cap = cv2.VideoCapture(0)

    detector = DetectorMaos() #inicializa a classe

    while True:
        _, imagem = cap.read()

        imagem = detector.encontrar_maos(imagem)

        lista_pontos = detector.encontrar_pontos(imagem)

        cv2.imshow('Captura', imagem)

        cv2.waitKey(1)


if __name__ == '__main__':
    main()
