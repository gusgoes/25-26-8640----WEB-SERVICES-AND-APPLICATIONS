{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4f368b45",
   "metadata": {},
   "outputs": [
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'interactapi'",
     "output_type": "error",
     "traceback": [
      "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
      "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
      "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[8]\u001b[39m\u001b[32m, line 4\u001b[39m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msys\u001b[39;00m\n\u001b[32m      3\u001b[39m sys.path.append(\u001b[33m\"\u001b[39m\u001b[33m../lab02\u001b[39m\u001b[33m\"\u001b[39m)\n\u001b[32m----> \u001b[39m\u001b[32m4\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01minteractapi\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mipynb\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m updatebook, readbook, createbook, deletebook\n",
      "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'interactapi'"
     ]
    }
   ],
   "source": [
    "import requests\n",
    "import sys\n",
    "sys.path.append(\"../lab02\")\n",
    "from interactapi.ipynb import updatebook, readbook, createbook, deletebook\n"
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
   "version": "3.11.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
