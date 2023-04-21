
import datetime
import numpy as np
import pandas as pd
import requests
import csv
import streamlit as st
import pandas as pd


st.write("Hi")

df = pd.read_csv("data.csv")
df2 = pd.read_csv("Barometer.csv")
st.line_chart(df)
st.bar_chart(df2)
