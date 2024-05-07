from django.urls import path
from .views import *

urlpatterns = [
    path('text-translation/', translate_view, name='text-translation'),
    path('text-replace/', text_replace_view, name='text-replace'),
    path('text-correction/', text_correction_view, name='text-correction'),
    path('extract-patterns/', extract_pattern_view, name='extract-patterns'),
    path('detect-ner/', detect_ner_view, name='detect-ner'),
    path('text-summarize/', text_summarize_view, name='text-summarize'),
    path('text-qa/', text_qa_view, name='text-qa'),
    path('text-intent/', text_intent_view, name='text-intent'),
    path('text-lemstem/', text_lemstem_view, name='text-lemstem'),
    path('text-tokenize/', text_tokenize_view, name='text-tokenize'),
    path('text-embedd/', text_embedd_view, name='text-embedd'),
    path('text-generate/', text_generate_view, name='text-generate'),
    path('text-clean/', text_clean_view, name='text-clean'),
    path('text-normalize/', text_normalize_view, name='text-normalize'),
    path('text-srl/', text_srl_view, name='text-srl'),

    

    
    
    
    

]
