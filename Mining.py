peso = Player.Weight
if peso < 450:
    Journal.Clear()
    while not Journal.Search("There is no metal here to mine."):
        playerX = Player.Position.X    
        playerY = Player.Position.Y
        pickaxe = Items.FindByID(3718,-1,Player.Backpack.Serial)
        Items.UseItem(pickaxe.Serial)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(playerX, playerY, 1 ,1339)
        Misc.Pause(2000)
    Misc.SendMessage("finished mining tile!")
    while not Journal.Search("There is no metal here to mine."):
        playerX = Player.Position.X    
        playerY = Player.Position.Y + 1
        pickaxe = Items.FindByID(3718,-1,Player.Backpack.Serial)
        Items.UseItem(pickaxe.Serial)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(playerX, playerY, 1 ,1339)
        Misc.Pause(2000)
    Misc.SendMessage("finished mining tile!")
    while not Journal.Search("There is no metal here to mine."):
        playerX = Player.Position.X    
        playerY = Player.Position.Y - 1
        pickaxe = Items.FindByID(3718,-1,Player.Backpack.Serial)
        Items.UseItem(pickaxe.Serial)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(playerX, playerY, 1 ,1339)
        Misc.Pause(2000)
    Misc.SendMessage("finished mining tile!")
    Player.Walk("Left")
else:
    Misc.SendMessage("To pesado papai!")
    Misc.Pause(3000)
    
    # 1 ,1339) - Mina Newbie Area
    # 0 ,1339) - Minoc Mine
    # 0 ,1343) - Mina Hilgolth
    # -28) - Golem Cave
    # 0) - Destard
    