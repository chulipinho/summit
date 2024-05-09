from pathlib import Path
import hashlib
import google.generativeai as genai
import os
from dotenv import load_dotenv

import logger

log = logger.get_logger()

load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

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

system_instruction = "Based on a given meeting recording, generate a summary covering the main topics discussed. Add a brief conclusion to the end. "

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
    response = model.generate_content(prompt_parts, request_options={"timeout": 100})
    print(response.text)
    for uploaded_file in uploaded_files:
        genai.delete_file(name=uploaded_file.name)
  	
    return response

if __name__ == "__main__":
	res = analize_audio("tmp\Product Marketing Meeting (weekly) 2021-06-28 (480p).mp3")
	print(res)
	
