peso = Player.Weight
if peso < 480:
    Items.UseItemByID(0x0E9B, 0)
    Misc.Pause(300)
    Gumps.WaitForGump(0x38920abd, 10000)
    Gumps.SendAction(0x38920abd, 24)
    Misc.Pause(300)
    Gumps.WaitForGump(0x1220462e, 10000)
    Gumps.SendAction(0x1220462e, 3)
    Misc.Pause(60000)
else:
    Misc.Pause(120000)
