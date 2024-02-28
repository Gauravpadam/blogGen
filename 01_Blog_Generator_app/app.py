import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers

def getModelResponse(input, no_words, blog_style):

    llm=CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin' # Use a .env for better code
                      model_type='llama',
                      config={'max_new_tokens':256,
                              'temperature': 0.01})
    
    ## Prompt template
    template = """
        Write a blog for {blog_style} job profile for a topic {input} within {no_words} words.
               """
    
    prompt = PromptTemplate(input_variables=["blog_style", "input", "no_words"],
                            template=template)
    response = llm(prompt.format(blog_style=blog_style, input=input, no_words=no_words))
    print(response)
    return response

st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input = st.text_input("Enter the blog topic")

## Two more columns for the blog style and words

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No. of words')
with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data scientists', 'Common People'), index=0)

submit = st.button("Generate")

# Final response
if submit:
    st.write(getModelResponse(input, no_words, blog_style))



    



