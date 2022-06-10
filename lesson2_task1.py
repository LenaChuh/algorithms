{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "97dfb56a",
   "metadata": {},
   "outputs": [],
   "source": [
    "1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.\n",
    "Числа и знак операции вводятся пользователем. \n",
    "После выполнения вычисления программа не завершается, а запрашивает новые данные для вычислений.\n",
    "Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. \n",
    "Если пользователь вводит неверный знак (не '0', '+', '-', '', '/'), \n",
    "программа должна сообщать об ошибке и снова запрашивать знак операции. \n",
    "Также она должна сообщать пользователю о невозможности деления на ноль, если он ввел его в качестве делителя."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9356173e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "введите первое число: 1\n",
      "введите второе число: 2\n",
      "введите действие: *\n",
      "2\n",
      "введите первое число: 1\n",
      "введите второе число: 4\n",
      "введите действие: 0\n",
      "выход\n"
     ]
    }
   ],
   "source": [
    "while True:  \n",
    "    num1 = int(input('введите первое число: '))\n",
    "    num2 = int(input('введите второе число: '))\n",
    "    oper = input('введите действие: ')\n",
    "    \n",
    "    if oper in ['+', '-', '*', '/']:\n",
    "        if oper == '+':\n",
    "            print (num1+num2)\n",
    "        elif oper == '-':\n",
    "            print (num1-num2)\n",
    "        elif oper == '*':\n",
    "            print (num1*num2)\n",
    "        elif oper == '/':\n",
    "            if num2==0:\n",
    "                print ('на ноль делить нельзя!')\n",
    "            else: \n",
    "                print (num1/num2)\n",
    "    elif oper=='0':\n",
    "        print ('выход')\n",
    "        break\n",
    "    else:\n",
    "        print('введите новый знак операции')"
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
