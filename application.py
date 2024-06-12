import streamlit as st
from utils import invoke_chain

map_data= [{"Find Imperial market share for outlet 0015I00000OYJeHQAX":"perf_ins_1.1"},
               {"Find the market share for all product groups in the outlet 0015I00000OYJeHQAX month wise product group wise":"perf_ins_1.2"},
               {"Find market share for all SKU for Cigarettes in outlet 0015I00000OYJeHQAX month wise":"perf_ins_1.3"},
               {"Find Imperial market share for all SKU for Cigarettes in outlet 0015I00000OYJeHQAX month wise and SKU wise":"perf_ins_1.4"},
               {"Find the product with lowest sales for outlet 0015I00000OYJeHQAX for Cigarettes product group":"perf_ins_1.5"},
               {"Find the name and Imperial market share of all the outlets in the micro region of outlet 0015I00000OYJeHQAX":"perf_ins_1.6"},
               {"Find the market share for Cigarettes and Fine Cut product groups in the outlet 0015I00000OYJeHQAX month wise product group wise":"perf_ins_1.7"},
               {"Find Imperial market share for outlet 0017S00000Aw8TpQAJ":"perf_ins_2.1"},
               {"Find the market share for all product groups in the outlet 0017S00000Aw8TpQAJ month wise product group wise":"perf_ins_2.2"},
               {"Find market share for all SKU for Cigarettes in outlet 0017S00000Aw8TpQAJ month wise":"perf_ins_2.3"},
               {"Find Imperial market share for all SKU for Cigarettes in outlet 0017S00000Aw8TpQAJ month wise and SKU wise":"perf_ins_2.4"},
               {"Find the lowest sales product from 0017S00000Aw8TpQAJ for Cigarettes product group":"perf_ins_2.5"},
               {"Find the name and Imperial market share of all the outlets in the micro region of outlet 0017S00000Aw8TpQAJ":"perf_ins_2.6"},
               {"Find the market share for Cigarettes and Fine Cut product groups in the outlet 0017S00000Aw8TpQAJ month wise product group wise":"perf_ins_2.7"},
               {"Find Imperial market share for outlet 0017S00000eKOdmQAG":"perf_ins_3.1"},
               {"Find the market share for all product groups in the outlet 0017S00000eKOdmQAG month wise product group wise":"perf_ins_3.2"},
               {"Find market share for all SKU for Cigarettes in outlet 0017S00000eKOdmQAG month wise":"perf_ins_3.3"},
               {"Find Imperial market share for all SKU for Cigarettes in outlet 0017S00000eKOdmQAG month wise and SKU wise":"perf_ins_3.4"},
               {"Find the product with lowest sales from outlet 0017S00000eKOdmQAG for Cigarettes product group":"perf_ins_3.5"},
               {"Find the name and Imperial market share of all the outlets in the micro region of outlet 0017S00000eKOdmQAG":"perf_ins_3.6"},
               {"Find the market share for all Cigarettes and Fine Cut product groups in the outlet 0017S00000eKOdmQAG month wise product group wise":"perf_ins_3.7"},
               {"Find Imperial market share for outlet 0017S00000eKOdZQAW":"perf_ins_4.1"},
               {"Find the market share for all product groups in the outlet 0017S00000eKOdZQAW month wise product group wise":"perf_ins_4.2"},
               {"Find market share for all SKU for Cigarettes in outlet 0017S00000eKOdZQAW month wise":"perf_ins_4.3"},
               {"Find Imperial market share for all SKU for Cigarettes in outlet 0017S00000eKOdZQAW month wise and SKU wise":"perf_ins_4.4"},
               {"Find the lowest sales product from 0017S00000eKOdZQAW for Cigarettes product group":"perf_ins_4.5"},
               {"Find Imperial market share for outlet 0017S00000lexgKQAQ":"perf_ins_5.1"},
               {"Find the market share for all product groups in the outlet 0017S00000lexgKQAQ month wise product group wise":"perf_ins_5.2"},
               {"Find market share for all SKU for Cigarettes in outlet 0017S00000lexgKQAQ month wise":"perf_ins_5.3"},
               {"Find Imperial market share for all SKU for Cigarettes in outlet 0017S00000lexgKQAQ month wise and SKU wise":"perf_ins_5.4"},
               {"Find the lowest sales product from 0017S00000lexgKQAQ for Cigarettes product group":"perf_ins_5.5"},
               {"Find name of the 3 top performing SKUs for Imperial for outlet 0015I00000OYJeHQAX":"dist_ins_1.1"},
               {"Find name and rank of the distinct top 3 power rank for Imperial SKUs from the micro region of outlet 0015I00000OYJeHQAX":"dist_ins_1.2"},
               {"Find name of the 15 top performing SKUs for Imperial for outlet 0015I00000OYJeHQAX":"dist_ins_1.3"},
               {"Find name and rank of the distinct top 15 power rank for Imperial SKUs from the micro region of outlet 0015I00000OYJeHQAX":"dist_ins_1.4"},
               {"Find name of the 3 top performing SKUs for Imperial for outlet 0017S00000eKOdmQAG":"dist_ins_2.1"},
               {"Find name and rank of the distinct top 3 power rank for Imperial SKUs from the micro region of outlet 0017S00000eKOdmQAG":"dist_ins_2.2"},
               {"Find name of the 15 top performing SKUs for Imperial for outlet 0017S00000eKOdmQAG":"dist_ins_2.3"},
               {"Find name and rank of the distinct top 15 power rank for Imperial SKUs from the micro region of outlet 0017S00000eKOdmQAG":"dist_ins_2.4"},
               {"Find name of the 3 top performing SKUs for Imperial for outlet 0017S00000eKOdZQAW":"dist_ins_3.1"},
               {"Find name and rank of the distinct top 3 power rank for Imperial SKUs from the micro region of outlet 0017S00000eKOdZQAW":"dist_ins_3.2"},
               {"Find name of the 15 top performing SKUs for Imperial for outlet 0017S00000eKOdZQAW":"dist_ins_3.3"},
               {"Find name and rank of the distinct top 15 power rank for Imperial SKUs from the micro region of outlet 0017S00000eKOdZQAW":"dist_ins_3.4"},
               ]

st.title("Imperial Brands Chatbot")


if "messages" not in st.session_state:
    
    st.session_state.messages = []


for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if prompt := st.chat_input("What is up?"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
        

    
    with st.spinner("Generating response..."):
        with st.chat_message("assistant"):
            response = invoke_chain(prompt,st.session_state.messages)
            st.markdown(response)
                            
    st.session_state.messages.append({"role": "assistant", "content": response})