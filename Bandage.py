if Player.Visible == True and Player.Hits < Player.HitsMax or Player.Poisoned == True:
    Items.UseItemByID(0x0E21, 0)
    Target.WaitForTarget(1500, False)
    Target.Self()    
    Misc.Pause(7000)
else:
    Misc.Pause(1000)