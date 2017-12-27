<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE eagle SYSTEM "eagle.dtd">
<eagle version="7.5.0">
<drawing>
<settings>
<setting alwaysvectorfont="no"/>
<setting verticaltext="up"/>
</settings>
<grid distance="0.1" unitdist="inch" unit="inch" style="lines" multiple="1" display="no" altdistance="0.01" altunitdist="inch" altunit="inch"/>
<layers>
<layer number="1" name="Top" color="4" fill="1" visible="no" active="no"/>
<layer number="16" name="Bottom" color="1" fill="1" visible="no" active="no"/>
<layer number="17" name="Pads" color="2" fill="1" visible="no" active="no"/>
<layer number="18" name="Vias" color="2" fill="1" visible="no" active="no"/>
<layer number="19" name="Unrouted" color="6" fill="1" visible="no" active="no"/>
<layer number="20" name="Dimension" color="15" fill="1" visible="no" active="no"/>
<layer number="21" name="tPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="22" name="bPlace" color="7" fill="1" visible="no" active="no"/>
<layer number="23" name="tOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="24" name="bOrigins" color="15" fill="1" visible="no" active="no"/>
<layer number="25" name="tNames" color="7" fill="1" visible="no" active="no"/>
<layer number="26" name="bNames" color="7" fill="1" visible="no" active="no"/>
<layer number="27" name="tValues" color="7" fill="1" visible="no" active="no"/>
<layer number="28" name="bValues" color="7" fill="1" visible="no" active="no"/>
<layer number="29" name="tStop" color="7" fill="3" visible="no" active="no"/>
<layer number="30" name="bStop" color="7" fill="6" visible="no" active="no"/>
<layer number="31" name="tCream" color="7" fill="4" visible="no" active="no"/>
<layer number="32" name="bCream" color="7" fill="5" visible="no" active="no"/>
<layer number="33" name="tFinish" color="6" fill="3" visible="no" active="no"/>
<layer number="34" name="bFinish" color="6" fill="6" visible="no" active="no"/>
<layer number="35" name="tGlue" color="7" fill="4" visible="no" active="no"/>
<layer number="36" name="bGlue" color="7" fill="5" visible="no" active="no"/>
<layer number="37" name="tTest" color="7" fill="1" visible="no" active="no"/>
<layer number="38" name="bTest" color="7" fill="1" visible="no" active="no"/>
<layer number="39" name="tKeepout" color="4" fill="11" visible="no" active="no"/>
<layer number="40" name="bKeepout" color="1" fill="11" visible="no" active="no"/>
<layer number="41" name="tRestrict" color="4" fill="10" visible="no" active="no"/>
<layer number="42" name="bRestrict" color="1" fill="10" visible="no" active="no"/>
<layer number="43" name="vRestrict" color="2" fill="10" visible="no" active="no"/>
<layer number="44" name="Drills" color="7" fill="1" visible="no" active="no"/>
<layer number="45" name="Holes" color="7" fill="1" visible="no" active="no"/>
<layer number="46" name="Milling" color="3" fill="1" visible="no" active="no"/>
<layer number="47" name="Measures" color="7" fill="1" visible="no" active="no"/>
<layer number="48" name="Document" color="7" fill="1" visible="no" active="no"/>
<layer number="49" name="Reference" color="7" fill="1" visible="no" active="no"/>
<layer number="51" name="tDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="52" name="bDocu" color="7" fill="1" visible="no" active="no"/>
<layer number="90" name="Modules" color="5" fill="1" visible="yes" active="yes"/>
<layer number="91" name="Nets" color="2" fill="1" visible="yes" active="yes"/>
<layer number="92" name="Busses" color="1" fill="1" visible="yes" active="yes"/>
<layer number="93" name="Pins" color="2" fill="1" visible="no" active="yes"/>
<layer number="94" name="Symbols" color="4" fill="1" visible="yes" active="yes"/>
<layer number="95" name="Names" color="7" fill="1" visible="yes" active="yes"/>
<layer number="96" name="Values" color="7" fill="1" visible="yes" active="yes"/>
<layer number="97" name="Info" color="7" fill="1" visible="yes" active="yes"/>
<layer number="98" name="Guide" color="6" fill="1" visible="yes" active="yes"/>
</layers>
<schematic xreflabel="%F%N/%S.%C%R" xrefpart="/%S.%C%R">
<libraries>
<library name="Adafruitmotordriver">
<packages>
<package name="ADAMTRDRVR">
<pad name="PWMA" x="2.54" y="2.54" drill="0.8"/>
<pad name="AIN2" x="2.54" y="5.08" drill="0.8"/>
<pad name="AIN1" x="2.54" y="7.62" drill="0.8"/>
<pad name="STBY" x="2.54" y="10.16" drill="0.8"/>
<pad name="BIN1" x="2.54" y="12.7" drill="0.8"/>
<pad name="BIN2" x="2.54" y="15.24" drill="0.8"/>
<pad name="PWMB" x="2.54" y="17.78" drill="0.8"/>
<pad name="GND" x="2.54" y="20.32" drill="0.8"/>
<pad name="VCC" x="2.54" y="22.86" drill="0.8"/>
<pad name="VM" x="2.54" y="25.4" drill="0.8"/>
<pad name="MOTORA1" x="17.78" y="7.62" drill="0.8"/>
<pad name="MOTORA2" x="17.78" y="10.16" drill="0.8"/>
<pad name="GND1" x="17.78" y="12.7" drill="0.8"/>
<pad name="GND2" x="17.78" y="15.24" drill="0.8"/>
<pad name="MOTORB1" x="17.78" y="17.78" drill="0.8"/>
<pad name="MTOTORB2" x="17.78" y="20.32" drill="0.8"/>
<wire x1="0" y1="0" x2="0" y2="27.94" width="0.127" layer="21"/>
<wire x1="0" y1="27.94" x2="20.32" y2="27.94" width="0.127" layer="21"/>
<wire x1="20.32" y1="27.94" x2="20.32" y2="0" width="0.127" layer="21"/>
<wire x1="20.32" y1="0" x2="0" y2="0" width="0.127" layer="21"/>
<text x="0" y="27.94" size="1.27" layer="21">&gt;Name</text>
<text x="0" y="-2.54" size="1.27" layer="21">&gt;Value</text>
</package>
</packages>
<symbols>
<symbol name="ADAMTRDRVR">
<wire x1="-12.7" y1="25.4" x2="-12.7" y2="-25.4" width="0.254" layer="94"/>
<wire x1="-12.7" y1="-25.4" x2="12.7" y2="-25.4" width="0.254" layer="94"/>
<wire x1="12.7" y1="-25.4" x2="12.7" y2="25.4" width="0.254" layer="94"/>
<wire x1="12.7" y1="25.4" x2="-12.7" y2="25.4" width="0.254" layer="94"/>
<pin name="VM" x="-17.78" y="22.86" length="middle"/>
<pin name="VCC" x="-17.78" y="17.78" length="middle"/>
<pin name="GND" x="-17.78" y="12.7" length="middle"/>
<pin name="PWMB" x="-17.78" y="7.62" length="middle"/>
<pin name="BIN2" x="-17.78" y="2.54" length="middle"/>
<pin name="BIN1" x="-17.78" y="-2.54" length="middle"/>
<pin name="STBY" x="-17.78" y="-7.62" length="middle"/>
<pin name="AIN1" x="-17.78" y="-12.7" length="middle"/>
<pin name="AIN2" x="-17.78" y="-17.78" length="middle"/>
<pin name="PWMA" x="-17.78" y="-22.86" length="middle"/>
<pin name="MOTORB1" x="17.78" y="12.7" length="middle" rot="R180"/>
<pin name="MOTORB2" x="17.78" y="7.62" length="middle" rot="R180"/>
<pin name="GND1" x="17.78" y="2.54" length="middle" rot="R180"/>
<pin name="GND2" x="17.78" y="-2.54" length="middle" rot="R180"/>
<pin name="MOTORA1" x="17.78" y="-7.62" length="middle" rot="R180"/>
<pin name="MOTORA2" x="17.78" y="-12.7" length="middle" rot="R180"/>
<text x="-12.7" y="35.56" size="1.778" layer="94">&gt;NAME</text>
<text x="-12.7" y="-27.94" size="1.778" layer="94">&gt;VALUE</text>
</symbol>
</symbols>
<devicesets>
<deviceset name="ADAMTRDRVR">
<gates>
<gate name="G$1" symbol="ADAMTRDRVR" x="0" y="0"/>
</gates>
<devices>
<device name="" package="ADAMTRDRVR">
<connects>
<connect gate="G$1" pin="AIN1" pad="AIN1"/>
<connect gate="G$1" pin="AIN2" pad="AIN2"/>
<connect gate="G$1" pin="BIN1" pad="BIN1"/>
<connect gate="G$1" pin="BIN2" pad="BIN2"/>
<connect gate="G$1" pin="GND" pad="GND"/>
<connect gate="G$1" pin="GND1" pad="GND1"/>
<connect gate="G$1" pin="GND2" pad="GND2"/>
<connect gate="G$1" pin="MOTORA1" pad="MOTORA1"/>
<connect gate="G$1" pin="MOTORA2" pad="MOTORA2"/>
<connect gate="G$1" pin="MOTORB1" pad="MOTORB1"/>
<connect gate="G$1" pin="MOTORB2" pad="MTOTORB2"/>
<connect gate="G$1" pin="PWMA" pad="PWMA"/>
<connect gate="G$1" pin="PWMB" pad="PWMB"/>
<connect gate="G$1" pin="STBY" pad="STBY"/>
<connect gate="G$1" pin="VCC" pad="VCC"/>
<connect gate="G$1" pin="VM" pad="VM"/>
</connects>
<technologies>
<technology name=""/>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
<library name="con-molex">
<description>&lt;b&gt;Molex Connectors&lt;/b&gt;&lt;p&gt;
&lt;author&gt;Created by librarian@cadsoft.de&lt;/author&gt;</description>
<packages>
<package name="22-23-2081">
<description>.100" (2.54mm) Center Header - 8 Pin</description>
<wire x1="-10.16" y1="3.175" x2="10.16" y2="3.175" width="0.254" layer="21"/>
<wire x1="10.16" y1="3.175" x2="10.16" y2="1.27" width="0.254" layer="21"/>
<wire x1="10.16" y1="1.27" x2="10.16" y2="-3.175" width="0.254" layer="21"/>
<wire x1="10.16" y1="-3.175" x2="-10.16" y2="-3.175" width="0.254" layer="21"/>
<wire x1="-10.16" y1="-3.175" x2="-10.16" y2="1.27" width="0.254" layer="21"/>
<wire x1="-10.16" y1="1.27" x2="-10.16" y2="3.175" width="0.254" layer="21"/>
<wire x1="-10.16" y1="1.27" x2="10.16" y2="1.27" width="0.254" layer="21"/>
<pad name="1" x="-8.89" y="0" drill="1" shape="long" rot="R90"/>
<pad name="2" x="-6.35" y="0" drill="1" shape="long" rot="R90"/>
<pad name="3" x="-3.81" y="0" drill="1" shape="long" rot="R90"/>
<pad name="4" x="-1.27" y="0" drill="1" shape="long" rot="R90"/>
<pad name="5" x="1.27" y="0" drill="1" shape="long" rot="R90"/>
<pad name="6" x="3.81" y="0" drill="1" shape="long" rot="R90"/>
<pad name="7" x="6.35" y="0" drill="1" shape="long" rot="R90"/>
<pad name="8" x="8.89" y="0" drill="1" shape="long" rot="R90"/>
<text x="-10.16" y="3.81" size="1.016" layer="25" ratio="10">&gt;NAME</text>
<text x="-10.16" y="-5.08" size="1.016" layer="27" ratio="10">&gt;VALUE</text>
</package>
<package name="22-23-2021">
<description>.100" (2.54mm) Center Headers - 2 Pin</description>
<wire x1="-2.54" y1="3.175" x2="2.54" y2="3.175" width="0.254" layer="21"/>
<wire x1="2.54" y1="3.175" x2="2.54" y2="1.27" width="0.254" layer="21"/>
<wire x1="2.54" y1="1.27" x2="2.54" y2="-3.175" width="0.254" layer="21"/>
<wire x1="2.54" y1="-3.175" x2="-2.54" y2="-3.175" width="0.254" layer="21"/>
<wire x1="-2.54" y1="-3.175" x2="-2.54" y2="1.27" width="0.254" layer="21"/>
<wire x1="-2.54" y1="1.27" x2="-2.54" y2="3.175" width="0.254" layer="21"/>
<wire x1="-2.54" y1="1.27" x2="2.54" y2="1.27" width="0.254" layer="21"/>
<pad name="1" x="-1.27" y="0" drill="1" shape="long" rot="R90"/>
<pad name="2" x="1.27" y="0" drill="1" shape="long" rot="R90"/>
<text x="-2.54" y="3.81" size="1.016" layer="25" ratio="10">&gt;NAME</text>
<text x="-2.54" y="-5.08" size="1.016" layer="27" ratio="10">&gt;VALUE</text>
</package>
</packages>
<symbols>
<symbol name="MV">
<wire x1="1.27" y1="0" x2="0" y2="0" width="0.6096" layer="94"/>
<text x="2.54" y="-0.762" size="1.524" layer="95">&gt;NAME</text>
<text x="-0.762" y="1.397" size="1.778" layer="96">&gt;VALUE</text>
<pin name="S" x="-2.54" y="0" visible="off" length="short" direction="pas"/>
</symbol>
<symbol name="M">
<wire x1="1.27" y1="0" x2="0" y2="0" width="0.6096" layer="94"/>
<text x="2.54" y="-0.762" size="1.524" layer="95">&gt;NAME</text>
<pin name="S" x="-2.54" y="0" visible="off" length="short" direction="pas"/>
</symbol>
</symbols>
<devicesets>
<deviceset name="22-23-2081" prefix="X">
<description>.100" (2.54mm) Center Header - 8 Pin</description>
<gates>
<gate name="-1" symbol="MV" x="0" y="7.62" addlevel="always" swaplevel="1"/>
<gate name="-2" symbol="M" x="0" y="5.08" addlevel="always" swaplevel="1"/>
<gate name="-3" symbol="M" x="0" y="2.54" addlevel="always" swaplevel="1"/>
<gate name="-4" symbol="M" x="0" y="0" addlevel="always" swaplevel="1"/>
<gate name="-5" symbol="M" x="0" y="-2.54" addlevel="always" swaplevel="1"/>
<gate name="-6" symbol="M" x="0" y="-5.08" addlevel="always" swaplevel="1"/>
<gate name="-7" symbol="M" x="0" y="-7.62" addlevel="always" swaplevel="1"/>
<gate name="-8" symbol="M" x="0" y="-10.16" addlevel="always" swaplevel="1"/>
</gates>
<devices>
<device name="" package="22-23-2081">
<connects>
<connect gate="-1" pin="S" pad="1"/>
<connect gate="-2" pin="S" pad="2"/>
<connect gate="-3" pin="S" pad="3"/>
<connect gate="-4" pin="S" pad="4"/>
<connect gate="-5" pin="S" pad="5"/>
<connect gate="-6" pin="S" pad="6"/>
<connect gate="-7" pin="S" pad="7"/>
<connect gate="-8" pin="S" pad="8"/>
</connects>
<technologies>
<technology name="">
<attribute name="MF" value="MOLEX" constant="no"/>
<attribute name="MPN" value="22-23-2081" constant="no"/>
<attribute name="OC_FARNELL" value="1756826" constant="no"/>
<attribute name="OC_NEWARK" value="01C7592" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
<deviceset name="22-23-2021" prefix="X">
<description>.100" (2.54mm) Center Header - 2 Pin</description>
<gates>
<gate name="-1" symbol="MV" x="0" y="0" addlevel="always" swaplevel="1"/>
<gate name="-2" symbol="M" x="0" y="-2.54" addlevel="always" swaplevel="1"/>
</gates>
<devices>
<device name="" package="22-23-2021">
<connects>
<connect gate="-1" pin="S" pad="1"/>
<connect gate="-2" pin="S" pad="2"/>
</connects>
<technologies>
<technology name="">
<attribute name="MF" value="MOLEX" constant="no"/>
<attribute name="MPN" value="22-23-2021" constant="no"/>
<attribute name="OC_FARNELL" value="1462926" constant="no"/>
<attribute name="OC_NEWARK" value="25C3832" constant="no"/>
</technology>
</technologies>
</device>
</devices>
</deviceset>
</devicesets>
</library>
</libraries>
<attributes>
</attributes>
<variantdefs>
</variantdefs>
<classes>
<class number="0" name="default" width="0" drill="0">
</class>
</classes>
<parts>
<part name="U$1" library="Adafruitmotordriver" deviceset="ADAMTRDRVR" device=""/>
<part name="U$3" library="Adafruitmotordriver" deviceset="ADAMTRDRVR" device=""/>
<part name="MOTOR" library="con-molex" deviceset="22-23-2081" device=""/>
<part name="SUPPLY-IN" library="con-molex" deviceset="22-23-2021" device=""/>
<part name="SUPPLY-OUT" library="con-molex" deviceset="22-23-2021" device=""/>
<part name="M1" library="con-molex" deviceset="22-23-2021" device=""/>
<part name="M2" library="con-molex" deviceset="22-23-2021" device=""/>
<part name="M3" library="con-molex" deviceset="22-23-2021" device=""/>
<part name="M4" library="con-molex" deviceset="22-23-2021" device=""/>
</parts>
<sheets>
<sheet>
<plain>
</plain>
<instances>
<instance part="U$1" gate="G$1" x="25.4" y="55.88"/>
<instance part="U$3" gate="G$1" x="25.4" y="-10.16"/>
<instance part="MOTOR" gate="-1" x="-45.72" y="38.1"/>
<instance part="MOTOR" gate="-2" x="-45.72" y="35.56"/>
<instance part="MOTOR" gate="-3" x="-45.72" y="33.02"/>
<instance part="MOTOR" gate="-4" x="-45.72" y="30.48"/>
<instance part="MOTOR" gate="-5" x="-45.72" y="27.94"/>
<instance part="MOTOR" gate="-6" x="-45.72" y="25.4"/>
<instance part="MOTOR" gate="-7" x="-45.72" y="22.86"/>
<instance part="MOTOR" gate="-8" x="-45.72" y="20.32"/>
<instance part="SUPPLY-IN" gate="-1" x="-38.1" y="88.9"/>
<instance part="SUPPLY-IN" gate="-2" x="-38.1" y="86.36"/>
<instance part="SUPPLY-OUT" gate="-1" x="-38.1" y="78.74"/>
<instance part="SUPPLY-OUT" gate="-2" x="-38.1" y="76.2"/>
<instance part="M1" gate="-1" x="76.2" y="68.58"/>
<instance part="M1" gate="-2" x="76.2" y="66.04"/>
<instance part="M2" gate="-1" x="78.74" y="45.72"/>
<instance part="M2" gate="-2" x="78.74" y="43.18"/>
<instance part="M3" gate="-1" x="81.28" y="2.54"/>
<instance part="M3" gate="-2" x="81.28" y="0"/>
<instance part="M4" gate="-1" x="81.28" y="-17.78"/>
<instance part="M4" gate="-2" x="81.28" y="-20.32"/>
</instances>
<busses>
</busses>
<nets>
<net name="VM" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="VM"/>
<wire x1="7.62" y1="78.74" x2="5.08" y2="78.74" width="0.1524" layer="91"/>
<label x="-2.54" y="78.74" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="VM"/>
<wire x1="7.62" y1="12.7" x2="0" y2="12.7" width="0.1524" layer="91"/>
<label x="-10.16" y="12.7" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="SUPPLY-IN" gate="-1" pin="S"/>
<wire x1="-40.64" y1="88.9" x2="-45.72" y2="88.9" width="0.1524" layer="91"/>
<label x="-45.72" y="88.9" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="SUPPLY-OUT" gate="-1" pin="S"/>
<wire x1="-40.64" y1="78.74" x2="-45.72" y2="78.74" width="0.1524" layer="91"/>
<label x="-45.72" y="78.74" size="1.778" layer="95"/>
</segment>
</net>
<net name="3.3V" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="VCC"/>
<wire x1="7.62" y1="73.66" x2="5.08" y2="73.66" width="0.1524" layer="91"/>
<label x="-2.54" y="73.66" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="VCC"/>
<wire x1="7.62" y1="7.62" x2="0" y2="7.62" width="0.1524" layer="91"/>
<label x="-10.16" y="7.62" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="MOTOR" gate="-1" pin="S"/>
<wire x1="-48.26" y1="38.1" x2="-50.8" y2="38.1" width="0.1524" layer="91"/>
<label x="-50.8" y="38.1" size="1.778" layer="95"/>
</segment>
</net>
<net name="GND" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="GND"/>
<wire x1="7.62" y1="68.58" x2="5.08" y2="68.58" width="0.1524" layer="91"/>
<label x="-2.54" y="68.58" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$1" gate="G$1" pin="GND1"/>
<wire x1="43.18" y1="58.42" x2="45.72" y2="58.42" width="0.1524" layer="91"/>
<label x="50.8" y="58.42" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$1" gate="G$1" pin="GND2"/>
<wire x1="43.18" y1="53.34" x2="45.72" y2="53.34" width="0.1524" layer="91"/>
<label x="50.8" y="53.34" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="GND"/>
<wire x1="7.62" y1="2.54" x2="0" y2="2.54" width="0.1524" layer="91"/>
<label x="-10.16" y="2.54" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="GND1"/>
<wire x1="43.18" y1="-7.62" x2="45.72" y2="-7.62" width="0.1524" layer="91"/>
<label x="55.88" y="-7.62" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="U$3" gate="G$1" pin="GND2"/>
<wire x1="43.18" y1="-12.7" x2="45.72" y2="-12.7" width="0.1524" layer="91"/>
<label x="55.88" y="-12.7" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="MOTOR" gate="-8" pin="S"/>
<wire x1="-48.26" y1="20.32" x2="-50.8" y2="20.32" width="0.1524" layer="91"/>
<label x="-50.8" y="20.32" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="SUPPLY-IN" gate="-2" pin="S"/>
<wire x1="-40.64" y1="86.36" x2="-45.72" y2="86.36" width="0.1524" layer="91"/>
<label x="-45.72" y="86.36" size="1.778" layer="95"/>
</segment>
<segment>
<pinref part="SUPPLY-OUT" gate="-2" pin="S"/>
<wire x1="-40.64" y1="76.2" x2="-45.72" y2="76.2" width="0.1524" layer="91"/>
<label x="-45.72" y="76.2" size="1.778" layer="95"/>
</segment>
</net>
<net name="PWMR" class="0">
<segment>
<pinref part="MOTOR" gate="-2" pin="S"/>
<label x="-50.8" y="35.56" size="1.778" layer="95"/>
<wire x1="-48.26" y1="35.56" x2="-60.96" y2="35.56" width="0.1524" layer="91"/>
<wire x1="-60.96" y1="35.56" x2="-60.96" y2="63.5" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="PWMB"/>
<wire x1="7.62" y1="63.5" x2="0" y2="63.5" width="0.1524" layer="91"/>
<wire x1="0" y1="63.5" x2="0" y2="33.02" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="PWMA"/>
<wire x1="0" y1="33.02" x2="7.62" y2="33.02" width="0.1524" layer="91"/>
<junction x="0" y="63.5"/>
<wire x1="-60.96" y1="63.5" x2="0" y2="63.5" width="0.1524" layer="91"/>
<label x="-10.16" y="63.5" size="1.778" layer="95"/>
</segment>
</net>
<net name="PWML" class="0">
<segment>
<pinref part="MOTOR" gate="-3" pin="S"/>
<label x="-50.8" y="33.02" size="1.778" layer="95"/>
<wire x1="-48.26" y1="33.02" x2="-60.96" y2="33.02" width="0.1524" layer="91"/>
<wire x1="-60.96" y1="33.02" x2="-60.96" y2="-2.54" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="PWMB"/>
<wire x1="7.62" y1="-2.54" x2="-2.54" y2="-2.54" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="PWMA"/>
<wire x1="7.62" y1="-33.02" x2="-2.54" y2="-33.02" width="0.1524" layer="91"/>
<wire x1="-2.54" y1="-33.02" x2="-2.54" y2="-2.54" width="0.1524" layer="91"/>
<junction x="-2.54" y="-2.54"/>
<wire x1="-60.96" y1="-2.54" x2="-2.54" y2="-2.54" width="0.1524" layer="91"/>
<label x="-10.16" y="-2.54" size="1.778" layer="95"/>
</segment>
</net>
<net name="DIRMR1" class="0">
<segment>
<pinref part="MOTOR" gate="-4" pin="S"/>
<label x="-50.8" y="30.48" size="1.778" layer="95"/>
<wire x1="-48.26" y1="30.48" x2="-58.42" y2="30.48" width="0.1524" layer="91"/>
<wire x1="-58.42" y1="30.48" x2="-58.42" y2="58.42" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="BIN2"/>
<wire x1="7.62" y1="58.42" x2="2.54" y2="58.42" width="0.1524" layer="91"/>
<wire x1="2.54" y1="58.42" x2="2.54" y2="38.1" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="AIN2"/>
<wire x1="2.54" y1="38.1" x2="7.62" y2="38.1" width="0.1524" layer="91"/>
<junction x="2.54" y="58.42"/>
<wire x1="-58.42" y1="58.42" x2="2.54" y2="58.42" width="0.1524" layer="91"/>
<label x="-10.16" y="58.42" size="1.778" layer="95"/>
</segment>
</net>
<net name="DIRMR2" class="0">
<segment>
<pinref part="MOTOR" gate="-5" pin="S"/>
<label x="-50.8" y="27.94" size="1.778" layer="95"/>
<pinref part="U$1" gate="G$1" pin="BIN1"/>
<wire x1="7.62" y1="53.34" x2="5.08" y2="53.34" width="0.1524" layer="91"/>
<wire x1="5.08" y1="53.34" x2="5.08" y2="43.18" width="0.1524" layer="91"/>
<pinref part="U$1" gate="G$1" pin="AIN1"/>
<wire x1="5.08" y1="43.18" x2="7.62" y2="43.18" width="0.1524" layer="91"/>
<junction x="5.08" y="53.34"/>
<wire x1="5.08" y1="53.34" x2="-55.88" y2="53.34" width="0.1524" layer="91"/>
<wire x1="-55.88" y1="53.34" x2="-55.88" y2="27.94" width="0.1524" layer="91"/>
<wire x1="-55.88" y1="27.94" x2="-48.26" y2="27.94" width="0.1524" layer="91"/>
<label x="-10.16" y="53.34" size="1.778" layer="95"/>
</segment>
</net>
<net name="DIRML1" class="0">
<segment>
<pinref part="MOTOR" gate="-6" pin="S"/>
<label x="-50.8" y="25.4" size="1.778" layer="95"/>
<wire x1="-48.26" y1="25.4" x2="-58.42" y2="25.4" width="0.1524" layer="91"/>
<wire x1="-58.42" y1="25.4" x2="-58.42" y2="-7.62" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="BIN2"/>
<wire x1="7.62" y1="-7.62" x2="0" y2="-7.62" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="AIN2"/>
<wire x1="7.62" y1="-27.94" x2="0" y2="-27.94" width="0.1524" layer="91"/>
<wire x1="0" y1="-27.94" x2="0" y2="-7.62" width="0.1524" layer="91"/>
<junction x="0" y="-7.62"/>
<wire x1="-58.42" y1="-7.62" x2="0" y2="-7.62" width="0.1524" layer="91"/>
<label x="-10.16" y="-7.62" size="1.778" layer="95"/>
</segment>
</net>
<net name="DIRML2" class="0">
<segment>
<pinref part="MOTOR" gate="-7" pin="S"/>
<label x="-50.8" y="22.86" size="1.778" layer="95"/>
<wire x1="-48.26" y1="22.86" x2="-55.88" y2="22.86" width="0.1524" layer="91"/>
<wire x1="-55.88" y1="22.86" x2="-55.88" y2="-12.7" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="BIN1"/>
<wire x1="7.62" y1="-12.7" x2="2.54" y2="-12.7" width="0.1524" layer="91"/>
<pinref part="U$3" gate="G$1" pin="AIN1"/>
<wire x1="7.62" y1="-22.86" x2="2.54" y2="-22.86" width="0.1524" layer="91"/>
<wire x1="2.54" y1="-22.86" x2="2.54" y2="-12.7" width="0.1524" layer="91"/>
<junction x="2.54" y="-12.7"/>
<wire x1="-55.88" y1="-12.7" x2="2.54" y2="-12.7" width="0.1524" layer="91"/>
<label x="-10.16" y="-12.7" size="1.778" layer="95"/>
</segment>
</net>
<net name="N$1" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="MOTORB1"/>
<pinref part="M1" gate="-1" pin="S"/>
<wire x1="43.18" y1="68.58" x2="73.66" y2="68.58" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$2" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="MOTORB2"/>
<pinref part="M1" gate="-2" pin="S"/>
<wire x1="43.18" y1="63.5" x2="73.66" y2="63.5" width="0.1524" layer="91"/>
<wire x1="73.66" y1="63.5" x2="73.66" y2="66.04" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$3" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="MOTORA1"/>
<pinref part="M2" gate="-1" pin="S"/>
<wire x1="43.18" y1="48.26" x2="76.2" y2="48.26" width="0.1524" layer="91"/>
<wire x1="76.2" y1="48.26" x2="76.2" y2="45.72" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$4" class="0">
<segment>
<pinref part="U$1" gate="G$1" pin="MOTORA2"/>
<pinref part="M2" gate="-2" pin="S"/>
<wire x1="43.18" y1="43.18" x2="76.2" y2="43.18" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$5" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="MOTORB1"/>
<wire x1="43.18" y1="2.54" x2="78.74" y2="2.54" width="0.1524" layer="91"/>
<pinref part="M3" gate="-1" pin="S"/>
</segment>
</net>
<net name="N$6" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="MOTORB2"/>
<wire x1="43.18" y1="-2.54" x2="78.74" y2="-2.54" width="0.1524" layer="91"/>
<pinref part="M3" gate="-2" pin="S"/>
<wire x1="78.74" y1="-2.54" x2="78.74" y2="0" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$7" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="MOTORA1"/>
<pinref part="M4" gate="-1" pin="S"/>
<wire x1="43.18" y1="-17.78" x2="78.74" y2="-17.78" width="0.1524" layer="91"/>
</segment>
</net>
<net name="N$8" class="0">
<segment>
<pinref part="U$3" gate="G$1" pin="MOTORA2"/>
<pinref part="M4" gate="-2" pin="S"/>
<wire x1="43.18" y1="-22.86" x2="78.74" y2="-22.86" width="0.1524" layer="91"/>
<wire x1="78.74" y1="-22.86" x2="78.74" y2="-20.32" width="0.1524" layer="91"/>
</segment>
</net>
</nets>
</sheet>
</sheets>
</schematic>
</drawing>
</eagle>
