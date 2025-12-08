import streamlit as st



#Home PAGE

st.title("CLIENT QUERY MANAGEMENT SYSTEM")

st.image("C:/Users/Karthika/Downloads/photo-logicpath-customer-support.webp")

page = st.sidebar.selectbox(
    "Navigation",
    ["Home", "Client", "Support"]
)

st.write("You selected:", page)

#LOGIN PAGE

st.title("LOGIN PAGE")

# User ID
email_id = st.text_input("Enter the Email ID")


# Password
password = st.text_input("Enter the Password", type="password")

#Role
role = st.radio("Select Role", ["Client", "Support"])
st.write("Selected role:", role)



allowed_users = {
    "priya.sharma@example.com": {"password": "Priya@123", "role": "Client"},
    "karthik.reddy@example.com": {"password": "Karthik@654", "role": "Client"},
    "divya.nair@example.com": {"password": "Divya@987", "role": "Client"},
    "rahul.verma@example.com": {"password": "Rahul@456", "role": "Support"},
    "sneha.iyer@example.com": {"password": "Sneha@789", "role": "Support"},
    "arjun.mehta@example.com": {"password": "Arjun@321", "role": "Support"},

}

if st.button("Login"):
    if email_id in allowed_users:
        if password == allowed_users[email_id]["password"]:
            user_role = allowed_users[email_id]["role"]

            if role == user_role:
                if role == "Client":
                    st.switch_page("pages/Client.py")
                elif role == "Support":
                    st.switch_page("pages/support.py")
                else:
                    st.error("Invalid role selected")
            else:
                st.error("Incorrect role for this user")
        else:
            st.error("Incorrect password")
    else:
        st.error("Email ID not found")
                    
