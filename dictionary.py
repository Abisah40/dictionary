import requests
 
def dictionary(word):    
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{search}'
    params = {
        'word' : search
    }
    response = requests.get(url, params = params)
    #print(response)
    if response.status_code == 200:
        data = response.json()
        #print(data)
        for words in data:
            #print(words)
            try:
                latters = {
                    'word' : words['word'],
                    'phonetics' : words['phonetics'][0]['text'],
                    'partOfSpeech' : words['meanings'][0]['partOfSpeech'],
                    'meanings' : words['meanings'][0]['definitions'][0]['definition'],
                    'definition' : words['meanings'][0]['definitions'][0]['definition'],
                    'example' : words['meanings'][1]['definitions'][0]['example'],
                    'synonyms': words['meanings'][0]['definitions'][0]['synonyms'],
                    'antonyms': words['meanings'][0]['definitions'][0]['antonyms']
                }

                '''print the information below whenever 'example' is among the information provide by the dictionary'''
            
                if latters:
                    print(f'word : {words['word']}......')
                    print(f'phonetics : {words['phonetics'][0]['text']}')
                    print(f'part of speech : {words['meanings'][0]['partOfSpeech']}')
                    print(f'meanings : {words['meanings'][0]['definitions'][0]['definition']}')
                    print(f'definition : {words['meanings'][0]['definitions'][0]['definition']}')
                    print(f'synonyms : {words['meanings'][0]['definitions'][0]['synonyms']}')
                    print(f'antonyms : { words['meanings'][0]['definitions'][0]['antonyms']}')
                    print(f'example : {words['meanings'][1]['definitions'][0]['example']}')

                    '''print the information below whenever 'example' is not among the information provide by the dictionary'''
            except IndexError:
                #print(f'phonetics : {words['phonetics'][0]['text']}')
                print(f'word : {words['word']}')
                print(f'part of speech : {words['meanings'][0]['partOfSpeech']}')
                print(f'meanings : {words['meanings'][0]['definitions'][0]['definition']}')
                print(f'definition : {words['meanings'][0]['definitions'][0]['definition']}')


            except:
                    print(f'word : {words['word']}')
                    print(f'part of speech : {words['meanings'][0]['partOfSpeech']}')
                    print(f'meanings : {words['meanings'][0]['definitions'][0]['definition']}')
                    print(f'definition : {words['meanings'][0]['definitions'][0]['definition']}')
                    print(f'synonyms : {words['meanings'][0]['definitions'][0]['synonyms']}')
                    print(f'antonyms : { words['meanings'][0]['definitions'][0]['antonyms']}')
                    print(f'phonetics : {words['phonetics'][0]['text']}')

    else:
        print("Sorry, couldn't find definitions for the word you were looking for, You can try the web instead.")

search = input(('enter word: ').title()).strip()
dictionary(search)