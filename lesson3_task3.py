{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62fa835f",
   "metadata": {},
   "outputs": [],
   "source": [
    "В массиве случайных целых чисел поменять местами минимальный и максимальный элементы."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4c67add7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[7, 9, 1, 3, 9, 7, 6, 5, 4, 3]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "[7, 1, 9, 3, 9, 7, 6, 5, 4, 3]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import random\n",
    "\n",
    "list2 = [random.randint(1,10) for _ in range(10)]\n",
    "list2\n",
    "list1 = list2.copy()\n",
    "print (list2)\n",
    "\n",
    "\n",
    "max_razn = 0\n",
    "pos1 = 0\n",
    "pos2 = 0\n",
    "pos1_n = 0\n",
    "pos2_n = 0\n",
    "\n",
    "for i,n in enumerate(list2[:]):\n",
    "    \n",
    "    list2.remove(n)\n",
    "    \n",
    "    for j in list2:\n",
    "        if abs(n-j) > max_razn:\n",
    "            max_razn = abs(n-j)\n",
    "            pos1 = j\n",
    "            pos2 = n\n",
    "            pos1_n = i\n",
    "            pos2_n = list2[list2==j] + i\n",
    "            \n",
    "list1[pos1_n],list1[pos2_n] = list1[pos2_n],list1[pos1_n]\n",
    "\n",
    "list1"
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
