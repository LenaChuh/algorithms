{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5bda8d9",
   "metadata": {},
   "outputs": [],
   "source": [
    "6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. \n",
    "Сами минимальный и максимальный элементы в сумму не включать."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "45d3d213",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[12, 3, 7, 14, 4, 13, 5, 11, 14, 15]\n",
      "98\n"
     ]
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "list1 = [random.randint(0,18) for _ in range(10)]\n",
    "print (list1)\n",
    "\n",
    "left = list1[0]\n",
    "right = list1[len(list1)-1]\n",
    "\n",
    "for i in range(1,len(list1)):\n",
    "    if list1[i] < left:\n",
    "        left = list1[i]\n",
    "    elif list1[i] > right:\n",
    "        right = list1[i]\n",
    "        \n",
    "summ=0       \n",
    "for i in list1:\n",
    "    if i!=right or i!=left:\n",
    "        summ += i\n",
    "        \n",
    "print (summ)"
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
