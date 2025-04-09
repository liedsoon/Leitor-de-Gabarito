import cv2
import numpy as np


def reiniciar_video(caminho):
    video = cv2.VideoCapture(caminho)
    return video


def extrairMaiorContorno(frame):
    wcEscalaCinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    wcBinarizacao = cv2.adaptiveThreshold(wcEscalaCinza, 255,
    cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 12)
    kernel = np.ones((2, 2), np.uint8)
    wcDilatacao = cv2.dilate(wcBinarizacao, kernel)
    contornos, hi = cv2.findContours(wcDilatacao, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    maiorContorno = max(contornos, key=cv2.contourArea)
    x, y, w, h = cv2.boundingRect(maiorContorno)
    box = [x, y, w, h]
    recorteGabarito = frame[y: y + h, x: x + w]
    recorteGabarito = cv2.resize(recorteGabarito, (400, 500))

    return recorteGabarito, box


campos = [(2, 2, 96, 96), (102, 2, 96, 96), (202, 2, 96, 96), (302, 2, 96, 96),
          (2, 102, 96, 96), (102, 102, 96, 96), (202, 102, 96, 96), (302, 102, 96, 96),
          (2, 202, 96, 96), (102, 202, 96, 96), (202, 202, 96, 96), (302, 202, 96, 96),
          (2, 302, 96, 96), (102, 302, 96, 96), (202, 302, 96, 96), (302, 302, 96, 96),
          (2, 402, 96, 96), (102, 402, 96, 96), (202, 402, 96, 96), (302, 402, 96, 96)]

alternativas = ['1-A', '1-B', '1-C', '1-D',
        '2-A', '2-B', '2-C', '2-D',
        '3-A', '3-B', '3-C', '3-D',
        '4-A', '4-B', '4-C', '4-D',
        '5-A', '5-B', '5-C', '5-D']


respostasCorretas = ["1-A", "2-D", "3-B", "4-C", "5-A"]

#WebCam Nativa 0 WebCam Externa 1
#video = cv2.VideoCapture(1)

#video de teste
video_path = 'testeCam.mp4'
video = reiniciar_video(video_path)

if video.isOpened():

    validacao, frame = video.read()

    while True:

        validacao, frame = video.read()

        if not validacao:
            video = reiniciar_video(video_path)
            continue

        frame = cv2.resize(frame, (400, 500))
        gabarito, box = extrairMaiorContorno(frame)

        gbEscalaCinza = cv2.cvtColor(gabarito, cv2.COLOR_BGR2GRAY)
        #80 WebCam1 ou 100 Video
        ret, frameBinarizacao = cv2.threshold(gbEscalaCinza, 100, 255, cv2.THRESH_BINARY_INV)
        cv2.rectangle(frame, (box[0], box[1]), (box[0] + box[2], box[1] + box[3]), (255, 0, 0), 3)

        respostas = []
        respostas_indices = []

        for id, vg in enumerate(campos):
            x = int(vg[0])
            y = int(vg[1])
            w = int(vg[2])
            h = int(vg[3])

            cv2.rectangle(gabarito, (x, y), (x + w, y + h),(255, 0, 0), 2)
            cv2.rectangle(frameBinarizacao, (x, y), (x + w, y + h), (255, 255, 255), 2)

            campo = frameBinarizacao[y:y + h, x:x + w]
            height, width = campo.shape
            tamanho = height * width
            pixelBranco = cv2.countNonZero(campo)
            percentual = round((pixelBranco / tamanho) * 100, 2)
            if percentual >= 10:
                respostas.append(alternativas[id])
                respostas_indices.append(id)

        erros = 0
        acertos = 0

        if len(respostas) == len(respostasCorretas):
            for num, resposta in enumerate(respostas):
                if resposta == respostasCorretas[num]:
                    acertos += 1
                    idx = respostas_indices[num]
                    x, y, w, h = campos[idx]
                    cv2.rectangle(gabarito, (x, y), (x + w, y + h), (0, 255, 0), 2)
                else:
                    erros += 1
                    idx = respostas_indices[num]
                    x, y, w, h = campos[idx]
                    cv2.rectangle(gabarito, (x, y), (x + w, y + h), (0, 0, 255), 2)

            pontuacao = acertos * 2

            cv2.rectangle(frame, (0, 435), (400, 500), (232, 190, 150), - 1)
            cv2.putText(frame, f'Acertos: {acertos} | Nota: {pontuacao}', (30, 480),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 0), 2)

        cv2.imshow('WebCam', frame)
        cv2.imshow('Gabarito', gabarito)
        cv2.imshow('Binarização', frameBinarizacao)
        key = cv2.waitKey(15)
        if key == 27:
            break



video.release()
cv2.destroyAllWindows()

