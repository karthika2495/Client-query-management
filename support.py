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

st.title("SUPPORT DASHBOARD")

col1, col2 = st.columns([1, 2])


with col1:
    st.image("c:/Users/Karthika/Downloads/support-concept-illustration-idea-advice-help-assistance_613284-2215.avif", width=500)

with col2:


    query_id = st.text_input(
        "Enter Query ID",
        value=st.session_state.get("last_query_id", "")
    )

    if st.button("Fetch Query", key="fetch_btn"):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT query_id, client_email, client_mobile, query_heading,
                   query_description, query_created_time, status
            FROM query
            WHERE query_id = %s
        """, (query_id,))

        data = cur.fetchone()


        cur.close()
        conn.close()

        if data:
            st.session_state["query_data"] = data 
            st.session_state["last_query_id"] = query_id
        else:
            st.error("No query found with that ID.")
            st.session_state["query_data"] = None

 
    if "query_data" in st.session_state and st.session_state["query_data"]:
        data = st.session_state["query_data"]

        st.write("### Query Details")
        st.write(f"**Query ID:** {data[0]}")
        st.write(f"**Email:** {data[1]}")
        st.write(f"**Mobile:** {data[2]}")
        st.write(f"**Heading:** {data[3]}")
        st.write(f"**Description:** {data[4]}")
        st.write(f"**Created On:** {data[5]}")
        st.write(f"**Status:** {data[6]}")

        query_solution = st.text_area("QUERY SOLUTION")
        resolved_by = st.text_input("RESOLVED BY")

       
        if st.button("SUBMIT", key="submit_btn"):
            conn = get_connection()
            cur = conn.cursor()
            
            cur.execute("""
                UPDATE query
                SET status = 'Closed',
                    query_closed_time = NOW(),
                    query_solution = %s,
                    resolved_by = %s
                WHERE query_id = %s
            """, (query_solution, resolved_by, query_id))

            conn.commit()
            cur.close()
            conn.close()

    
            st.success("Query resolved")

query_tabs = ["OPEN QUERY","CLOSED QUERY","HISTORY"]
tab1, tab2,tab3 = st.tabs(query_tabs)

with tab1:
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT * FROM query
        WHERE status = 'Open'
    """)
    open_results = cur.fetchall()
    cur.close()
    conn.close()
    

    st.dataframe(pd.DataFrame(open_results,
        columns=["query_id","client_email","client_mobile","query_heading",
                 "query_description","status","query_created_time",
                 "query_closed_time","query_solution","resolved_by"]
    ))
with tab2:
    conn=get_connection()
    cur = conn.cursor()
    cur.execute("""
         SELECT * FROM query
         WHERE status = 'Closed'
         """)
    closed_result = cur.fetchall()
    cur.close()
    conn.close()

    st.dataframe(pd.DataFrame(closed_result,
        columns=["query_id","client_email","client_mobile","query_heading",
                 "query_description","status","query_created_time",
                 "query_closed_time","query_solution","resolved_by"]
    ))

with tab3:
    df=pd.read_csv("c:/Users/Karthika/Downloads/synthetic_client_queries (1).csv")
    st.write(df)
if st.button("LOG OUT"):
     st.switch_page("home.py")



       




    

