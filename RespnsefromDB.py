from langchain.text_splitter import RecursiveCharacterTextSplitter
# import os
# import argparse
# from dotenv import load_dotenv
# from langchain.chains import RetrievalQA
#from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import BedrockEmbeddings
# from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
# from langchain.vectorstores.azuresearch import AzureSearch
from langchain.vectorstores import Chroma
from langchain.schema.document import Document

from langchain.document_loaders.json_loader import JSONLoader
from langchain.document_loaders.xml import UnstructuredXMLLoader

# import json
# import regex as re
# import pyodbc as pc

from chromadb.config import Settings



# Define the folder for storing database

# embeddings = HuggingFaceEmbeddings(model_name='all-mpnet-base-v2')
embeddings = BedrockEmbeddings(credentials_profile_name="default",model_id="cohere.embed-multilingual-v3")
# # Define the Chroma settings
CHROMA_SETTINGS = Settings(
        chroma_db_impl='duckdb+parquet',
        persist_directory='dbm',
        anonymized_telemetry=False
)
db = Chroma(
        persist_directory='dbm',
        embedding_function=embeddings,
        client_settings=CHROMA_SETTINGS,
    )


responses = db.similarity_search_with_score('''"Protocolo",
     "Número de centro",
       "Número de selección",
       "Número de aleatorización",
      "Fecha de evaluación",
#         "Evaluador",
#         "Historial de firmas",
#         "Completado y firmado por",
#         "Nombre",
#         "Fecha/Hora (UTC)",
#         "Editado y firmado por",
#         "Versión",
#         "Page2",
#         "Page7",
#         "  \nTeniendo en cuenta toda su experiencia clínica con estos individuos en particular (pacientes que padecen la enfermedad de Parkinson), ¿cómo calificaría la gravedad de la condición del paciente en este momento al evaluar sus alucinaciones e ideas delirantes?",
#         "Text1",
#         "Normal, nada enfermo",
#         "Casi a punto de que se le considere enfermo",
#         " \nTeniendo en cuenta toda su experiencia clínica con estos individuos en particular (pacientes que padecen la enfermedad de Parkinson), ¿cómo calificaría la gravedad de la condición del paciente en este momento al evaluar sus alucinaciones e ideas delirantes? ",
#         "CGI-S PD Psychosis",
#         "Levemente enfermo",
#         "Moderadamente enfermo",
#         "Notablemente enfermo",
#         "Gravemente enfermo",
#         "Entre los pacientes más extremadamente enfermos",
#         "Notas"''', k=1)
# # ls=[]
print(responses)