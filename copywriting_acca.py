import os
import streamlit as st
from tenacity import retry, stop_after_attempt, wait_random_exponential
import google.generativeai as genai


def main():
    set_page_config()
    custom_css()
    hide_elements()
    title_and_description()
    input_section()

def set_page_config():
    st.set_page_config(
        page_title="Alwrity ACCA Copywriting",
        layout="wide",
    )

def custom_css():
    st.markdown("""
        <style>
                ::-webkit-scrollbar-track {
        background: #e1ebf9;
        }

        ::-webkit-scrollbar-thumb {
            background-color: #90CAF9;
            border-radius: 10px;
            border: 3px solid #e1ebf9;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #64B5F6;
        }

        ::-webkit-scrollbar {
            width: 16px;
        }
        div.stButton > button:first-child {
            background: #1565C0;
            color: white;
            border: none;
            padding: 12px 24px;
            border-radius: 8px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 10px 2px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
            font-weight: bold;
        }
        </style>
    """, unsafe_allow_html=True)

def hide_elements():
    hide_decoration_bar_style = '<style>header {visibility: hidden;}</style>'
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    hide_streamlit_footer = '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>'
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)


def title_and_description():
    st.title("✍️ Alwrity - AI Generator for CopyWriting ACCA Formula")


def input_section():
    with st.expander("**💡 PRO-TIP** - Highlight Campaign's Key Features and Benefits to Build **Interest & Desire**", expanded=True):
        col1, space, col2 = st.columns([5, 0.1, 5])
        with col1:
            brand_name = st.text_input('**🏢 Enter Brand/Company Name**', placeholder="e.g., Alwrity")
        with col2:
            description = st.text_input(f'**📝 Describe What Your Company Does (In 5-6 words)**', placeholder="e.g., AI writing tools")

        problem = st.text_input('❓ **What Problem Does Your Audience Face?**', 
                    help="Example: 'Struggling to manage finances'", 
                    placeholder="e.g., Struggling to manage finances")
        agitate = st.text_input('🔥 **Why is This Problem Serious for Your Audience?**', 
                    help="Highlight the negative impact", 
                    placeholder="e.g., Leads to financial instability")
        solution = st.text_input('💡 **How Does Your Product/Service Solve This Problem?**', 
                    help="Explain how your solution helps", 
                    placeholder="e.g., Provides easy-to-use budgeting tools")

        if st.button('**🚀 Get ACCA Copy**'):
            if problem.strip() and agitate.strip() and solution.strip():
                with st.spinner("🔄 Generating ACCA Copy..."):
                    acca_copy = generate_acca_copy(brand_name, description, problem, agitate, solution)
                    if acca_copy:
                        st.subheader('**✨ Your ACCA Copy**')
                        st.markdown(acca_copy)
                    else:
                        st.error("💥 **Failed to generate ACCA copy. Please try again!**")
            else:
                st.error("🚫 **Problem, Agitate, and Solution fields are required!**")


def generate_acca_copy(brand_name, description, problem, agitate, solution):
    prompt = f"""You are a top-tier social media copywriter. Create 5 different persuasive marketing campaigns for {brand_name}, 
        a company that specializes in {description}. Use the ACCA (Awareness-Curiosity-Conviction-Action) formula to craft 5 compelling copies.
        Here are the details:
        - **Awareness**: {problem}
        - **Curiosity**: {agitate}
        - **Conviction**: {solution}
        Please provide the final ad copy directly without any explanations.
    """
    try:
        response = generate_text_with_exception_handling(prompt)
        return response
    except Exception as err:
        st.error(f"Exit: Failed to get response from LLM: {err}")
        exit(1)


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def generate_text_with_exception_handling(prompt):
    """
    Generates text using the Gemini model with exception handling.

    Args:
        api_key (str): Your Google Generative AI API key.
        prompt (str): The prompt for text generation.

    Returns:
        str: The generated text.
    """

    try:
        genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

        generation_config = {
            "temperature": 0.7,
            "top_p": 0.6,
            "top_k": 0,
            "max_output_tokens": 1024,
        }

        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        model = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                      generation_config=generation_config,
                                      safety_settings=safety_settings)

        convo = model.start_chat(history=[])
        convo.send_message(prompt)
        return convo.last.text

    except Exception as e:
        st.exception(f"An unexpected error occurred: {e}")
        return None


if __name__ == "__main__":
    main()

