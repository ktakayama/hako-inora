#----------------------------------------------------------------------
# Ȣ����� ver2.30
# �ȥåץ⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# ���Τ���� ver1.04
# Ȣ������http://espion.s7.xrea.com/tyotou/��
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �ȥåץڡ����⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub topPageMain {
	# ����
	unlock();

	# �ƥ�ץ졼�Ƚ���
	tempTopPage();
}

# �ȥåץڡ���
sub tempTopPage {
	# �����ȥ�
	out("${HtagTitle_}$Htitle${H_tagTitle}");

	# �ǥХå��⡼�ɤʤ�֥������ʤ��ץܥ���
	if($Hdebug == 1) {
		out(<<END);
<FORM action="$HthisFile" method="POST">
<INPUT TYPE="submit" VALUE="�������ʤ��" NAME="TurnButton">
</FORM>
END
	}
	if($makeMode eq 'cgi') {
		$owner = ' checked';
	} else {
		$java = ' checked';
	}
	my($mStr1) = '';
	if($HhideMoneyMode != 0) {
		$mStr1 = "<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}���${H_tagTH}</NOBR></TH>";
	}

	# ����ɽ��
	my($hour, $min, $sec);
	my($now) = time;
	my($showTIME) = ($HislandLastTime + $HunitTime - $now);
	$hour = int($showTIME / 3600);
	$min  = int(($showTIME - ($hour * 3600)) / 60);
	$sec  = $showTIME - ($hour * 3600) - ($min * 60);

	if ($sec < 0){
		out(<<END);
<H1>${HtagHeader_}������$HislandTurn/$HislandLastTurn${H_tagHeader}��$fightmode</H1><B><font size=+1>��${HtagHeader_}�������Ʋ�����${H_tagHeader}��</font></b>
END
	} else {
		out(<<END);
<H1>${HtagHeader_}������$HislandTurn/$HislandLastTurn${H_tagHeader} <font size=+1>�ʼ��Υ�����ޤǡ����� $hour ���� $min ʬ $sec �á�</font></b></H1>
END
	}

	# �ե�����
	out(<<END);
<SCRIPT language="JavaScript">
<!--
function develope(){
		if(document.Island.CHBOX.checked)
				document.Island.target = "_blank";
		else
				document.Island.target = "";
				return true;
}

//-->
</SCRIPT>
<HR>
<H1>${HtagHeader_}��ʬ�����${H_tagHeader}</H1>
<FORM name="Island" action="$HthisFile" method="POST">
���ʤ������̾���ϡ�<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT><BR>

�ѥ���ɤ�ɤ�������<BR>
<INPUT TYPE="password" NAME="PASSWORD" VALUE="$HdefaultPassword" SIZE=32 MAXLENGTH=32><BR>
<INPUT TYPE="submit" VALUE="��ȯ���˹Ԥ�" NAME="OwnerButton" onClick="develope()">
<INPUT TYPE="checkbox" NAME="CHBOX" VALUE="on">���������̤ǳ�ȯ<BR>
<INPUT TYPE="radio" NAME=JAVAMODE VALUE=cgi${owner}>�̾�⡼��
<INPUT TYPE="radio" NAME=JAVAMODE VALUE=java${java}>Java������ץȥ⡼��
</FORM>

<HR>

<H1>${HtagHeader_}����ξ���${H_tagHeader}</H1>
<P>
���̾���򥯥�å�����ȡ�<B>�Ѹ�</B>���뤳�Ȥ��Ǥ��ޤ���
</P>
<TABLE BORDER CELLSPACING=1>
<TR>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}���${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}��${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}���Τ����${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}�͸�${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}����${H_tagTH}</NOBR></TH>
$mStr1
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}����${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}���쵬��${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}���쵬��${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}�η��쵬��${H_tagTH}</NOBR></TH>
</TR>
END

	my($island, $j, $farm, $factory, $mountain, $name, $id, $prize, $ii, $contest);
	for($ii = 0; $ii < $HislandNumber; $ii++) {
		$j = $ii + 1;
		$island = $Hislands[$ii];

		$id = $island->{'id'};
		$farm = $island->{'farm'};
		$factory = $island->{'factory'};
		$mountain = $island->{'mountain'};
		$farm = ($farm == 0) ? "��ͭ����" : "${farm}0$HunitPop";
		$factory = ($factory == 0) ? "��ͭ����" : "${factory}0$HunitPop";
		$mountain = ($mountain == 0) ? "��ͭ����" : "${mountain}0$HunitPop";
		if($island->{'absent'}  == 0) {
			$name = "${HtagName_}$island->{'name'}��${H_tagName}";
		} else {
			$name = "${HtagName2_}$island->{'name'}��($island->{'absent'})${H_tagName2}";
		}

		$prize = $island->{'prize'};
		my($flags, $monsters, $turns);
		$prize =~ /([0-9]*),([0-9]*),(.*)/;
		$flags = $1;
		$monsters= $2;
		$turns = $3;
		$prize = '';

		# �������դ�ɽ��
		while($turns =~ s/([0-9]*),//) {
			$prize .= "<IMG SRC=\"prize0.png\" ALT=\"$1${Hprize[0]}\" WIDTH=16 HEIGHT=16> ";
		}

		# ̾���˾ޤ�ʸ�����ɲ�
		my($f) = 1;
		my($i);
		for($i = 1; $i < 10; $i++) {
			if($flags & $f) {
				$prize .= "<IMG SRC=\"prize${i}.png\" ALT=\"${Hprize[$i]}\" WIDTH=16 HEIGHT=16> ";
			}
			$f *= 2;
		}

		# �ݤ������åꥹ��
		$f = 1;
		my($max) = -1;
		my($mNameList) = '';
		for($i = 0; $i < $HmonsterNumber; $i++) {
			if($monsters & $f) {
				$mNameList .= "[$HmonsterName[$i]] ";
				$max = $i;
			}
			$f *= 2;
		}
		if($max != -1) {
			$prize .= "<IMG SRC=\"${HmonsterImage[$max]}\" ALT=\"$mNameList\" WIDTH=16 HEIGHT=16> ";
		}

		$prize .= "<BR>";
		my($c_arm, $c_cute, $c_int) = split(",",$island->{'i_cont'});
		for($co = 0;$co < $c_arm;$co++) {
			$prize .= "<IMG SRC=\"monster7.png\" ALT=\"${Hprize[10]}ͥ��\" WIDTH=16 HEIGHT=16> ";
		}
		for($co = 0;$co < $c_cute;$co++) {
			$prize .= "<IMG SRC=\"monster8.png\" ALT=\"${Hprize[11]}ͥ��\" WIDTH=16 HEIGHT=16> ";
		}
		for($co = 0;$co < $c_int;$co++) {
			$prize .= "<IMG SRC=\"monster9.png\" ALT=\"${Hprize[12]}ͥ��\" WIDTH=16 HEIGHT=16> ";
		}

		my($mStr1) = '';
		if($HhideMoneyMode == 1) {
			$mStr1 = "<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$island->{'money'}$HunitMoney</NOBR></TD>";
		} elsif($HhideMoneyMode == 2) {
			my($mTmp) = aboutMoney($island->{'money'});
			$mStr1 = "<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$mTmp</NOBR></TD>";
		}

		my($comname) ="${HtagTH_}�����ȡ�${H_tagTH}";
		if(($island->{'ownername'} ne '0') && ($island->{'ownername'} ne "������")){
			$comname = "<FONT COLOR=\"blue\"><B>$island->{'ownername'}��</b></font>";
		}

		my($image_name);
		$image_name = $HmonsterImage[$island->{'i_type'}];
		$image_name2 = $image_name;
		$image_name = "an_".$image_name2 if($island->{'i_ang'} < 1000);
		$image_name = "sl_".$image_name2 if($island->{'i_sleep'} > 100);
		$i_image = "<IMG SRC=\"${image_name}\" WIDTH=48 HEIGHT=48 ALIGN=LEFT> ";

		my $i_hp   = int($island->{'i_hp'} / 1000);
		my $i_arm  = int($island->{'i_arm'} / 1000);
		my $i_int  = int($island->{'i_int'} / 1000);
		my $i_cute = int($island->{'i_cute'} / 1000);
		$i_hp = 1 if($i_hp < 1);
		$i_arm = 0 if($i_arm < 1);
		$i_int = 0 if($i_int < 1);
		$i_cute = 0 if($i_cute < 1);

		out(<<END);
<TR>
<TD $HbgNumberCell ROWSPAN=2 align=center nowrap=nowrap><NOBR>${HtagNumber_}$j${H_tagNumber}</NOBR></TD>
<TD $HbgNameCell ROWSPAN=2 align=left nowrap=nowrap>
<NOBR>
<A STYlE=\"text-decoration:none\" HREF="${HthisFile}?Sight=${id}">
$name
</A><BR>
$prize
</NOBR>
</TD>
<TD $HbgNameCell ROWSPAN=2 nowrap=nowrap>
<TABLE CELLSPACING=0 CELLPADDING=0>
<TR><TD>
<NOBR>
$i_image
<TD nowrap=nowrap>
̾����${HtagIName_}$island->{'i_name'}${H_tagIName}<BR>
���ࡧ$HmonsterName[$island->{'i_type'}]<BR>
�Ρ�${i_hp} </b>
�ӡ�${i_arm} </b>
̥��${i_cute} </b>
�Ρ�${i_int}<BR></b>
</TABLE>
</TD>
<TD $HbgInfoCell align=right nowrap=nowrap>
<NOBR>$island->{'pop'}$HunitPop</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$island->{'area'}$HunitArea</NOBR></TD>
$mStr1
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$island->{'food'}$HunitFood</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$farm</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$factory</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$mountain</NOBR></TD>
</TR>
<TR>
<TD $HbgCommentCell COLSPAN=7 align=left nowrap=nowrap><NOBR>$comname$island->{'comment'}</NOBR></TD>
</TR>
END
	}

	out(<<END);
</TABLE>

<HR>
<H1>${HtagHeader_}���������õ��${H_tagHeader}</H1>
END

	if($HislandNumber < $HmaxIsland) {
		out(<<END);
<FORM action="$HthisFile" method="POST">
���̾��<BR>
<INPUT TYPE="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>��<BR>
���Τ��̾��(<FONT COLOR=RED>�����ѹ��Բġ�10ʸ�����٤�˾�ޤ���</FONT>)<BR>
<INPUT TYPE="text" NAME="MONSTERNAME" SIZE=32 MAXLENGTH=64><BR>
�ѥ���ɤϡ�<BR>
<INPUT TYPE="password" NAME="PASSWORD" SIZE=32 MAXLENGTH=32><BR>
ǰ�Τ���ѥ���ɤ�⤦���<BR>
<INPUT TYPE="password" NAME="PASSWORD2" SIZE=32 MAXLENGTH=32><BR>

<INPUT TYPE="submit" VALUE="õ���˹Ԥ�" NAME="NewIslandButton">
</FORM>
END
	} else {
		out(<<END);
		��ο���������Ǥ�������������Ͽ�Ǥ��ޤ���
END
	}

	my($Himfflag);
	if($HimgLine eq '' || $HimgLine eq $imageDir){
		$Himfflag = '<FONT COLOR=RED>̤����</FONT>';
	} else {
		$Himfflag = $baseIMG;
	}

	out(<<END);
<HR><P>
<TABLE>
<TR><TD WIDTH=420 ROWSPAN=2 VALIGN=TOP>
<H1>${HtagHeader_}���̾���ȥѥ���ɤ��ѹ�${H_tagHeader}</H1>
<P>
(���)̾�����ѹ��ˤ�$HcostChangeName${HunitMoney}������ޤ���
</P>
<FORM action="$HthisFile" method="POST">
�ɤ���Ǥ�����<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<BR>
�ɤ��̾�����Ѥ��ޤ�����(�ѹ�������Τ�)<BR>
<INPUT TYPE="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>��<BR>
�ѥ���ɤϡ�(ɬ��)<BR>
<INPUT TYPE="password" NAME="OLDPASS" SIZE=32 MAXLENGTH=32><BR>
�������ѥ���ɤϡ�(�ѹ�������Τ�)<BR>
<INPUT TYPE="password" NAME="PASSWORD" SIZE=32 MAXLENGTH=32><BR>
ǰ�Τ���ѥ���ɤ�⤦���(�ѹ�������Τ�)<BR>
<INPUT TYPE="password" NAME="PASSWORD2" SIZE=32 MAXLENGTH=32><BR>

<INPUT TYPE="submit" VALUE="�ѹ�����" NAME="ChangeInfoButton">
</FORM>

</TD>

<TD VALIGN=TOP WIDTH=350>
<H1>${HtagHeader_}�����Υ���������${H_tagHeader}</H1>
<NOBR>���ߤ�����<B>[</b> ${Himfflag} <B>]</B></NOBR>
<BR><A HREF=${imageExp} target=_blank><FONT SIZE=+1> �� �� </FONT></A>
<form action=$HthisFile method=POST>
<INPUT TYPE=file NAME="IMGLINE">
<INPUT TYPE="submit" VALUE="����" name=IMGSET>
</form>

<form action=$HthisFile method=POST>
Mac�桼������<BR>
<INPUT TYPE=text NAME="IMGLINEMAC">
<INPUT TYPE="submit" VALUE="����" name=IMGSET><BR>
<FONT SIZE=-1>Mac�����ϡ����������Ѥ��Ʋ�������</FONT>
</form>
</TD></TR>

<TR HEIGHT=100><TD ALIGN=CENTER>
<form action=$HthisFile method=POST>
<INPUT TYPE=hidden NAME="IMGLINE" value="deletemodenow">
<INPUT TYPE="submit" VALUE="�����������" name=IMGSET>
</form>
</TD></TR>
</TABLE>
<HR>
<H1>${HtagHeader_}�����ʡ���̾�����ꡪ${H_tagHeader}</H1>
<FORM action="$HthisFile" method="POST">
���ʤ�����ϡ�
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>����̾������
<INPUT TYPE="text" NAME="OWNERNAME" SIZE=16 MAXLENGTH=32>
�����ѥ����
<INPUT TYPE="password" NAME="OLDPASS" SIZE=16 MAXLENGTH=32>
<INPUT TYPE="submit" VALUE="����ˤ���" NAME="ChangeOwnerName">
</form>
<HR>
<H1>${HtagHeader_}ȯ���ε�Ͽ${H_tagHeader}</H1>
END
	historyPrint();
}

# ��Ͽ�ե�����ɽ��
sub historyPrint {
	open(HIN, "${HdirName}/hakojima.his");
	my(@line, $l);
	while($l = <HIN>) {
		chomp($l);
		push(@line, $l);
	}
	@line = reverse(@line);

	foreach $l (@line) {
		$l =~ /^([0-9]*),(.*)$/;
		out("<NOBR>${HtagNumber_}������${1}${H_tagNumber}��${2}</NOBR><BR>\n");
	}
	close(HIN);
}


#----------------------------------------------------------------------
# ��ɽ���⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub logViewMain {

	# ����
	unlock();

	# �ƥ�ץ졼�Ƚ���
	tempLogPage();
}

sub tempLogPage {

	out(<<END);

<font size=+3><b>${HtagHeader_}�Ƕ�ν����${H_tagHeader}</b></font>��
��<a href="$HthisFile?LogFileView=1"><FONT COLOR="blue" size=2><B>��������</a>
��<a href="$HthisFile?LogFileView=2">2������ʬɽ��</a>
END
for($i = 3; $i -1 < $HlogMax; $i++) {
		out("��<a href=\"$HthisFile?LogFileView=${i}\">${i}������ʬ</a>\n");
}
	out(<<END);
</b></font><br>
END
	logPrintTop();

}

# ��ɽ��
sub logPrintTop {
	my($i);
	for($i = 0; $i < $Hlogturn; $i++) {
		out("<hr>\n");
		logFilePrint($i, 0, 0);

	}
}

1;

