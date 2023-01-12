import json
json_file = 'candidates.json'

# Функции

def load_candidates(file):
    '''чтение json файла'''
    with open(file, encoding='utf8') as candidates_list:
        return json.load(candidates_list)


def get_alls(file):
    '''Возвращает необработанный список кандидатов'''
    return load_candidates(file)



def get_by_pk(pk, candidates_list):
    '''Вернёт кандидата по номеру'''
    for candidate in candidates_list:
        if int(pk) == int(candidate['id']):
            return candidate
    return 'Такого номера нет'


def get_by_skill(skill_name, candidates_list):
    '''Возвращает кандидатов по навыку'''
    candidates_with_skills = []
    for candidatе in candidates_list:
        if skill_name.lower() in candidatе['skills'].lower():
            candidates_with_skills.append(candidatе)
    return candidates_with_skills


def get_by_name(name, candidates_list):
    '''Возвращает кандидатов по имени'''
    candidates_with_name = []
    for candidate in candidates_list:
        if name.lower() in candidate['name'].lower():
            candidates_with_name.append(candidate)
    return candidates_with_name

