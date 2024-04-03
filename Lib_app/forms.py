from django import forms

class TranslationForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    target_lang = forms.CharField(label='Target Language')
    
class TextReplacementForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    replacement_rules = forms.CharField(label='Replacement Rules')

class TextCorrectionForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    
class ExtractPatternForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    patterns = forms.CharField(label='Patterns')
    
class DetectNERForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    ner_tags = forms.CharField(label='NER-Tags')
    
class TextSummarizeForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    summary_length = forms.CharField(label='Summary-Length')

class TextQAForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    question = forms.CharField(label='Question')
    
class TextIntentForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')


    
 
    