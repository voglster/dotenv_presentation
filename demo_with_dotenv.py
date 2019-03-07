from settings import config
import druidia

druidia.login(
  user=config.user,
  password=config.password
)

# breath all the perri-air your want!
druidia.open_planet()
