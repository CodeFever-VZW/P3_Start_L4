from bs4 import BeautifulSoup

navigatie_html = '''
<nav class="menu-drawer__navigation">
  <ul class="menu-drawer__menu has-submenu list-menu" role="list"><li><a href="/" class="menu-drawer__menu-item list-menu__item link link--text focus-inset menu-drawer__menu-item--active" aria-current="page">
            Home
          </a></li><li><a href="/collections/all" class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
            Producten
          </a></li><li><a href="/pages/faq" class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
            FAQ
          </a></li><li><a href="https://codefever.be" class="menu-drawer__menu-item list-menu__item link link--text focus-inset">
            CodeFever
          </a></li></ul>
</nav>
'''

soup = BeautifulSoup(navigatie_html, 'html.parser')

# Zoek alle a-tags in een nav-tag
links = soup.select('nav a')

for a in links:
    titel = a.text.strip()
    link = a['href']
    print(f"{titel}: {link}")
