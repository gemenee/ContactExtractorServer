import sys
from app.Extractor import person

sys.path.insert(0, '../../..')

gnc = person.gnc_relation()
tokenizer = person.MorphTokenizer().add_rules(person.EMAIL_RULE, person.PHONE_RULE)
org_names = person.fill_synonyms(person.ORG_NAMES)
parser = person.Parser(person.PERSON, tokenizer)

testText = '''Заместитель начальника организационно-экономического отдела управления Пенсионного фонда Иван Семенович Гостюхин (+71234567890, i.s.gostiuhin@gmail.com).
Оперативный сотрудник 3 отдела полиции Злыбин О.П. (89876543210).
Преподаватель Пензенского государственного университета Замутин Георгий Сергеевич (+71029384756).
Антонов Григорий Васильевич (+71134567890, gvantonov@mail.ru)'''


def extract_facts(text):
    text = text.replace('(', '')
    text = text.replace(')', '')
    #text = text.replace('использует телефоный номер', '')
    #text = text.replace(' телефон', '')
    # pr = cProfile.Profile()
    # pr.enable()
    persons = []
    for match in parser.findall(text):
        persons.append(match.fact)
    # pr.disable    # original_stdout = sys.stdout  # Save a reference to the original standard output
    # with open('result.txt', 'w') as f:
    #     sys.stdout = f  # Change the standard output to the file we created.
    #         print(match)
    #     sys.stdout = original_stdout  # Reset the standard output to its original value()
    # after your program ends
    original_stdout = sys.stdout
    # with open('../../CorpusReader/dump.txt', 'w') as dump:
    #     sys.stdout = dump
    #     pr.print_stats(sort="calls")
    #     sys.stdout = original_stdout
    return persons


# print(persons)

def save_facts(facts):
    original_stdout = sys.stdout  # Save a reference to the original standard output
    with open('../../CorpusReader/result.txt', 'w') as f:
        sys.stdout = f  # Change the standard output to the file we created.
        for f in facts:
            print(f.contacts.phone)
        sys.stdout = original_stdout  # Reset the standard output to its original value



def print_facts(facts):
    for fact in facts:
        print(fact)


# text = '''заместитель начальника организационно-экономического отдела управления Пенсионного фонда Иван Семенович Гостюхин (+71234567890, i.s.gostiuhin@gmail.com)
# Оперативный сотрудник 3 отдела полиции Злобин О.П. (89876543210)
# Преподаватель Пензенского государственного университета Замотин Георгий Сергеевич (+71029384756).
# Григорий Васильевич Антонов (+71134567890, gvantonov@mail.ru)'''

jsonnFacts = []

testText2 = '''Иван Семенович Гостюхин  +71234567890  i.s.gostiuhin@gmail.com  - заместитель начальника организационно-экономического отдела управления Пенсионного фонда.  Оперативный сотрудник 3 отдела полиции Злобин О.П.  89876543210   Преподаватель Пензенского государственного университета Тюрин Глеб Евгеньевич  +71029384756 .  +71134567890  gvantonov@mail.ru Максимов Николай Валентинович +71134567890  gvantonov@mail.ru   Марина Евгеньевна Ростоцкая  директор Детского музыкального театра  Ромашка   телефон +380487297933  romashka@mail.ru.  '''

facts = extract_facts(testText2)
for fact in facts:
    jsonnFacts.append(fact.as_json)

print_facts(jsonnFacts)
# save_facts(facts)
