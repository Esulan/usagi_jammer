{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Choose 1 picture\n",
      "a\n",
      "Nothing picture\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "def usagi(img, rect):\n",
    "    (x1, y1, x2, y2) = rect\n",
    "    w = x2 - x1\n",
    "    h = y2 - y1\n",
    "    newimg = cv2.imread(\"usagi.png\")\n",
    "    i_rect = img[y1:y2, x1:x2]\n",
    "    \n",
    "    i_mos = cv2.resize(newimg, (w, h), interpolation=cv2.INTER_AREA)\n",
    "    \n",
    "    img2 = img.copy()\n",
    "    img2[y1:y2, x1:x2] = i_mos\n",
    "    return img2\n",
    "\n",
    "cascade_file = \"haarcascade_frontalface_alt.xml\"\n",
    "cascade = cv2.CascadeClassifier(cascade_file)\n",
    "\n",
    "print(\"Choose 1 picture\")\n",
    "str = input()\n",
    "img = cv2.imread(str)\n",
    "if img is not None:\n",
    "    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
    "\n",
    "    face_list = cascade.detectMultiScale(img_gray, minSize=(10, 10))\n",
    "    if len(face_list) == 0:\n",
    "        quit()\n",
    "\n",
    "    for (x, y, w, h) in face_list:\n",
    "        img = usagi(img, (x, y, x + w, y + h))\n",
    "\n",
    "    cv2.imwrite(\"autousagi.png\", img)\n",
    "    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))\n",
    "    plt.show()\n",
    "else:\n",
    "    print(\"Nothing picture\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
