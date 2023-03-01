# Import necessary libraries
from ast import Lambda
from cProfile import label
from cgitb import text
import io
from msilib.schema import CheckBox
import tkinter
from turtle import back
import urllib.request
from lib2to3.pgen2 import driver
from tkinter import Image
from tkinter import *
import tkinter as tk
from urllib import request
import urllib
from tkinter import messagebox
from webbrowser import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
import os
import selenium
from selenium import webdriver
import urllib
import time
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Define the function to send the message
def sendmsg():
    # Show a message box
    messagebox.showwarning("WHATSSAP BOT", "Scannez le code QR")
    # Wait for 2 seconds
    time.sleep(2)
    messagebox.CANCEL
    # Set up the Chrome driver
    driver = webdriver.Chrome("E:\\chromedriver.exe")
    driver.maximize_window()
    driver.get("https://web.whatsapp.com/")
    # Wait for 30 seconds (to give the user time to scan the QR code)
    time.sleep(30)
    # Find the search box and enter the contact name
    search = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[3]/div/div[1]/div/div/div[2]/div/div[2]",
    )
    search.send_keys(inputn.get())
    search.send_keys(Keys.ENTER)
    # Wait for 2 seconds
    time.sleep(2)
    # Find the input box and enter the message
    input = driver.find_element(
        By.XPATH,
        "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]",
    )
    time.sleep(2)
    input.send_keys(inputm.get())
    # Wait for 2 seconds
    time.sleep(2)
    input.send_keys(Keys.ENTER)
    # Wait for 3 seconds
    time.sleep(3)
    # Clear the input boxes
    inputm.delete(0, END)
    inputn.delete(0, END)
    # If the disconnect checkbox is selected
    if var1.get() == 1:
        # Find and click the disconnect button
        dbar = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[3]/div/span",
        )
        time.sleep(2)
        dbar.click()
        time.sleep(2)
        dbtn = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/div/div[3]/header/div[2]/div/span/div[3]/span/div/ul/li[4]/div[1]",
        )
        time.sleep(2)
        dbtn.click()
        time.sleep(2)
        lg = driver.find_element(
            By.XPATH,
            "/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/div[2]/div/div",
        )
        time.sleep(2)
        lg.click()
        time.sleep(8)
    else:
        # Wait for 2 seconds
        time.sleep(2)


# Define the function to clear the input boxes
def clear():
    inputm.delete(0, END)
    inputn.delete(0, END)


# Create the window
window = Tk()
window.title("Whatsapp Bot (By Ilyass Salout)")

# Add an icon to the window
photo = tk.PhotoImage(file="E:\wp.png")
window.wm_iconphoto(False, photo)

# set window size and background color
window.geometry("700x300")
window.configure(bg="green")

# create a label for the app name
en = tkinter.Label(
    window,
    text="WHATSAPP BOT",
    font=("Helvetica bold", 26),
    anchor=tkinter.CENTER,
    bg="white",
    fg="green",
    background="white",
)
en.place(x=200, y=10)

# create a label for the contact name input
name = tkinter.Label(
    window,
    text="Enter Nom Du Contact :",
    font=("Helvetica bold", 15),
    anchor=tkinter.CENTER,
    bg="green",
    fg="white",
)
name.place(x=10, y=75)

# create an input field for contact name
inputn = tkinter.Entry(window)
inputn.place(x=400, y=80, width=260, height=20)

# create a label for the message input
message = tkinter.Label(
    window,
    text="Enter Votre Message  :",
    font=("Helvetica bold", 15),
    anchor=tkinter.CENTER,
    bg="green",
    fg="white",
)
message.place(x=10, y=130)

# create an input field for message
inputm = tkinter.Entry(window)
inputm.place(x=400, y=136, width=260, height=20)

# create a check button for disconnect option
var1 = tkinter.IntVar()
c1 = tkinter.Checkbutton(
    window,
    text="Disconnect",
    variable=var1,
    font=("Helvetica bold", 14),
    onvalue=1,
    offvalue=0,
)
c1.place(x=300, y=200)

# create a button to send the message
b1 = tkinter.Button(
    window,
    text="SEND",
    font=("Helvetica bold", 15),
    width=20,
    anchor=tkinter.CENTER,
    foreground="green",
    activeforeground="red",
    bg="white",
    command=sendmsg,
)
b1.place(x=100, y=250)

# create a button to clear the inputs
b2 = tkinter.Button(
    window,
    text="CLEAR",
    font=("Helvetica bold", 15),
    width=20,
    anchor=tkinter.CENTER,
    foreground="green",
    activeforeground="red",
    bg="white",
    command=clear,
)
b2.place(x=400, y=250)

# start the main event loop
window.mainloop()
