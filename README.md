# Alwrity - AI Generator for Copywriting ACCA Formula

Alwrity is a web application built with Streamlit that utilizes OpenAI's GPT-3.5 model to generate marketing copy using the ACCA (Awareness-Comprehension-Conviction-Action) formula. This application enables users to create persuasive marketing content by inputting key details about their brand, the problem their audience faces, and the solution they offer.

## ACCA Copywriting Formula

ACCA stands for Awareness-Comprehension-Conviction-Action. It's a copywriting formula that involves:

1. **Awareness**: Capturing the audience's attention by highlighting a problem or need.
2. **Comprehension**: Helping the audience understand the problem better through information and examples.
3. **Conviction**: Persuading the audience that your solution is the best option by showcasing benefits and addressing objections.
4. **Action**: Motivating the audience to take action, such as making a purchase or signing up.

The ACCA formula guides copywriters in creating persuasive content that leads the audience from awareness to action.

### ACCA Copywriting Formula: Simple Example

- **Awareness**: Are you tired of waking up tired every morning?
- **Comprehension**: Imagine struggling through the day, constantly battling fatigue and low energy levels.
- **Conviction**: Our energy-boosting supplement provides a natural solution to help you feel revitalized and refreshed every day.
- **Action**: Order now and start your journey to better energy levels!

## Features

- **ACCA Formula**: Utilizes the Awareness-Comprehension-Conviction-Action copywriting formula to guide users in creating persuasive marketing copy.
- **AI-Powered**: Employs OpenAI's GPT-3.5 model to generate high-quality marketing content based on user inputs.
- **User-Friendly Interface**: Offers an intuitive interface for users to input campaign details and view generated copy.
- **Retry Logic**: Implements retry logic using the Tenacity library to handle potential errors when communicating with the OpenAI API.

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies listed in the `requirements.txt` file.
3. Set up your OpenAI API key as an environment variable named `OPENAI_API_KEY`.
4. Run the `app.py` file to start the Streamlit application.
5. Input your brand/company name, description, problem, agitate, and solution in the provided text fields.
6. Click the "Get ACCA Copy" button to generate marketing copy based on the ACCA formula.
7. View the generated copy and iterate as needed.

## Dependencies

- Streamlit
- OpenAI
- Streamlit Lottie
- Tenacity

## Contributing

Contributions are welcome! If you have any ideas for improvements or bug fixes, please open an issue or submit a pull request.

## License

[TODO: Insert license information here]

## Acknowledgements

- Special thanks to OpenAI for providing access to the GPT-3.5 model.
- This project was inspired by the need for efficient and effective marketing copy generation.
