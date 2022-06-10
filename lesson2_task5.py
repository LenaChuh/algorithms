{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b25c60d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.\n",
    "Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91834486",
   "metadata": {},
   "outputs": [],
   "source": [
    "i=32\n",
    "st=1\n",
    "\n",
    "while i<=127:\n",
    "    \n",
    "    st+=1\n",
    "    print (f'{i}-{chr(i)} ',end='')\n",
    "    \n",
    "    if st%11==0:\n",
    "        print ('\\n')\n",
    "        s=0\n",
    "        \n",
    "    i+=1"
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
