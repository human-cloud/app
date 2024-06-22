import streamlit as st 
from PIL import Image
import io
import matplotlib.pyplot as plt 
from streamlit_option_menu import option_menu
from keras.layers import *
from keras.models import *
import requests
import pandas as pd
import numpy as np
import tarfile
import os
import tensorflow as tf
import random
from keras.utils import *


def extract_tar_gz(file_path, extract_path):
    try:
        with tarfile.TarFile.open(file_path, "r:gz") as tar:
            tar.extractall(extract_path)
        print("Extraction successful.")
    except Exception as e:
        print(f"Extraction failed: {e}")


def find_rows(n):
    if n%5 == 0:
        return (int(n/5))
    else:
        return int(n//5)


def func(web,idx):
    try:
        url = web
        resp = requests.get(url)
        byt = resp.content
        cont = byt.decode('utf-8')
        g = cont.split(" ")
        pth = g[idx][6:-1]
        fin = web+pth
        return fin

    except Exception as e:
        url = web
        resp = requests.get(url)
        byt = resp.content
        cont = byt.decode('utf-8')
        g = cont.split(" ")
        pth = g[idx][6:-1]
        fin = web+pth
        return fin


def main():
    st.title("AI Image Generator")
    st.sidebar.title("Image type")
    with st.sidebar.expander("**NAVIGATION**", expanded = True):
        opt = st.selectbox(
                "**Select Type**",
                ['Person','Anime Characters','Night Sky','Iris (eye)','City Maps'] )


    if opt == 'Person':
        st.header("Person Generator")

        inp = st.text_input("**Enter the number of images to be generated (more than 5)**",value = '5')
        if inp and st.button("GO"):
            n = int(inp)
            rows = find_rows(n)
            cols= 5
            tot_pics = int(rows*cols)
            for row in range(rows):
                column = st.columns(cols)
                for j in range(cols):
                    url = 'https://www.thispersondoesnotexist.com/'
                    resp = requests.get(url)
                    img = Image.open(io.BytesIO(resp.content))
                    column[j].image(img)


    elif opt == "Anime Characters":
        st.header("Anime Character Generator")

        inp = st.text_input("**Enter the number of images to be generated (more than 5)**",value = '5')
        if inp and st.button("GO"):
            n = int(inp)
            rows = find_rows(n)
            for i in range(rows):
                columns = st.columns(5)
                nums=0
                while nums<5:
                    try:
                        i = str(random.randint(0,10))
                        j = str(random.randint(0,10))
                        k = str(random.randint(0,10))
                        l = str(random.randint(0,10))
                        m = str(random.randint(0,10))
                        fin = i+j+k+l+m
                        resp1 = requests.get(f"https://www.thiswaifudoesnotexist.net/example-{fin}.jpg")
                        img = Image.open(io.BytesIO(resp1.content))
                        columns[nums].image(img)
                        nums+=1
                    except Exception as e:
                        pass

    elif opt == "Night Sky":
        st.header("Night Sky Generator")
        inp = st.text_input("**Enter the number of images to be generated (more than 5)**",value = '5')
        if inp and st.button("GO"):
            n = int(inp)
            rows = find_rows(n)
            for i in range(rows):
                columns = st.columns(5)
                nums=0
                while nums<5:
                    try:
                        i = str(random.randint(0,10))
                        j = str(random.randint(0,10))
                        k = str(random.randint(0,10))
                        l = str(random.randint(0,10))
                        fin = i+j+k+l
                        resp1 = requests.get(f"https://firebasestorage.googleapis.com/v0/b/thisnightskydoesnotexist.appspot.com/o/images%2Fseed{fin}.jpg?alt=media")
                        img = Image.open(io.BytesIO(resp1.content))
                        columns[nums].image(img)
                        nums+=1
                    except Exception as e:
                        pass

    elif opt == "Iris (eye)":
        st.header("Iris (eye) Generator")
        inp = st.text_input("**Enter the number of images to be generated (more than 5)**",value = '5')
        
        if inp and st.button("GO"):
            n = int(inp)
            rows = find_rows(n)
            for i in range(rows):
                columns = st.columns(5)
                for j in range(5):
                    columns[j].image(func('https://thisirisdoesnotexist.com/',80))
    
    elif opt == "City Maps":
        st.header("City Maps Generator")
        inp = st.text_input("**Enter the number of images to be generated (more than 5)**",value = '5')
        
        if inp and st.button("GO"):
            n = int(inp)
            rows = find_rows(n)
            for i in range(rows):
                columns = st.columns(5)
                for j in range(5):
                    columns[j].image(func('https://thiscitydoesnotexist.com/',15))
        

if __name__ == "__main__":
    main()