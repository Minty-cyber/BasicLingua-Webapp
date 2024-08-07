from django.shortcuts import render
from .utils import *
from .forms import *
from django.http import JsonResponse, HttpResponse

    
def translate_view(request):
    translated_text = None

    if request.method == 'POST':
        form = TranslationForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            target_lang = form.cleaned_data['target_lang']
            translated_text = Translate(api_key, user_input, target_lang)  
            
            return JsonResponse({'translated_text': translated_text})
    else:
        form = TranslationForm()

    return render(request, 'Text_Trans.html', {'form': form, 'translated_text': translated_text})

def text_replace_view(request):
    answer = None

    if request.method == 'POST':
        form = TextReplacementForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            replacement_rules = form.cleaned_data['replacement_rules']
            answer = Text_Replace(api_key, user_input, replacement_rules) 

            return JsonResponse({'answer': answer})
    else:
        form = TextReplacementForm()

    return render(request, 'Text_Replace.html', {'form': form, 'answer': answer})


def text_correction_view(request):
    corrected_text = None

    if request.method == 'POST':
        form = TextCorrectionForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            corrected_text = Text_Correction(api_key, user_input)
        
            return JsonResponse({'corrected_text': corrected_text})
            
    else:
        form = TextCorrectionForm()

    return render(request, 'text_correction.html', {'form': form, 'corrected_text': corrected_text})

def extract_pattern_view(request):
    extracted_patterns = None
    
    if request.method == 'POST':
        form = ExtractPatternForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            patterns = form.cleaned_data['patterns']
            extracted_patterns = ExtractPattern(api_key, user_input, patterns) 

            return JsonResponse({'extracted_patterns': extracted_patterns})
    else:
        form = ExtractPatternForm()

    return render(request, 'Extract_Pattern.html', {'form': form, 'extracted_patterns': extracted_patterns})

def detect_ner_view(request):
    answer = None
    
    if request.method == 'POST':
        form = DetectNERForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            ner_tags = form.cleaned_data['ner_tags']
            answer = DetectNER(api_key, user_input, ner_tags) 

            return JsonResponse({'answer': answer})
    else:
        form = DetectNERForm()

    return render(request, 'Detect_NER.html', {'form': form, 'answer': answer})

def text_summarize_view(request):
    summary = None
    
    if request.method == 'POST':
        form = TextSummarizeForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            summary_length = form.cleaned_data['summary_length']
            summary = TextSummarize(api_key, user_input, summary_length) 

            return JsonResponse({'summary': summary})
    else:
        form = TextSummarizeForm()

    return render(request, 'Text_Summarize.html', {'form': form, 'summary': summary})

def text_qa_view(request):
    answer = None
    
    if request.method == 'POST':
        form = TextQAForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            question = form.cleaned_data['question']
            answer = TextQA(api_key, user_input, question) 

            return JsonResponse({'answer': answer})
    else:
        form = TextQAForm()

    return render(request, 'Text_QA.html', {'form': form, 'answer': answer})

def text_intent_view(request):
    intent = None

    if request.method == 'POST':
        form = TextIntentForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            intent = TextIntent(api_key, user_input) 

            return JsonResponse({'intent': intent})
    else:
        form = TextIntentForm()

    return render(request, 'Text_Intent.html', {'form': form, 'intent': intent})

def text_lemstem_view(request):
    answer = None

    if request.method == 'POST':
        form = TextLemstemForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            task_type = form.cleaned_data['task_type']
            answer = TextLemstem(api_key, user_input, task_type) 

            return JsonResponse({'answer': answer})
    else:
        form = TextLemstemForm()

    return render(request, 'Text_Lemstem.html', {'form': form, 'answer': answer})

def text_tokenize_view(request):
    answer = None

    if request.method == 'POST':
        form = TextTokenizeForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            answer = TextTokenize(api_key, user_input) 

            return JsonResponse({'answer': answer})
    else:
        form = TextTokenizeForm()

    return render(request, 'Text_Tokenize.html', {'form': form, 'answer': answer})

def text_embedd_view(request):
    answer = None

    if request.method == 'POST':
        form = TextEmbeddForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            task_type = form.cleaned_data['task_type']
            answer = TextEmbedd(api_key, user_input, task_type) 

            return JsonResponse({'answer': answer})
    else:
        form = TextEmbeddForm()

    return render(request, 'Text_Embedd.html', {'form': form, 'answer': answer})


def text_generate_view(request):
    answer = None

    if request.method == 'POST':
        form = TextGenerateForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            ans_length = form.cleaned_data['ans_length']
            answer = TextGenerate(api_key, user_input, ans_length) 

            return JsonResponse({'answer': answer})
    else:
        form = TextGenerateForm()

    return render(request, 'Text_Generate.html', {'form': form, 'answer': answer})    

def text_clean_view(request):
    answer = None
    
    if request.method == 'POST':
        form = TextCleanForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            clean_info = form.cleaned_data['clean_info']
            answer = TextClean(api_key, user_input, clean_info)
            
            return JsonResponse({'answer': answer })
    else:
        form = TextCleanForm()
        
    return render(request, 'Text_Clean.html', {'form': form, 'answer': answer})

def text_normalize_view(request):
    transformed_answer = None
    
    if request.method == 'POST':
        form = TextNormalizeForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            mode = form.cleaned_data['mode']
            transformed_answer = TextNormalize(api_key, user_input, mode)
            
            return JsonResponse({'transformed_answer': transformed_answer })
    else:
        form = TextNormalizeForm()
        
    return render(request, 'Text_Normalize.html', {'form': form, 'transformed_answer': transformed_answer})

def text_srl_view(request):
    srl_result = None

    if request.method == 'POST':
        form = TextSRLForm(request.POST)
        if form.is_valid():
            api_key = form.cleaned_data['api_key']
            user_input = form.cleaned_data['user_input']
            answer = TextSRL(api_key, user_input) 

            return JsonResponse({'srl_result': srl_result})
    else:
        form = TextSRLForm()

    return render(request, 'Text_SRL.html', {'form': form, 'srl_result': srl_result})

