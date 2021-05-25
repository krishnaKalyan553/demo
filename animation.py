import cv2
import matplotlib.pyplot as plt
class Cartoonizer:
	def __init__(self):
		pass
	def render(self, img_rgb):
		img_rgb = cv2.imread(img_rgb)
		numDownSamples = 2
		numBilateralFilters = 50
		img_color = img_rgb
		for _ in range(numDownSamples):
			img_color = cv2.pyrDown(img_color)
		for _ in range(numBilateralFilters):
			img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
		for _ in range(numDownSamples):
			img_color = cv2.pyrUp(img_color)
		img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
		img_blur = cv2.medianBlur(img_gray, 3)

		img_edge = cv2.adaptiveThreshold(img_blur, 255,
										cv2.ADAPTIVE_THRESH_MEAN_C,
										cv2.THRESH_BINARY, 9, 2)
		(x,y,z) = img_color.shape
		img_edge = cv2.resize(img_edge,(y,x))
		img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
		cv2.imwrite("edge.png",img_edge)
		return cv2.bitwise_and(img_color, img_edge)

tmp_canvas = Cartoonizer()

file_name = "cartoondemo.jpeg" #File_name will come here
res = tmp_canvas.render(file_name)

cv2.imwrite("Cartoon version.jpg", res)
#plt.imshow("Cartoon version.jpg")

cv2.imshow("Cartoon version", res)
img=cv2.cvtColor(res,cv2.COLOR_BGR2RGB)
plt.subplot(1,1,1)
plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
