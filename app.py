from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
import os
from langchain.vectorstores import Deeplake
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import streamlit as st
from streamlit_chat import message
from dotenv import load_dotenv

load_dotenv()

