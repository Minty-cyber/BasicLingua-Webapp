from basiclingua import GeminiLingua


def Translate(api_key, user_input, target_lang):
    client = GeminiLingua(api_key=api_key)
    translated_text = client.text_translate(user_input, target_lang)
    return translated_text

def Text_Replace(api_key, user_input, replacement_rules):
    client = GeminiLingua(api_key=api_key)
    answer = client.text_replace(user_input, replacement_rules)
    return answer


def Text_Correction(api_key, user_input):
    
    gemini_model = GeminiLingua(api_key=api_key, model_name='gemini-1.0-pro-latest', 
                                vision_model_name='models/gemini-1.5-pro-latest')
    corrected_text = gemini_model.text_spellcheck(user_input)
    
    return corrected_text

def ExtractPattern(api_key, user_input, patterns):
    client = GeminiLingua(api_key=api_key)
    extracted_patterns = client.extract_patterns(user_input, patterns)
    return extracted_patterns

def DetectNER(api_key, user_input, ner_tags):
    client = GeminiLingua(api_key=api_key)
    answer = client.detect_ner(user_input, ner_tags)
    return answer

def TextSummarize(api_key, user_input, summary_length):
    client = GeminiLingua(api_key=api_key, model_name="gemini-1.0-pro-latest")
    summary = client.text_summarize(user_input, summary_length)
    return summary

def TextQA(api_key, user_input, question):
    client = GeminiLingua(api_key=api_key)
    answer = client.text_qna(user_input, question)
    return answer
    
def TextIntent(api_key, user_input):
    client = GeminiLingua(api_key=api_key)
    intent = client.text_intent(user_input)
    return intent

def TextLemstem(api_key, user_input, task_type):
    client = GeminiLingua(api_key=api_key)
    answer = client.text_lemstem(user_input, task_type)
    return answer

def TextTokenize(api_key, user_input):
    client = GeminiLingua(api_key=api_key)
    answer = client.text_tokenize(user_input)
    return answer

def TextEmbedd(api_key, user_input, task_type):
    client =  GeminiLingua(api_key=api_key)
    answer = client.text_embedd(user_input, task_type)
    return answer

def TextGenerate(api_key, user_input, ans_length):
    client = GeminiLingua(api_key=api_key)
    answer = client.text_generate(user_input, ans_length)
    return answer

def TextClean(api_key, user_input, clean_info):
    client = GeminiLingua(api_key=api_key)
    answer = client.text_clean(user_input, clean_info)
    return answer

def TextNormalize(api_key, user_input, mode):
    client = GeminiLingua(api_key=api_key)
    transformed_answer = client.text_normalize(user_input, mode)
    return transformed_answer

def TextSRL(api_key, user_input):
    client = GeminiLingua(api_key=api_key)
    srl_result = client.text_srl(user_input)
    return srl_result





# from basiclingua import GeminiLingua

# gemini_model = GeminiLingua(api_key="YOUR_GEMINI_API_KEY", model_name="gemini-1.0-pro-latest")
# summary = gemini_model.text_summarize(input_text, summary_length)

# print(summary) 