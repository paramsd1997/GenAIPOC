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



### CGI-C_HD
### CGI-S_Essential_Tremor
### CGI-S_PD_Psychosis
text  =  '''
        "Protocol",
        "Site Number",
        "Screening Number",
        "Randomization Number",
        "Assessment Date",
        "Rater",
        "Signature History",
        "Completed and Signed by",
        "Name",
        "Date/Time (UTC)",
        "Edited and Signed by",
        "Version",
        "Page2",
        "Page3",
        "Clinical Global Impression of Change",
        "Please choose the response below that best describes the change in his/her overall clinical status since starting this study:",
        "Text8",
        "Very much improved ",
        "Text8",
        "Much improved",
        "Text18",
        "Minimally improved",
        "Text19",
        "No  \nchange ",
        "Text20",
        "Minimally worse",
        "Text21",
        "Much  \nworse",
        "Text21",
        "Very much \nworse",
        "Text21",
        " 1 ",
        " The overall change in your health condition, since starting this study:",
        "SingleChoice1",
        " 2 ",
        "&nbsp;3&nbsp;",
        " 4 ",
        " 5 ",
        "&nbsp;6&nbsp;",
        " 7 ",
        "   Yes   ",
        "   No   ",
        "Has this change in his/her overall clinical status had a meaningful impact on his/her daily life? \n ",
        "SelectableRows1",
        "Notes"
,'''

text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=0,
            length_function=len
            )
chunks = text_splitter.split_text(text=text)
for chunk in chunks:

        data = [Document(page_content = chunk , metadata= {'id':'CGI-C_HD_alt1'}  )]
        print(type(data))
        db.add_documents(data)



# responses = db.similarity_search_with_score('''"Protocolo",
#         "Número de centro",
#         "Número de selección",
#         "Número de aleatorización",
#         "Fecha de evaluación",
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
# print(responses)