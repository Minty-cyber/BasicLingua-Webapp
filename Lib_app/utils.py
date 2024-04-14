from basiclingua import BasicLingua


def Translate(api_key, user_input, target_lang):
    client = BasicLingua(api_key=api_key)
    translated_text = client.text_translate(user_input, target_lang)
    return translated_text

def Text_Replace(api_key, user_input, replacement_rules):
    client = BasicLingua(api_key=api_key)
    answer = client.text_replace(user_input, replacement_rules)
    return answer

def Text_Correction(api_key, user_input):
    client = BasicLingua(api_key=api_key)
    corrected_text = client.text_spellcheck(user_input)
    return corrected_text

def ExtractPattern(api_key, user_input, patterns):
    client = BasicLingua(api_key=api_key)
    extracted_patterns = client.extract_patterns(user_input, patterns)
    return extracted_patterns

def DetectNER(api_key, user_input, ner_tags):
    client = BasicLingua(api_key=api_key)
    answer = client.detect_ner(user_input, ner_tags)
    return answer

def TextSummarize(api_key, user_input, summary_length):
    client = BasicLingua(api_key=api_key)
    summary = client.text_summarize(user_input, summary_length)
    return summary

def TextQA(api_key, user_input, question):
    client = BasicLingua(api_key=api_key)
    answer = client.text_qna(user_input, question)
    return answer
    
def TextIntent(api_key, user_input):
    client = BasicLingua(api_key=api_key)
    intent = client.text_intent(user_input)
    return intent

def TextLemstem(api_key, user_input, task_type):
    client = BasicLingua(api_key=api_key)
    answer = client.text_lemstem(user_input, task_type)
    return answer

def TextTokenize(api_key, user_input):
    client = BasicLingua(api_key=api_key)
    answer = client.text_tokenize(user_input)
    return answer

def TextEmbedd(api_key, user_input, task_type):
    client =  BasicLingua(api_key=api_key)
    answer = client.text_embedd(user_input, task_type)
    return answer

def TextGenerate(api_key, user_input, ans_length):
    client = BasicLingua(api_key=api_key)
    answer = client.text_generate(user_input, ans_length)
    return answer

def TextClean(api_key, user_input, clean_info):
    client = BasicLingua(api_key=api_key)
    answer = client
