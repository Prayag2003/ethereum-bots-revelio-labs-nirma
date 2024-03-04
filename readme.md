## ResumeRevealer Track: Advanced Resume Parsing Challenge<br>
### Home institute: Pandit Deendayal Energy University Gujarat<br>
###[Video and Demo Link](https://drive.google.com/drive/folders/1ylObFJslXcwDefmXUtW7ImHQ1tuQHBiF?usp=sharing)
## Team Name: Ethereum Bots<br>
### Team Members: Prayag Bhatt , Denil Bhatt , Aum Pandya , Aniket Suthar , Bhavya Thumar

![image](https://github.com/Prayag2003/ethereum-bots-revelio-labs-nirma/assets/94465961/77ce6f4b-1c47-4b07-b04d-d509ae645062)

<hr>

## Proposed Approach
<hr>

### 1. Parsing Task
Streamlining the handling of diverse resume formats through appropriate extraction
functions.

### 2. Preprocessing -
Punctuation is removed using regular expressions, and each line is converted to
lowercase, split into words, and rejoined after eliminating empty strings and spaces.
This preprocessing yields a lowercase text without punctuation, suitable for
subsequent analysis.

### 3. Section classification and ordering based on profile
The identify_sections function categorizes lines of preprocessed text into different
sections based on predefined rule-based matching, providing a simple yet effective
approach for section classification.

### 4. Parsing dates -
The get_date_time function parses date strings, handling both single dates and date
ranges, returning a tuple of (START_DATE: datetime, END_DATE: datetime) in ISO
format or None if parsing fails. It efficiently handles various date formats, providing
flexibility and reliability in date extraction tasks.

### 5. Applying O-net Standardization -
Utilizing vector embeddings, cosine similarity, and sentence transformers, we apply
O-net standardization to align candidate profiles with standardized frameworks.

### 6. Skill extraction from the summary -
Use of n-gram scoring to predict skills along with SentenceTransformer, spacy, and
custom libraries (skillNer) for natural language processing and skill extraction tasks.
based on their relevance, producing a comprehensive list of both directly matched
and predicted skill set.

### 7. Career Trajectory representation using Graph-
The career trajectory is graphically depicted using the Digraph class from graphviz,
which provides a brief and visually intuitive summary of educational and professional
milestones.

<br>

# Installation Guide

## Installing Required Packages

To install the necessary Python packages, please run the following commands:



## Also include OPEN_API_KEY and HF_TOKEN in your collab notebook's environment variables




bash
```
!pip install graphviz 
!pip install pdfminer.six PyPDF2 pytesseract PyMuPDF opencv-python python-docx openai==0.28
!pip install -U sentence-transformers
!pip install spacy
!pip install skillNer
!python -m spacy download en_core_web_lg
```

Also include OPEN_AI_KEY and HF_TOKEN in your collab notebook

# Parsing Task:

*Purpose of this section:*
- This section is dedicated to the parsing task. The goal is to accept resumes from users and return the text contained within these files.
- The acceptable formats are: pdf, docx, image('.jpg', '.jpeg', '.png', '.gif', '.tiff', '.tif'), html, and .tex files.
- The load_text_from_files function is used to iterate over files in a directory (root) and extract text from each file based on its extension. The extracted text is then stored in a list (extracted_content) and returned.

*Dependencies:*

- The following Python libraries are required: os, re, cv2, BeautifulSoup, pytesseract, pdfminer, docx, dateutil, datetime, openai, json, csv, sentence_transformers, numpy, spacy, skillNer, graphviz.
- The SentenceTransformer model 'all-MiniLM-L6-v2' is used.
- The Spacy model 'en_core_web_lg' is used.

*Input Handling:*

- The function takes one argument:root, which specifies the directory containing the files.



*Processing Steps:*

- For each file in the directory, the function checks its extension using file_name.endswith() and calls the appropriate extraction function (extract_text_from_pdf, extract_text_from_docx, extract_text_from_img, extract_text_from_html) based on the file type.
- The extracted text is appended to the extracted_content list.

*Output:*

- The function returns a list (extracted_content) containing the extracted text from all files in the directory.

# PREPROCESSING:

*Purpose:*

- The remove_punctuations function removes specified punctuation characters (period and comma) from a given line using regular expressions.
- The preprocess_document function preprocesses a document by converting each line to lowercase, removing punctuation, splitting into words, removing empty strings and spaces, and rejoining the words into a line.

*Input Handling:*

- The remove_punctuations function takes a single argument line, representing a single line of text.
- The preprocess_document function takes a list document as input, where each element of the list is a line of text.

*Processing Steps:*

- remove_punctuations: Uses the re.sub function to replace periods and commas with an empty string in the input line.
- preprocess_document:
  - Converts each line to lowercase.
  - Removes punctuation using remove_punctuations.
  - Splits each line into a list of words using the space character as a delimiter.
  - Removes any empty strings or spaces from the list.
  - Joins the words back into a line using a space as a separator.
  - Appends the preprocessed line to the preprocessed_document list if it is not empty.



# Section Classification and ordering based on profiles:

*Function Purpose:*

- The identify_sections function categorizes lines of text from a document into different sections based on predefined rule based matching.

*Benefit:*
- The simple based matching outperformed in the results based on qualitative matching than complex techniques we tried such as creating embeddings and comparision and use of LLM. Plus it's less compute heavy

*Input Handling:*

- The function takes a list document as input, where each element of the list is a preprocessed line of text from the document.

*Processing Steps:*

- The function first initializes a dictionary sections with section names as keys and empty lists as values.
- It then iterates over each line in the document.
- For each line, it attempts to find a match with any of the predefined section synonyms using a regular expression pattern (regex_pattern).
- If a match is found, the line is added to the corresponding section list in the sections dictionary.
- If no match is found, the line is added to the current section if a section header has been previously identified.

*Output:*

- The function returns a dictionary sections containing the categorized lines of text for each section.


# Parsing Dates:
*Function Purpose of get_date_time:*  
   - The function get_date_time takes a date string as input, which can be in various formats, and returns a tuple (START_DATE: datetime, END_DATE: datetime).

*Input Handling:*  
   - If the input string contains " - " or " to " (indicating a date range), it splits the string into date_parts.
   - If the input string does not contain a date range delimiter, it considers the entire input as a single date part.

*Parsing Start Date:*  
   - It tries to parse the first part of the date_parts list (representing the start date) using parser.parse from the dateutil library.

*Parsing End Date:*  
   - If date_parts has more than one element (indicating an end date is present), it checks if the end date is "present". If it is, it sets the end_date to the current date and time using datetime.now().
   - Otherwise, it tries to parse the second part of date_parts (representing the end date) using parser.parse.
   - If parsing fails, it returns (None, None).

*Formatting Dates:*  
   - It converts the start_date and end_date to ISO format strings (YYYY-MM-DDTHH:MM:SS) if they are not None.

*Returning Dates:*  
   - It returns a tuple (start_date, end_date) where each date is either a valid ISO format string or None if parsing failed.


*Function Purpose generate_response - LLM api based part:*

- The generate_response function generates a response to a system prompt followed by a user prompt using the OpenAI API.

*Input Handling:*

- The function takes three arguments: system_prompt (the prompt for the system), user_prompt (the prompt for the user), and max_tokens (maximum number of tokens in the response).

*Processing Steps:*

- The function uses the OpenAI API to create a completion for the given prompts (system_prompt and user_prompt) using the GPT-3.5-turbo-instruct engine.
- The prompt parameter in the API call is formatted to include the system and user prompts.
- The max_tokens, temperature, and stop parameters control the length and creativity of the response.

*Output:*

- The function returns the generated response as a string.



- *Function Purpose:*
  - The functions get_formatted_education_section, get_formatted_experience_section, and get_formatted_projects_section use a large language model (LLM) to fetch rich descriptions for sections.

- *Input Handling:*
  - The function takes a single argument section, which represents the input text section containing education information.

- *Processing Steps:*
  - The function generates a user prompt and uses it to generate a response using the generate_response function (assumed to utilize the LLM).
  - The response is converted from JSON format to a Python dictionary (structure).
  - The function then adds start_date and end_date to each education entry by calling the get_date_time function with the duration of each education entry.

- *Output:*
  - The function returns a structured JSON/dictionary containing education information with added start_date and end_date.


# APPLYING O-NET STANDARDIZATION TO JOB TITLES:
load_o_net_job_data(csv_file_path):
- Purpose: Loads O-NET job standard data from a CSV file and returns it as a tuple of lists.
- Input: csv_file_path (str) - Path to the CSV file containing O-NET job standard data.
- Output: Tuple of lists containing codes, titles, and descriptions of O-NET job standards.

prepare_o_net_job_description_embeddings(descriptions):
- Purpose: Prepares O-NET job description embeddings using a pre-trained model.
- Input: descriptions (list) - List of job descriptions.
- Output: Embeddings of job descriptions generated by the pre-trained model.

get_o_net_std_job_format(job):
- Purpose: Extracts O-NET job standard format information from a given job structure and returns it as a dictionary.
- Input: job (dict) - A dictionary representing a job structure containing fields like title and descriptions.
- Output: A dictionary containing O-NET job standard format information including code, title, and description.


# SKILL EXTRACTION:
extract_skills_using_descriptions(descriptions):
- Purpose: Extracts skills from the description section of a work experience and returns them as a dictionary.
- Input: descriptions (list) - List of strings representing descriptions of work experience.
- Output: A dictionary containing lists of skills, including full matches and predicted matches, based on matching and n-gram scoring.



# MAIN EXECUTION:
The script processes resumes extracted from files in a directory, performs segmentation, and structures sections including education and experience.

For each resume:
- The content is preprocessed and segmented into sections such as education and experience.
- Education and experience sections are structured and augmented with O-NET job standard format information and extracted skills.
- The processed documents are appended to a global list.

The script concludes by recording the end time, completing the resume processing pipeline.

# CAREER TRAJECTORY:

The script combines education and experience entries into a single list, sorts them by start date, and visualizes them using a Digraph.

For each entry:
- The script formats the title, start date, end date, and duration.
- Nodes are added to the graph with labels containing this information.
- Arrows between nodes indicate the chronological order of entries.
