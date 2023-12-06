import cv2

def condicionalesLetras(dedos, frame):
    font = cv2.FONT_HERSHEY_SIMPLEX

    letras = {
        'A': {'dedos': [1, 1, 0, 0, 0, 0]},
        'E': {'dedos': [0, 0, 0, 0, 0, 0]},
        'I': {'dedos': [0, 0, 1, 0, 0, 0]},
        'O': {'dedos': [1, 0, 1, 0, 0, 0]},
        'U': {'dedos': [0, 0, 1, 0, 0, 1]},
        'B': {'dedos': [0, 0, 1, 1, 1, 1]},
        'D': {'dedos': [0, 0, 0, 0, 0, 1]},
        'K': {'dedos': [1, 1, 0, 0, 1, 1]},
        'L': {'dedos': [1, 1, 0, 0, 0, 1]},
        'W': {'dedos': [0, 1, 0, 1, 1, 1]},
        'N': {'dedos': [0, 1, 0, 0, 1, 1]},
        'Y': {'dedos': [1, 1, 1, 0, 0, 0]},
        'F': {'dedos': [1, 1, 1, 1, 1, 0]},
        'P': {'dedos': [0, 1, 1, 1, 1, 1]},
        'V': {'dedos': [0, 1, 0, 0, 1, 1]}
    }

    for letra, info in letras.items():
        if dedos == info['dedos']:
            mostrar_letra(frame, letra)
            return dedos

    return dedos

def mostrar_letra(frame, letra):
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.rectangle(frame, (0, 0), (100, 100), (255, 255, 255), -1)
    cv2.putText(frame, letra, (20, 80), font, 3, (0, 0, 0), 2, cv2.LINE_AA)
    print(letra)
