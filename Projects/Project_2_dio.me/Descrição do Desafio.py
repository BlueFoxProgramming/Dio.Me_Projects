import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Carregar a imagem (substitua pelo caminho correto da imagem)
image_path = "photo-1660616246653-e2c57d1077b9.avif"  # Caminho para a imagem
image = Image.open(image_path)
image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

# Converter para níveis de cinza
image_gray = cv2.cvtColor(image_cv, cv2.COLOR_BGR2GRAY)

# Binarizar a imagem (threshold = 127)
_, image_binary = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)

# Exibir as imagens
plt.figure(figsize=(15, 5))

# Imagem original
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image_cv, cv2.COLOR_BGR2RGB))
plt.title("Imagem Colorida")
plt.axis("off")

# Imagem em níveis de cinza
plt.subplot(1, 3, 2)
plt.imshow(image_gray, cmap="gray")
plt.title("Imagem em Níveis de Cinza")
plt.axis("off")

# Imagem binarizada
plt.subplot(1, 3, 3)
plt.imshow(image_binary, cmap="gray")
plt.title("Imagem Binarizada")
plt.axis("off")

plt.tight_layout()
plt.show()