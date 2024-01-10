import os
import random
import bullet
import colorama

colorama.init()

# ======================================================================
# =================       Variables            =========================
# ======================================================================

start_a = 0
clase_result = 0 

vida_max = 0
vida_max_temp = 0
vida = 0
mana_max = 0
mana_max_temp = 0
mana = 0
atac = 0

fin_vida = 0
fin_mana = 0
fin_atac = 0

e_vida_max = 100
e_vida = 100
e_mana_max = 100
e_mana = 100
e_atac = 10

vida_potion = 10
mana_potion = 10
e_vida_potion = 6
e_mana_potion = 10

line_vida = 0
line_mana = 0
line_e_vida = 0
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
potion_line_vida = "💉"

rondas = 0

ne_weapon_old = 0
ne_armor_old = 0
ne_casco_old = 0
ne_weapon_old_temp = 0
ne_armor_old_temp = 0
ne_casco_old_temp= 0

dañototal = 0
curatotal = 0
manatotal = 0
resmanatotal = 0
e_dañototal = 0
e_curatotal = 0
e_manatotal = 0
e_resmanatotal = 0

list_weapon = ["Excalibur", "Blade of Shadows", "Thunderstrike", "Frostbite", "Sword of the Elders", "Bow of Essence", "Lance of Destiny", "Axe of Valor", "Sword of Light", "Bow of the Serpent", "Lance of the Titan", "Machete of the Ancients", "Ironclad Sword", "Steelbow", "Lance of the Sea", "Machete of Fury", "Dwarven Blade", "Skyward Bow", "Lance of the Abyss", "Machete of Chaos", "Adamantine Sword", "Arcane Bow", "Lance of Spectres", "Machete of the Void", "Ruby Sword", "Emerald Bow", "Lance of Justice", "Machete of Legends", "Crimson Blade", "Silver Bow", "Lance of Kings", "Machete of Storms", "Vorpal Sword", "Ivory Bow", "Lance of Hope", "Machete of Radiance", "Ethereal Blade", "Phoenix Bow", "Lance of Salvation", "Machete of Wisdom", "Onyx Blade", "Eclipse Bow", "Lance of Illusion", "Machete of Truth", "Demonsbane Sword", "Soulfire Bow", "Lance of Redemption", "Machete of Destiny", "Seraphic Blade", "Stellar Bow", "Lance of Eternity", "Machete of Infinity"]
list_armor = ["Power Armor", "Dragonplate Armor", "Daedric Armor", "T-51b Power Armor", "X-01 Power Armor", "Scorched Sierra Power Armor", "Lorenzos Suit", "Framework", "Raider Power Armor", "T-45 power armor", "Leather Armor", "Combat Armor", "Metal Armor", "Robocoat", "Tribal Power Armor", "Mistress of Mystery Armor", "Bone Armor", "Wood Armor", "Bamboo Armor", "Levantadoras de minerales", "Fencing Armor", "Knight Armor", "Crystal Armor", "Battle Armor", "Miner Gear", "Gold Armor", "Space Armor", "Plastic Armor", "Manta Armor", "Steel Armor", "Sophie Suit", "Rubber Armor", "McGill Armor", "Carbon armor", "Cornerstone Armor", "Sirje Armor", "Tatata Armor", "Zerog Armor", "Byte Armor", "Wreck Armor", "Ardent Armor", "Crystal Armor", "Canary Armor", "Pebbled Armor", "Tomorrow Armor", "Tyles Armor", "Golden Armor", "Warrior Armor", "Titanium Armor", "Rusty Armor", "Cave Armor"]
list_helmets = ["Amulet of Strength", "Necklace of Wisdom", "Pendant of Power", "Charm of Courage", "Talisman of Agility", "Crystal Choker", "Pendant of the Elements", "Ruby Amulet", "Emerald Necklace", "Sapphire Pendant", "Diamond Choker", "Necklace of the Serpent", "Lunar Locket", "Necklace of the Abyss", "Pendant of Destiny", "Glowing Talisman", "Necklace of Radiance", "Amulet of the Ancients", "Necklace of the Void", "Onyx Choker", "Ethereal Pendant", "Celestial Charm", "Necklace of the Titans", "Choker of Eternity", "Phoenix Amulet", "Serpentine Locket"]
criaturas_magicas = ["Bigfoot", "Sasquatch", "Wendigo", "Thunderbird", "Chupacabra", "Jersey Devil", "Goblin", "Orc", "Troll", "Dragon", "Unicorn", "Phoenix", "Cerberus", "Nymph", "Banshee", "Griffin", "Sphinx", "Giant", "Gorgon", "Minotaur", "Giant Spider", "Werewolf", "Vampire", "Golem", "Kraken", "Siren", "Centaur", "Mermaid", "Chimera", "Fairy", "Tengu", "Yeti", "Hydra", "Cyclops", "Pegasus", "Salamander", "Harpy", "Medusa", "Chimera"]



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

def mana_vida_e_vida():
  global vida, mana, e_vida, e_mana, line_vida, line_mana, line_e_vida
  global line_e_mana, vida_max, mana_max, e_vida_max, e_mana_max
  global mana_potion, vida_potion, line_potion, rondas

  if  vida == (vida_max * 0):
    line_vida = line_0 + " ❤ "
  elif vida <= (vida_max * 0.1):
    line_vida = line_10 + " ❤ "
  elif vida <= (vida_max * 0.2):
    line_vida = line_20 + " ❤ "
  elif vida <= (vida_max * 0.3):
    line_vida = line_30 + " ❤ "
  elif vida <= (vida_max * 0.4):
    line_vida = line_40 + " ❤ "
  elif vida <= (vida_max * 0.5):
    line_vida = line_50 + " ❤ "
  elif vida <= (vida_max * 0.6):
    line_vida = line_60 + " ❤ "
  elif vida <= (vida_max * 0.7):
    line_vida = line_70 + " ❤ "
  elif vida <= (vida_max * 0.8):
    line_vida = line_80 + " ❤ "
  elif vida <= (vida_max * 0.9):
    line_vida = line_90 + " ❤ "
  elif vida <= (vida_max * 1):
    line_vida = line_100 + " ❤ "

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

  if e_vida <= (e_vida_max * 0):
    line_e_vida = line_0 + " 🔥"
  elif e_vida <= (e_vida_max * 0.1):
    line_e_vida = line_10 + " 🔥"
  elif e_vida <= (e_vida_max * 0.2):
    line_e_vida = line_20 + " 🔥"
  elif e_vida <= (e_vida_max * 0.3):
    line_e_vida = line_30 + " 🔥"
  elif e_vida <= (e_vida_max * 0.4):
    line_e_vida = line_40 + " 🔥"
  elif e_vida <= (e_vida_max * 0.5):
    line_e_vida = line_50 + " 🔥"
  elif e_vida <= (e_vida_max * 0.6):
    line_e_vida = line_60 + " 🔥"
  elif e_vida <= (e_vida_max * 0.7):
    line_e_vida = line_70 + " 🔥"
  elif e_vida <= (e_vida_max * 0.8):
    line_e_vida = line_80 + " 🔥"
  elif e_vida <= (e_vida_max * 0.9):
    line_e_vida = line_90 + " 🔥"
  elif e_vida <= (e_vida_max * 1):
    line_e_vida = line_100 + " 🔥"
  mana_max = mana_max_temp 
  vida_max = vida_max_temp
  if mana_potion > 20:
    mana_potion = 20
  if vida_potion > 20:
    vida_potion = 20


  datos = [
    {
        "nombre": colorama.Fore.BLUE + str(line_mana),
        "promedio": "{:.0f}".format(mana) + " / " + "{:.0f}".format(mana_max),
        "potion": str(potion_line_mana * mana_potion),
    },
    {
      "nombre": colorama.Fore.LIGHTGREEN_EX + str(line_vida),
      "promedio": "" + "{:.0f}".format(vida) + " / " + "{:.0f}".format(vida_max),
      "potion": str(potion_line_vida * vida_potion),
    },
    {
      "nombre": colorama.Fore.RED + str(line_e_vida),
      "promedio": "{:.0f}".format(e_vida) + " / " + "{:.0f}".format(e_vida_max),
      "potion": str(colorama.Fore.WHITE + "rondas: " + colorama.Fore.GREEN + colorama.Style.BRIGHT + str(rondas)),
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
def vida_potion_act():
  global vida, vida_potion, curatotal
  vida += (vida_max * 0.38)
  vida_potion -= 1
  curatotal += (vida_max * 0.38)
  if vida > vida_max:
    vida = vida_max 
# accion pocion de mana
def mana_potion_act():
  global mana, mana_potion, resmanatotal
  mana += (mana_max * 0.25)
  resmanatotal += (mana_max * 0.25)
  mana_potion -= 1
  if mana > mana_max:
    mana = mana_max 
# accion pocion de vida enemigo
def e_vida_potion_act():
  global e_vida, e_vida_potion, e_curatotal
  e_vida += (e_vida * 0.17) 
  e_vida_potion -= 1
  e_curatotal += (e_vida * 0.17)
  if e_vida > e_vida_max:
    e_vida = e_vida_max 
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
  act_1 = 1
  while act_1 == 1:
    surrender()
    mana_vida_e_vida()
    global mana, vida, e_vida, dañototal, manatotal
    player_act = bullet.Bullet(
      prompt = "\nElije accion: ",
      choices = ["Atacar", "Curar", "Restaurar mana"],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == ('Atacar', 0) and mana >= 10:
      mana -= 10
      e_vida -= atac
      dañototal += atac
      manatotal += 10
      act_1 = 0
      print("Has atacado al enemigo")
    elif player_act_result == ('Curar', 1) and vida_potion >= 1:
      vida_potion_act()
      act_1 = 0
    elif player_act_result == ('Restaurar mana', 2) and mana_potion >= 1:
      mana_potion_act()
      act_1 = 0
    else:
      act_1 = 1
    os.system("clear")
  os.system("clear") 
# ataque del npc
def npc_act():
  global e_vida, e_mana, vida, mana, e_vida_max, e_mana_max, vida_max, mana_max, e_manatotal
  global e_vida_potion, e_mana_potion, vida_potion, mana_potion, e_atac, e_dañototal
  global e_resmanatotal

  # si e_vida < vida i e_vida > (e_vidamax 50%) = curar
  # si evida > vida i emana > (emanamax 30%) = atacar
  # si emana > (emanamax 30%) = restaurar mana

  if e_mana <= (e_mana_max * 0.3) and e_mana_potion != 0 :
    e_mana_potion_act()
    print("1")
  elif e_vida < vida and e_vida < (e_vida_max * 0.5):
    e_vida_potion_act()
    vida -= (e_atac * 0.5)
    e_mana -= 10
    e_dañototal += e_atac
    e_manatotal += 10
    print("2")
  elif e_mana > (e_mana_max * 0.3):
    vida -= e_atac
    e_mana -= 10
    e_dañototal += e_atac
    e_manatotal += 10
    print("3")
  elif e_mana <= (e_mana_max * 0.3) and e_mana_potion == 0 :
    e_mana_potion = 1
    print("4") 
# restauracion de vida del npc y mejora de sus habilidades
def npc_dead():
  global e_vida, e_vida_max, e_mana, e_mana_max, e_vida_potion, e_mana_potion, e_atac
  npcdead = random.randint(1,3)
  if npcdead == 1:
    e_atac = int(e_atac + 5) 
  elif npcdead == 2:
    e_mana_max += int(e_mana_max * 0.1)  
  elif npcdead == 3:
    e_vida_max += int(e_vida_max * 0.1)
  e_vida_max = int(e_vida_max + (e_vida_max * 0.1))
  e_mana_max = int(e_mana_max + (e_mana_max * 0.1))
  e_atac = int(e_atac + (e_atac * 0.2))
  e_vida = e_vida_max
  e_mana = e_mana_max
  e_vida_potion = 10
  e_mana_potion = 10 
# (WIN) mensaje, selector de mejoras i restauracion 
def player_win():
  global vida, mana, mana_potion, vida_potion, mana_max, vida_max, atac
  global vida, mana, vida_potion, mana_potion, mana_max, vida_max, atac
  global mana_max_temp, vida_max_temp, rondas, winimg
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
  print("Se te ha curado un +50%")
  print(colorama.Fore.RESET + colorama.Style.NORMAL + "Has conseguido un cofre")
  win = bullet.Bullet(
    prompt = "\nEscoje tu premio: ",
    choices = [ "mas ataque", "mas mana", "mas vida"],
    indent = 0,
    align = 5, 
    margin = 2,
    shift = 0,
    bullet = "",
    pad_right = 5,
    return_index = True
  )
  win_result = win.launch()
  if win_result == ('mas ataque', 0):
    atac = int(atac + 5) 
  elif win_result == ('mas mana', 1):
    mana_max = int(mana_max * 1.1)  # Increase by 10%
  elif win_result == ('mas vida', 2):
    vida_max = int(vida_max * 1.1)  # Increase by 10%
  mana += mana_max * 0.8
  vida += vida_max * 0.89
  mana_max_temp = mana_max
  vida_max_temp = vida_max
  if vida > vida_max:
    vida = vida_max
  if mana > mana_max:
    mana = mana_max 
  os.system("clear")

  global list_armor, list_weapon, list_helmets, criaturas_magicas

  nombre_enemigo = random.choice(criaturas_magicas)
  print(colorama.Fore.BLUE + "Bienvenido a la nueva sala. Te enfrentarás a un " + colorama.Fore.LIGHTRED_EX + str(nombre_enemigo) + colorama.Fore.BLUE + " con " + str(e_vida) + " puntos de vida" + colorama.Fore.RESET)  

  mana_max = int(mana_max)
  vida_max = int(vida_max)
  ne_casco_old = 0
  ne_weapon_old = 0
  ne_armadura_old = 0
  ne_casco = colorama.Fore.BLUE + random.choice(list_helmets)
  ne_armadura = colorama.Fore.LIGHTGREEN_EX + random.choice(list_armor)
  ne_arma = colorama.Fore.CYAN + random.choice(list_weapon)
  ne_1 = random.randint(1, 3)
  ne = bullet.Bullet(
    prompt = "\nEscoje tu Arma: ",
    choices = [str(ne_armadura), str(ne_casco), str(ne_arma), "No necesito arma"],
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
    print("Tu armadura es: " + colorama.Fore.MAGENTA + str(ne_armadura))
    print(colorama.Fore.RESET + "Este armadura te dará " + colorama.Fore.MAGENTA + str(ne_armor_res_val) + colorama.Fore.RESET + " de vida")

    ne_armor_quest = bullet.Bullet(
      prompt = "\nQuieres cambiar: ",
      choices = ["si", "no"],
      indent = 0,
      align = 5,
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
      return_index = True
      )
    ne_armor_questresult = ne_armor_quest.launch()
    if ne_armor_questresult == ('si', 0):
      vida_max_temp += ne_armor_res_val - ne_armadura_old
      if vida_max_temp != (vida_max_temp + ne_armor_res_val):
        vida_max_temp = int(vida_max + ne_armor_res_val)
      vida += int(ne_armor_res_val - ne_armadura_old)
      ne_armadura_old_temp = int(ne_armor_res_val)
    elif ne_armor_questresult == ('no', 1):
      pass

  elif ne_result == (str(ne_casco), 1):
    os.system("clear")
    ne_helmet_res_val = random.randint(5 , 50)
    print("Tu casco es: " + colorama.Fore.MAGENTA + str(ne_casco))
    print(colorama.Fore.RESET + "Este elemento te dará " + colorama.Fore.MAGENTA + str(ne_helmet_res_val) + colorama.Fore.RESET + " de mana")
  
    ne_helmet_quest = bullet.Bullet(
      prompt = "\nQuieres cambiar: ",
      choices = ["si", "no"],
      indent = 0,
      align = 5,  
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
      return_index = True
      )
    ne_helmet_questresult = ne_helmet_quest.launch()
    if ne_helmet_questresult == ('si', 0):
      mana_max_temp += ne_helmet_res_val - ne_casco_old_temp
      if mana_max_temp != (mana_max_temp + ne_helmet_res_val):
        mana_max_temp = int(mana_max_temp + ne_helmet_res_val)
      mana += int(ne_helmet_res_val - ne_casco_old_temp)
      ne_casco_old_temp = int(ne_helmet_res_val)
    elif ne_helmet_questresult == ('no', 1):
      pass

  elif ne_result == (str(ne_arma), 2):
    os.system("clear")
    ne_weapon_res_val = random.randint(5 , 50)
    print("Tu arma es: " + colorama.Fore.MAGENTA + str(ne_arma))
    print(colorama.Fore.RESET + "Esta arma te dará " + colorama.Fore.MAGENTA + str(ne_weapon_res_val) + colorama.Fore.RESET + " de daño adicional")

    ne_weapon_quest = bullet.Bullet(
      prompt = "\nQuieres cambiar: ",
      choices = ["si", "no"],
      indent = 0,
      align = 5,
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
      return_index = True
      )
    ne_weapon_questresult = ne_weapon_quest.launch()
    if ne_weapon_questresult == ('si', 0):
      atac += ne_weapon_res_val - ne_weapon_old
      if atac != (atac + ne_weapon_res_val):
        atac = int(atac + ne_weapon_res_val)
      ne_weapon_old_temp = int(ne_weapon_res_val)
    elif ne_weapon_questresult == ('no', 1):
      pass

  elif ne_result == ('No necesito arma', 3):
    pass
# (LOOSE) mensaje de perder
def player_loose():# (LOOSE) mensaje de perder
  global rondas, game, vida, vida_max
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

  print("Has sobrevivido " + str(rondas) + " rondas.")
  playerloose = input("Has perdido, pulsa ENTER para salir")
  if playerloose == "revive":
    game = 1
    vida = (vida_max*0.259876382376)
  else:
    game = 0
    vida = 0
    finish()
# Cofre random pociones
def random_chest():
  global e_vida, e_mana, vida, mana, e_vida_max, e_mana_max, vida_max, mana_max
  global e_vida_potion, e_mana_potion, vida_potion, mana_potion, e_atac
  chest = random.randint(1, 5000)
  if chest < 15:
    vida_potion +=  random.randint(1, 3)
  elif chest < 30:
    mana_potion +=  random.randint(1, 2)  
# cofre random pociones enemigo
def e_random_chest():
  global e_vida, e_mana, vida, mana, e_vida_max, e_mana_max, vida_max, mana_max
  global e_vida_potion, e_mana_potion, vida_potion, mana_potion, e_atac
  e_chest = random.randint(1, 5000)
  if e_chest < 10:
    e_vida_potion +=  random.randint(1, 2)
  elif e_chest < 20:
    e_mana_potion +=  random.randint(1, 3) 
# selector de nuevo elemento y explicar nueva sala
def new_enemy():
 pass
# ANTIbloqueo de parida por falta de pociones
def surrender():
  global vida_potion, mana_potion, vida 
  if vida_potion == 0 and mana_potion == 0:
    vida = 0
    player_loose()
  else:
    pass
# creditos
def finish():
  global vida, mana, vida_max, mana_max, vida_potion, mana_potion, e_curatotal
  global dañototal, manatotal, vidatotal, vida_total, mana_total, rondas
  global e_vida, e_mana, e_vida_max, e_mana_max, e_vida_potion, e_mana_potion
  global resmanatotal, e_dañototal, e_manatotal, e_vidatotal, e_vida_total
  global e_resmanatotal, e_dañototal, e_manatotal, e_vidatotal, curatotal
  global clase_result, start_a, game, clase_result
  global fin_vida_max, fin_vida, fin_mana_max, fin_mana, fin_atac
  
  if clase_result == ('Mago = vida 100 mana 100 atk 10', 0):
    fin_vida_max = 100
    fin_vida = 100
    fin_mana_max = 100
    fin_mana = 100
    fin_atac = 10.7
  elif clase_result == ('Arquero = vida 75 mana 100 atk 15', 1):
    fin_vida_max = 75
    fin_vida = 75
    fin_mana_max = 90
    fin_mana = 90
    fin_atac = 15.7
  elif clase_result == ('Guerrero = vida 130 mana 100 atk 7', 2):
    fin_vida_max = 130
    fin_vida = 130
    fin_mana_max = 150
    fin_mana = 150
    fin_atac = 7.9

  if start_a == "easteregg":
    fin_vida_max = 100
    fin_vida = 1
    fin_mana_max = 100
    fin_mana = 10
    fin_atac = 1
  elif start_a == "easymode":
    fin_vida_max = 999999999999999
    fin_vida = 999999999999999
    fin_mana_max = 999999999999999
    fin_mana = 999999999999999
    fin_atac = 999999999999999

  os.system("clear")
  print(colorama.Fore.YELLOW + "████████████████████████████████████████" + colorama.Fore.MAGENTA + "    ██████╗░██╗░░░██╗" + colorama.Fore.RED + "██████╗░██████╗░░██████╗░")
  print(colorama.Fore.YELLOW + "██████████████████▒────██▓██████████████" + colorama.Fore.MAGENTA + "    ██╔══██╗╚██╗░██╔╝" + colorama.Fore.RED + "██╔══██╗██╔══██╗██╔════╝░")
  print(colorama.Fore.YELLOW + "█████████████═──────────█▓▓█████████████" + colorama.Fore.MAGENTA + "    ██████╔╝░╚████╔╝░" + colorama.Fore.RED + "██████╔╝██████╔╝██║░░██╗░")
  print(colorama.Fore.YELLOW + "██████████▓───────────████══██████─█████" + colorama.Fore.LIGHTMAGENTA_EX + "    ██╔═══╝░░░╚██╔╝░░" + colorama.Fore.LIGHTRED_EX + "██╔══██╗██╔═══╝░██║░░╚██╗")
  print(colorama.Fore.YELLOW + "█████████────────────══─██──████─────███" + colorama.Fore.LIGHTMAGENTA_EX + "    ██║░░░░░░░░██║░░░" + colorama.Fore.LIGHTRED_EX + "██║░░██║██║░░░░░╚██████╔╝")
  print(colorama.Fore.YELLOW + "████████─────" + colorama.Fore.LIGHTYELLOW_EX + "▒────██" + colorama.Fore.YELLOW + "────█─█─███──██──▓██" + colorama.Fore.LIGHTMAGENTA_EX + "    ╚═╝░░░░░░░░╚═╝░░░" + colorama.Fore.LIGHTRED_EX + "╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░")
  print(colorama.Fore.YELLOW + "████▓▓██─────" + colorama.Fore.LIGHTYELLOW_EX + "█──▓███" + colorama.Fore.YELLOW + "────────▓██─████──██")
  print(colorama.Fore.YELLOW + "███───██───" + colorama.Fore.LIGHTYELLOW_EX + "█▒█──█──█▓" + colorama.Fore.YELLOW + "───────▓█─▒████──██" + "    Estadisticas Jugador")
  print(colorama.Fore.YELLOW + "███──▓███──" + colorama.Fore.LIGHTYELLOW_EX + "███▓─═█──█▓" + colorama.Fore.YELLOW + "───────██▓█████──█" + "      Rondas  " + str(rondas))
  print(colorama.Fore.YELLOW + "███──████─═" + colorama.Fore.LIGHTYELLOW_EX + "███▒─█▒──██" + colorama.Fore.YELLOW + "───────████████──█" + "      Daño total causado: " + str(dañototal))
  print(colorama.Fore.YELLOW + "██──▓████──" + colorama.Fore.LIGHTYELLOW_EX + "███──███─▓█" + colorama.Fore.YELLOW + "───────████████──█" + "      Maná total gastado: " + str(manatotal))
  print(colorama.Fore.YELLOW + "██──█████─" + colorama.Fore.LIGHTYELLOW_EX + "██═█─█▒═█─██" + colorama.Fore.YELLOW + "───────████████─██" + "      Vida total ganada: " + str(curatotal))
  print(colorama.Fore.YELLOW + "██──█████─═" + colorama.Fore.LIGHTYELLOW_EX + "█─█────█─█▓" + colorama.Fore.YELLOW + "───────███████──██" + "      Mana total ganada: " + str(resmanatotal))
  print(colorama.Fore.YELLOW + "██──█████─────────" + colorama.Fore.LIGHTYELLOW_EX + "█─█▒" + colorama.Fore.YELLOW + "───────███████─███" + "      Pociones de vida sobrantes  " + str(vida_potion))
  print(colorama.Fore.YELLOW + "██──█████─────────" + colorama.Fore.LIGHTYELLOW_EX + "█─█" + colorama.Fore.YELLOW + "────────██████──███" + "      Pociones de maná sobrantes  " + str(mana_potion))
  print(colorama.Fore.YELLOW + "██──▓████─────────" + colorama.Fore.LIGHTYELLOW_EX + "█─█" + colorama.Fore.YELLOW + "───────═█████──████")
  print(colorama.Fore.YELLOW + "██───████▒────────" + colorama.Fore.LIGHTYELLOW_EX + "█─█" + colorama.Fore.YELLOW + "───────▓████──█████" + "    Estadisticas enemigo")
  print(colorama.Fore.YELLOW + "██───████▓───────" + colorama.Fore.LIGHTYELLOW_EX + "▒█─█" + colorama.Fore.YELLOW + "───────████──██████" + "      Daño total causado: " + str(e_dañototal))
  print(colorama.Fore.YELLOW + "██▒───████───────" + colorama.Fore.LIGHTYELLOW_EX + "▒█─█" + colorama.Fore.YELLOW + "───────███──███████" + "      Maná total gastado: " + str(e_manatotal))
  print(colorama.Fore.YELLOW + "███────███───────" + colorama.Fore.LIGHTYELLOW_EX + "▓█─█" + colorama.Fore.YELLOW + "───────██──████████" + "      Vida total ganada: " + str(e_curatotal))
  print(colorama.Fore.YELLOW + "███═───███───────" + colorama.Fore.LIGHTYELLOW_EX + "██─█" + colorama.Fore.YELLOW + "──────▒█▓─█████████" + "      Mana total ganada: " + str(e_resmanatotal))
  print(colorama.Fore.YELLOW + "████────██▒──────" + colorama.Fore.LIGHTYELLOW_EX + "█▒─███" + colorama.Fore.YELLOW + "────██─██████████" + "      Pociones de vida sobrantes  " + str(e_vida_potion))
  print(colorama.Fore.YELLOW + "████────██───" + colorama.Fore.LIGHTYELLOW_EX + "▒▓▓█───██" + colorama.Fore.YELLOW + "────█▒─███████████" + "      Pociones de maná sobrantes  " + str(e_mana_potion))
  print(colorama.Fore.YELLOW + "█████────█───" + colorama.Fore.LIGHTYELLOW_EX + "███▓───██" + colorama.Fore.YELLOW + "────█─▓███████████")
  print(colorama.Fore.YELLOW + "██████───██──" + colorama.Fore.LIGHTYELLOW_EX + "▓█─────█▓" + colorama.Fore.YELLOW + "───██─████████████" + "    Stats Iniciales      " + str(start_a))
  print(colorama.Fore.YELLOW + "███████───█──═" + colorama.Fore.LIGHTYELLOW_EX + "█─█████" + colorama.Fore.YELLOW + "═───█──▓███████████" + "        " + "Vida inicial  " + str(fin_vida))
  print(colorama.Fore.YELLOW + "███████───██──" + colorama.Fore.LIGHTYELLOW_EX + "██████▒" + colorama.Fore.YELLOW + "────█──────████████" + "        " + "Mana inicial  " + str(fin_mana))
  print(colorama.Fore.YELLOW + "████████──██──" + colorama.Fore.LIGHTYELLOW_EX + "▒" + colorama.Fore.YELLOW + "─────────██──────████████" + "        " + "Ataque inicial  " + str(fin_atac))
  print(colorama.Fore.YELLOW + "████████──▓█▓───────────███────█████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "████████═─▓██──────────█████─▒██████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "Echo por:")
  print(colorama.Fore.YELLOW + "████████▓─████────────▓█████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "      " + "USR1 y USR2")
  print(colorama.Fore.YELLOW + "████████──████▓──────═██████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "███████──██████▓────▓███████████████████" + colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "    " + "'Si la vida te da limones, hazte un bocata.'")
  print(colorama.Fore.YELLOW + "██████▒─████████████████████████████████" + colorama.Fore.RED + colorama.Style.BRIGHT + "    " + "  - USR1")
  print(colorama.Fore.YELLOW + "████████████████▒▒▓──███████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "████████████████▒───▓███████████████████" + colorama.Fore.MAGENTA + colorama.Style.BRIGHT + "    " + "'Sonrie porque todos los días son igual de malos.'")
  print(colorama.Fore.YELLOW + "█████████████████───████████████████████" + colorama.Fore.RED + colorama.Style.BRIGHT + "    " + "  - USR2")
  print(colorama.Fore.YELLOW + "█████████████████──▒████████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "████████████████████████████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    Gracias por jugar a " + colorama.Fore.MAGENTA + "PY" + colorama.Fore.RED + "RPG" )
  print(colorama.Fore.YELLOW + "█████████████████▓▒────█████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    Este juego ha tomado muuuchas horas y ")
  print(colorama.Fore.YELLOW + "███████████████─────────▒███████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    lineas y " + colorama.Fore.RED + "espero que no nos suspendan por esto.")
  print(colorama.Fore.YELLOW + "██████████████══█▓██████████████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "Puede que hayamos perdido horas de FOL para terminar esto")
  print(colorama.Fore.YELLOW + "█████████████████████████████▓██████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "████████████──────────────▓█▒▒██████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "Apruebanos y te dejamos poner la frase que quieras")
  print(colorama.Fore.YELLOW + "█████████▒██─────═─══════─██▒▓██████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "█████████▓▓█──══════════──██▒███████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "██████████▒█▒─══─═────────█▓▒███████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "██████████▒██──────────▒─▒█▓▓███████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "██████████▒▓█─▒████████████▒▓███████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "")
  print(colorama.Fore.YELLOW + "██████████▓▒███████▓▓▓▓▓▒▒▒▒████████████" + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    " + "Si le das a enter vas a volver al menu.")
  print(colorama.Fore.YELLOW + "███████████▒█▓▓▒▒▒▒▓▓▓▓▓████████████████"   + colorama.Fore.WHITE + colorama.Style.BRIGHT + "    Escribe 'start' para continuar la partida")
  end = input(colorama.Fore.YELLOW + "███████████▓▓▓▓█████████████████████████")
  game = 0
  if end == "loose":
    player_loose()
  elif end == "start":
    if vida == 0:
      game = 0
    else:
      game = 1
      player_win()
  else:
    menu()
#menu principal
def menu():
  global frases
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
    choices = ["{:^70}".format("Iniciar Partida"), "{:^70}".format("Iniciar Tutorial"), "{:^70}".format("Partida Custom"), "{:^70}".format("Creditos"), "{:^70}".format("Salir"), ], 
    bullet = "",
    bullet_color=bullet.colors.bright(bullet.colors.foreground["cyan"]),
    word_color=bullet.colors.bright(bullet.colors.foreground["yellow"]),
    word_on_switch=bullet.colors.bright(bullet.colors.foreground["yellow"]),
    background_on_switch=bullet.colors.background["black"],
    pad_right = 0
  )

  result = "{:^80}".format(cli.launch())
  if result == "{:^80}".format("Iniciar Partida"):
    tutorial()
  elif result == "{:^80}".format("Iniciar Tutorial"):
    comojugar()
  elif result == "{:^80}".format("Partida Custom"):
    partida_personalizada()
  elif result == "{:^80}".format("Creditos"):
    finish()
  elif result == "{:^80}".format("Salir"):
    exit()

  
# como jugar
def tutorial():

  global start_a, clase_result, vida_max, vida_max_temp, vida, mana_max, mana_max_temp, mana, atac, e_vida_max, e_vida, e_mana_max, e_mana, e_atac, vida_potion, mana_potion, e_vida_potion, e_mana_potion, rondas, clase_result
  global dañototal, curatotal, manatotal, resmanatotal, e_dañototal, e_curatotal, e_manatotal, e_resmanatotal

  
  dañototal = 0
  curatotal = 0
  manatotal = 0
  resmanatotal = 0
  e_dañototal = 0
  e_curatotal = 0
  e_manatotal = 0
  e_resmanatotal = 0
  
  rondas = 0
  start_a = 0
  clase_result = 0

  vida_max = 0
  vida_max_temp = 0
  vida = 0
  mana_max = 0
  mana_max_temp = 0
  mana = 0
  atac = 0

  e_vida_max = 100
  e_vida = 100
  e_mana_max = 100
  e_mana = 100
  e_atac = 10

  vida_potion = 10
  mana_potion = 10
  e_vida_potion = 6
  e_mana_potion = 10
  os.system("clear")
  
  print(colorama.Fore.LIGHTYELLOW_EX + colorama.Style.BRIGHT)

  print(colorama.Fore.MAGENTA + "██████╗░██╗░░░██╗" + colorama.Fore.RED + "██████╗░██████╗░░██████╗░")
  print(colorama.Fore.MAGENTA + "██╔══██╗╚██╗░██╔╝" + colorama.Fore.RED + "██╔══██╗██╔══██╗██╔════╝░")
  print(colorama.Fore.MAGENTA + "██████╔╝░╚████╔╝░" + colorama.Fore.RED + "██████╔╝██████╔╝██║░░██╗░")
  print(colorama.Fore.LIGHTMAGENTA_EX + "██╔═══╝░░░╚██╔╝░░" + colorama.Fore.LIGHTRED_EX + "██╔══██╗██╔═══╝░██║░░╚██╗")
  print(colorama.Fore.LIGHTMAGENTA_EX + "██║░░░░░░░░██║░░░" + colorama.Fore.LIGHTRED_EX + "██║░░██║██║░░░░░╚██████╔╝")
  print(colorama.Fore.LIGHTMAGENTA_EX + "╚═╝░░░░░░░░╚═╝░░░" + colorama.Fore.LIGHTRED_EX + "╚═╝░░╚═╝╚═╝░░░░░░╚═════╝░ \n")
  print(colorama.Fore.WHITE + "Este juego es un RPG en el que has de ir sobreviviendo oleadas. Cuantas más rondas ganes," + colorama.Fore.MAGENTA + " mejor será tu puntuación." + colorama.Fore.WHITE)
  print("Al empezar el juego tendrás que elegir entre " + colorama.Fore.GREEN + "tres personajes" + colorama.Fore.WHITE + ", cada uno es el " + colorama.Fore.RED + "mejor en su habilidad" + colorama.Fore.WHITE + " característica. Durante el ataque habrás de escoger entre curar, atacar y regenerar mana.")
  print("En caso de perder se acabará el juego, pero si ganas recibirás un " + colorama.Fore.YELLOW + "cofre" + colorama.Fore.WHITE + " con varias opciones, elige sabiamente.")
  print("Cada vez que derrotes a un enemigo, te enfrentarás a uno aún más fuerte que el anterior. \n")
  start_a = input("Presiona " + colorama.Fore.LIGHTCYAN_EX + "𝗘𝗡𝗧𝗘𝗥" + colorama.Fore.WHITE + " para comenzar" + colorama.Style.RESET_ALL)

  os.system("clear")
  elejir_personaje()
# escoger personaje
def elejir_personaje():
  global vida, vida_max, mana_max, mana, atac, start_a, vida_max_temp, mana_max_temp, mana_temp, atac_temp, vida_temp
  global fin_vida_max, fin_vida, fin_mana_max, fin_mana, fin_atac, e_vida_max, e_vida, e_mana_max, e_mana, e_atac, vida_potion, mana_potion, e_vida_potion, e_mana_potion
  
  e_vida_max = 100
  e_vida = 100
  e_mana_max = 100
  e_mana = 100
  e_atac = 10

  vida_potion = 10
  mana_potion = 10
  e_vida_potion = 6
  e_mana_potion = 10
  print(colorama.Fore.LIGHTYELLOW_EX + colorama.Style.BRIGHT)
  print("█▀▀ █▀█ █▀▄▀█ █▀█   ░░█ █░█ █▀▀ ▄▀█ █▀█ " + colorama.Fore.LIGHTMAGENTA_EX + "▀█" + colorama.Fore.LIGHTYELLOW_EX)
  print("█▄▄ █▄█ █░▀░█ █▄█   █▄█ █▄█ █▄█ █▀█ █▀▄ " + colorama.Fore.LIGHTMAGENTA_EX + "░▄")
  print(colorama.Fore.RESET)
  print("Para moverte entre las diferentes opciones tienes que usar" + colorama.Fore.GREEN + " las teclas 🠕 y 🠗 " + colorama.Fore.WHITE + "y para aceptar tienes que usar " + colorama.Fore.GREEN + "ENTER" + colorama.Fore.WHITE + ".")
  print("Si quieres una partida" + colorama.Fore.LIGHTGREEN_EX + " facil" + colorama.Fore.RESET + ", recomendamos que eligas " + colorama.Fore.RED + "el arquero" + colorama.Fore.WHITE + ".")
  print("Si quieres una partida" + colorama.Fore.LIGHTGREEN_EX + " normal" + colorama.Fore.RESET + ", recomendamos que eligas " + colorama.Fore.RED + "el mago" + colorama.Fore.WHITE + ".")
  print("Si quieres una partida" + colorama.Fore.LIGHTGREEN_EX + " dificil" + colorama.Fore.RESET + ", recomendamos que eligas " + colorama.Fore.RED + "el guerrero" + colorama.Fore.WHITE + ".")
  Mago = colorama.Fore.BLUE + "Mago 🇳🇴🇷🇲🇦🇱"
  Arquero = colorama.Fore.GREEN + "Arquero 🇫🇦🇨🇮🇱"
  Guerrero = colorama.Fore.RED + "Guerrero 🇩🇮🇫🇮🇨🇮🇱"
  clase = bullet.Bullet(
    prompt = "\nEscoje tu clase: ",
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
    vida_max = 100
    vida = 100
    mana_max = 100
    mana = 100
    atac = 10
    fin_vida_max = 100
    fin_vida = 100
    fin_mana_max = 100
    fin_mana = 100
    fin_atac = 10
  elif clase_result == Arquero:
    vida_max = 75
    vida = 75
    mana_max = 90
    mana = 90
    atac = 16
    fin_vida_max = 75
    fin_vida = 75
    fin_mana_max = 90
    fin_mana = 90
    fin_atac = 16
  elif clase_result == Guerrero:
    vida_max = 130
    vida = 130
    mana_max = 150
    mana = 150
    atac = 7
    fin_vida_max = 130
    fin_vida = 130
    fin_mana_max = 150
    fin_mana = 150
    fin_atac = 7
  else:
      print("No es una opcion valida")
      exit()

  if start_a == "easteregg":
    vida_max = 1000
    vida = 1
    mana_max = 1000
    mana = 10
    atac = 5
  elif start_a == "easymode":
    vida_max = 999999999999999
    vida = 999999999999999
    mana_max = 999999999999999
    mana = 999999999999999
    atac = 999999999999999
  else:
    pass

  mana_max_temp = mana_max
  vida_max_temp = vida_max
  juego()
  os.system("clear")


# juego
def juego():
  global vida, game, vida_max, vida_max_temp, mana, mana_max, mana_max_temp, atac, ne_weapon_old, ne_weapon_old_temp, ne_armor_old, ne_armor_old_temp, ne_casco_old, ne_casco_old_temp, ne_armadura_old, ne_armadura_old_temp, e_vida, e_vida_max, e_vida_max_temp, e_mana, e_mana_max, e_mana_max_temp, e_atac, vida_potion, mana_potion, vida_potion_max, mana_potion_max, e_vida_potion, e_vida_potion_max, e_mana_potion, rondas
  game = 1
  rondas = 0
  vida = int(vida)
  mana = int(mana)
  atac = int(atac)
  vida_max = int(vida_max)
  mana_max = int(mana_max)
  vida_max_temp = int(vida_max_temp)
  mana_max_temp = int(mana_max_temp)
  e_vida = int(e_vida)
  e_mana = int(e_mana)
  e_atac = int(e_atac)
  e_vida_max = int(e_vida_max)
  e_mana_max = int(e_mana_max)
  vida_potion = int(vida_potion)
  mana_potion = int(mana_potion)
  e_vida_potion = int(e_vida_potion)
  e_mana_potion = int(e_mana_potion)
  while game == 1:
    if vida <= 0:
      player_loose()
      if game == 0:
        break
      else:
        pass
    random_chest()
    e_random_chest()
    vida_max = vida_max_temp
    mana_max = mana_max_temp
    ne_weapon_old = ne_weapon_old_temp
    ne_armor_old = ne_armor_old_temp
    ne_casco_old = ne_casco_old_temp
    os.system("clear")
    player_act_def()
    npc_act()
    if e_vida <= 0:
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
  global start_a, clase_result, vida_max, vida_max_temp, vida, mana_max, mana_max_temp, mana, atac, fin_vida, fin_mana, fin_atac, e_vida_max, e_vida, e_mana_max, e_mana, e_atac, vida_potion, mana_potion, e_vida_potion, e_mana_potion
  
  os.system("clear")
  tf1 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "─────" + colorama.Fore.MAGENTA + "█" + colorama.Fore.WHITE + "─" + colorama.Fore.LIGHTRED_EX + "▄▀█" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "█▀▄" + colorama.Fore.WHITE + "─" + colorama.Fore.MAGENTA + "█" + colorama.Fore.WHITE + "─────"
  tf2 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "────" + colorama.Fore.MAGENTA + "▐▌" + colorama.Fore.WHITE + "──────────" + colorama.Fore.MAGENTA + "▐▌" + colorama.Fore.WHITE + "────"
  tf3 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "────" + colorama.Fore.MAGENTA + "█▌" + colorama.Fore.LIGHTRED_EX + "▀▄" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▄▄" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▄▀" + colorama.Fore.MAGENTA + "▐█" + colorama.Fore.WHITE + "────"
  tf4 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "───" + colorama.Fore.MAGENTA + "▐██" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▀▀" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▀▀" + colorama.Fore.WHITE + "──" + colorama.Fore.MAGENTA + "██▌" + colorama.Fore.WHITE + "───"
  tf5 = colorama.Fore.WHITE + colorama.Style.BRIGHT + "──" + colorama.Fore.MAGENTA + "▄████▄" + colorama.Fore.WHITE + "──" + colorama.Fore.LIGHTRED_EX + "▐▌" + colorama.Fore.WHITE + "──" + colorama.Fore.MAGENTA + "▄████▄" + colorama.Fore.WHITE + "──"
  
  print(str(tf1) + "  " + "Hola jugador!")
  print(str(tf2) + "  " + "Bienvenido a " + colorama.Fore.RED + "PYRPG!!")
  print(str(tf3) + "  " + "Parece que eres nuevo en este mundo," + colorama.Fore.MAGENTA + " ¿quieres aprender cómo jugar?")
  print(str(tf4) + "  " + "Si es así, " + colorama.Fore.GREEN + "te enseñaremos" + colorama.Fore.WHITE + " todo lo que necesitas")
  print(str(tf5) + "  " + "Dale a" + colorama.Fore.RED + " ENTER" + colorama.Fore.WHITE + " para continuar")
  input("")
  os.system("clear")

  print(str(tf1) + "  " + "Cuando empiezes te van a dejar elejir entre" + colorama.Fore.YELLOW + " tres personajes" + colorama.Fore.WHITE + ", estos son:")
  print(str(tf2) + "  " + "" + colorama.Fore.GREEN + "Arquero:" + colorama.Fore.WHITE + " Facil de usar gracias a la cantidad de " + colorama.Fore.GREEN + "ataque" + colorama.Fore.WHITE + " que tiene.")
  print(str(tf3) + "  " + "" + colorama.Fore.BLUE + "Mago:" + colorama.Fore.WHITE + " Modo de juego " + colorama.Fore.BLUE + "normal" + colorama.Fore.WHITE + " y ataque " + colorama.Fore.BLUE + "normal.")
  print(str(tf4) + "  " + "" + colorama.Fore.LIGHTRED_EX + "Guerrero:" + colorama.Fore.WHITE + " Mas " + colorama.Fore.LIGHTRED_EX + "dificil" + colorama.Fore.WHITE + " de usar ya que, aunque tiene" + colorama.Fore.LIGHTRED_EX + " mucha vida" + colorama.Fore.WHITE + ", tiene " + colorama.Fore.LIGHTRED_EX + "poco ataque.")
  print(str(tf5) + "  " + "Dale a ENTER para continuar -Es asi en todas :)-")
  input("")
  os.system("clear")
  print(str(tf1) + "  " + "Este es el " + colorama.Fore.GREEN + "menu principal" + colorama.Fore.WHITE + ", en el cual encontraras" + colorama.Fore.LIGHTYELLOW_EX + " informacion sobre la partida.")
  print(str(tf2) + "  " + "" + colorama.Fore.BLUE + "La linea azul marca tu mana, " + colorama.Fore.WHITE + "este es necesario para poder atacar.")
  print(str(tf3) + "  " + "" + colorama.Fore.GREEN + "La linea verde es tu vida, " + colorama.Fore.WHITE + "ten quidado no baje mucho o podras perder la partida.")
  print(str(tf4) + "  " + "" + colorama.Fore.RED + "La linea roja es la vida de tu enemigo" + colorama.Fore.WHITE + ", es importante que esa este baja, o mas baja que la tuya.")
  print(str(tf5) + "  " + "A la derecha puedes ver la cantidad de pociones que tienes, " + colorama.Fore.LIGHTYELLOW_EX + "estas te ayudaran a tener mas vida y mana.")
  vida_max = 10
  vida_max_temp = 10
  vida = 10
  mana_max = 10
  mana_max_temp = 10
  mana = 10
  e_vida_max = 10
  e_vida = 10
  vida_potion = 4
  mana_potion = 4
  mana_vida_e_vida()
  input("")
  os.system("clear")

  tut1 = 0
  while tut1 == 0:
    print(str(tf1) + "  " + "¡Es tu turno!!")
    print(str(tf2) + "  " + "Tienes tres opciones: " + colorama.Fore.CYAN + "Atacar," + colorama.Fore.BLUE + " restaurar mana o " + colorama.Fore.GREEN + "restaurar vida.")
    print(str(tf3) + "  " + "Empecemos con " + colorama.Fore.CYAN + "atacar" + colorama.Fore.WHITE + ", función esencial para " + colorama.Fore.GREEN + "ganar.")
    print(str(tf4) + "  " + "Cuando ataques " + colorama.Fore.GREEN + "le bajarás la vida al enemigo" + colorama.Fore.RED + ", y viceversa.")
    print(str(tf5) + "  " + "Además te" + colorama.Fore.LIGHTBLUE_EX + " restará mana" + colorama.Fore.WHITE + ", así que no te emociones tanto y " + colorama.Fore.LIGHTYELLOW_EX + "juega con estrategia.")

    mana_vida_e_vida()
    print("Para moverte entre las diferentes opciones tienes que usar" + colorama.Fore.GREEN + " las teclas 🠕 y 🠗 " + colorama.Fore.WHITE + "y para aceptar tienes que usar " + colorama.Fore.GREEN + "ENTER" + colorama.Fore.WHITE + ".")
    player_act = bullet.Bullet(
      prompt = "\nElije accion: ",
      choices = ["Atacar (-10 mana)", "Curar (+20%)", "Restaurar mana (+20%)"],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == ('Atacar (-10 mana)', 0) and mana >= 10:
      tut1 = 1
    elif player_act_result == ('Curar (+20%)', 1) and vida_potion >= 1:
      tut1 = 0
    elif player_act_result == ('Restaurar mana (+20%)', 2) and mana_potion >= 1:
      tut1 = 0

    os.system("clear")
  os.system("clear") 
  os.system("clear")
  
  vida_max = 10
  vida_max_temp = 10
  vida = 10
  mana_max = 10
  mana_max_temp = 10
  mana = 0
  e_vida_max = 10
  e_vida = 5
  vida_potion = 4
  mana_potion = 4
  tut1 = 0
  while tut1 == 0:
    print(str(tf1) + "  " + "")
    print(str(tf2) + "  " + "¡Ahora no puedes atacar!")
    print(str(tf3) + "  " + "¡Necesitas " + colorama.Fore.BLUE + "restaurar tu mana" + colorama.Fore.WHITE + " para poder atacar!")
    print(str(tf4) + "  " + "Para hacerlo selecciona la opción" + colorama.Fore.BLUE + " restaurar mana.")
    print(str(tf5) + "  " + "")
    mana_vida_e_vida()
    player_act = bullet.Bullet(
      prompt = "\nElije accion: ",
      choices = ["Atacar (-10 mana)", "Curar (+20%)", "Restaurar mana (+20%)"],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == ('Atacar (-10 mana)', 0) and mana >= 10:
      tut1 = 0
    elif player_act_result == ('Curar (+20%)', 1) and vida_potion >= 1:
      tut1 = 0
    elif player_act_result == ('Restaurar mana (+20%)', 2) and mana_potion >= 1:
      tut1 = 1

    os.system("clear")
  os.system("clear")

  vida_max = 10
  vida_max_temp = 10
  vida = 5
  mana_max = 10
  mana_max_temp = 10
  mana = 10
  e_vida_max = 10
  e_vida = 5
  vida_potion = 4
  mana_potion = 3
  tut1 = 0
  while tut1 == 0:
    print(str(tf1) + "  " + "")
    print(str(tf2) + "  " + "Parece que te han tocado,")
    print(str(tf3) + "  " + "" + colorama.Fore.RED + "Tienes la vida muy baja, " + colorama.Fore.GREEN + "prueba de curarte")
    print(str(tf4) + "  " + "")
    print(str(tf5) + "  " + "")
    mana_vida_e_vida()
    player_act = bullet.Bullet(
      prompt = "\nElije accion: ",
      choices = ["Atacar (-10 mana)", "Curar (+20%)", "Restaurar mana (+20%)"],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == ('Atacar (-10 mana)', 0) and mana >= 10:
      tut1 = 0
    elif player_act_result == ('Curar (+20%)', 1) and vida_potion >= 1:
      tut1 = 1
    elif player_act_result == ('Restaurar mana (+20%)', 2) and mana_potion >= 1:
      tut1 = 0

    os.system("clear")
  os.system("clear")
  
  vida_max = 10
  vida_max_temp = 10
  vida = 10
  mana_max = 10
  mana_max_temp = 10
  mana = 10
  e_vida_max = 10
  e_vida = 5
  vida_potion = 3
  mana_potion = 3
  tut1 = 0
  while tut1 == 0:
    print(str(tf1) + "  " + "")
    print(str(tf2) + "  " + "¡Ahora" + colorama.Fore.CYAN + " ataca" + colorama.Fore.WHITE + " y " + colorama.Fore.RED + "mátalo!")
    print(str(tf3) + "  " + "")
    print(str(tf4) + "  " + "")
    print(str(tf5) + "  " + "")
    mana_vida_e_vida()
    player_act = bullet.Bullet(
      prompt = "\nElije accion: ",
      choices = ["Atacar (-10 mana)", "Curar (+20%)", "Restaurar mana (+20%)"],
      indent = 0,
      align = 5, 
      margin = 2,
      shift = 0,
      bullet = "",
      pad_right = 5,
    return_index = True
    )
    player_act_result = player_act.launch()
    if player_act_result == ('Atacar (-10 mana)', 0) and mana >= 10:
      tut1 = 1
    elif player_act_result == ('Curar (+20%)', 1) and vida_potion >= 1:
      tut1 = 0
    elif player_act_result == ('Restaurar mana (+20%)', 2) and mana_potion >= 1:
      tut1 = 0

    os.system("clear")
  os.system("clear")
  print(str(tf1) + "  " + "")
  print(str(tf2) + "  " + "¡Perfecto!" + colorama.Fore.LIGHTGREEN_EX + " ¡Has ganado la partida!")
  print(str(tf3) + "  " + "" + colorama.Fore.GREEN + "Cuando ganes," + colorama.Fore.WHITE + " tendrás" + colorama.Fore.LIGHTBLUE_EX + " tres opciones:" + colorama.Fore.CYAN + " ¡Más ataque," + colorama.Fore.BLUE + " más maná o" + colorama.Fore.GREEN + " más vida!")
  print(str(tf4) + "  " + "Elige el más " + colorama.Fore.GREEN + "conveniente para ganar.")
  print(str(tf5) + "  " + "")
  input("")
  os.system("clear")

  print(str(tf1) + "  " + "¡Después pasarás a la siguiente sala," + colorama.Fore.GREEN + " ¡aquí también te dan objetos!")
  print(str(tf2) + "  " + "No te preocupes por los nombres, son raros pero están hechos así")
  print(str(tf3) + "  " + "¡para que no se quejen de las faltas de ortografía!")
  print(str(tf4) + "  " + "" + colorama.Fore.GREEN + "El primero mejora la vida," + colorama.Fore.BLUE + " el segundo el maná y" + colorama.Fore.CYAN + " el tercero el ataque.")
  print(str(tf5) + "  " + "" + colorama.Fore.RED + "¡El cuarto es para valientes. " + colorama.Fore.LIGHTYELLOW_EX + "¡Elige!")
  input("")
  os.system("clear")

  print(str(tf1) + "  " + "")
  print(str(tf2) + "  " + "")
  print(str(tf3) + "  " + "Parece que ya has aprendido a jugar," + colorama.Fore.LIGHTYELLOW_EX + " ¿quieres empezar una partida?")
  print(str(tf4) + "  " + "")
  print(str(tf5) + "  " + "")


  input("")
  os.system("clear")
  elejir_personaje()
#partida personalizada
def partida_personalizada():
  global criaturas_magicas
  global start_a, clase_result, vida_max, vida_max_temp, vida, mana_max, mana_max_temp, mana, atac, fin_vida, fin_mana, fin_atac, e_vida_max, e_vida, e_mana_max, e_mana, e_atac, vida_potion, mana_potion, e_vida_potion, e_mana_potion, mana_max_temp, mana_max, vida_max_temp, vida_max, fin_vida, fin_mana, fin_atac, fin_e_vida, fin_e_mana, fin_e_atac
  start_a = "CUSTOM GAME"
  print(colorama.Style.BRIGHT)
  os.system("clear")
  enemy = random.choice(criaturas_magicas)
  
  print("" + colorama.Fore.WHITE + "░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    " + colorama.Fore.WHITE + "Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    " + colorama.Fore.WHITE + "Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    " + colorama.Fore.WHITE + "Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    " + colorama.Fore.WHITE + "Si algún valor lo dejas sin decidir se pondrá el valor por defecto. (MAGO) \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░ \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  
  print("Empezamos con la vida que deseas tener.")
  vida_max_temp = input()
  if (vida_max_temp.isspace() or len(vida_max_temp) ==0):
    vida_max_temp = 100
  try:
    int(vida_max_temp)
  except ValueError:
    vida_max_temp = 100
  vida = vida_max_temp
  fin_vida = vida_max_temp
  
  os.system("clear")
  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Si algún valor lo dejas sin decidir se pondrá el valor por defecto. (MAGO) \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░ \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("De acuerdo, ahora con el maná que quieres tener.")
  mana_max_temp = input()
  if (mana_max_temp.isspace() or len(mana_max_temp) ==0):
    mana_max_temp = 100
  try:
    int(mana_max_temp)
  except ValueError:
    mana_max_temp = 100
  mana = mana_max_temp
  fin_mana = mana_max_temp
  os.system("clear")
  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Si algún valor lo dejas sin decidir se pondrá el valor por defecto. (MAGO) \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░ \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("Ahora con el ataque que quieres tener.")
  atac = input()
  if (atac.isspace() or len(atac) ==0):
    atac = 10
  try:
    int(atac)
  except ValueError:
    atac = 10
  atac = int(atac)
  fin_atac = atac
  os.system("clear")

  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Empezamos con el enemigo, pondremos un " + str(enemy) + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    Si no se especifican valores pondremos el predeterminado (100) \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("Elige su vida.")
  e_vida = input()
  if (e_vida.isspace() or len(e_vida) ==0):
    e_vida = 100
  try:
    int(e_vida)
  except ValueError:
    e_vida = 100
  e_vida = int(e_vida)
  e_vida_max = e_vida
  fin_e_vida = e_vida
  
  os.system("clear")
  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Empezamos con el enemigo, pondremos un " + str(enemy) + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    Si no se especifican valores pondremos el predeterminado (100) \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("Ahora su maná.")
  e_mana = input()
  if (e_mana.isspace() or len(e_mana) ==0):
    e_mana = 100
  try:
    int(e_mana)
  except ValueError:
    e_mana = 100
  e_mana = int(e_mana)
  e_mana_max = e_mana
  fin_e_mana = e_mana
  os.system("clear")
  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Empezamos con el enemigo, pondremos un " + str(enemy) + " \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    Si no se especifican valores pondremos el predeterminado (100) \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("Y ahora el daño que causa.")
  e_atac = input()
  if (e_atac.isspace() or len(e_atac) ==0):
    e_atac = 10
  try:
    int(e_atac)
  except ValueError:
    e_atac = 10
  e_atac = int(e_atac)
  fin_e_atac = e_atac
  os.system("clear")

  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Perfecto, una vez terminado esto, quieres pociones? \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    Si no se especifica se pondrán 10 en cada uno. \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("Elige las pociones de vida.")
  vida_potion = input()
  if (vida_potion.isspace() or len(vida_potion) ==0):
    vida_potion = 10
  try:
    int(vida_potion)
  except ValueError:
    vida_potion = 10
  vida_potion = int(vida_potion)
  os.system("clear")
  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Perfecto, una vez terminado esto, quieres pociones? \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    Si no se especifica se pondrán 10 en cada uno. \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("Elige las pociones de maná.")
  mana_potion = input()
  if (mana_potion.isspace() or len(mana_potion) ==0):
    mana_potion = 10
  try:
    int(mana_potion)
  except ValueError:
    mana_potion = 10
  mana_potion = int(mana_potion)
  os.system("clear")
  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Perfecto, una vez terminado esto, quieres pociones? \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    Si no se especifica se pondrán 10 en cada uno. \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("Elige las pociones de vida del enemigo.")
  e_vida_potion = input()
  if (e_vida_potion.isspace() or len(e_vida_potion) ==0):
    e_vida_potion = 10
  try:
    int(e_vida_potion)
  except ValueError:
    e_vida_potion = 10
  e_vida_potion = int(e_vida_potion)
  os.system("clear")
  print("░░░░░░░░░░░█▀▀░░█░░░░░░ \n░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░ \n░░░░░░█░█░░░░░░░░░░▐░░░    Bienvenidos al menú de partidas personalizadas. \n░░░░░░▐▐░░░░░░░░░▄░▐░░░    Aquí podréis seleccionar los valores con los que quieres jugar. \n░░░░░░█░░░░░░░░▄▀▀░▐░░░    Después de esto se te llevara a la partida y jugaras con los valores que hayas seleccionado. \n░░░░▄▀░░░░░░░░▐░▄▄▀░░░░    Perfecto, una vez terminado esto, quieres pociones? \n░░▄▀░░░▐░░░░░█▄▀░▐░░░░░    Si no se especifica se pondrán 10 en cada uno. \n░░█░░░▐░░░░░░░░▄░█░░░░░ \n░░░█▄░░▀▄░░░░▄▀▐░█░░░░░ \n░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░ \n░░▐█▐▄░░" + colorama.Fore.RED + "▀" + colorama.Fore.WHITE + "░░░░░░▐░█▄▄░░░ \n░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░ \n░░░░░░░░░░░░░░░░░░░░░░░ \n")
  print("Elige las pociones de maná del enemigo.")
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
menu()