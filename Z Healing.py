if Player.Hits == (112):
    Player.EquipItem(0x404304D4)
    Misc.Pause(500)
    Items.UseItemByID(0x0E21, 0)
    Target.WaitForTarget(1500, False)
    Target.Self()
    Misc.Pause (10000)
else:
    Items.Move(0x404304D4, 0x400CDE76, 1)
    Misc.Pause(500)
        
        


