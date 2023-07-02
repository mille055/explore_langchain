import streamlit as st
import pandas as pd
import os
import numpy as np

from pdf2image import convert_from_path
import pytesseract
from PyPDF2 import PdfReader
from langchain.agents import create_csv_agent
from langchain.llms import OpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

api_key = os.ENVIRON('OPENAI_API_KEY')
if api_key is not None:
  print('I have an openai api key')

                     
