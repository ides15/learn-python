from collections import ChainMap
from pprint import pprint

defaults = {
    'theme': 'Default',
    'language': 'eng',
    'showIndex': True,
    'showFooter': True
}

default_settings = ChainMap(defaults)
# pprint(default_settings)

user_settings = default_settings.new_child({
    'theme': 'Bluesky',
    'language': 'fr'
})
# pprint(user_settings)

# print(user_settings['theme'])

# print(user_settings.pop('theme'))

# print(user_settings['theme'])

user_settings.maps[0] = {
    'theme': 'desert',
    'showIndex': False
}
# pprint(user_settings)

# pprint(user_settings.parents)
user_settings_2 = user_settings.new_child({
    'theme': 'Dark',
    'language': 'fr'
})

pprint(user_settings)
pprint(user_settings_2)
user_settings_2.pop('theme')
print(user_settings_2['theme'])
pprint(user_settings_2)

# print(user_settings['showIndex'])