
# 形態學轉換挑戰總覽

- 形態學轉換是基於圖像形狀進行處理的影像運算，常用於去除雜訊、平滑影像和強化邊緣。
- 本挑戰將使用 OpenCV 實作多種形態學操作，針對二值影像進行處理。

---

## 1. 產生二值圖像

- 產生黑底的二值影像。
- 隨機放置不同大小和顏色（白或黑）的圖形（圓形、矩形、線條）。
- 使用 OpenCV 的繪圖函式（`cv2.circle()`、`cv2.rectangle()`、`cv2.line()`）。
- 回傳生成的二值圖像。

---

## 2. 膨脹與侵蝕操作

- 膨脹用於擴張白色區域，侵蝕用於縮小白色區域。
- 支援不同形狀的結構元素：矩形、橢圓形、十字形。
- 可調整結構元素大小及膨脹、侵蝕次數。
- 使用 OpenCV 的 `cv2.getStructuringElement()`、`cv2.dilate()` 和 `cv2.erode()`。
- 回傳處理後的影像。

---

## 3. 開運算與閉運算

- 開運算：先侵蝕後膨脹，用於移除小白點雜訊。
- 閉運算：先膨脹後侵蝕，用於填補小黑洞。
- 支援多種結構元素形狀與大小。
- 使用 `cv2.morphologyEx()` 搭配 `MORPH_OPEN` 與 `MORPH_CLOSE`。
- 回傳處理後的影像。

---

## 4. 形態學梯度

- 計算膨脹與侵蝕的差值，用於強調圖像邊緣。
- 支援不同結構元素形狀與大小。
- 使用 `cv2.morphologyEx()` 搭配 `MORPH_GRADIENT`。
- 回傳處理後的影像。

---

## 總結

完成本挑戰後，你將能夠：

- 產生含隨機圖形的二值影像。
- 使用基本形態學操作（膨脹、侵蝕）調整圖像形狀。
- 應用複合形態學操作（開運算、閉運算）清理雜訊和填洞。
- 利用形態學梯度突出邊緣。
- 根據需求選擇及調整結構元素，提升影像處理效果。

建議先分別測試各子任務函式，再將它們結合成完整的影像處理流程。


# Morphological Transformations Challenge Overview

Morphological transformations are image processing operations based on shapes, often used for noise removal, smoothing, and edge enhancement. This challenge involves implementing various morphological operations on binary images using OpenCV.

---

## 1. Binary Image Generator

- Generate a binary image with a black background.
- Randomly place shapes (circles, rectangles, lines) of varying sizes and colors (white or black).
- Use OpenCV drawing functions (`cv2.circle()`, `cv2.rectangle()`, `cv2.line()`).
- Return the generated binary image.

---

## 2. Dilation and Erosion Operations

- Apply dilation to expand white regions and erosion to shrink them.
- Use different structuring element shapes: rectangular, elliptical, cross-shaped.
- Vary the size of the structuring element and the number of iterations.
- Use OpenCV functions: `cv2.getStructuringElement()`, `cv2.dilate()`, and `cv2.erode()`.
- Return the processed image.

---

## 3. Opening and Closing Operations

- Opening = erosion followed by dilation, removes small white noise.
- Closing = dilation followed by erosion, fills small black holes.
- Use structuring elements of various shapes and sizes.
- Use OpenCV's `cv2.morphologyEx()` with `MORPH_OPEN` and `MORPH_CLOSE`.
- Return the processed image.

---

## 4. Morphological Gradient

- Calculate the difference between dilation and erosion of an image.
- Used to highlight edges.
- Use different structuring element shapes and sizes.
- Use OpenCV's `cv2.morphologyEx()` with `MORPH_GRADIENT`.
- Return the processed image.

---

## Summary

By completing these tasks, you will understand how to:

- Generate binary images with random shapes.
- Apply fundamental morphological operations (dilation, erosion).
- Use compound operations (opening, closing) for noise removal and hole filling.
- Extract edges using morphological gradient.
- Select and tune structuring elements for different effects.

Test each function individually and then combine them to build a complete image processing pipeline.
