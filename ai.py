from pathlib import Path
import hashlib
import google.generativeai as genai
import os
from dotenv import load_dotenv

import logger

log = logger.get_logger()

load_dotenv()
LANGUAGE = os.getenv("LANGUAGE", "PT-BR")

genai.configure(api_key=os.getenv("API_KEY"))

instruction_set = {
	"simple": "Listen to the attached audio recording of a meeting and provide a concise summary of the key points discussed. Organize the summary by topic and conclude with the main outcomes or decisions reached.",
	"detailed": "Analyze the attached audio recording of a meeting and generate a comprehensive report. Identify the main topics discussed, key arguments presented, and decisions made. Organize the report by topic and for each, include relevant details such as supporting evidence, dissenting opinions, and action items. Conclude with a summary of the meeting's overall objectives and effectiveness.",
  "action": "Review the attached meeting recording and create an action-oriented summary. Identify key discussion points, decisions made, and assigned tasks. Organize the summary by topic and for each, clearly outline the next steps, responsible individuals, and deadlines. Conclude with a brief overview of the meeting's main goals and action plan."
}

instruction = instruction_set["simple"]

if LANGUAGE == "PT-BR":
  instruction += "\nTraduza o resultado para português brasileiro."

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
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

system_instruction = instruction

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              system_instruction=system_instruction,
                              safety_settings=safety_settings)

uploaded_files = []
def upload_if_needed(pathname: str) -> list[str]:
	path = Path(pathname)
	hash_id = hashlib.sha256(path.read_bytes()).hexdigest()
	try:
		existing_file = genai.get_file(name=hash_id)
		return [existing_file]
	except:
		pass
	uploaded_files.append(genai.upload_file(path=path, display_name=hash_id))
	return [uploaded_files[-1]]

def analize_audio(path):
    prompt_parts = [
		*upload_if_needed(path),
	]
	
    log.info("Generating content")
    response = model.generate_content(prompt_parts, request_options={"timeout": 200})

    for uploaded_file in uploaded_files:
        genai.delete_file(name=uploaded_file.name)
  	
    return response.text

if __name__ == "__main__":
	res = analize_audio("tmp\Product Marketing Meeting (weekly) 2021-06-28 (480p).mp3")
	print(res)
	
