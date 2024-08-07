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
    user_input = forms.CharField(widget=forms.Textarea, label='Text to Correct')
   
    
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
    summary_length = forms.IntegerField(label='Summary-Length')

class TextQAForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    question = forms.CharField(label='Question')
    
class TextIntentForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')

class TextLemstemForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    task_type = forms.CharField(label='Task Type')
    
class TextTokenizeForm(forms. Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    
class TextEmbeddForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    task_type = forms.CharField(label='Task Type')

class TextGenerateForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    ans_length = forms.CharField(label='Answer Length')

# class DetectSpamForm(forms.Form):
#     api_key = forms.CharField(label='API Key')
#     user_input = forms.CharField(label='User Input')
#     num_classes = 

class TextCleanForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    clean_info = forms.CharField(label='Clean Info')

class TextNormalizeForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
    mode = forms.CharField(label= 'Mode')


class TextSRLForm(forms.Form):
    api_key = forms.CharField(label='API Key')
    user_input = forms.CharField(label='User Input')
   
   
 
    