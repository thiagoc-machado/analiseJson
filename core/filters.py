from .service import openfile, processingTime

@processingTime
def get_superusers():
    """
        Filtro: score >= 900 e active = true
        Retorna os dados e o tempo de processamento da requisição.
    """

    usuarios = openfile()
    superusers = [user for user in usuarios if user['score'] >= 900 and user['ativo']]

    return len(superusers)

@processingTime
def top_countries():
    """
        Agrupa os superusuários por país.
        Retorna os 5 países com maior número de superusuários.
    """
    usuarios = openfile()
    superusers = [user for user in usuarios if user['score'] >= 900 and user['ativo']]
    countries = {}

    for user in superusers:
        country = user['pais']
        if country in countries:
            countries[country] += 1
        else:
            countries[country] = 1

    sorted_countries = sorted(countries.items(), key=lambda x: x[1], reverse=True)
    top_5_countries = sorted_countries[:5]

    return top_5_countries

@processingTime
def team_insights():
    """
        Agrupa por team.name.
        Retorna: total de membros, líderes, projetos concluídos e % de membros ativos.
    """
    usuarios = openfile()
    teams = {}

    for user in usuarios:
        team_name = user['equipe']['nome']
        if team_name not in teams:
            teams[team_name] = {
                'total_members': 0,
                'leaders': 0,
                'completed_projects': 0,
                'active_members': 0,
                'active_percentage': 0
            }
        teams[team_name]['total_members'] += 1
        if user['equipe']['lider']:
            teams[team_name]['leaders'] += 1
        if any(p['concluido'] for p in user['equipe']['projetos']):
            teams[team_name]['completed_projects'] += 1
        if user['ativo']:
            teams[team_name]['active_members'] += 1
        teams[team_name]['active_percentage'] = round((teams[team_name]['active_members'] / teams[team_name]['total_members']) * 100, 2)

    return teams

@processingTime
def active_users_per_day(request=None):
    """
        Conta quantos logins aconteceram por data.
        Query param opcional: ?min=3000 para filtrar dias com pelo menos 3.000 logins.
        Retorna: data, total de logins, % de logins ativos.
    """
    usuarios = openfile()
    logins = {}

    for user in usuarios:
        for log in user.get('logs', []):
            if log['acao'] == 'login':
                login_date = log['data']
                if login_date not in logins:
                    logins[login_date] = {
                        'total_logins': 0,
                        'active_logins': 0
                    }
                logins[login_date]['total_logins'] += 1
                if user['ativo']:
                    logins[login_date]['active_logins'] += 1

    # Calcula % de logins ativos
    for date, data in logins.items():
        data['active_percentage'] = round((data['active_logins'] / data['total_logins']) * 100, 2)

    # Filtro opcional ?min=valor
    min_value = 0
    if request:
        query_params = request.GET
        min_param = query_params.get('min')
        if min_param and min_param.isdigit():
            min_value = int(min_param)

    # Aplica o filtro
    filtered_logins = {
        date: data for date, data in logins.items()
        if data['total_logins'] >= min_value
    }

    return filtered_logins

@processingTime
def evaluation():
    """
        Se o status retornado é 200
        O tempo em milisegundos de resposta
        Se o retorno é um JSON válido
    """
    ...
    return