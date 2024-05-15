# Summit: Automatic Meeting Summaries
[![pt-br](https://img.shields.io/badge/lang-pt--br-green.svg)](https://github.com/chulipinho/summit/blob/master/README.pt-br.md)

Summit is a tool that uses Google Cloud's AI Platform and artificial intelligence to generate automatic summaries of your Google Meet meetings.

### Practical Applications:

**Business Environment**:

* Summit is the ideal tool for companies that want to provide a weekly summary to their employees.
* With just one click, Summit generates and distributes detailed summaries to all provided emails, optimizing internal communication and information sharing.

**Personal Use**:

* Summit is perfect for users who need to stay organized amidst multiple meetings.
* Get instant summaries of each meeting, allowing you to focus on the most important points and make more effective decisions.

## Index

1. [Installation](#installation)

2. [Usage](#usage)

3. [How it Works](#how-it-works)

4. [Notes](#notes)

5. [Contact](#contact)

## Installation

**Prerequisites**:

* Python 3.6 or higher

* Pip

* Google Cloud Platform Account

* Google Workspace Account

**Steps**:

1. **Clone the repository**:

```bash
git clone https://github.com/chulipinho/summit
```

2. **Install dependencies**:

```bash
cd summit
python -m pip install -r requirements.txt
```

3. **Create the `.env` file**:

Create a file named `.env` in the project's root directory and add the following information:

```
API_KEY=your_ai_studio_api_key  # Your Ai Studio API Key
VIDEO_PATH=meetings          # The name of the folder where recordings are located in Google Drive

# Other optional configurations
# CLEAR_TMP: Boolean - Defines if the content of the tmp folder will be deleted after execution
# LOG_PATH: String - Path to the folder where the Log will be stored
# PORT_NUMBER: String - Port for redirection of your OAuth2 authentication URL, default value is 3031
# LANGUAGE: String - Language of the Ai Studio response, default value is PT-BR (currently only supports Portuguese and English)
```

4. **Create the JSON credential files**:

Follow the instructions in [this tutorial](https://developers.google.com/workspace/guides/create-credentials?hl=en) from Google to create the JSON credential files. Remove the "_example" from your file names.

**Notes**:

* The Ai Studio API key can be obtained from your Google Cloud Platform account.

* The path to the video folder on Google Drive should be adjusted according to your organization.

* The optional configurations in the `.env` file can be customized according to your needs.

## Usage

1. **Run the script**:

```bash
python main.py
```

2. **Follow the on-screen instructions**:
- Authenticate with your Google Account.

- Enter the email addresses of the recipients who will receive the summaries.

**Summit will process your meeting recordings and send the summaries via email to the specified recipients.**

## How it Works

1. **Summit accesses Google Drive**: It automatically searches for video files in the folder configured in the `.env` file.

2. **Processing each video**:
- **Local storage**: The video is stored locally on the computer.

- **Audio extraction**: Only the audio is extracted from the video to reduce the use of Ai Studio API tokens.

- **Ai Studio analysis**: The audio file is sent to Ai Studio, which generates a summary of the meeting.

- **Summary storage**: The summary is stored in a list.

3. **Sending emails**:
- **Email creation**: For each summary, an email is created with the content of the summary and the informed recipients.

- **Sending via Gmail API**: Emails are sent to the recipients using the Gmail API.

## Notes

- Summit can be used for any meeting platform. Just store the recordings in Google Drive.

- Summit is under development and new features will be added soon.

- If you encounter any problems, please submit a bug report in the GitHub repository.

## Contact

For more information about Summit or to report issues, you can contact us through the following channels:

- **LinkedIn:** [Fellipe Machado](https://www.linkedin.com/in/fellipe-luz/)
- **Email:** fellipe.luz.machado@gmail.com

Thank you for your interest in Summit!
