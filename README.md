
<h1 align='center'> Series-Finder</h1>

<p align="center">
  <a href="https://www.django-rest-framework.org" target="blank"><img src="https://storage.caktusgroup.com/media/blog-images/drf-logo2.png" width="200" alt="Django Logo" /></a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white"/>
  <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>
  <img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"/>
  <img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white"/>
</p>

Essa é uma API de séries que foi construída utilizando Django Rest Framework. Ela permite que você acesse informações sobre séries, temporadas, episódios, gêneros e plataformas de streaming. A API pode ser acessada online <a href="https://series-finder.onrender.com">AQUI</a>.

</p>

<h2>Endpoints</h2>

A API possui os seguintes endpoints:

- `/platforms/`: Retorna a lista de todas as plataformas de streaming disponíveis.
- `/platforms/<id>/`: Retorna os detalhes de uma plataforma específica.
- `/platforms/<id>/series_list/`: Retorna a lista de todas as séries disponíveis em uma plataforma específica.
- `/genders/`: Retorna a lista de todos os gêneros disponíveis.
- `/genders/<id>/`: Retorna os detalhes de um gênero específico.
- `/genders/<id>/series_list/`: Retorna a lista de todas as séries disponíveis em um gênero específico.
- `/series/`: Retorna a lista de todas as séries disponíveis.
- `/series/<id>/`: Retorna os detalhes de uma série específica.
- `/series/<id>/seasons_list/`: Retorna a lista de todas as temporadas disponíveis de uma série específica.
- `/series/<id>/episodes_list/`: Retorna a lista de todos os episódios disponíveis de uma série específica.
- `/seasons/`: Retorna a lista de todas as temporadas disponíveis no sistema independente da série.
- `/seasons/<id>/`: Retorna os detalhes de uma temporada específica.
- `/seasons/<id>/episodes_list/`: Retorna a lista de todos os episódios disponíveis de uma temporada específica.
- `/episodes/`: Retorna a lista de todos os episódios disponíveis.
- `/episodes/<id>/`: Retorna os detalhes de um episódio específico.


<h1>Licença</h1>

<p>Este projeto é licenciado sob a Licença MIT - veja o arquivo <a href="https://github.com/mts-lucas/series-finder/blob/main/LICENSE">LICENSE</a> para mais detalhes.</p>


