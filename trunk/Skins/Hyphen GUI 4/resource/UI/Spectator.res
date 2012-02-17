// TEAM HYPHEN GUI
// BY KLUTCH
// www.teamhyphen.org

"Resource/UI/SpectatorGUI.res"
{
	"SpectatorGUI"
	{
		"ControlName"	"Frame"
		"fieldName"		"SpectatorGUI"
		"tall"			"480"
		"wide"			"640"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
	}
	
	
	
	
	"timerclock"    // timer clock and changes to c4 when c4 is planted
	{
		"ControlName"	"Label"
		"fieldName"		"timerclock"
		
		
		// 16:9 Ratio
		"ypos"			"178"
		"xpos"			"20"
		
		// 3:4 Ratio
		//"ypos"		"142"
		//"xpos"		"16"
		
		"zpos"			"-12"
		"wide"			"32"
		"tall"			"32"
		"autoResize"	"1"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"textAlignment"	"west"
		"dulltext"		"0"
		"brighttext"	"1"
		"labelText"		"e"
		"font"		"Icons"
	}
	
	
	"extrainfo"   // Things like how many specs, what map and your cash.
	{
		"ControlName"	"Label"
		"fieldName"		"extrainfo"
		"font"			"HyphenSpec"
		"xpos"			"16"
		
		// 16:9 Ratio
		"ypos"			"185"
		
		// 3:4 Ratio
		//"ypos"			"150"
		
		
		"wide"			"160"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		""
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"1"
		"fgcolor_override"		"255 255 255 255"
		"bgcolor_override"		"0 0 0 0"
	}
	
	
	
	
	
	
	
	
	
	
	
	"topbar"
	{
		"ControlName"	"Panel"
		"fieldName"		"topbar"
		"xpos"			"-1000"
		"ypos"			"-1000"
		"tall"			"0"
		"wide"			"640"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
		"fillcolor"			"0 0 0 0"
		"fgcolor_override"	"0 0 0 0"
		"bgcolor_override"	"0 0 0 0"
	}
	"bottombarblank"
	{
		"ControlName"	"Panel"
		"fieldName"		"bottombarblank"
		"xpos"			"-1000"
		"ypos"			"-1000"
		"tall"			"55"		// this needs to match the size of BottomBar
		"wide"			"640"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
	}
	"playerlabel"
	{
		"ControlName"	"Label"
		"font"			"HyphenPlayerBar"
		"fieldName"		"playerlabel"
		"xpos"			"c-175"
		"ypos"			"441"
		"wide"			"350"
		"tall"			"40"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"0"
		"enabled"		"1"
		"tabPosition"	"0"
		"textAlignment"	"center"
	}
	"HyphSpec"
	{
		"ControlName"	"Label"
		"fieldName"		"hyphyouarespec"
		"labelText"		"you are spectating"
		"font"			"HyphenSpecLabel"
		"xpos"			"c-175"
		"ypos"			"428"
		"wide"			"350"
		"tall"			"32"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
		"textAlignment"	"center"
	}
	"CTScoreLabel"
	{
		"ControlName"	"Label"
		"fieldName"		"CTScoreLabel"
		"font"			"HyphenSpec"
		"xpos"			"c-180"
		"ypos"			"7"
		"wide"			"150"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"Counter-Terrorists  "
		"textAlignment"	"east"
		"dulltext"		"0"
		"brighttext"	"1"
		"bgcolor_override"		"0 0 255 50"
	}
	"TERScoreLabel"
	{
		"ControlName"	"Label"
		"fieldName"		"TERScoreLabel"
		"font"			"HyphenSpec"
		"xpos"			"c+30"
		"ypos"			"7"
		//"zpos"			"-12"
		"wide"			"150"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"  Terrorists"
		"textAlignment"	"west"
		"dulltext"		"0"
		"brighttext"	"1"
		"bgcolor_override"		"255 0 0 50"
	}
	"TERScoreValue"
	{
		"ControlName"	"Label"
		"fieldName"		"TERScoreValue"
		"font"			"HyphenSpec"
		"xpos"			"c0"
		"ypos"			"7"
		"wide"			"25"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		""
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"1"
		"bgcolor_override"		"255 0 0 50"
	}
	"CTScoreValue"
	{
		"ControlName"	"Label"
		"fieldName"		"CTScoreValue"
		"font"			"HyphenSpec"
		"xpos"			"c-25"
		"ypos"			"7"
		"wide"			"25"
		"tall"			"20"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		""
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"1"
		"bgcolor_override"		"0 0 255 50"
	}
	"DividerBar"
	{
		"ControlName"	"ImagePanel"
		"fieldName"		"DividerBar"
		"xpos"			"-1000"
		"ypos"			"-1000"
		"wide"			"1"
		"tall"			"30"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"tabPosition"	"0"
		"fillcolor"		"BorderBright"
		"labelText"		""
		"textAlignment"	"center"
	}
	"timerlabel"
	{
		"ControlName"	"Label"
		"fieldName"		"timerlabel"
		"font"			"HyphenTimer"
		"xpos"			"c-40"
		"ypos"			"30"
		"wide"			"80"
		"tall"			"40"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"labelText"		"00:00"
		"textAlignment"	"center"
		"dulltext"		"0"
		"brighttext"	"1"
	}
	"titlelabel"
	{
		"ControlName"	"Label"
		"fieldName"		"titlelabel"
		"font"			"HyphenSpecLabel"
		"xpos"			"c-50"
		"ypos"			"390"
		"wide"			"100"
		"tall"			"32"
		"autoResize"	"0"
		"pinCorner"		"0"
		"visible"		"1"
		"enabled"		"1"
		"font"			"HudNumbersSmall"
		"labelText"		""
		"textAlignment"	"south"
		"dulltext"		"0"
		"brighttext"	"1"
	}
	//BG GRAD
	"Top"
	{
		"ControlName"	        "ImagePanel"
		"fieldName"		        "BGANIM"
		"xpos"					"0"
		"ypos"					"0"
		"zpos"					"-11"
		"wide"		            "f0"
		"tall"		            "80"
		"visible"				"1"
		"enabled"				"1"
		//"image"					"../VGUI/grad_bt"
		"scaleImage"			"1"		
	}
    "BGIMG1"
	{
		"ControlName"	        "ImagePanel"
		"fieldName"		        "BGIMG1"
		"xpos"		 	 	    "0"
		"ypos"				    "0"
		"zpos"					"-11"
		"wide"				    "2000"
		"tall"				    "400"
		"visible"				"1"
		"enabled"				"1"
		"image"					"../../../hl2/materials/VGUI/zoom"
		"scaleImage"			"1"		
	}
	"Bottom"
	{
		"ControlName"	        "ImagePanel"
		"fieldName"		        "BGANIM"
		"xpos"					"0"
		"ypos"					"400"
		"zpos"					"-11"
		"wide"		            "f0"
		"tall"		            "80"
		"visible"				"1"
		"enabled"				"1"
		//"image"					"../VGUI/grad_tb"
		"scaleImage"			"1"		
	}
	"Bottom"
	{
		"ControlName"	        "ImagePanel"
		"fieldName"		        "BGANIM"
		"xpos"					"0"
		"ypos"					"-500"
		"zpos"					"-11"
		"wide"		            "5000"
		"tall"		            "1000"
		"visible"				"1"
		"enabled"				"1"
		//"image"				"../effects/fire_cloud1"
		//"image"					"../cs_assualt/assault_hide01"
		"image"					"../sprites/scope_arc"
		"tileimage"				"0"
		"scaleImage"			"1"
	}
	
}
