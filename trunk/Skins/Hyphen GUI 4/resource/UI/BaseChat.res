"Resource/UI/BaseChat.res"
{
	"HudChat"
	{
		"ControlName"	"EditablePanel"
		"fieldName" 	"HudChat"
		"visible" 		"1"
		"enabled" 		"1"
		"xpos"			"6"
		"ypos"			"365"
		"wide"	 		"350"
		"tall"	 		"100"
		"PaintBackgroundType"	"0"
		"backgroundtype" "0"
	}

	ChatInputLine
	{
		"ControlName"	"EditablePanel"
		"fieldName" 	ChatInputLine
		"visible" 		"1"
		"enabled" 		"1"
		"xpos"			"0"
		"ypos"			"350"
		"wide"	 		"300"
		"tall"	 		"2"
		"PaintBackgroundType"	"0"
		"backgroundtype" "0"
	}

	"ChatFiltersButton"
	{
		"ControlName"	"Button"
		"fieldName"		"ChatFiltersButton"
		"xpos"			"0"
		"ypos"			"350"
		"wide"			"45"
		"tall"			"15"
		"autoResize"	"1"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
		"labelText"		"#chat_filterbutton"
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"0"
		"Default"		"0"		
	}

	"HudChatHistory"
	{
		"ControlName"	"RichText"
		"fieldName"		"HudChatHistory"
		"xpos"			"0"
		"ypos"			"0"
		"wide"	 		"350"
		"tall"			"75"
		"wrap"			"1"
		"autoResize"	"1"
		"pinCorner"		"1"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		""
		"textAlignment"	"north-west"
		"font"			"HyphenDeath"
		"maxchars"		"-1"
	}
}
