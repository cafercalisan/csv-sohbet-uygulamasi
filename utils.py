
import os
from typing import TextIO

import openai
import pandas as pd
import streamlit as st
from langchain.agents import create_csv_agent, create_pandas_dataframe_agent
from langchain.llms import OpenAI

#openai.api_key = st.secrets["OPENAI_API_KEY"]


def get_answer_csv(file: TextIO, query: str) -> str:
    

    # CSV dosyanızı pandas çerçevesinde yükleyin.
    df = pd.read_csv(file)
    df = pd.read_csv("titanic.csv")

    # Pandas çerçevesinde bir open ai ajanı oluşturarak devam edin.
    agent = create_csv_agent(OpenAI(temperature=0), file, verbose=False)
    #agent = create_pandas_dataframe_agent(OpenAI(temperature=0), df, verbose=False)

    # Çalıştıralım.
    #sorgu  = "Tablodaki ortalama yaş değeri nedir?"
    answer = agent.run(query)
    return answer
