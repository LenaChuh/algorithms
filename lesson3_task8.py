{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "74597854",
   "metadata": {},
   "source": [
    "8. Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк. \n",
    "Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. \n",
    "В конце следует вывести полученную матрицу."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4b5762f6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "введите число: 1\n",
      "введите число: 2\n",
      "введите число: 3\n",
      "введите число: 4\n",
      "введите число: 5\n",
      "введите число: 6\n",
      "введите число: 7\n",
      "введите число: 3\n",
      "введите число: 4\n",
      "введите число: 2\n",
      "введите число: 4\n",
      "введите число: 6\n",
      "введите число: 3\n",
      "введите число: 4\n",
      "введите число: 5\n",
      "   1   2   3   |6\n",
      "   4   5   6   |15\n",
      "   7   3   4   |14\n",
      "   2   4   6   |12\n",
      "   3   4   5   |12\n",
      "---------------\n"
     ]
    }
   ],
   "source": [
    "matrix = [[int(input('введите число: ')) for _ in range(3)] for _ in range(5)]\n",
    "\n",
    "sum_column = [0]*len(matrix)\n",
    "\n",
    "for line in matrix:\n",
    "    sum_line=0\n",
    "    \n",
    "    for i,item in enumerate(line):\n",
    "        \n",
    "        sum_line += item\n",
    "        \n",
    "        print(f'{item:>4}', end='')\n",
    "        \n",
    "    print (f'   |{sum_line}')\n",
    "print ('-'*len(matrix)*3)"
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
