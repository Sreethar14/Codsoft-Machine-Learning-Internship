{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "16886692",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-13 16:44:08.425 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.368 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\ProgramData\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2024-10-13 16:44:09.376 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.376 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.376 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.376 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.376 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.381 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.381 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.384 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.385 Session state does not function when running a script without `streamlit run`\n",
      "2024-10-13 16:44:09.385 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.385 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.388 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.396 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.396 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-13 16:44:09.396 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "from sklearn.feature_extraction.text import CountVectorizer\n",
    "import numpy as np\n",
    "from win32com.client import Dispatch\n",
    "\n",
    "def speak(text):\n",
    "\tspeak=Dispatch((\"SAPI.SpVoice\"))\n",
    "\tspeak.Speak(text)\n",
    "\n",
    "\n",
    "model = pickle.load(open('spam.pkl','rb'))\n",
    "cv=pickle.load(open('vectorizer.pkl','rb'))\n",
    "\n",
    "\n",
    "def main():\n",
    "\tst.title(\"Email Spam Classification Application\")\n",
    "\tst.write(\"Build with Streamlit & Python\")\n",
    "\tactivites=[\"Classification\",\"About\"]\n",
    "\tchoices=st.sidebar.selectbox(\"Select Activities\",activites)\n",
    "\tif choices==\"Classification\":\n",
    "\t\tst.subheader(\"Classification\")\n",
    "\t\tmsg=st.text_input(\"Enter a text\")\n",
    "\t\tif st.button(\"Process\"):\n",
    "\t\t\tprint(msg)\n",
    "\t\t\tprint(type(msg))\n",
    "\t\t\tdata=[msg]\n",
    "\t\t\tprint(data)\n",
    "\t\t\tvec=cv.transform(data).toarray()\n",
    "\t\t\tresult=model.predict(vec)\n",
    "\t\t\tif result[0]==0:\n",
    "\t\t\t\tst.success(\"This is Not A Spam Email\")\n",
    "\t\t\t\tspeak(\"This is Not A Spam Email\")\n",
    "\t\t\telse:\n",
    "\t\t\t\tst.error(\"This is A Spam Email\")\n",
    "\t\t\t\tspeak(\"This is A Spam Email\")\n",
    "main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a6c1890c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
