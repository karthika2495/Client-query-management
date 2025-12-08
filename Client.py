import streamlit as st
import psycopg2
import pandas as pd
from datetime import datetime


def get_connection():
    return psycopg2.connect(
        host="localhost",
        database="karthikalocal",
        user="postgres",
        password="Yeira23"
    )

st.title("QUERY")

# Layout
col1, col2 = st.columns([1, 2])
with col1:
    st.image("c:/Users/Karthika/Downloads/client.jpg", width=500)

with col2:
    email_id = st.text_input("EMAIL ID")
    mobile_no = st.text_input("MOBILE NUMBER")
    query_Heading = st.text_input("QUERY HEADING")
    query_Description = st.text_area("QUERY DESCRIPTION")

    if st.button("SUBMIT"):
       
        conn = get_connection()
        cur = conn.cursor()

     
        cur.execute("""
            INSERT INTO query (
                client_email,
                client_mobile,
                query_heading,
                query_description,
                status
            ) VALUES (%s, %s, %s, %s, %s)
            RETURNING query_id;
        """, (email_id, mobile_no,query_Heading, query_Description, "Open"))

        
        query_id = cur.fetchone()[0]

        conn.commit()
        conn.close()

       
        st.session_state["last_query_id"] = query_id

        st.success(f"Your query has been submitted! Query ID: {query_id}")

    if st.button("LOG OUT"):
           st.switch_page("home.py")

  

       
