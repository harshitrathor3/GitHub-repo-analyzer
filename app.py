from mainn import main
from utils import get_all_repo_name
import streamlit as st

if __name__=='__main__':
    # text = st.text_input('Enter the github url')
    # text = input('Enter the github url')
    # text = 'https://github.com/cmooredev/RepoReader'
    # username = input('Enter the github username : ')
    st.title('GitHub Analyzer')
    # api_key = st.text_input('Enter your API key (this will be deleted when you close the application) : ')
    # st.secrets["openai_key"] = api_key
    username = st.text_input('Enter the github username : ')
    if username:
        repos = get_all_repo_name(username)

        for repo in repos:
            github_url = 'https://github.com/'+username+'/'+repo
            st.write(f'Repo Name {repo}')
            ans = main(github_url)
            st.write(f'Model says : \n')
            st.write(ans)
            st.write(github_url)
