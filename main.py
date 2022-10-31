from dotenv import load_dotenv
import os
import json
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, CategoriesOptions, ConceptsOptions, EmotionOptions

load_dotenv()
authenticator = IAMAuthenticator(os.environ["apikey"])
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2022-04-07',
    authenticator=authenticator
)
natural_language_understanding.set_service_url(os.environ["url"])
response = natural_language_understanding.analyze(
    text='IBM is an American multinational technology company '
    'headquartered in Armonk, New York, United States, '
    'with operations in over 170 countries.',
    features=Features(categories=CategoriesOptions(limit=3), concepts=ConceptsOptions(limit=3), emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))
