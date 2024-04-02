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
    
    
      
]
