# first need to
# - get access to the bw-dev-datascience0 project (which has the translate api enabled)
# - generate the api key json file see [here](https://cloud.google.com/video-intelligence/docs/common/auth#set_up_a_service_account)
# - make sure the GOOGLE_APPLICATION_CREDENTIALS environmental variable is set to the path to the json file. 
# - install the google cloud modules on your distribution
# - run `gcloud auth login`


import six # needed for google.cloud translate
from google.cloud import translate
def translate_text(target, text):
    """Translates text into the target language.
    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    translate_client = translate.Client()
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(
        text, target_language=target)
    translated = result['translatedText']
    #print(u'Text: {}'.format(result['input']))
    #print(u'Translation: {}'.format(translated))
    #print(u'Source language: {}'.format(result['detectedSourceLanguage']))
    return(translated)

text = 'this is the text that i want translated into a foreign language'
lang = 'vi' # this is the language i want the text translated to
translate_text(lang, text)
