import re
import numpy as np
import translators as ts


def map_labels(labels):
    ''' This function takes a list of bank labels and returns a dictionary of bank groups
    that maps each label to its corresponding bank group.
    - labels: list of bank labels
    - returns: dictionary of bank groups
    '''

    # define regex patterns for the different banks
    agricole_regex = '(agricole)'
    bmce_regex = '(bmce|africa)'
    barid_regex = '(barid|بريد)'
    tijari_regex = '(tijari|wafa|تجاري|وفا)'
    chaabi_regex = '(chaabi|populaire|شعبي)'
    cih_regex = '(cih)'
    akhdar_regex = '(akhdar|أخضر)'
    citi_regex = '(citi)'
    assafa_regex = '(safa|صفا)'
    cfg_regex = '(cfg)'
    yousr_regex = '(yousr|يسر)'
    umnia_regex = '(umnia|umb|أمنية)'
    credits_regex = '(cr[ée]dit|قرض)'
    ste_regex = '(g[ée]n[ée]rale|عامة)'
    bmci_regex = '(bmci)'

    # create a dictionary that maps each bank label to its corresponding bank
    bank_dict = {}
    for label in labels:
        if re.search(bmce_regex, label, re.IGNORECASE):
            bank_dict[label] = 'BMCE Group'
        elif re.search(barid_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Barid Bank'
        elif re.search(tijari_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Attijariwafa Bank'
        elif re.search(chaabi_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Banque Populaire'
        elif re.search(cih_regex, label, re.IGNORECASE):
            bank_dict[label] = 'CIH Bank'
        elif re.search(akhdar_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Al Akhdar Bank'
        elif re.search(citi_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Citi Bank'
        elif re.search(assafa_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Assafa Bank'
        elif re.search(cfg_regex, label, re.IGNORECASE):
            bank_dict[label] = 'CFG Bank'
        elif re.search(yousr_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Yousr Bank'
        elif re.search(umnia_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Umnia Bank'
        elif re.search(agricole_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Credit Agricole'
        elif re.search(credits_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Crédit du Maroc'
        elif re.search(ste_regex, label, re.IGNORECASE):
            bank_dict[label] = 'Société Générale'
        elif re.search(bmci_regex, label, re.IGNORECASE):
            bank_dict[label] = 'BMCI'
        else:
            bank_dict[label] = 'unknown'
    return bank_dict


def translate(ser, translator='google'):
    """
    Translates a pandas series of text using the specified translator.

    Args:
        ser (pandas.Series): The series containing the text to be translated.
        translator (str, optional): The translator service to be used (default is 'google').

    Returns:
        pandas.Series: The translated series.

    """
    trans_ser = []
    for idx, text in enumerate(ser):
        try:
            trans_text = ts.translate_text(text, translator=translator, from_language='fr', to_language='en')
            trans_ser.append(trans_text)
        except:
            trans_ser.append(np.nan)
    return trans_ser
