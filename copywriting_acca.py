import time
import os
import json
import openai
import streamlit as st
from streamlit_lottie import st_lottie
from tenacity import retry, stop_after_attempt, wait_random_exponential

def main():
    set_page_config()
    custom_css()
    hide_elements()
    sidebar()
    title_and_description()
    input_section()

def set_page_config():
    st.set_page_config(
        page_title="Alwrity",
        layout="wide",
        page_icon="img/logo.png"
    )

def custom_css():
    st.markdown("""
        <style>
            .block-container {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 1rem;
                padding-right: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <style>
            [class="st-emotion-cache-7ym5gk ef3psqc12"] {
                display: inline-block;
                padding: 5px 20px;
                background-color: #4681f4;
                color: #FBFFFF;
                width: 300px;
                height: 35px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                border-radius: 8px;
            }
        </style>
    """, unsafe_allow_html=True)

def hide_elements():
    hide_decoration_bar_style = '<style>header {visibility: hidden;}</style>'
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)

    hide_streamlit_footer = '<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>'
    st.markdown(hide_streamlit_footer, unsafe_allow_html=True)

def sidebar():
    st.sidebar.title("Awareness-Comprehension-Conviction-Action")
    st.sidebar.image("img/alwrity.jpeg", use_column_width=True)
    st.sidebar.markdown("🧕 :red[Checkout Alwrity], complete **AI writer & Blogging solution**:[Alwrity](https://alwrity.netlify.app)")


def title_and_description():
    st.title("✍️ Alwrity - AI Generator for CopyWriting ACCA Formula")
    with st.expander("What is **Copywriting ACCA formula** & **How to Use**? 📝❗"):
        st.markdown('''
            ### What's ACCA copywriting Formula, How to use this AI generator 🗣️
            ---
            #### ACCA Copywriting Formula

            ACCA stands for Awareness-Comprehension-Conviction-Action. It's a copywriting formula that involves:

            1. **Awareness**: Capturing the audience's attention by highlighting a problem or need.
            2. **Comprehension**: Helping the audience understand the problem better through information and examples.
            3. **Conviction**: Persuading the audience that your solution is the best option by showcasing benefits and addressing objections.
            4. **Action**: Motivating the audience to take action, such as making a purchase or signing up.

            The ACCA formula guides copywriters in creating persuasive content that leads the audience from awareness to action.

            #### ACCA Copywriting Formula: Simple Example

            - **Awareness**: Are you tired of waking up tired every morning?
            - **Comprehension**: Imagine struggling through the day, constantly battling fatigue and low energy levels.
            - **Conviction**: Our energy-boosting supplement provides a natural solution to help you feel revitalized and refreshed every day.
            - **Action**: Order now and start your journey to better energy levels!

            ---
        ''')

def input_section():
    with st.expander("**PRO-TIP** - Campaign's Key features and benefits to build **Interest & Desire**", expanded=True):
        col1, space, col2 = st.columns([5, 0.1, 5])
        with col1:
            brand_name = st.text_input('**Enter Brand/Company Name**')
        with col2:
            description = st.text_input(f'**Describe What {brand_name} Does ?** (In 5-6 words)')

        problem = st.text_input('What Problem Does Your Audience Face?', help="Example: 'Struggling to manage finances'")
        agitate = st.text_input('Why is This Problem Serious for Your Audience?', help="Guide: 'Highlight the negative impact'")
        solution = st.text_input('How Does Your Product/Service Solve This Problem?', help="Guide: 'Explain how your solution helps'")

        if st.button('**Get ACCA Copy**'):
            if problem.strip() and agitate.strip() and solution.strip():
                with st.spinner("Generating ACCA Copy..."):
                    acca_copy = generate_acca_copy(brand_name, description, problem, agitate, solution)
                    if acca_copy:
                        st.subheader('**👩🔬👩🔬 Your ACCA Copy**')
                        st.markdown(acca_copy)
                    else:
                        st.error("💥 **Failed to generate ACCA copy. Please try again!**")
            else:
                st.error("Problem, Agitate, and Solution fields are required!")

    page_bottom()


@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def generate_acca_copy(brand_name, description, problem, agitate, solution):
    prompt = f"""As an expert social media copywriter, I need your help in creating a marketing campaign for {brand_name}, 
        which is a {description}. Your task is to use the ACCA (Awareness-Comprehension-Conviction-Action) formula to craft compelling copy.
        Use below Details:
        - Awareness: {problem}
        - Comprehension: {agitate}
        - Conviction: {solution}
        Do not provide explanations in your response, provide response as final ad copy.
    """
    return openai_chatgpt(prompt)



@retry(wait=wait_random_exponential(min=1, max=60), stop=stop_after_attempt(6))
def openai_chatgpt(prompt, model="gpt-3.5-turbo-0125", max_tokens=500, top_p=0.9, n=1):
    try:
        client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            n=n,
            top_p=top_p
        )
        return response.choices[0].message.content
    except openai.APIError as e:
        st.error(f"OpenAI API Error: {e}")
    except openai.APIConnectionError as e:
        st.error(f"Failed to connect to OpenAI API: {e}")
    except openai.RateLimitError as e:
        st.error(f"Rate limit exceeded on OpenAI API request: {e}")
    except Exception as err:
        st.error(f"An error occurred: {err}")


# Function to import JSON data
def import_json(path):
    with open(path, "r", encoding="utf8", errors="ignore") as file:
        url = json.load(file)
        return url


def page_bottom():
    """ """
    data_oracle = import_json(r"lottie_files/brain_robot.json")
    st_lottie(data_oracle, width=600, key="oracle")

    st.markdown('''
    Copywrite using ACCA formula - powered by AI (OpenAI, Gemini Pro).

    Implemented by [Alwrity](https://alwrity.netlify.app).

    Learn more about [Google's Stance on AI generated content](https://alwrity.netlify.app/post/googles-guidelines-on-using-ai-generated-content-everything-you-need-to-know).
    ''')

    st.markdown("""
    ### Problem:
    Are you struggling to create compelling marketing campaigns that grab your audience's attention and drive them to take action?

    ### Agitate:
    Imagine spending hours crafting a message, only to find it doesn't resonate with your audience or compel them to engage with your brand. Your campaigns may lack the attention-grabbing headlines, compelling details, and persuasive calls-to-action needed to stand out in today's crowded digital landscape.

    ### Conviction:
    Introducing Alwrity - Your AI Generator for Copywriting ACCA Formula.
    """)



if __name__ == "__main__":
    main()

