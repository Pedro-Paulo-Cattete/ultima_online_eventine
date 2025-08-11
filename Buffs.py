# Buffs Auto:
# Chilvary: Consecrate Weapon(12s, +dmg) (10 mana)
# Chilvary: Divine Fury (20s, +atk - def) (15 mana)
# Spellweaving: Immolating Weapon (30s, Fire damage) (32 Mana)
# Mysticism: Enchant (120s, Hit Spell) (6 Mana)

# Buff order:
# Enchant -> Immolating Weapon -> Divine Fury -> Consecrate Weapon -> Consecrate Weapon -> 
# Immolating Weapon -> Divine Fury -> Consecrate Weapon -> Consecrate Weapon

Spells.CastMysticism("Enchant") #120s
Gumps.WaitForGump(0x475732cb, 10000)
Gumps.SendAction(0x475732cb, 1)
Misc.Pause(1500)
Spells.CastSpellweaving("Immolating Weapon") #30s
Misc.Pause(2000)
Spells.CastChivalry("Divine Fury") #20s
Misc.Pause(2000)
Spells.CastChivalry("Consecrate Weapon") #12s
Misc.Pause(7000)
Spells.CastSpellweaving("Immolating Weapon") #30s
Misc.Pause(6000)
Spells.CastChivalry("Consecrate Weapon") #12s
Misc.Pause(6000)
Spells.CastChivalry("Divine Fury") #20s
Misc.Pause(2000)

# Buffs Manual:
# Chilvary: Enemy of One (200s, +atk target) (20 Mana)
# Magery: Bless (120s, Buff Atr)
# Spellweaving: Gift of Life: 16m, Auto-Ress)