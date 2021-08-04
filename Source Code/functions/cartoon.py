def cartoon(img):
  color = cv2.bilateralFilter(img, 9,300,300)
  cartoon = cv2.bitwise_and(color, color, mask = edge())
  cartoon = cv2.detailEnhance(cartoon, sigma_s= enhance, sigma_r=0.15)
  return cartoon
