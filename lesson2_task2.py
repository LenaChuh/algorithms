{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d87e94ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "2. Посчитать четные и нечетные цифры введенного натурального числа.\n",
    "Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07d7b073",
   "metadata": {},
   "outputs": [],
   "source": [
    "num = int(input('Введите число: '))\n",
    "tch=0\n",
    "ntch=0\n",
    "i=len(str(num))\n",
    "\n",
    "while i>0:\n",
    "    \n",
    "    if int(num%10)%2==0:\n",
    "        tch+=1\n",
    "    else:\n",
    "        ntch+=1\n",
    "    i-=1\n",
    "    num=num/10\n",
    "    \n",
    "print (tch,ntch)"
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
