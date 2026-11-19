from PIL import Image

img = Image.open("patterned_paving_02_diff_4k.jpg")

imgResized = img.resize((700, 500))

imgResized.show()
