# analiseJson

Projeto Django, DRF e REDIS que lê um arquivo JSON com 100 mil cadastros de usuários, aplica filtros analíticos e expõe os resultados via API RESTful.

## Funcionalidade

- Os dados são lidos do arquivo `usuarios.json`, armazenado em cache por 10 minutos.
- Todas as funções são cronometradas para retorno do tempo de execução.

## Arquivos principais

### `service.py`
- `openfile()`: Lê o JSON e armazena os dados no cache.
- `processingTime`: Decorador que mede o tempo de execução e retorna com timestamp.

### `filters.py`
Contém os filtros aplicados sobre os dados:

- `get_superusers()`: Retorna total de usuários com `score >= 900` e `ativo = true`.
- `top_countries()`: Retorna os 5 países com mais superusuários.
- `team_insights()`: Retorna total de membros, líderes, projetos concluídos e % de ativos por equipe.
- `active_users_per_day(request)`: Agrupa e filtra logins por data; aceita `?min=3000`.
- `evaluation()`: Placeholder para testes de retorno HTTP e performance.

### `views.py`
- Cada view chama um filtro e retorna:
  - Resultado
  - Tempo de execução
  - Timestamp

As views disponíveis são:
- `/superusers/`
- `/top-countries/`
- `/team-insights/`
- `/active-users-per-day/`

### `urls.py`
- Define as rotas usando `DefaultRouter` para os filtros acima.

