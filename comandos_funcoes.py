# Comandos e Funções:

# Checar Life ou Mana:
    
if Player.Hits > 110:
else:
if Player.Mana >= 100:
else:
    
# Checar Peso:
    
peso = Player.Weight
if peso < 480:    
else
    
# Checar Skill e Skillcap:
while Player.GetRealSkillValue("Mysticism") < Player.GetSkillCap("Mysticism"):
else

# Enviar mensagem:
    
Misc.SendMessage("Ta fácil já, parte pro próximo!")

# Pausar:
    
Misc.Pause(10000)

# Usar Item Pelo ID:
    
Items.UseItemByID(0x0E21, 0)

# Usar Item pelo ID e Target Item por ID

smith = Items.FindByID(0x13E3,-1,Player.Backpack.Serial)
Items.UseItem(smith.Serial)
       
itemToSmelt = Items.FindByID(0x1441,-1,Player.Backpack.Serial)
Target.TargetExecute( itemToSmelt.Serial )
