
import datetime
import numpy as np
import pandas as pd
import requests
import csv
import streamlit as st
import pandas as pd


st.write("")

df = pd.read_csv("Barometer.csv")
#df2= pd.read_csv("Barometer.csv")
st.line_chart(df)
#st.line_chart(df2)
