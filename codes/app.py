import streamlit as st
st.title('my home page')
st.header('i am header')
st.markdown('**streamlit is amazing**')
st.markdown('#heading1')
st.markdown('# heading1')
st.markdown('## heading1')
st.markdown('### heading1')
st.markdown('#### heading1')
st.markdown('##### heading1')

st.title('streamlit rocks :100: :white_check_mark:')
st.code('''
//hello world in java
class test{
public static void main(string args[])
{
}
}
''', language='java'
)
st.divider()
st.text("i am sanju", help='https://github.com/farhana-codes/Mobile-Shop-CRUD/tree/main/virtual/scripts')

st.text(f"the sum of {10} and {20} is {sum(10,20)}")