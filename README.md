# settings-changer
This script is to edit lines in profile.cfg in Apex Legends (C:\Users\User\Saved Games\Respawn\Apex\profile). For now it modify only controller settings - sensitivity, ALC, Optics, it does not touch any other values or preferences.

If you are testing different settings from other players and there are alot of changes to be done, especially in ALC - this script is for you. Also, it is impossible to have rounded up values to be set in-game, even you perfectly set it as 1 - in cfg it will be 1.03405 or something similar (Rounded up values works best with XIM). So you can round up your cfg values once and save it, don't have to do it each time.

![App interface](https://i.ibb.co/Ms58Qz1/unknown.png)

## What it does:
1. Once you open the app 1st time - it will backup your current config automatically, you can restore it anytime by clicking "Restore Original cfg" button
2. App reading configs located in the "Profiles" folder. You may get the config from the guy whose settings you want to copy and place it there, or do all the changes in-game once, then copy your own "profile.cfg" from "C:\Users\User\Saved Games\Respawn\Apex\profile", rename it and place it in the "Profiles" folder.
3. These are the values that APP is modifying in v1.0:
```
gamepad_ads_advanced_sensitivity_scalar_0 "" 
gamepad_ads_advanced_sensitivity_scalar_1 "" 
gamepad_ads_advanced_sensitivity_scalar_2 "" 
gamepad_ads_advanced_sensitivity_scalar_3 ""
gamepad_ads_advanced_sensitivity_scalar_4 ""
gamepad_ads_advanced_sensitivity_scalar_5 ""
gamepad_ads_advanced_sensitivity_scalar_6 ""
gamepad_ads_advanced_sensitivity_scalar_7 ""
gamepad_aim_speed ""
gamepad_aim_speed_ads_0 ""
gamepad_custom_ads_pitch ""
gamepad_custom_ads_turn_delay ""
gamepad_custom_ads_turn_pitch ""
gamepad_custom_ads_turn_time ""
gamepad_custom_ads_turn_yaw ""
gamepad_custom_ads_yaw ""
gamepad_custom_assist_on ""
gamepad_custom_assist_style ""
gamepad_custom_curve ""
gamepad_custom_deadzone_in ""
gamepad_custom_deadzone_out ""
gamepad_custom_enabled ""
gamepad_custom_hip_pitch ""
gamepad_custom_hip_turn_delay ""
gamepad_custom_hip_turn_pitch ""
gamepad_custom_hip_turn_time ""
gamepad_custom_hip_turn_yaw ""
gamepad_custom_hip_yaw ""
gamepad_deadzone_index_look ""
gamepad_deadzone_index_move ""
gamepad_look_curve ""
gamepad_trigger_threshold ""
```

#### Script was created exclusively for "XIM Share settings" Discord Members - https://discord.gg/rZAHr9BJw7

Latest version can be downloaded in the Releases Tab - https://github.com/Gl2imm/settings-changer/releases

# !!WARNING!!
Do not run the app while the game is running. Quit the game, then use the app.. If use it while in-game EAC might react to it negatively.
