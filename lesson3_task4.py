{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "89ccfca9",
   "metadata": {},
   "source": [
    "В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.\n",
    "Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный». Это два абсолютно разных значения."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ab702472",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[-7, 8, -6, 2, -5, -1, 6, 5, 4, 5]\n",
      "-1 5\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "list1=[random.randint(-8,8) for _ in range(10)]\n",
    "print (list1)\n",
    "\n",
    "razn = 1\n",
    "\n",
    "right = list1[-1]\n",
    "num = 0\n",
    "pos = 0\n",
    "right = 0\n",
    "left = list1[0]\n",
    "\n",
    "for i in range(1,len(list1)):\n",
    "    if list1[i] < left:\n",
    "        left = list1[i]\n",
    "        \n",
    "max_min_pos=0\n",
    "\n",
    "for i in range(1,len(list1)):\n",
    "    r = abs(left)\n",
    "    if list1[i] < 0 and abs(list1[i]) < r:\n",
    "        left = list1[i]\n",
    "        r = abs(left)\n",
    "        max_min_pos = list1.index(left)\n",
    "        \n",
    "print (left,max_min_pos)        "
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
