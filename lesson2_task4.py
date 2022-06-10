{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eeb53c27",
   "metadata": {},
   "outputs": [],
   "source": [
    "4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… \n",
    "    Количество элементов (n) вводится с клавиатуры."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4369097f",
   "metadata": {},
   "outputs": [],
   "source": [
    "n = int(input('введите количество элементов: '))\n",
    "\n",
    "i=n\n",
    "summ=1\n",
    "\n",
    "    \n",
    "while i>1:\n",
    "    summ+=1/((-2)**(i-1))\n",
    "    i-=1\n",
    "else:\n",
    "    print (summ)"
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
