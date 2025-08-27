while Player.GetRealSkillValue("Cartography") < 100:
    Items.UseItemByID(0x0FBF, 0)
    Misc.Pause(300)
    Gumps.WaitForGump(0x38920abd, 10000)
    Gumps.SendAction(0x38920abd, 24)
    Misc.Pause(300)
    Gumps.WaitForGump(0x1220462e, 10000)
    Gumps.SendAction(0x1220462e, 3)
    Misc.Pause(20000)
else:
    Misc.Pause(3000)
    Misc.SendMessage("Próximo, esse já tá fácil!")

# (0x38920abd, 3)  = < 50 (Local Maps)
# (0x38920abd, 10) = < 65 (City Maps)
# (0x38920abd, 17) = < 70 (Sea Charts)
# (0x38920abd, 24) = < 99.5 (World Charts)