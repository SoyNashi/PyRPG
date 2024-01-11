import os
import random
import bullet
import colorama
from deep_translator import GoogleTranslator
colorama.init()

# ======================================================================
# =================       Variables            =========================
# ======================================================================

start_a = 0
class_result = 0 

life_max = 0
life_max_temp = 0
life = 0
mana_max = 0
mana_max_temp = 0
mana = 0
atac = 0

end_life = 0
end_mana = 0
end_atac = 0

e_life_max = 100
e_life = 100
e_mana_max = 100
e_mana = 100
e_atac = 10

life_potion = 10
mana_potion = 10
e_life_potion = 6
e_mana_potion = 10

line_life = 0
line_mana = 0
line_e_life = 0
line_0 = "▒▒▒▒▒▒▒▒▒▒"
line_10 = "█▒▒▒▒▒▒▒▒▒"
line_20 = "██▒▒▒▒▒▒▒▒" 
line_30 = "███▒▒▒▒▒▒▒" 
line_40 = "████▒▒▒▒▒▒" 
line_50 = "█████▒▒▒▒▒" 
line_60 = "██████▒▒▒▒" 
line_70 = "███████▒▒▒" 
line_80 = "████████▒▒" 
line_90 = "█████████▒" 
line_100 = "██████████" 

potion_line_mana = "🧪"
potion_line_life = "💉"

rondas = 0

ne_weapon_old = 0
ne_armor_old = 0
ne_casco_old = 0
ne_weapon_old_temp = 0
ne_armor_old_temp = 0
ne_casco_old_temp= 0

dmgtotal = 0
healtotal = 0
manatotal = 0
resmanatotal = 0
e_dmgtotal = 0
e_healtotal = 0
e_manatotal = 0
e_resmanatotal = 0

lang = "en"

list_weapon = ["Excalibur", "Blade of Shadows", "Thunderstrike", "Frostbite", "Sword of the Elders", "Bow of Essence", "Lance of Destiny", "Axe of Valor", "Sword of Light", "Bow of the Serpent", "Lance of the Titan", "Machete of the Ancients", "Ironclad Sword", "Steelbow", "Lance of the Sea", "Machete of Fury", "Dwarven Blade", "Skyward Bow", "Lance of the Abyss", "Machete of Chaos", "Adamantine Sword", "Arcane Bow", "Lance of Spectres", "Machete of the Void", "Ruby Sword", "Emerald Bow", "Lance of Justice", "Machete of Legends", "Crimson Blade", "Silver Bow", "Lance of Kings", "Machete of Storms", "Vorpal Sword", "Ivory Bow", "Lance of Hope", "Machete of Radiance", "Ethereal Blade", "Phoenix Bow", "Lance of Salvation", "Machete of Wisdom", "Onyx Blade", "Eclipse Bow", "Lance of Illusion", "Machete of Truth", "Demonsbane Sword", "Soulfire Bow", "Lance of Redemption", "Machete of Destiny", "Seraphic Blade", "Stellar Bow", "Lance of Eternity", "Machete of Infinity"]
list_armor = ["Power Armor", "Dragonplate Armor", "Daedric Armor", "T-51b Power Armor", "X-01 Power Armor", "Scorched Sierra Power Armor", "Lorenzos Suit", "Framework", "Raider Power Armor", "T-45 power armor", "Leather Armor", "Combat Armor", "Metal Armor", "Robocoat", "Tribal Power Armor", "Mistress of Mystery Armor", "Bone Armor", "Wood Armor", "Bamboo Armor", "Levantadoras de minerales", "Fencing Armor", "Knight Armor", "Crystal Armor", "Battle Armor", "Miner Gear", "Gold Armor", "Space Armor", "Plastic Armor", "Manta Armor", "Steel Armor", "Sophie Suit", "Rubber Armor", "McGill Armor", "Carbon armor", "Cornerstone Armor", "Sirje Armor", "Tatata Armor", "Zerog Armor", "Byte Armor", "Wreck Armor", "Ardent Armor", "Crystal Armor", "Canary Armor", "Pebbled Armor", "Tomorrow Armor", "Tyles Armor", "Golden Armor", "Warrior Armor", "Titanium Armor", "Rusty Armor", "Cave Armor"]
list_helmets = ["Amulet of Strength", "Necklace of Wisdom", "Pendant of Power", "Charm of Courage", "Talisman of Agility", "Crystal Choker", "Pendant of the Elements", "Ruby Amulet", "Emerald Necklace", "Sapphire Pendant", "Diamond Choker", "Necklace of the Serpent", "Lunar Locket", "Necklace of the Abyss", "Pendant of Destiny", "Glowing Talisman", "Necklace of Radiance", "Amulet of the Ancients", "Necklace of the Void", "Onyx Choker", "Ethereal Pendant", "Celestial Charm", "Necklace of the Titans", "Choker of Eternity", "Phoenix Amulet", "Serpentine Locket"]
magic_creatures = ["Bigfoot", "Sasquatch", "Wendigo", "Thunderbird", "Chupacabra", "Jersey Devil", "Goblin", "Orc", "Troll", "Dragon", "Unicorn", "Phoenix", "Cerberus", "Nymph", "Banshee", "Griffin", "Sphinx", "Giant", "Gorgon", "Minotaur", "Giant Spider", "Werewolf", "Vampire", "Golem", "Kraken", "Siren", "Centaur", "Mermaid", "Chimera", "Fairy", "Tengu", "Yeti", "Hydra", "Cyclops", "Pegasus", "Salamander", "Harpy", "Medusa", "Chimera"]



frases = [
  "Hola, ¿cómo estás?",
  "El cielo está despejado hoy",
  "No te preocupes, todo estará bien",
  "La vida es un viaje, no un destino",
  "Nunca es tarde para empezar de nuevo",
  "La creatividad es contagiosa, pásala", 
  "El tiempo es el más sabio de todos los consejeros",
  "La vida es lo que pasa mientras estás ocupado haciendo otros planes",
  "La práctica hace al maestro",
  "La vida es dura, pero la práctica es fuerte",
  "Haz el bien sin mirar a quien",
  "Sé el cambio que quieres ver en el mundo",
  "Mantén la calma y sigue adelante",
  "La vida es un juego, ¡no te rindas!",
  "La vida es dura, pero la felicidad es infinita",
  "La vida es corta, pero el arte es largo",
  "La suerte favorece a la mente preparada",
  "La vida es corta, pero el dinero es barato",
  "La vida es corta, pero el trabajo es duro",
  "Si quieres paz, prepárate para la guerra",
  "No dejes que tus miedos tomen el lugar de tus sueños",
  "La verdad os hará libres",
  "El que siembra vientos, recoge tempestades",
  "ruben apruebame",
  "La esperanza es el peor de los males, pues prolonga el tormento del hombre",
  "Si tienes un porqué para vivir, soportarás cualquier cómo",
  "Que fluya lo que tenga que fluyir y que se vaya lo que tenga que vayarse"
]
winimg = [
  "─────────────────────────────▄██▄\n─────────────────────────────▀███\n────────────────────────────────█\n───────────────▄▄▄▄▄────────────█\n──────────────▀▄────▀▄──────────█\n──────────▄▀▀▀▄─█▄▄▄▄█▄▄─▄▀▀▀▄──█\n─────────█──▄──█────────█───▄─█─█\n─────────▀▄───▄▀────────▀▄───▄▀─█\n──────────█▀▀▀────────────▀▀▀─█─█\n──────────█───────────────────█─█\n▄▀▄▄▀▄────█──▄█▀█▀█▀█▀█▀█▄────█─█\n█▒▒▒▒█────█──█████████████▄───█─█\n█▒▒▒▒█────█──██████████████▄──█─█\n█▒▒▒▒█────█───██████████████▄─█─█\n█▒▒▒▒█────█────██████████████─█─█\n█▒▒▒▒█────█───██████████████▀─█─█\n█▒▒▒▒█───██───██████████████──█─█\n▀████▀──██▀█──█████████████▀──█▄█\n──██───██──▀█──█▄█▄█▄█▄█▄█▀──▄█▀\n──██──██────▀█─────────────▄▀▓█\n──██─██──────▀█▀▄▄▄▄▄▄▄▄▄▀▀▓▓▓█\n──████────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n──███─────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n──██──────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n──██──────────█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n──██─────────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n──██────────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█\n──██───────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌\n──██──────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌\n──██─────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌\n──██────▐█▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█▌", "───────────────────────────────────────\n───▐▀▄───────▄▀▌───▄▄▄▄▄▄▄─────────────\n───▌▒▒▀▄▄▄▄▄▀▒▒▐▄▀▀▒██▒██▒▀▀▄──────────\n──▐▒▒▒▒▀▒▀▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄────────\n──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▒▒▒▒▒▒▒▒▒▒▒▒▀▄──────\n▀█▒▒▒█▌▒▒█▒▒▐█▒▒▒▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────\n▀▌▒▒▒▒▒▒▀▒▀▒▒▒▒▒▒▀▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐───▄▄\n▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌▄█▒█\n▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▒█▀─\n▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█▀───\n▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌────\n─▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────\n─▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▌─────\n──▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐─────\n──▐▄▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▄▌──────\n────▀▄▄▀▀▀▀▀▄▄▀▀▀▀▀▀▀▄▄▀▀▀▀▀▄▄▀────────", "┼┼▓▓▓▓▓▓▓▓\n┼┼┼▓░░▓░░▓┼┼┼▒\n┼┼┼▓░░▓░░▓┼┼┼▒\n┼┼┼▓░░▓░░▓▓┼┼▒\n┼┼┼▓░░▓░░░▓┼┼▒\n┼┼┼▓░░▓░░░▓┼┼▒\n┼┼▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓\n┼▓▓███▓▓▒▒▓████▓▓\n┼┼█████▓▓▒▓▓▓▓▓▓▓▓\n┼███▒███▓▒▓▓▓▓▓▓▓▓\n┼██▒▒▒██▓▓▓▓▓▓██▓▓\n┼███▒███┼┼┼┼┼█▒▒█\n┼┼█████┼┼┼┼┼┼█▒▒█\n┼┼┼███┼┼┼┼┼┼┼┼██ \n"
]

# ======================================================================
# =================       Funciones            =========================
# ======================================================================

def topgui():
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  global life, mana, e_life, e_mana, line_life, line_mana, line_e_life
  global line_e_mana, life_max, mana_max, e_life_max, e_mana_max
  global mana_potion, life_potion, line_potion, rondas

  if  life == (life_max * 0):
    line_life = line_0 + " ❤ "
  elif life <= (life_max * 0.1):
    line_life = line_10 + " ❤ "
  elif life <= (life_max * 0.2):
    line_life = line_20 + " ❤ "
  elif life <= (life_max * 0.3):
    line_life = line_30 + " ❤ "
  elif life <= (life_max * 0.4):
    line_life = line_40 + " ❤ "
  elif life <= (life_max * 0.5):
    line_life = line_50 + " ❤ "
  elif life <= (life_max * 0.6):
    line_life = line_60 + " ❤ "
  elif life <= (life_max * 0.7):
    line_life = line_70 + " ❤ "
  elif life <= (life_max * 0.8):
    line_life = line_80 + " ❤ "
  elif life <= (life_max * 0.9):
    line_life = line_90 + " ❤ "
  elif life <= (life_max * 1):
    line_life = line_100 + " ❤ "

  if mana <= (mana_max * 0):
    line_mana = line_0 + " ⚡"
  elif mana <= (mana_max * 0.1):
    line_mana = line_10 + " ⚡"
  elif mana <= (mana_max * 0.2):
    line_mana = line_20 + " ⚡"
  elif mana <= (mana_max * 0.3):
    line_mana = line_30 + " ⚡"
  elif mana <= (mana_max * 0.4):
    line_mana = line_40 + " ⚡"
  elif mana <= (mana_max * 0.5):
    line_mana = line_50 + " ⚡"
  elif mana <= (mana_max * 0.6):
    line_mana = line_60 + " ⚡"
  elif mana <= (mana_max * 0.7):
    line_mana = line_70 + " ⚡"
  elif mana <= (mana_max * 0.8):
    line_mana = line_80 + " ⚡"
  elif mana <= (mana_max * 0.9):
    line_mana = line_90 + " ⚡"
  elif mana <= (mana_max * 1):
    line_mana = line_100   + " ⚡"

  if e_life <= (e_life_max * 0):
    line_e_life = line_0 + " 🔥"
  elif e_life <= (e_life_max * 0.1):
    line_e_life = line_10 + " 🔥"
  elif e_life <= (e_life_max * 0.2):
    line_e_life = line_20 + " 🔥"
  elif e_life <= (e_life_max * 0.3):
    line_e_life = line_30 + " 🔥"
  elif e_life <= (e_life_max * 0.4):
    line_e_life = line_40 + " 🔥"
  elif e_life <= (e_life_max * 0.5):
    line_e_life = line_50 + " 🔥"
  elif e_life <= (e_life_max * 0.6):
    line_e_life = line_60 + " 🔥"
  elif e_life <= (e_life_max * 0.7):
    line_e_life = line_70 + " 🔥"
  elif e_life <= (e_life_max * 0.8):
    line_e_life = line_80 + " 🔥"
  elif e_life <= (e_life_max * 0.9):
    line_e_life = line_90 + " 🔥"
  elif e_life <= (e_life_max * 1):
    line_e_life = line_100 + " 🔥"
  mana_max = mana_max_temp 
  life_max = life_max_temp
  if mana_potion > 20:
    mana_potion = 20
  if life_potion > 20:
    life_potion = 20


  datos = [
    {
        "nombre": colorama.Fore.BLUE + str(line_mana),
        "promedio": "{:.0f}".format(mana) + " / " + "{:.0f}".format(mana_max),
        "potion": str(potion_line_mana * mana_potion),
    },
    {
      "nombre": colorama.Fore.LIGHTGREEN_EX + str(line_life),
      "promedio": "" + "{:.0f}".format(life) + " / " + "{:.0f}".format(life_max),
      "potion": str(potion_line_life * life_potion),
    },
    {
      "nombre": colorama.Fore.RED + str(line_e_life),
      "promedio": "{:.0f}".format(e_life) + " / " + "{:.0f}".format(e_life_max),
      "potion": str(colorama.Fore.WHITE + traductor.translate("Rondas") + colorama.Fore.GREEN + colorama.Style.BRIGHT + str(rondas)),
    },
  ]

  print(colorama.Fore.WHITE + "╔═══════════════════════════════════╗")
  print(colorama.Fore.WHITE + "╠════════" + colorama.Fore.MAGENTA + "█▀█ █▄█" + colorama.Fore.RED + " █▀█ █▀█ █▀▀" + colorama.Fore.WHITE + "════════╣")
  print(colorama.Fore.WHITE + "╠════════" + colorama.Fore.LIGHTMAGENTA_EX + "█▀▀ ░█░" + colorama.Fore.LIGHTRED_EX + " █▀▄ █▀▀ █▄█" + colorama.Fore.WHITE + "════════╣")
  print(colorama.Fore.WHITE + "╠═══════════════════════════════════╝")
  for dato in datos:
    nombre = dato["nombre"]
    promedio = dato["promedio"]
    potion = dato["potion"]
    cadena = colorama.Fore.WHITE + "╠{:<10} {:<30} {:>10}".format(nombre, promedio, potion)
    print(cadena)
  print(colorama.Fore.WHITE + "╚══════════════════════════════════╝")
# accion pocion de vida
def life_potion_act():
  global life, life_potion, healtotal
  life += (life_max * 0.38)
  life_potion -= 1
  healtotal += (life_max * 0.38)
  if life > life_max:
    life = life_max 
# accion pocion de mana
def mana_potion_act():
  global mana, mana_potion, resmanatotal
  mana += (mana_max * 0.25)
  resmanatotal += (mana_max * 0.25)
  mana_potion -= 1
  if mana > mana_max:
    mana = mana_max 
# accion pocion de vida enemigo
def e_life_potion_act():
  global e_life, e_life_potion, e_healtotal
  e_life += (e_life * 0.17) 
  e_life_potion -= 1
  e_healtotal += (e_life * 0.17)
  if e_life > e_life_max:
    e_life = e_life_max 
# accion pocion de mana enemigo
def e_mana_potion_act():
  global e_mana, e_mana_potion, e_resmanatotal
  e_mana += (e_mana_max * 0.2)
  e_mana_potion -= 1
  e_resmanatotal += (e_mana_max * 0.2)
  if e_mana > e_mana_max:
    e_mana = e_mana_max 
# (body) Accion de ataque del jugador
def player_act_def():
  # open the sample file used
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  act_1 = 1
  while act_1 == 1:
    surrender()
    topgui()
    global mana, life, e_life, dmgtotal, manatotal
    player_act = bullet.Bullet(
      prompt = traductor.translate("\nElije accion:") ,
      choices = [traductor.translate("Atacar"), traductor.translate("Curar"), traductor.translate("Restaurar mana")],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
      return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == (traductor.translate("Atacar"), 0) and mana >= 10:
      mana -= 10
      e_life -= atac
      dmgtotal += atac
      manatotal += 10
      act_1 = 0
    elif player_act_result == (traductor.translate("Curar"), 1) and life_potion >= 1:
      life_potion_act()
      act_1 = 0
    elif player_act_result == (traductor.translate("Restaurar mana"), 2) and mana_potion >= 1:
      mana_potion_act()
      act_1 = 0
    else:
      act_1 = 1
    os.system("clear")
  os.system("clear") 
# ataque del npc
def npc_act():
  global e_life, e_mana, life, mana, e_life_max, e_mana_max, life_max, mana_max, e_manatotal
  global e_life_potion, e_mana_potion, life_potion, mana_potion, e_atac, e_dmgtotal
  global e_resmanatotal

  # si e_life < life i e_life > (e_lifemax 50%) = curar
  # si elife > life i emana > (emanamax 30%) = atacar
  # si emana > (emanamax 30%) = restaurar mana

  if e_mana <= (e_mana_max * 0.3) and e_mana_potion != 0 :
    e_mana_potion_act()
  elif e_life < life and e_life < (e_life_max * 0.5):
    e_life_potion_act()
    life -= (e_atac * 0.5)
    e_mana -= 10
    e_dmgtotal += e_atac
    e_manatotal += 10
  elif e_mana > (e_mana_max * 0.3):
    life -= e_atac
    e_mana -= 10
    e_dmgtotal += e_atac
    e_manatotal += 10
  elif e_mana <= (e_mana_max * 0.3) and e_mana_potion == 0 :
    e_mana_potion = 1
# restauracion de vida del npc y mejora de sus habilidades
def npc_dead():
  global e_life, e_life_max, e_mana, e_mana_max, e_life_potion, e_mana_potion, e_atac
  npcdead = random.randint(1,3)
  if npcdead == 1:
    e_atac = int(e_atac + 5) 
  elif npcdead == 2:
    e_mana_max += int(e_mana_max * 0.1)  
  elif npcdead == 3:
    e_life_max += int(e_life_max * 0.1)
  e_life_max = int(e_life_max + (e_life_max * 0.1))
  e_mana_max = int(e_mana_max + (e_mana_max * 0.1))
  e_atac = int(e_atac + (e_atac * 0.2))
  e_life = e_life_max
  e_mana = e_mana_max
  e_life_potion = 10
  e_mana_potion = 10 
# (WIN) mensaje, selector de mejoras i restauracion 
  
def player_win():
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  global life, mana, mana_potion, life_potion, mana_max, life_max, atac
  global life, mana, life_potion, mana_potion, mana_max, life_max, atac
  global mana_max_temp, life_max_temp, rondas, winimg
  global ne_weapon_old, ne_armor_old, ne_casco_old, ne_weapon_old_temp, ne_armor_old_temp, ne_casco_old_temp

  rondas += 1
  os.system("clear")
  print(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT)
  print(random.choice(winimg))
  print("██╗░░██╗░█████╗░░██████╗  ░██████╗░░█████╗░███╗░░██╗░█████╗░██████╗░░█████╗░")
  print("██║░░██║██╔══██╗██╔════╝  ██╔════╝░██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗")
  print("███████║███████║╚█████╗░  ██║░░██╗░███████║██╔██╗██║███████║██║░░██║██║░░██║")
  print("██╔══██║██╔══██║░╚═══██╗  ██║░░╚██╗██╔══██║██║╚████║██╔══██║██║░░██║██║░░██║")
  print("██║░░██║██║░░██║██████╔╝  ╚██████╔╝██║░░██║██║░╚███║██║░░██║██████╔╝╚█████╔╝")
  print("╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░░╚════╝░")
  print(traductor.translate("Se te ha curado un +50%"))
  print(colorama.Fore.RESET + colorama.Style.NORMAL + traductor.translate("Has conseguido un cofre"))
  win = bullet.Bullet(
    prompt = traductor.translate("\nEscoje tu premio: "),
    choices = [ traductor.translate("mas ataque"), traductor.translate("mas mana"), traductor.translate("mas vida")],
    indent = 0,
    align = 5, 
    margin = 2,
    shift = 0,
    bullet = "",
    pad_right = 5,
    return_index = True
  )
  win_result = win.launch()
  if win_result == (traductor.translate('mas ataque'), 0):
    atac = int(atac + 5) 
  elif win_result == (traductor.translate('mas mana'), 1):
    mana_max = int(mana_max * 1.1)  # Increase by 10%
  elif win_result == (traductor.translate('mas vida'), 2):
    life_max = int(life_max * 1.1)  # Increase by 10%
  mana += mana_max * 0.8
  life += life_max * 0.89
  mana_max_temp = mana_max
  life_max_temp = life_max
  if life > life_max:
    life = life_max
  if mana > mana_max:
    mana = mana_max 
  os.system("clear")

  global list_armor, list_weapon, list_helmets, magic_creatures

  nombre_enemigo = random.choice(magic_creatures)
  print(colorama.Fore.BLUE + traductor.translate("Bienvenido a la nueva sala. Te enfrentarás a un ") + colorama.Fore.LIGHTRED_EX + str(nombre_enemigo) + colorama.Fore.BLUE + traductor.translate(" con ") + str(e_life) + traductor.translate(" puntos de vida") + colorama.Fore.RESET)  

  mana_max = int(mana_max)
  life_max = int(life_max)
  ne_casco_old = 0
  ne_weapon_old = 0
  ne_armadura_old = 0
  ne_casco = colorama.Fore.BLUE + random.choice(list_helmets)
  ne_armadura = colorama.Fore.LIGHTGREEN_EX + random.choice(list_armor)
  ne_arma = colorama.Fore.CYAN + random.choice(list_weapon)
  ne_1 = random.randint(1, 3)
  ne = bullet.Bullet(
    prompt = traductor.translate("\nEscoje tu Arma: "),
    choices = [str(ne_armadura), str(ne_casco), str(ne_arma), traductor.translate("No necesito arma")],
    indent = 0,
    align = 5, 
    margin = 2,
    shift = 0,
    bullet = "",
    pad_right = 5,
    return_index = True
  )
  ne_result = ne.launch()

  if ne_result == (str(ne_armadura), 0):
    os.system("clear")
    ne_armor_res_val = random.randint(5 , 50)
    print(traductor.translate("Tu armadura es:") + " " + colorama.Fore.MAGENTA + str(ne_armadura))
    print(colorama.Fore.RESET + traductor.translate("Este armadura te dará") + " " + colorama.Fore.MAGENTA + str(ne_armor_res_val) + " " + colorama.Fore.RESET + traductor.translate("de vida"))

    ne_armor_quest = bullet.Bullet(
      prompt = traductor.translate("\nQuieres cambiar: "),
      choices = [traductor.translate("si"), traductor.translate("no")],
      indent = 0,
      align = 5,
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
      return_index = True
      )
    ne_armor_questresult = ne_armor_quest.launch()
    if ne_armor_questresult == (traductor.translate('si'), 0):
      life_max_temp += ne_armor_res_val - ne_armadura_old
      if life_max_temp != (life_max_temp + ne_armor_res_val):
        life_max_temp = int(life_max + ne_armor_res_val)
      life += int(ne_armor_res_val - ne_armadura_old)
      ne_armadura_old_temp = int(ne_armor_res_val)
    elif ne_armor_questresult == (traductor.translate('no'), 1):
      pass

  elif ne_result == (str(ne_casco), 1):
    os.system("clear")
    ne_helmet_res_val = random.randint(5 , 50)
    print(traductor.translate("Tu casco es:") + " " + colorama.Fore.MAGENTA + str(ne_casco))
    print(colorama.Fore.RESET + traductor.translate("Este elemento te dará") + " " + colorama.Fore.MAGENTA + str(ne_helmet_res_val) + colorama.Fore.RESET + " " + traductor.translate("de mana"))

    ne_helmet_quest = bullet.Bullet(
      prompt = traductor.translate("\nQuieres cambiar: "),
      choices = [traductor.translate("si"), traductor.translate("no")],
      indent = 0,
      align = 5,  
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
      return_index = True
      )
    ne_helmet_questresult = ne_helmet_quest.launch()
    if ne_helmet_questresult == (traductor.translate('si'), 0):
      mana_max_temp += ne_helmet_res_val - ne_casco_old_temp
      if mana_max_temp != (mana_max_temp + ne_helmet_res_val):
        mana_max_temp = int(mana_max_temp + ne_helmet_res_val)
      mana += int(ne_helmet_res_val - ne_casco_old_temp)
      ne_casco_old_temp = int(ne_helmet_res_val)
    elif ne_helmet_questresult == (traductor.translate('no'), 1):
      pass

  elif ne_result == (str(ne_arma), 2):
    os.system("clear")
    ne_weapon_res_val = random.randint(5 , 50)
    print(traductor.translate("Tu arma es: ") + colorama.Fore.MAGENTA + str(ne_arma))
    print(colorama.Fore.RESET + traductor.translate("Esta arma te dará") + " " + colorama.Fore.MAGENTA + str(ne_weapon_res_val) + " " + colorama.Fore.RESET + traductor.translate("de daño adicional"))

    ne_weapon_quest = bullet.Bullet(
      prompt = traductor.translate("\nQuieres cambiar: "),
      choices = [traductor.translate("si"), traductor.translate("no")],
      indent = 0,
      align = 5,
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
      return_index = True
      )
    ne_weapon_questresult = ne_weapon_quest.launch()
    if ne_weapon_questresult == (traductor.translate('si'), 0):
      atac += ne_weapon_res_val - ne_weapon_old
      if atac != (atac + ne_weapon_res_val):
        atac = int(atac + ne_weapon_res_val)
      ne_weapon_old_temp = int(ne_weapon_res_val)
    elif ne_weapon_questresult == (traductor.translate('no'), 1):
      pass

  elif ne_result == (traductor.translate('No necesito arma'), 3):
    pass
    
# (LOOSE) mensaje de perder
def player_loose():# (LOOSE) mensaje de perder
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  global rondas, game, life, life_max
  os.system("clear")
  print(colorama.Fore.RED + colorama.Style.BRIGHT)
  print("  ▒▒▒▒▒▒▒▒▒▒▒▄▄▄▄░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ▒▒▒▒▒▒▒▒▒▄██████▒▒▒▒▒▄▄▄█▄▒▒▒▒▒▒▒▒▒▒")
  print("  ▒▒▒▒▒▒▒▄██▀░░▀██▄▒▒▒▒████████▄▒▒▒▒▒▒")
  print("  ▒▒▒▒▒▒███░░░░░░██▒▒▒▒▒▒█▀▀▀▀▀██▄▄▒▒▒")
  print("  ▒▒▒▒▒▄██▌░░░░░░░██▒▒▒▒▐▌▒▒▒▒▒▒▒▒▀█▄▒")
  print(colorama.Fore.RED + "  ▒▒▒▒▒███░░" + colorama.Fore.BLUE + "▐█" + colorama.Fore.RED + "░" + colorama.Fore.BLUE + "█▌" + colorama.Fore.RED + "░██▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▀▌")
  print(colorama.Fore.RED + "  ▒▒▒▒████░" + colorama.Fore.BLUE + "▐█▌" + colorama.Fore.RED + "░" + colorama.Fore.BLUE + "▐█▌" + colorama.Fore.RED + "██▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print(colorama.Fore.RED + "  ▒▒▒▐████░" + colorama.Fore.BLUE + "▐" + colorama.Fore.RED + "░░░░░" + colorama.Fore.BLUE + "▌" + colorama.Fore.RED + "██▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print(colorama.Fore.RED + "  ▒▒▒▒████░░░" + colorama.Fore.BLUE + "▄█" + colorama.Fore.RED + "░░░██▒▒▐█▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print(colorama.Fore.RED + "  ▒▒▒▒████░░░" + colorama.Fore.BLUE + "██" + colorama.Fore.RED + "░░██▌▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print(colorama.Fore.RED + "  ▒▒▒▒████▌░" + colorama.Fore.BLUE + "▐█" + colorama.Fore.RED + "░░███▒▒▒█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print(colorama.Fore.RED + "  ▒▒▒▒▐████░░" + colorama.Fore.BLUE + "▌" + colorama.Fore.RED + "░███▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ▒▒▒▒▒████░░░███▒▒▒▒█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ▒▒▒██████▌░████▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ▒▐████████████▒▒███▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ▒█████████████▄████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ██████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  █████████████████▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  █████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("  ████████████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
  print("")
  print("  ██╗░░██╗░█████╗░░██████╗  ██████╗░███████╗██████╗░██████╗░██╗██████╗░░█████╗░")
  print("  ██║░░██║██╔══██╗██╔════╝  ██╔══██╗██╔════╝██╔══██╗██╔══██╗██║██╔══██╗██╔══██╗")
  print("  ███████║███████║╚█████╗░  ██████╔╝█████╗░░██████╔╝██║░░██║██║██║░░██║██║░░██║")
  print("  ██╔══██║██╔══██║░╚═══██╗  ██╔═══╝░██╔══╝░░██╔══██╗██║░░██║██║██║░░██║██║░░██║")
  print("  ██║░░██║██║░░██║██████╔╝  ██║░░░░░███████╗██║░░██║██████╔╝██║██████╔╝╚█████╔╝")
  print("  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚══════╝╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░╚════╝░")

  print(traductor.translate("Has sobrevivido") + " " + str(rondas) + " " + traductor.translate("rondas."))
  playerloose = input(traductor.translate("Has perdido, pulsa ENTER para salir"))
  if playerloose == "revive":
    game = 1
    life = (life_max*0.259876382376)
  else:
    game = 0
    life = 0
    finish()
# Cofre random pociones
def random_chest():
  global e_life, e_mana, life, mana, e_life_max, e_mana_max, life_max, mana_max
  global e_life_potion, e_mana_potion, life_potion, mana_potion, e_atac
  chest = random.randint(1, 5000)
  if chest < 15:
    life_potion +=  random.randint(1, 3)
  elif chest < 30:
    mana_potion +=  random.randint(1, 2)  
# cofre random pociones enemigo
def e_random_chest():
  global e_life, e_mana, life, mana, e_life_max, e_mana_max, life_max, mana_max
  global e_life_potion, e_mana_potion, life_potion, mana_potion, e_atac
  e_chest = random.randint(1, 5000)
  if e_chest < 10:
    e_life_potion +=  random.randint(1, 2)
  elif e_chest < 20:
    e_mana_potion +=  random.randint(1, 3) 
# selector de nuevo elemento y explicar nueva sala
def new_enemy():
 pass

# ANTIbloqueo de parida por falta de pociones
def surrender():
  global life_potion, mana_potion, life 
  if life_potion == 0 and mana_potion == 0:
    life = 0
    player_loose()
  else:
    pass
# creditos
def finish():
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  global life, mana, life_max, mana_max, life_potion, mana_potion, e_healtotal
  global dmgtotal, manatotal, lifetotal, life_total, mana_total, rondas
  global e_life, e_mana, e_life_max, e_mana_max, e_life_potion, e_mana_potion
  global resmanatotal, e_dmgtotal, e_manatotal, e_lifetotal, e_life_total
  global e_resmanatotal, e_dmgtotal, e_manatotal, e_lifetotal, healtotal
  global class_result, start_a, game, class_result
  global end_life_max, end_life, end_mana_max, end_mana, end_atac

  if class_result == (traductor.translate('Mago = vida 100 mana 100 atk 10'), 0):
    end_life_max = 100
    end_life = 100
    end_mana_max = 100
    end_mana = 100
    end_atac = 10.7
  elif class_result == (traductor.translate('Arquero = vida 75 mana 100 atk 15'), 1):
    end_life_max = 75
    end_life = 75
    end_mana_max = 90
    end_mana = 90
    end_atac = 15.7
  elif class_result == (traductor.translate('Guerrero = vida 130 mana 100 atk 7'), 2):
    end_life_max = 130
    end_life = 130
    end_mana_max = 150
    end_mana = 150
    end_atac = 7.9

  if start_a == "easteregg":
    end_life_max = 100
    end_life = 1
    end_mana_max = 100
    end_mana = 10
    end_atac = 1
  elif start_a == "easymode":
    end_life_max = 999999999999999
    end_life = 999999999999999
    end_mana_max = 999999999999999
    end_mana = 999999999999999
    end_atac = 999999999999999

  os.system("clear")
  print(colorama.Fore.YELLOW + "████████████████████████████████████████" + colorama.Fore.MAGENTA + "    ██████╗░██╗░░░██╗" + colorama.Fore.RED + "██████╗░██████╗░░██████╗░")
  print(colorama.Fore.YELLOW + "██████████████████▒────██▓██████████████" + colorama.Fore.MAGENTA + "    ██╔══██╗╚██╗░██╔╝" + colorama.Fore.RED + "██╔══██╗██╔══██╗██╔════╝░")
  print(colorama.Fore.YELLOW + "█████████████═──────────█▓▓█████████████" + colorama.Fore.MAGENTA + "    ██████╔╝░╚████╔╝░" + colorama.Fore.RED + "██████╔╝██████╔╝██║░░██╗░")
  print(colorama.Fore.YELLOW + "██████████▓───────────████══██████─█████" + colorama.Fore.LIGHTMAGENTA_EX + "    ██╔═══╝░░░╚██╔╝░░" + colorama.Fore.LIGHTRED_EX + "██╔══██╗██╔═══╝░██║░░╚██╗")
  print(colorama.Fore.YELLOW + "█████████────────────══─██──████─────███" + colorama.Fore.LIGHTMAGENTA_EX + "    ██║░░░░░░░░██║░░░" + colorama.Fore.LIGHTRED_EX + "██║░░██║██║░░░░░╚██████╔╝")
  print(colorama.Fore.YELLOW + "████████─────" + colorama.Fore.LIGHTYELLOW_EX + "▒────██" + colorama.Fore.YELLOW + "────█─█─███──██──▓██" + colorama.Fore.LIGHTMAGENTA_EX + "    ╚═╝░░░░░░░░╚═╝░░░" + colorama.Fore.LIGHTRED_EX + "╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░")
  print(colorama.Fore.YELLOW + "████▓▓██─────" + colorama.Fore.LIGHTYELLOW_EX + "█──▓███" + colorama.Fore.YELLOW + "────────▓██─████──██")
  print(colorama.Fore.YELLOW + "███───██───" + colorama.Fore.LIGHTYELLOW_EX + "█▒█──█──█▓" + colorama.Fore.YELLOW + "───────▓█─▒████──██" + "    " + traductor.translate("Estadisticas Jugador"))
  print(colorama.Fore.YELLOW + "███──▓███──" + colorama.Fore.LIGHTYELLOW_EX + "███▓─═█──█▓" + colorama.Fore.YELLOW + "───────██▓█████──█" + "      " + traductor.translate("Rondas") + "  " + str(rondas))
  print(colorama.Fore.YELLOW + "███──████─═" + colorama.Fore.LIGHTYELLOW_EX + "███▒─█▒──██" + colorama.Fore.YELLOW + "───────████████──█" + "      " + traductor.translate("Daño total causado:") + " " + str(dmgtotal))
  print(colorama.Fore.YELLOW + "██──▓████──" + colorama.Fore.LIGHTYELLOW_EX + "███──███─▓█" + colorama.Fore.YELLOW + "───────████████──█" + "      " + traductor.translate("Maná total gastado:") + " " + str(manatotal))
  print(colorama.Fore.YELLOW + "██──█████─" + colorama.Fore.LIGHTYELLOW_EX + "██═█─█▒═█─██" + colorama.Fore.YELLOW + "───────████████─██" + "      " + traductor.translate("Vida total ganada:") + " " + str(healtotal))
  print(colorama.Fore.YELLOW + "██──█████─═" + colorama.Fore.LIGHTYELLOW_EX + "█─█────█─█▓" + colorama.Fore.YELLOW + "───────███████──██" + "      " + traductor.translate("Mana total ganada:") + " " + str(resmanatotal))
  print(colorama.Fore.YELLOW + "██──█████─────────" + colorama.Fore.LIGHTYELLOW_EX + "█─█▒" + colorama.Fore.YELLOW + "───────███████─███" + "      " + traductor.translate("Pociones de vida sobrantes") + "  " + str(life_potion))
  print(colorama.Fore.YELLOW + "██──█████─────────" + colorama.Fore.LIGHTYELLOW_EX + "█─█" + colorama.Fore.YELLOW + "────────██████──███" + "      " + traductor.translate("Pociones de maná sobrantes") + "  " + str(mana_potion))
  print(colorama.Fore.YELLOW + "██──▓████─────────" + colorama.Fore.LIGHTYELLOW_EX + "█─█" + colorama.Fore.YELLOW + "───────═█████──████")
  print(colorama.Fore.YELLOW + "██───████▒────────" + colorama.Fore.LIGHTYELLOW_EX + "█─█" + colorama.Fore.YELLOW + "───────▓████──█████" + "    " + traductor.translate("Estadisticas enemigo"))
  print(colorama.Fore.YELLOW + "██───████▓───────" + colorama.Fore.LIGHTYELLOW_EX + "▒█─█" + colorama.Fore.YELLOW + "───────████──██████" + "      " + traductor.translate("Daño total causado:") + " " + str(e_dmgtotal))
  print(colorama.Fore.YELLOW + "██▒───████───────" + colorama.Fore.LIGHTYELLOW_EX + "▒█─█" + colorama.Fore.YELLOW + "───────███──███████" + "      " + traductor.translate("Maná total gastado:") + " " + str(e_manatotal))
  print(colorama.Fore.YELLOW + "███────███───────" + colorama.Fore.LIGHTYELLOW_EX + "▓█─█" + colorama.Fore.YELLOW + "───────██──████████" + "      " + traductor.translate("Vida total ganada:") + " " + str(e_healtotal))
  print(colorama.Fore.YELLOW + "███═───███───────" + colorama.Fore.LIGHTYELLOW_EX + "██─█" + colorama.Fore.YELLOW + "──────▒█▓─█████████" + "      " + traductor.translate("Mana total ganada:") + " " + str(e_resmanatotal))
  print(colorama.Fore.YELLOW + "████────██▒──────" + colorama.Fore.LIGHTYELLOW_EX + "█▒─███" + colorama.Fore.YELLOW + "────██─██████████" + "      " + traductor.translate("Pociones de vida sobrantes") + "  " + str(e_life_potion))
  print(colorama.Fore.YELLOW + "████────██───" + colorama.Fore.LIGHTYELLOW_EX + "▒▓▓█───██" + colorama.Fore.YELLOW + "────█▒─███████████" + "      " + traductor.translate("Pociones de maná sobrantes") + "  " + str(e_mana_potion))
  print(colorama.Fore.YELLOW + "█████────█───" + colorama.Fore.LIGHTYELLOW_EX + "███▓───██" + colorama.Fore.YELLOW + "────█─▓███████████")
  print(colorama.Fore.YELLOW + "██████───██──" + colorama.Fore.LIGHTYELLOW_EX + "▓█─────█▓" + colorama.Fore.YELLOW + "───██─████████████" + "    " + traductor.translate("Stats Iniciales") + "      " + str(start_a))
  print(colorama.Fore.YELLOW + "███████───█──═" + colorama.Fore.LIGHTYELLOW_EX + "█─█████" + colorama.Fore.YELLOW + "═───█──▓███████████" + "        " + traductor.translate("Vida inicial") + "  " + str(end_life))
  print(colorama.Fore.YELLOW + "███████───██──" + colorama.Fore.LIGHTYELLOW_EX + "██████▒" + colorama.Fore.YELLOW + "────█──────████████" + "        " + traductor.translate("Mana inicial") + "  " + str(end_mana))
  print(colorama.Fore.YELLOW + "████████──██──" + colorama.Fore.LIGHTYELLOW_EX + "▒" + colorama.Fore.YELLOW + "─────────██──────████████" + "        " + traductor.translate("Ataque inicial") + " " + str(end_atac))
  print(colorama.Fore.YELLOW + "████████──▓█▓───────────███────█████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "████████═─▓██──────────█████─▒██████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + traductor.translate("Echo por:"))
  print(colorama.Fore.YELLOW + "████████▓─████────────▓█████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "      " + traductor.translate("USR1 y USR2"))
  print(colorama.Fore.YELLOW + "████████──████▓──────═██████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "███████──██████▓────▓███████████████████" + colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "    " + traductor.translate("'Si la vida te da limones, hazte un bocata.'"))
  print(colorama.Fore.YELLOW + "██████▒─████████████████████████████████" + colorama.Fore.RED + colorama.Style.BRIGHT + "    " + "  " + "- USR1")
  print(colorama.Fore.YELLOW + "████████████████▒▒▓──███████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "████████████████▒───▓███████████████████" + colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "    " + traductor.translate("'Sonrie porque todos los días son igual de malos.'"))
  print(colorama.Fore.YELLOW + "█████████████████───████████████████████" + colorama.Fore.RED + colorama.Style.BRIGHT + "    " + "  - USR2")
  print(colorama.Fore.YELLOW + "█████████████████──▒████████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "████████████████████████████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + traductor.translate("Gracias por jugar a") + " " + colorama.Fore.MAGENTA + "PY" + colorama.Fore.RED + "RPG" )
  print(colorama.Fore.YELLOW + "█████████████████▓▒────█████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + traductor.translate("Este juego ha tomado muuuchas horas y "))
  print(colorama.Fore.YELLOW + "███████████████─────────▒███████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + traductor.translate("lineas y") + " " + colorama.Fore.RED + " " + traductor.translate("espero que no nos suspendan por esto."))
  print(colorama.Fore.YELLOW + "██████████████══█▓██████████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + traductor.translate("Puede que hayamos perdido horas de FOL para terminar esto"))
  print(colorama.Fore.YELLOW + "█████████████████████████████▓██████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "████████████──────────────▓█▒▒██████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + traductor.translate("Apruebanos y te dejamos poner la frase que quieras"))
  print(colorama.Fore.YELLOW + "█████████▒██─────═─══════─██▒▓██████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "█████████▓▓█──══════════──██▒███████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "██████████▒█▒─══─═────────█▓▒███████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "██████████▒██──────────▒─▒█▓▓███████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "██████████▒▓█─▒████████████▒▓███████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "██████████▓▒███████▓▓▓▓▓▒▒▒▒████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + traductor.translate("Si le das a enter vas a volver al menu."))
  print(colorama.Fore.YELLOW + "███████████▒█▓▓▒▒▒▒▓▓▓▓▓████████████████"   + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + traductor.translate("Escribe 'start' para continuar la partida"))
  end = input(colorama.Fore.YELLOW + "███████████▓▓▓▓█████████████████████████")
  game = 0
  if end == "loose":
    player_loose()
  elif end == "start":
    if life == 0:
      game = 0
    else:
      game = 1
      player_win()
  else:
    menu()
#menu principal
def menu():
  global frases
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  os.system("clear")


  datos = [
    {
        "nombre": colorama.Fore.MAGENTA + "██████╗░██╗░░░██╗" + colorama.Fore.RED + "██████╗░██████╗░░██████╗░",

    },
    {
        "nombre": colorama.Fore.MAGENTA + "██╔══██╗╚██╗░██╔╝" + colorama.Fore.RED + "██╔══██╗██╔══██╗██╔════╝░",

    },
    {
        "nombre": colorama.Fore.MAGENTA + "██████╔╝░╚████╔╝░" + colorama.Fore.RED + "██████╔╝██████╔╝██║░░██╗░",

    },
    {
        "nombre": colorama.Fore.LIGHTMAGENTA_EX + "██╔═══╝░░░╚██╔╝░░" + colorama.Fore.LIGHTRED_EX + "██╔══██╗██╔═══╝░██║░░╚██╗",

    },
    {
        "nombre": colorama.Fore.LIGHTMAGENTA_EX + "██║░░░░░░░░██║░░░" + colorama.Fore.LIGHTRED_EX + "██║░░██║██║░░░░░╚██████╔╝",

    },
    {
        "nombre": colorama.Fore.LIGHTMAGENTA_EX + "╚═╝░░░░░░░░╚═╝░░░" + colorama.Fore.LIGHTRED_EX + "╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░",

    },
  ]

  for dato in datos:
    nombre = dato["nombre"]
    cadena = "{:^80}".format(nombre)
    print(cadena)
  print("{:^80}".format(colorama.Fore.LIGHTWHITE_EX + colorama.Style.BRIGHT + random.choice(frases)))
  cli = bullet.Bullet(
    choices = ["{:^70}".format(traductor.translate("Iniciar Partida")), "{:^70}".format(traductor.translate("Iniciar Tutorial")), "{:^70}".format(traductor.translate("Partida Custom")),  "{:^70}".format(traductor.translate("Cambiar idioma")), "{:^70}".format(traductor.translate("Creditos")), "{:^70}".format(traductor.translate("Salir")), ], 
    bullet = "",
    bullet_color=bullet.colors.bright(bullet.colors.foreground["cyan"]),
    word_color=bullet.colors.bright(bullet.colors.foreground["yellow"]),
    word_on_switch=bullet.colors.bright(bullet.colors.foreground["yellow"]),
    background_on_switch=bullet.colors.background["black"],
    pad_right = 0
  )

  result = "{:^80}".format(cli.launch())
  if result == "{:^80}".format(traductor.translate("Iniciar Partida")):
    tutorial()
  elif result == "{:^80}".format(traductor.translate("Iniciar Tutorial")):
    comojugar()
  elif result == "{:^80}".format(traductor.translate("Partida Custom")):
    partida_personalizada()
  elif result == "{:^80}".format(traductor.translate("Cambiar idioma")):
    cambiar_idioma()
  elif result == "{:^80}".format(traductor.translate("Creditos")):
    finish()
  elif result == "{:^80}".format(traductor.translate("Salir")):
    exit()


# como jugar
def cambiar_idioma():
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  os.system("clear")
  cli = bullet.Bullet(
    choices = [traductor.translate("Español"), traductor.translate("Ingles"), traductor.translate("Frances"),  traductor.translate("Catalan"), traductor.translate("Portuges") ], 
    bullet = "",
    bullet_color=bullet.colors.bright(bullet.colors.foreground["cyan"]),
    word_color=bullet.colors.bright(bullet.colors.foreground["yellow"]),
    word_on_switch=bullet.colors.bright(bullet.colors.foreground["yellow"]),
    background_on_switch=bullet.colors.background["black"],
    pad_right = 0
  )

  result = (cli.launch())
  if result == traductor.translate("Español"):
    lang = "es"
  elif result == traductor.translate("Ingles"):
    lang = "en"
  elif result == traductor.translate("Frances"):
    lang = "fr"
  elif result == traductor.translate("Catalan"):
    lang = "ca"
  elif result == traductor.translate("Portuges"):
    lang = "pt"
  menu()
  
def tutorial():
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  global start_a, class_result, life_max, life_max_temp, life, mana_max, mana_max_temp, mana, atac, e_life_max, e_life, e_mana_max, e_mana, e_atac, life_potion, mana_potion, e_life_potion, e_mana_potion, rondas, class_result
  global dmgtotal, healtotal, manatotal, resmanatotal, e_dmgtotal, e_healtotal, e_manatotal, e_resmanatotal


  dmgtotal = 0
  healtotal = 0
  manatotal = 0
  resmanatotal = 0
  e_dmgtotal = 0
  e_healtotal = 0
  e_manatotal = 0
  e_resmanatotal = 0

  rondas = 0
  start_a = 0
  class_result = 0

  life_max = 0
  life_max_temp = 0
  life = 0
  mana_max = 0
  mana_max_temp = 0
  mana = 0
  atac = 0

  e_life_max = 100
  e_life = 100
  e_mana_max = 100
  e_mana = 100
  e_atac = 10

  life_potion = 10
  mana_potion = 10
  e_life_potion = 6
  e_mana_potion = 10
  os.system("clear")

  print(colorama.Fore.LIGHTYELLOW_EX + colorama.Style.BRIGHT)

  print(colorama.Fore.MAGENTA + "██████╗░██╗░░░██╗" + colorama.Fore.RED + "██████╗░██████╗░░██████╗░")
  print(colorama.Fore.MAGENTA + "██╔══██╗╚██╗░██╔╝" + colorama.Fore.RED + "██╔══██╗██╔══██╗██╔════╝░")
  print(colorama.Fore.MAGENTA + "██████╔╝░╚████╔╝░" + colorama.Fore.RED + "██████╔╝██████╔╝██║░░██╗░")
  print(colorama.Fore.LIGHTMAGENTA_EX + "██╔═══╝░░░╚██╔╝░░" + colorama.Fore.LIGHTRED_EX + "██╔══██╗██╔═══╝░██║░░╚██╗")
  print(colorama.Fore.LIGHTMAGENTA_EX + "██║░░░░░░░░██║░░░" + colorama.Fore.LIGHTRED_EX + "██║░░██║██║░░░░░╚██████╔╝")
  print(colorama.Fore.LIGHTMAGENTA_EX + "╚═╝░░░░░░░░╚═╝░░░" + colorama.Fore.LIGHTRED_EX + "╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░ \n")
  print(colorama.Fore.WHITE + traductor.translate("Este juego es un RPG en el que has de ir sobreviviendo oleadas. Cuantas más rondas ganes,") + colorama.Fore.MAGENTA + " " + traductor.translate("mejor será tu puntuación.") + colorama.Fore.WHITE)
  print(traductor.translate("Al empezar el juego tendrás que elegir entre") + " " + colorama.Fore.GREEN + traductor.translate("tres personajes") + colorama.Fore.WHITE + traductor.translate(", cada uno es el") + " " + colorama.Fore.RED + traductor.translate("mejor en su habilidad") + colorama.Fore.WHITE + " " + traductor.translate("característica. Durante el ataque habrás de escoger entre curar, atacar y regenerar mana."))
  print(traductor.translate("En caso de perder se acabará el juego, pero si ganas recibirás un") + " " + colorama.Fore.YELLOW + traductor.translate("cofre") + colorama.Fore.WHITE + " " + traductor.translate("con varias opciones, elige sabiamente."))
  print(traductor.translate("Cada vez que derrotes a un enemigo, te enfrentarás a uno aún más fuerte que el anterior. \n"))
  start_a = input(traductor.translate("Presiona") + " " + colorama.Fore.LIGHTCYAN_EX + traductor.translate("𝗘𝗡𝗧𝗘𝗥") + colorama.Fore.WHITE + " " + traductor.translate("para comenzar") + colorama.Style.RESET_ALL)

  os.system("clear")
  elejir_personaje()
# escoger personaje
def elejir_personaje():
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  global life, life_max, mana_max, mana, atac, start_a, life_max_temp, mana_max_temp, mana_temp, atac_temp, life_temp
  global end_life_max, end_life, end_mana_max, end_mana, end_atac, e_life_max, e_life, e_mana_max, e_mana, e_atac, life_potion, mana_potion, e_life_potion, e_mana_potion

  e_life_max = 100
  e_life = 100
  e_mana_max = 100
  e_mana = 100
  e_atac = 10

  life_potion = 10
  mana_potion = 10
  e_life_potion = 6
  e_mana_potion = 10
  print(colorama.Fore.LIGHTYELLOW_EX + colorama.Style.BRIGHT)
  print("█▀▀ █▀█ █▀▄▀█ █▀█   ░░█ █░█ █▀▀ ▄▀█ █▀█ " + colorama.Fore.LIGHTMAGENTA_EX + "▀█" + colorama.Fore.LIGHTYELLOW_EX)
  print("█▄▄ █▄█ █░▀░█ █▄█   █▄█ █▄█ █▄█ █▀█ █▀▄ " + colorama.Fore.LIGHTMAGENTA_EX + "░▄")
  print(colorama.Fore.RESET)
  print(traductor.translate("Para moverte entre las diferentes opciones tienes que usar") + colorama.Fore.GREEN + " " + traductor.translate("las teclas 🠕 y 🠗") + " " + colorama.Fore.WHITE + traductor.translate("y para aceptar tienes que usar") + " " + colorama.Fore.GREEN + traductor.translate("ENTER") + colorama.Fore.WHITE + ".")
  print(traductor.translate("Si quieres una partida") + colorama.Fore.LIGHTGREEN_EX + " " + traductor.translate("facil") + colorama.Fore.RESET + traductor.translate(", recomendamos que eligas") + " " + colorama.Fore.RED + traductor.translate("el arquero") + colorama.Fore.WHITE + "."))
  print(traductor.translate("Si quieres una partida") + colorama.Fore.LIGHTGREEN_EX + " " + traductor.translate("normal") + colorama.Fore.RESET + traductor.translate(", recomendamos que eligas") + " " + colorama.Fore.RED + traductor.translate("el mago") + colorama.Fore.WHITE + ".")
  print(traductor.translate("Si quieres una partida") + colorama.Fore.LIGHTGREEN_EX + " " + traductor.translate("dificil") + colorama.Fore.RESET + traductor.translate(", recomendamos que eligas") + " " + colorama.Fore.RED + traductor.translate("el guerrero") + colorama.Fore.WHITE + ".")
  Mago = colorama.Fore.BLUE + traductor.translate("Mago - normal")
  Arquero = colorama.Fore.GREEN + traductor.translate("Arquero - facil")
  Guerrero = colorama.Fore.RED + traductor.translate("Guerrero - dificil")
  clase = bullet.Bullet(
    prompt = traductor.translate("\nEscoje tu clase: "),
    choices = [str(Arquero), str(Mago), str(Guerrero)],
    indent = 0,
    align = 5, 
    margin = 2,
    shift = 0,
    bullet = "",
    pad_right = 5,
    return_index = False
  )
  clase_result = clase.launch()

  if clase_result == Mago:
    life_max = 100
    life = 100
    mana_max = 100
    mana = 100
    atac = 10
    end_life_max = 100
    end_life = 100
    end_mana_max = 100
    end_mana = 100
    end_atac = 10
  elif clase_result == Arquero:
    life_max = 75
    life = 75
    mana_max = 90
    mana = 90
    atac = 16
    end_life_max = 75
    end_life = 75
    end_mana_max = 90
    end_mana = 90
    end_atac = 16
  elif clase_result == Guerrero:
    life_max = 130
    life = 130
    mana_max = 150
    mana = 150
    atac = 7
    end_life_max = 130
    end_life = 130
    end_mana_max = 150
    end_mana = 150
    end_atac = 7
  else:
      print(traductor.translate("No es una opcion valida"))
      exit()

  if start_a == "easteregg":
    life_max = 1000
    life = 1
    mana_max = 1000
    mana = 10
    atac = 5
  elif start_a == "easymode":
    life_max = 999999999999999
    life = 999999999999999
    mana_max = 999999999999999
    mana = 999999999999999
    atac = 999999999999999
  else:
    pass

  mana_max_temp = mana_max
  life_max_temp = life_max
  juego()
  os.system("clear")


# juego
def juego():
  global life, game, life_max, life_max_temp, mana, mana_max, mana_max_temp, atac, ne_weapon_old, ne_weapon_old_temp, ne_armor_old, ne_armor_old_temp, ne_casco_old, ne_casco_old_temp, ne_armadura_old, ne_armadura_old_temp, e_life, e_life_max, e_life_max_temp, e_mana, e_mana_max, e_mana_max_temp, e_atac, life_potion, mana_potion, life_potion_max, mana_potion_max, e_life_potion, e_life_potion_max, e_mana_potion, rondas
  game = 1
  rondas = 0
  life = int(life)
  mana = int(mana)
  atac = int(atac)
  life_max = int(life_max)
  mana_max = int(mana_max)
  life_max_temp = int(life_max_temp)
  mana_max_temp = int(mana_max_temp)
  e_life = int(e_life)
  e_mana = int(e_mana)
  e_atac = int(e_atac)
  e_life_max = int(e_life_max)
  e_mana_max = int(e_mana_max)
  life_potion = int(life_potion)
  mana_potion = int(mana_potion)
  e_life_potion = int(e_life_potion)
  e_mana_potion = int(e_mana_potion)
  while game == 1:
    if life <= 0:
      player_loose()
      if game == 0:
        break
      else:
        pass
    random_chest()
    e_random_chest()
    life_max = life_max_temp
    mana_max = mana_max_temp
    ne_weapon_old = ne_weapon_old_temp
    ne_armor_old = ne_armor_old_temp
    ne_casco_old = ne_casco_old_temp
    os.system("clear")
    player_act_def()
    npc_act()
    if e_life <= 0:
      if rondas == 10:
        finish()
        if game == 0:
          break
        elif game == 1:
          pass
      else:
        npc_dead()
        player_win()


# iniciar tutorial
def comojugar():
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  global start_a, class_result, life_max, life_max_temp, life, mana_max, mana_max_temp, mana, atac, end_life, end_mana, end_atac, e_life_max, e_life, e_mana_max, e_mana, e_atac, life_potion, mana_potion, e_life_potion, e_mana_potion

  os.system("clear")
  tf1 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "─────" + colorama.Fore.MAGENTA + "█" + colorama.Fore.WHITE + "─" + colorama.Fore.LIGHTRED_EX + "▄▀█" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "█▀▄" + colorama.Fore.WHITE + "─" + colorama.Fore.MAGENTA + "█" + colorama.Fore.WHITE + "─────"
  tf2 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "────" + colorama.Fore.MAGENTA + "▐▌" + colorama.Fore.WHITE + "──────────" + colorama.Fore.MAGENTA + "▐▌" + colorama.Fore.WHITE + "────"
  tf3 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "────" + colorama.Fore.MAGENTA + "█▌" + colorama.Fore.LIGHTRED_EX + "▀▄" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▄▄" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▄▀" + colorama.Fore.MAGENTA + "▐█" + colorama.Fore.WHITE + "────"
  tf4 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "───" + colorama.Fore.MAGENTA + "▐██" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▀▀" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▀▀" + colorama.Fore.WHITE + "──" + colorama.Fore.MAGENTA + "██▌" + colorama.Fore.WHITE + "───"
  tf5 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "──" + colorama.Fore.MAGENTA + "▄████▄" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▐▌" + colorama.Fore.WHITE + "──" + colorama.Fore.MAGENTA + "▄████▄" + colorama.Fore.WHITE + "──"

  print(str(tf1) + "  " + traductor.translate("Hola jugador!"))
  print(str(tf2) + "  " + traductor.translate("Bienvenido a") + " " + colorama.Fore.RED + "PYRPG!!")
  print(str(tf3) + "  " + traductor.translate("Parece que eres nuevo en este mundo,") + colorama.Fore.MAGENTA + " " + traductor.translate("¿quieres aprender cómo jugar?"))
  print(str(tf4) + "  " + traductor.translate("Si es así,") + " " + colorama.Fore.GREEN + traductor.translate("te enseñaremos") + colorama.Fore.WHITE + " " + traductor.translate("todo lo que necesitas"))
  print(str(tf5) + "  " + traductor.translate("Dale a") + colorama.Fore.RED + " " + traductor.translate("ENTER") + colorama.Fore.WHITE + " " + traductor.translate("para continuar"))
  input("")
  os.system("clear")

  print(str(tf1) + "  " + traductor.translate("Cuando empiezes te van a dejar elejir entre") + colorama.Fore.YELLOW + " " + traductor.translate("tres personajes") + colorama.Fore.WHITE + traductor.translate(", estos son:"))
  print(str(tf2) + "  " + "" + colorama.Fore.GREEN + traductor.translate("Arquero:") + colorama.Fore.WHITE + " " + traductor.translate("Facil de usar gracias a la cantidad de") + " " + colorama.Fore.GREEN + traductor.translate("ataque") + colorama.Fore.WHITE + " " + traductor.translate("que tiene."))
  print(str(tf3) + "  " + "" + colorama.Fore.BLUE + traductor.translate("Mago:") + colorama.Fore.WHITE + " " + traductor.translate("Modo de juego") + " " + colorama.Fore.BLUE + traductor.translate("normal") + colorama.Fore.WHITE + " " + traductor.translate("y ataque") + " " + colorama.Fore.BLUE + traductor.translate("normal."))
  print(str(tf4) + "  " + "" + colorama.Fore.LIGHTRED_EX + traductor.translate("Guerrero:") + colorama.Fore.WHITE + " " + traductor.translate("Mas") + " " + colorama.Fore.LIGHTRED_EX + traductor.translate("dificil") + colorama.Fore.WHITE + " " + traductor.translate("de usar ya que, aunque tiene") + colorama.Fore.LIGHTRED_EX + " " + traductor.translate("mucha vida") + colorama.Fore.WHITE + traductor.translate(", tiene") + " " + colorama.Fore.LIGHTRED_EX + traductor.translate("poco ataque."))
  print(str(tf5) + "  " + traductor.translate("Dale a ENTER para continuar -Es asi en todas :)-"))
  input("")
  os.system("clear")
  print(str(tf1) + "  " + traductor.translate("Este es el") +" " + colorama.Fore.GREEN + traductor.translate("menu principal") + colorama.Fore.WHITE + traductor.translate(", en el cual encontraras") + colorama.Fore.LIGHTYELLOW_EX + " " + traductor.translate("informacion sobre la partida."))
  print(str(tf2) + "  " + "" + colorama.Fore.BLUE + traductor.translate("La linea azul marca tu mana,") + " " + colorama.Fore.WHITE + traductor.translate("este es necesario para poder atacar."))
  print(str(tf3) + "  " + "" + colorama.Fore.GREEN + traductor.translate("La linea verde es tu vida,") + " " + colorama.Fore.WHITE + traductor.translate("ten quidado no baje mucho o podras perder la partida."))
  print(str(tf4) + "  " + "" + colorama.Fore.RED + traductor.translate("La linea roja es la vida de tu enemigo") + colorama.Fore.WHITE + traductor.translate(", es importante que esa este baja, o mas baja que la tuya."))
  print(str(tf5) + "  " + traductor.translate("A la derecha puedes ver la cantidad de pociones que tienes,") + " " + colorama.Fore.LIGHTYELLOW_EX + traductor.translate("estas te ayudaran a tener mas vida y mana."))
  life_max = 10
  life_max_temp = 10
  life = 10
  mana_max = 10
  mana_max_temp = 10
  mana = 10
  e_life_max = 10
  e_life = 10
  life_potion = 4
  mana_potion = 4
  topgui()
  input("")
  os.system("clear")

  tut1 = 0
  while tut1 == 0:
    print(str(tf1) + "  " + traductor.translate("¡Es tu turno!!"))
    print(str(tf2) + "  " + traductor.translate("Tienes tres opciones:") + " " + colorama.Fore.CYAN + traductor.translate("Atacar,") + colorama.Fore.BLUE + " " + traductor.translate("restaurar mana o") + " " + colorama.Fore.GREEN + traductor.translate("restaurar vida."))
    print(str(tf3) + "  " + traductor.translate("Empecemos con") + " " + colorama.Fore.CYAN + traductor.translate("atacar") + colorama.Fore.WHITE + traductor.translate(", función esencial para") + " " + colorama.Fore.GREEN + traductor.translate("ganar."))
    print(str(tf4) + "  " + traductor.translate("Cuando ataques") + " " + colorama.Fore.GREEN + traductor.translate("le bajarás la vida al enemigo") + colorama.Fore.RED + traductor.translate(", y viceversa."))
    print(str(tf5) + "  " + traductor.translate("Además te") + colorama.Fore.LIGHTBLUE_EX + " " + traductor.translate("restará mana") + colorama.Fore.WHITE + traductor.translate(", así que no te emociones tanto y") + " " + colorama.Fore.LIGHTYELLOW_EX + traductor.translate("juega con estrategia."))

    topgui()
    print(traductor.translate("Para moverte entre las diferentes opciones tienes que usar") + colorama.Fore.GREEN + " " + traductor.translate("las teclas 🠕 y 🠗") + " " + colorama.Fore.WHITE + traductor.translate("y para aceptar tienes que usar") + " " + colorama.Fore.GREEN + traductor.translate("ENTER") + colorama.Fore.WHITE + ".")
    player_act = bullet.Bullet(
      prompt = traductor.translate("\nElije accion: "),
      choices = [traductor.translate("Atacar (-10 mana)"), traductor.translate("Curar (+20%)"), traductor.translate("Restaurar mana (+20%)")],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == (traductor.translate('Atacar (-10 mana)'), 0) and mana >= 10:
      tut1 = 1
    elif player_act_result == (traductor.translate('Curar (+20%)'), 1) and life_potion >= 1:
      tut1 = 0
    elif player_act_result == (traductor.translate('Restaurar mana (+20%)'), 2) and mana_potion >= 1:
      tut1 = 0

    os.system("clear")
  os.system("clear") 
  os.system("clear")

  life_max = 10
  life_max_temp = 10
  life = 10
  mana_max = 10
  mana_max_temp = 10
  mana = 0
  e_life_max = 10
  e_life = 5
  life_potion = 4
  mana_potion = 4
  tut1 = 0
  while tut1 == 0:
    print(str(tf1) + "  " + "")
    print(str(tf2) + "  " + traductor.translate("¡Ahora no puedes atacar!"))
    print(str(tf3) + "  " + traductor.translate("¡Necesitas") + " " + colorama.Fore.BLUE + traductor.translate("restaurar tu mana") + colorama.Fore.WHITE + " " + traductor.translate("para poder atacar!"))
    print(str(tf4) + "  " + traductor.translate("Para hacerlo selecciona la opción") + colorama.Fore.BLUE + " " + traductor.translate("restaurar mana."))
    print(str(tf5) + "  " + "")
    topgui()
    player_act = bullet.Bullet(
      prompt = traductor.translate("\nElije accion: "),
      choices = [traductor.translate("Atacar (-10 mana)"), traductor.translate("Curar (+20%)"), traductor.translate("Restaurar mana (+20%)")],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == (traductor.translate('Atacar (-10 mana)'), 0) and mana >= 10:
      tut1 = 0
    elif player_act_result == (traductor.translate('Curar (+20%)'), 1) and life_potion >= 1:
      tut1 = 0
    elif player_act_result == (traductor.translate('Restaurar mana (+20%)'), 2) and mana_potion >= 1:
      tut1 = 1

    os.system("clear")
  os.system("clear")

  life_max = 10
  life_max_temp = 10
  life = 5
  mana_max = 10
  mana_max_temp = 10
  mana = 10
  e_life_max = 10
  e_life = 5
  life_potion = 4
  mana_potion = 3
  tut1 = 0
  while tut1 == 0:
    print(str(tf1) + "  " + "")
    print(str(tf2) + "  " + traductor.translate("Parece que te han tocado,"))
    print(str(tf3) + "  " + "" + colorama.Fore.RED + traductor.translate("Tienes la vida muy baja,") + " " + colorama.Fore.GREEN + traductor.translate("prueba de curarte"))
    print(str(tf4) + "  " + "")
    print(str(tf5) + "  " + "")
    topgui()
    player_act = bullet.Bullet(
      prompt = traductor.translate("\nElije accion: "),
      choices = [traductor.translate("Atacar (-10 mana)"), traductor.translate("Curar (+20%)"), traductor.translate("Restaurar mana (+20%)")],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == (traductor.translate('Atacar (-10 mana)'), 0) and mana >= 10:
      tut1 = 0
    elif player_act_result == (traductor.translate('Curar (+20%)'), 1) and life_potion >= 1:
      tut1 = 1
    elif player_act_result == (traductor.translate('Restaurar mana (+20%)'), 2) and mana_potion >= 1:
      tut1 = 0

    os.system("clear")
  os.system("clear")

  life_max = 10
  life_max_temp = 10
  life = 10
  mana_max = 10
  mana_max_temp = 10
  mana = 10
  e_life_max = 10
  e_life = 5
  life_potion = 3
  mana_potion = 3
  tut1 = 0
  while tut1 == 0:
    print(str(tf1) + "  " + "")
    print(str(tf2) + "  " + traductor.translate("¡Ahora") + colorama.Fore.CYAN + " " + traductor.translate("ataca") + colorama.Fore.WHITE + " " + traductor.translate("y") + " " + colorama.Fore.RED + traductor.translate("mátalo!"))
    print(str(tf3) + "  " + "")
    print(str(tf4) + "  " + "")
    print(str(tf5) + "  " + "")
    topgui()
    player_act = bullet.Bullet(
      prompt = traductor.translate("\nElije accion: "),
      choices = [traductor.translate("Atacar (-10 mana)"), traductor.translate("Curar (+20%)"), traductor.translate("Restaurar mana (+20%)")],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == (traductor.translate('Atacar (-10 mana)'), 0) and mana >= 10:
      tut1 = 1
    elif player_act_result == (traductor.translate('Curar (+20%)'), 1) and life_potion >= 1:
      tut1 = 0
    elif player_act_result == (traductor.translate('Restaurar mana (+20%)'), 2) and mana_potion >= 1:
      tut1 = 0

    os.system("clear")
  os.system("clear")
  print(str(tf1) + "  " + "")
  print(str(tf2) + "  " + traductor.translate("¡Perfecto!") + colorama.Fore.LIGHTGREEN_EX + " " + traductor.translate("¡Has ganado la partida!"))
  print(str(tf3) + "  " + "" + colorama.Fore.GREEN + traductor.translate("Cuando ganes,") + colorama.Fore.WHITE + " " + traductor.translate("tendrás") + colorama.Fore.LIGHTBLUE_EX + " " + traductor.translate("tres opciones:") + colorama.Fore.CYAN + " " + traductor.translate("¡Más ataque,") + colorama.Fore.BLUE + " " + traductor.translate("más maná o") + colorama.Fore.GREEN + " " + traductor.translate("más vida!"))
  print(str(tf4) + "  " + traductor.translate("Elige el más") + " " + colorama.Fore.GREEN + traductor.translate("conveniente para ganar."))
  print(str(tf5) + "  " + "")
  input("")
  os.system("clear")

  print(str(tf1) + "  " + traductor.translate("¡Después pasarás a la siguiente sala,") + colorama.Fore.GREEN + traductor.translate(" ¡aquí también te dan objetos!"))
  print(str(tf2) + "  " + traductor.translate("No te preocupes por los nombres, son raros pero están hechos así"))
  print(str(tf3) + "  " + traductor.translate("¡para que no se quejen de las faltas de ortografía!"))
  print(str(tf4) + "  " + "" + colorama.Fore.GREEN + traductor.translate("El primero mejora la vida,") + colorama.Fore.BLUE + " " + traductor.translate("el segundo el maná y") + colorama.Fore.CYAN + " " + traductor.translate("el tercero el ataque."))
  print(str(tf5) + "  " + "" + colorama.Fore.RED + traductor.translate("¡El cuarto es para valientes.") + " " + colorama.Fore.LIGHTYELLOW_EX + traductor.translate("¡Elige!"))
  input("")
  os.system("clear")

  print(str(tf1) + "  " + "")
  print(str(tf2) + "  " + "")
  print(str(tf3) + "  " + traductor.translate("Parece que ya has aprendido a jugar,") + colorama.Fore.LIGHTYELLOW_EX + " " + traductor.translate("¿quieres empezar una partida?"))
  print(str(tf4) + "  " + "")
  print(str(tf5) + "  " + "")


  input("")
  os.system("clear")
  elejir_personaje()
#partida personalizada
def partida_personalizada():
  global lang
  traductor = GoogleTranslator(source='es', target=lang)
  global magic_creatures
  global start_a, class_result, life_max, life_max_temp, life, mana_max, mana_max_temp, mana, atac, end_life, end_mana, end_atac, e_life_max, e_life, e_mana_max, e_mana, e_atac, life_potion, mana_potion, e_life_potion, e_mana_potion, mana_max_temp, mana_max, life_max_temp, life_max, end_life, end_mana, end_atac, end_e_life, end_e_mana, end_e_atac
  start_a = "CUSTOM GAME"
  print(colorama.Style.BRIGHT)
  os.system("clear")
  enemy = random.choice(magic_creatures)

  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + colorama.Fore.WHITE + traductor.translate("Si algún valor lo dejas sin decidir se pondrá el valor por defecto. (MAGO)") + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░ \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")

  print(traductor.translate("Empezamos con la vida que deseas tener."))
  life_max_temp = input()
  if (life_max_temp.isspace() or len(life_max_temp) ==0):
    life_max_temp = 100
  try:
    int(life_max_temp)
  except ValueError:
    life_max_temp = 100
  life = life_max_temp
  end_life = life_max_temp

  os.system("clear")
  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + colorama.Fore.WHITE + traductor.translate("Si algún valor lo dejas sin decidir se pondrá el valor por defecto. (MAGO)") + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░ \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("De acuerdo, ahora con el maná que quieres tener."))
  mana_max_temp = input()
  if (mana_max_temp.isspace() or len(mana_max_temp) ==0):
    mana_max_temp = 100
  try:
    int(mana_max_temp)
  except ValueError:
    mana_max_temp = 100
  mana = mana_max_temp
  end_mana = mana_max_temp
  os.system("clear")
  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + colorama.Fore.WHITE + traductor.translate("Si algún valor lo dejas sin decidir se pondrá el valor por defecto. (MAGO)") + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░ \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("Ahora con el ataque que quieres tener."))
  atac = input()
  if (atac.isspace() or len(atac) ==0):
    atac = 10
  try:
    int(atac)
  except ValueError:
    atac = 10
  atac = int(atac)
  end_atac = atac
  os.system("clear")

  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + traductor.translate("Empezamos con el enemigo, pondremos un ") + "" + str(enemy) + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    " + traductor.translate("Si no se especifican valores pondremos el predeterminado (100)") + "\n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("Elige su vida."))
  e_life = input()
  if (e_life.isspace() or len(e_life) ==0):
    e_life = 100
  try:
    int(e_life)
  except ValueError:
    e_life = 100
  e_life = int(e_life)
  e_life_max = e_life
  end_e_life = e_life

  os.system("clear")
  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + traductor.translate("Empezamos con el enemigo, pondremos un ") + "" + str(enemy) + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    " + traductor.translate("Si no se especifican valores pondremos el predeterminado (100)") + "\n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("Ahora su maná."))
  e_mana = input()
  if (e_mana.isspace() or len(e_mana) ==0):
    e_mana = 100
  try:
    int(e_mana)
  except ValueError:
    e_mana = 100
  e_mana = int(e_mana)
  e_mana_max = e_mana
  end_e_mana = e_mana
  os.system("clear")
  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + traductor.translate("Empezamos con el enemigo, pondremos un ") + "" + str(enemy) + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    " + traductor.translate("Si no se especifican valores pondremos el predeterminado (100)") + "\n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("Y ahora el daño que causa."))
  e_atac = input()
  if (e_atac.isspace() or len(e_atac) ==0):
    e_atac = 10
  try:
    int(e_atac)
  except ValueError:
    e_atac = 10
  e_atac = int(e_atac)
  end_e_atac = e_atac
  os.system("clear")

  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + traductor.translate("Perfecto, una vez terminado esto, quieres pociones?") + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    " + traductor.translate("Si no se especifica se pondrán 10 en cada uno.") + " \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("Elige las pociones de vida."))
  life_potion = input()
  if (life_potion.isspace() or len(life_potion) ==0):
    life_potion = 10
  try:
    int(life_potion)
  except ValueError:
    life_potion = 10
  life_potion = int(life_potion)
  os.system("clear")
  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + traductor.translate("Perfecto, una vez terminado esto, quieres pociones?") + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    " + traductor.translate("Si no se especifica se pondrán 10 en cada uno.") + " \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("Elige las pociones de maná."))
  mana_potion = input()
  if (mana_potion.isspace() or len(mana_potion) ==0):
    mana_potion = 10
  try:
    int(mana_potion)
  except ValueError:
    mana_potion = 10
  mana_potion = int(mana_potion)
  os.system("clear")
  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + traductor.translate("Perfecto, una vez terminado esto, quieres pociones?") + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    " + traductor.translate("Si no se especifica se pondrán 10 en cada uno.") + " \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("Elige las pociones de vida del enemigo."))
  e_life_potion = input()
  if (e_life_potion.isspace() or len(e_life_potion) ==0):
    e_life_potion = 10
  try:
    int(e_life_potion)
  except ValueError:
    e_life_potion = 10
  e_life_potion = int(e_life_potion)
  os.system("clear")
  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Bienvenidos al menú de partidas personalizadas.") + " \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Aquí podréis seleccionar los valores con los que quieres jugar.") + " \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + traductor.translate("Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado.") + " \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + traductor.translate("Perfecto, una vez terminado esto, quieres pociones?") + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    " + traductor.translate("Si no se especifica se pondrán 10 en cada uno.") + " \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print(traductor.translate("Elige las pociones de maná del enemigo."))
  e_mana_potion = input()
  if (e_mana_potion.isspace() or len(e_mana_potion) ==0):
    e_mana_potion = 10
  try:
    int(e_mana_potion)
  except ValueError:
    e_mana_potion = 10
  e_mana_potion = int(e_mana_potion)
  os.system("clear")


  juego()
##############################################################################################
os.system("clear")
cambiar_idioma()