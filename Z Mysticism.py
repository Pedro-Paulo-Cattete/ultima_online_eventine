# <63: Stone Form

#if Player.Mana >= 50:
#    Spells.CastMysticism("Stone Form")
#    Misc.Pause(4000)
#else:
#    Player.UseSkill("Meditation")
#    Misc.Pause(10000)
            
# <80: Cleansing Winds
while Player.GetRealSkillValue("Mysticism") < 80:
    if Player.Mana >= 50:
        Spells.CastMysticism("Cleansing Winds")
        Target.WaitForTarget(10000, False)
        Target.Self()
        Misc.Pause(4000)
    else:
        Player.UseSkill("Meditation")
        Misc.Pause(10000)
else:
    # <95: Hail Storm
    while Player.GetRealSkillValue("Mysticism") >= 80 and Player.GetRealSkillValue("Mysticism") < 95:
        if Player.Mana >= 50:
            Spells.CastMysticism("Hail Storm")
            Target.WaitForTarget(10000, False)
            Target.Self()
            Misc.Pause(4000)
        else:
            Player.UseSkill("Meditation")
            Misc.Pause(10000)
    else:
        while Player.GetRealSkillValue("Mysticism") >= 95 and Player.GetRealSkillValue("Mysticism") < 100:
            if Player.Mana >= 50:
                Spells.CastMysticism("Nether Cyclone")
                Target.WaitForTarget(10000, False)
                Target.Self()
                Misc.Pause(4000)
            else:
                Player.UseSkill("Meditation")
                Misc.Pause(10000)
        else:
            Misc.SendMessage("GM!!!")
            Misc.Pause(3000)
#    else:
# <120: Nether Cyclone
