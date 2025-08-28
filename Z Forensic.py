forensicTarget = Target.PromptTarget( 'Selecione o corpo para analisar CSI!' )

while Player.GetRealSkillValue("Forensic Evaluation") < Player.GetSkillCap("Forensic Evaluation"):
    Player.UseSkill("Forensics");
    Target.WaitForTarget(10000, False);
    Target.TargetExecute(forensicTarget);
    Misc.Pause(3000);
else:
    Misc.Pause(100000)