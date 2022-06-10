{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "16db65eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.\n",
    "Например, если введено число 3486, надо вывести 6843."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59416dd1",
   "metadata": {},
   "outputs": [],
   "source": [
    "num = int(input('Введите число: '))\n",
    "\n",
    "i = len(str(num))\n",
    "\n",
    "while i>0:\n",
    "    print (int(num%10),end='')\n",
    "    i-=1\n",
    "    num=num/10"
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
