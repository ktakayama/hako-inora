#----------------------------------------------------------------------
# Ȣ����� ver2.30
# �Ͽޥ⡼�ɥ⥸�塼��(ver1.00)
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# ���Τ���� ver1.03
# Ȣ������http://espion.x7.xrea.com/tyotou/��
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �Ѹ��⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub printIslandMain {
	# ����
	unlock();

	# id�������ֹ�����
	$HcurrentNumber = $HidToNumber{$HcurrentID};

	# �ʤ��������礬�ʤ����
	if($HcurrentNumber eq '') {
		tempProblem();
		return;
	}

	# ̾���μ���
	$HcurrentName = $Hislands[$HcurrentNumber]->{'name'};

	# �Ѹ�����
	tempPrintIslandHead(); # �褦����!!
	islandInfo(); # ��ξ���
	islandMap(0); # ����Ͽޡ��Ѹ��⡼��

	# �����������Ǽ���
	if($HuseLbbs) {
		tempLbbsHead();	 # ������Ǽ���
		tempLbbsInput();   # �񤭹��ߥե�����
		tempLbbsContents(); # �Ǽ�������
	}

	# �ᶷ
	tempRecent(0);
}

#----------------------------------------------------------------------
# ��ȯ�⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub ownerMain {
	# ����
	unlock();

	# �⡼�ɤ�����
	$HmainMode = 'owner';

	# id����������
	$HcurrentNumber = $HidToNumber{$HcurrentID};
	my($island) = $Hislands[$HcurrentNumber];
	$HcurrentName = $island->{'name'};

	# �ѥ����
	if(!checkPassword($island->{'password'},$HinputPassword)) {
		# password�ְ㤤
		tempWrongPassword();
		return;
	}

	# ��ȯ����
	if($HjavaMode eq 'java') {
		tempOwnerJava(); # ��Java������ץȳ�ȯ�ײ��
	}else{			   # ���̾�⡼�ɳ�ȯ�ײ��
		tempOwner();
	}

	# �����������Ǽ���
	if($HuseLbbs) {
		# ������Ǽ���
		tempLbbsHead();
		if($HjavaMode eq 'java') {
			# Java������ץ��ѽ񤭹��ߥե�����
			tempLbbsInputJava();
		}else{
			# ������Ǽ���
			tempLbbsInputOW();
		}
		tempLbbsContents(); # �Ǽ�������
	}

	# �ᶷ
	tempRecent(1);
}

#----------------------------------------------------------------------
# ���ޥ�ɥ⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub commandMain {
	# id����������
	$HcurrentNumber = $HidToNumber{$HcurrentID};
	my($island) = $Hislands[$HcurrentNumber];
	$HcurrentName = $island->{'name'};

	# �ѥ����
	if(!checkPassword($island->{'password'},$HinputPassword)) {
		# password�ְ㤤
		unlock();
		tempWrongPassword();
		return;
	}

	# �⡼�ɤ�ʬ��
	my($command) = $island->{'command'};

	if($HcommandMode eq 'delete') {
		slideFront($command, $HcommandPlanNumber);
		tempCommandDelete();
	} elsif(($HcommandKind == $HcomAutoPrepare) ||
			($HcommandKind == $HcomAutoPrepare2)) {
		# �ե����ϡ��ե��Ϥʤ餷
		# ��ɸ�������
		makeRandomPointArray();
		my($land) = $island->{'land'};

		# ���ޥ�ɤμ������
		my($kind) = $HcomPrepare;
		if($HcommandKind == $HcomAutoPrepare2) {
			$kind = $HcomPrepare2;
		}

		my($i) = 0;
		my($j) = 0;
		while(($j < $HpointNumber) && ($i < $HcommandMax)) {
			my($x) = $Hrpx[$j];
			my($y) = $Hrpy[$j];
			if($land->[$x][$y] == $HlandWaste) {
				slideBack($command, $HcommandPlanNumber);
				$command->[$HcommandPlanNumber] = {
					'kind' => $kind,
					'target' => 0,
					'x' => $x,
					'y' => $y,
					'arg' => 0
					};
				$i++;
			}
			$j++;
		}
		tempCommandAdd();
	} elsif($HcommandKind == $HcomAutoDelete) {
		# ���ä�
		my($i);
		for($i = 0; $i < $HcommandMax; $i++) {
			slideFront($command, $HcommandPlanNumber);
		}
		tempCommandDelete();
	} else {
		if($HcommandMode eq 'insert') {
			slideBack($command, $HcommandPlanNumber);
		}
		tempCommandAdd();
		# ���ޥ�ɤ���Ͽ
		$command->[$HcommandPlanNumber] = {
			'kind' => $HcommandKind,
			'target' => $HcommandTarget,
			'x' => $HcommandX,
			'y' => $HcommandY,
			'arg' => $HcommandArg
			};
	}

	# �ǡ����ν񤭽Ф�
	writeIslandsFile($HcurrentID);

	# owner mode��
	ownerMain();

}

#----------------------------------------------------------------------
# ���������ϥ⡼��
#----------------------------------------------------------------------
# �ᥤ��
sub commentMain {
	# id����������
	$HcurrentNumber = $HidToNumber{$HcurrentID};
	my($island) = $Hislands[$HcurrentNumber];
	$HcurrentName = $island->{'name'};

	# �ѥ����
	if(!checkPassword($island->{'password'},$HinputPassword)) {
		# password�ְ㤤
		unlock();
		tempWrongPassword();
		return;
	}

	# ��å������򹹿�
	$island->{'comment'} = htmlEscape($Hmessage);

	# �ǡ����ν񤭽Ф�
	writeIslandsFile($HcurrentID);

	# �����ȹ�����å�����
	tempComment();

	# owner mode��
	ownerMain();
}

#----------------------------------------------------------------------
# ������Ǽ��ĥ⡼��
#----------------------------------------------------------------------
# �ᥤ��

sub localBbsMain {
	# id�������ֹ�����
	$HcurrentNumber = $HidToNumber{$HcurrentID};
	my($island) = $Hislands[$HcurrentNumber];
	my($foreignName);

	# �ʤ��������礬�ʤ����
	if($HcurrentNumber eq '' && $HcurrentID != 0) {
		unlock();
		tempProblem();
		return;
	}

	# ����⡼�ɤ���ʤ���̾������å��������ʤ����
	if($HlbbsMode != 2) {
		if(($HlbbsName eq '') || ($HlbbsMessage eq '')) {
			unlock();
			tempLbbsNoMessage();
			return;
		}
	}

   # ��̵���Ѹ��԰ʳ��ϥѥ���ɥ����å�
		if($HlbbsMode == 0 && $HforID != 0) {
			# ����ԥ⡼��
			my($foreignNumber) = $HidToNumber{$HforID};
			if($foreignNumber eq ''){
				unlock();
				tempProblem();
				return;
			}
			my($fIsland) = $Hislands[$foreignNumber];
			if(!checkPassword($fIsland->{'password'},$HinputPassword)) {
				unlock();
				tempWrongPassword();
				return;
			}
			$foreignName = $fIsland->{'name'};
		} elsif($HlbbsMode) {
			# ���⡼��
			if(!checkPassword($island->{'password'},$HinputPassword)) {
				# password�ְ㤤
				unlock();
				tempWrongPassword();
				return;
			}
		}

	my($lbbs);
	$lbbs = $island->{'lbbs'};

	# �⡼�ɤ�ʬ��
	if($HlbbsMode == 2) {
		# ����⡼��
		# ��å����������ˤ��餹
		slideBackLbbsMessage($lbbs, $HcommandPlanNumber);
		tempLbbsDelete();
	} else {
		# ��Ģ�⡼��
		# ��å���������ˤ��餹
		slideLbbsMessage($lbbs);

		if($HforID == 0 and $HlbbsMode == 0){
			$HlbbsMessage = htmlEscape($HlbbsMessage);
			$message = '3';
		} elsif (($HlbbsMode == 0) && ($HforID != $island->{'id'})){
			$HlbbsMessage = htmlEscape($HlbbsMessage) . "����<font size=-1 color=gray>(${foreignName}��)</font>";
			$message = '0';
		} else {
			$HlbbsMessage = htmlEscape($HlbbsMessage);
			$message = '1';
		}
		$HlbbsName = "$HislandTurn��" . htmlEscape($HlbbsName);
		$lbbs->[0] = "$message>$HlbbsName>$HlbbsMessage";

		tempLbbsAdd();
	}

	# �ǡ����񤭽Ф�
	writeIslandsFile($HcurrentID);

	# ��ȤΥ⡼�ɤ�
	if($HlbbsMode == 0) {
		printIslandMain();
	} else {
		ownerMain();
	}
}

# ������Ǽ��ĤΥ�å��������ĸ��ˤ��餹
sub slideLbbsMessage {
	my($lbbs) = @_;
	my($i);
	pop(@$lbbs);
	unshift(@$lbbs, $lbbs->[0]);
}

# ������Ǽ��ĤΥ�å������������ˤ��餹
sub slideBackLbbsMessage {
	my($lbbs, $number) = @_;
	my($i);
	splice(@$lbbs, $number, 1);
	$lbbs->[$HlbbsMax - 1] = '0>>';
}

#----------------------------------------------------------------------
# ����Ͽ�
#----------------------------------------------------------------------

# �����ɽ��
sub islandInfo {
	my($island) = $Hislands[$HcurrentNumber];
	# ����ɽ��
	my($rank) = $HcurrentNumber + 1;
	my($farm) = $island->{'farm'};
	my($factory) = $island->{'factory'};
	my($mountain) = $island->{'mountain'};
	$farm = ($farm == 0) ? "��ͭ����" : "${farm}0$HunitPop";
	$factory = ($factory == 0) ? "��ͭ����" : "${factory}0$HunitPop";
	$mountain = ($mountain == 0) ? "��ͭ����" : "${mountain}0$HunitPop";

	my($mStr1) = '';
	my($mStr2) = '';
	if(($HhideMoneyMode == 1) || ($HmainMode eq 'owner')) {
		# ̵���ޤ���owner�⡼��
		$mStr1 = "<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}���${H_tagTH}</NOBR></TH>";
		$mStr2 = "<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$island->{'money'}$HunitMoney</NOBR></TD>";
	} elsif($HhideMoneyMode == 2) {
		my($mTmp) = aboutMoney($island->{'money'});

		# 1000��ñ�̥⡼��
		$mStr1 = "<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}���${H_tagTH}</NOBR></TH>";
		$mStr2 = "<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$mTmp</NOBR></TD>";
	}
	my($comname) ="${HtagTH_}�����ȡ�${H_tagTH}";
	if(($island->{'ownername'} ne '0') && ($island->{'ownername'} ne "������")){
		$comname = "<FONT COLOR=\"blue\"><B>$island->{'ownername'}��</b></font>";
	}

	my $i_hp   = int($island->{'i_hp'} / 1000);
	my $i_arm  = int($island->{'i_arm'} / 1000);
	my $i_int  = int($island->{'i_int'} / 1000);
	my $i_cute = int($island->{'i_cute'} / 1000);
	$i_hp = 1 if($i_hp < 1);
	$i_arm = 0 if($i_arm < 1);
	$i_int = 0 if($i_int < 1);
	$i_cute = 0 if($i_cute < 1);

	# ����ɽ��
	my($hour, $min, $sec);
	my($now) = time;
	my($showTIME) = ($HislandLastTime + $HunitTime - $now);
	$hour = int($showTIME / 3600);
	$min  = int(($showTIME - ($hour * 3600)) / 60);
	$sec  = $showTIME - ($hour * 3600) - ($min * 60);

	out(<<END);
<CENTER>
<BR><B><font size=+1>������$HislandTurn</font></b>�ʻĤꡢ$hour���� $minʬ $sec�á�
<TABLE BORDER CELLSPACING=1>
<TR>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}���${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}�͸�${H_tagTH}</NOBR></TH>
$mStr1
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}����${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}����${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}���쵬��${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}���쵬��${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}�η��쵬��${H_tagTH}</NOBR></TH>
</TR>
<TR>
<TD $HbgNumberCell align=middle nowrap=nowrap><NOBR>${HtagNumber_}$rank${H_tagNumber}</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$island->{'pop'}$HunitPop</NOBR></TD>
$mStr2
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$island->{'food'}$HunitFood</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$island->{'area'}$HunitArea</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>${farm}</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>${factory}</NOBR></TD>
<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>${mountain}</NOBR></TD>
</TR>
<TR>
<TD $HbgCommentCell COLSPAN=8 align=left nowrap=nowrap><NOBR>$comname$island->{'comment'}</NOBR></TD>
</TR>
</TABLE>
<TABLE BORDER CELLSPACING=1>
<TR>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}̾��${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}����${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}������${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}����${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}����${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}̥��${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell nowrap=nowrap><NOBR>${HtagTH_}����${H_tagTH}</NOBR></TH>
</TR>
<TR>
<TD $HbgInfoCell ALIGN=LEFT nowrap=nowrap><NOBR>$island->{'i_name'}</NOBR></TD>
<TD $HbgInfoCell ALIGN=LEFT nowrap=nowrap><NOBR>$HmonsterName[$island->{'i_type'}]</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>������$island->{'i_age'}</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>$i_hp</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>$i_arm</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>$i_cute</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>$i_int</NOBR></TD>
</TR>
END
	if($HinputPassword eq $masterPassword) {
		out(<<END);
<TR>
<TD $HbgInfoCell ALIGN=LEFT nowrap=nowrap><NOBR>����$island->{'i_ang'}</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>��$island->{'i_heal'}</NOBR></TD>
<TD $HbgInfoCell ALIGN=LEFT nowrap=nowrap><NOBR>��̲$island->{'i_sleep'}</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>$island->{'i_hp'}</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>$island->{'i_arm'}</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>$island->{'i_cute'}</NOBR></TD>
<TD $HbgInfoCell ALIGN=right nowrap=nowrap><NOBR>$island->{'i_int'}</NOBR></TD>
</TR>
END
	}
	out("</TABLE>\n</CENTER>\n");
}

# �Ͽޤ�ɽ��
# ������1�ʤ顢�ߥ�����������򤽤Τޤ�ɽ��
sub islandMap {
	my($mode) = @_;
	my($island);
	$island = $Hislands[$HcurrentNumber];

	out(<<END);
<CENTER><TABLE BORDER CELLSPACING=0><TR><TD>
END
	# �Ϸ����Ϸ��ͤ����
	my($land) = $island->{'land'};
	my($landValue) = $island->{'landValue'};
	my($l, $lv);

	# ���ޥ�ɼ���
	my($command) = $island->{'command'};
	my($com, @comStr, $i);
	if($HmainMode eq 'owner') {
		for($i = 0; $i < $HcommandMax; $i++) {
			my($j) = $i + 1;
			$com = $command->[$i];
			if($com->{'kind'} < 34) {
				$comStr[$com->{'x'}][$com->{'y'}] .=
					" [${j}]$HcomName[$com->{'kind'}]";
			}
		}
	}

	# ��ɸ(��)�����
	out("<IMG SRC=\"xbar.png\" width=400 height=16><BR>");

	# ���Ϸ�����Ӳ��Ԥ����
	my($x, $y);
	for($y = 0; $y < $HislandSize; $y++) {
		# �������ܤʤ��ֹ�����
		if(($y % 2) == 0) {
			out("<IMG SRC=\"space${y}.gif\" width=16 height=32>");
		}

		# ���Ϸ������
		for($x = 0; $x < $HislandSize; $x++) {
			$l = $land->[$x][$y];
			$lv = $landValue->[$x][$y];
			landString($l, $lv, $x, $y, $mode, $comStr[$x][$y], 0, $island);
		}

		# ������ܤʤ��ֹ�����
		if(($y % 2) == 1) {
			out("<IMG SRC=\"space${y}.gif\" width=16 height=32>");
		}

		# ���Ԥ����
		out("<BR>");
	}
	out("</TD></TR></TABLE></CENTER>\n");
}

sub landString {
	my($l, $lv, $x, $y, $mode, $comStr, $ikkatu, $island) = @_;
	my($point) = "($x,$y)";
	my($image, $alt);

	if($l == $HlandSea) {

		if($lv == 1) {
			# ����
			$image = 'land14.png';
			$alt = '��(����)';
		} else {
			# ��
			$image = 'land0.png';
			$alt = '��';
		}
	} elsif($l == $HlandWaste) {
		# ����
		if($lv == 1) {
			$image = 'land13.png'; # ������
			$alt = '����';
		} else {
			$image = 'land1.png';
			$alt = '����';
		}
	} elsif($l == $HlandPlains) {
		# ʿ��
		$image = 'land2.png';
		$alt = 'ʿ��';
	} elsif($l == $HlandForest) {
		# ��
		if($mode == 1) {
			$image = 'land6.png';
			$alt = "��(${lv}$HunitTree)";
		} else {
			# �Ѹ��Ԥξ����ڤ��ܿ�����
			$image = 'land6.png';
			$alt = '��';
		}
	} elsif($l == $HlandTown) {
		# Į
		my($p, $n);
		if($lv < 30) {
			$p = 3;
			$n = '¼';
		} elsif($lv < 100) {
			$p = 4;
			$n = 'Į';
		} else {
			$p = 5;
			$n = '�Ի�';
		}

		$image = "land${p}.png";
		$alt = "$n(${lv}$HunitPop)";
	} elsif($l == $HlandFarm) {
		# ����
		$image = 'land7.png';
		$alt = "����(${lv}0${HunitPop}����)";
	} elsif($l == $HlandFactory) {
		# ����
		$image = 'land8.png';
		$alt = "����(${lv}0${HunitPop}����)";
	} elsif($l == $HlandBase) {
		# �ߥ��������
		my($level) = expToLevel($l, $lv);
		$image = 'land9.png';
		$alt = "�ߥ�������� (��٥� ${level}/�и��� $lv)";
	} elsif($l == $HlandSbase) {
		# �������
		my($level) = expToLevel($l, $lv);
		$image = 'land12.png';
		$alt = "������� (��٥� ${level}/�и��� $lv)";
	} elsif($l == $HlandDefence) {
		# �ɱһ���
		$image = 'land10.png';
		$alt = '�ɱһ���';
	} elsif($l == $HlandHaribote) {
		# �ϥ�ܥ�
		$image = 'land10.png';
		if($mode == 0) {
			# �Ѹ��Ԥξ����ɱһ��ߤΤդ�
			$alt = '�ɱһ���';
		} else {
			$alt = '�ϥ�ܥ�';
		}
	} elsif($l == $HlandOil) {
		# ��������
		$image = 'land16.png';
		$alt = '��������';
	} elsif($l == $HlandMountain) {
		# ��
		my($str);
		$str = '';
		if($lv > 0) {
			$image = 'land15.png';
			$alt = "��(�η���${lv}0${HunitPop}����)";
		} else {
			$image = 'land11.png';
			$alt = '��';
		}
	} elsif($l == $HlandMonument) {
		# ��ǰ��
		$image = $HmonumentImage[$lv];
		$alt = $HmonumentName[$lv];
	} elsif($l == $HlandMonster) {
		# ����
		my($kind, $name, $hp) = monsterSpec($lv);
		my($special) = $HmonsterSpecial[$kind];
		if($kind < 4) {
			$image = $HmonsterImage[$kind];
			# �Ų���?
			if((($special == 3) && (($HislandTurn % 2) == 1)) ||
			   (($special == 4) && (($HislandTurn % 2) == 0))) {
				# �Ų���
				$image = $HmonsterImage2[$kind];
			}
			$alt = "$name(����${hp})";
		} else {
			$image = $HmonsterImage[$island->{'i_type'}];
			$image2 = $image;
			$image = "an_".$image2 if($island->{'i_ang'} < 1000);
			$image = "sl_".$image2 if($island->{'i_sleep'} > 100);
			$island->{'i_name'} .= "(�µ�)" if($island->{'i_sleep'} > 200);
			$alt = $island->{'i_name'};
		}
	}


	# ��ȯ���̤ξ��ϡ���ɸ����
	out(qq#<A HREF="JavaScript:void(0);" #);
	if($ikkatu and $mode) {
		# JS�������ѡ������ʡ�
		out(qq#onclick="ps($x,$y)" #);
		out(qq#onMouseOver="set_com($x, $y, '$point $alt');return true;">#);
		$comStr = "";
	}elsif($mode) {
		out("onclick=\"ps($x,$y)\" onMouseOver=\"ShowMsg('$point $alt $comStr'); return true;\">");
	} else {
		out("onMouseOver=\"ShowMsg('$point $alt $comStr'); return true;\">");
	}

	out("<IMG SRC=\"$image\" TITLE=\"$point $alt $comStr\" ALT=\"$point $alt $comStr\" width=32 height=32 BORDER=0></A>");

}


#----------------------------------------------------------------------
# �ƥ�ץ졼�Ȥ���¾
#----------------------------------------------------------------------
# ���̥�ɽ��
sub logPrintLocal {
	my($mode) = @_;
	my($i);
	for($i = 0; $i < $HlogMax; $i++) {
		logFilePrint($i, $HcurrentID, $mode, 1);
	}
}

# ������ؤ褦��������
sub tempPrintIslandHead {
	out(<<END);
<CENTER>
${HtagBig_}${HtagName_}��${HcurrentName}���${H_tagName}�ؤ褦��������${H_tagBig}<BR>
$HtempBack<BR>
</CENTER>
<SCRIPT Language="JavaScript">
<!--
function ShowMsg(n){
		status = n;
}
//-->
</SCRIPT>
END
}

# �����糫ȯ�ײ�
sub tempOwner {
    #���ޥ�ɥꥹ�ȥ��å�
	my($l_kind);
	$set_listcom = "";
	$All_listCom = 0;
	$com_count = @HcommandDivido;
	for($m = 0; $m < $com_count; $m++) {
		($aa,$dd,$ff) = split(/,/,$HcommandDivido[$m]);
		$set_listcom .= "\[ ";
	    for($i = 0; $i < $HcommandTotal; $i++) {
			$l_kind = $HcomList[$i];
			$l_cost = $HcomCost[$l_kind];
			if($l_cost == 0) { $l_cost = '̵��'	}
			elsif($l_cost < 0) { $l_cost = - $l_cost; $l_cost .= $HunitFood; }
			else { $l_cost .= $HunitMoney; }
			if($l_kind > $dd-1 && $l_kind < $ff+1) {
				$set_listcom .= "\[$l_kind\,\'$HcomName[$l_kind]\',\'$l_cost\'\]\,\n";
				$All_listCom++;
			}
			if($l_kind < $ff+1) { next; }
		}
		$bai = length($set_listcom);
		$set_listcom = substr($set_listcom, 0,$bai-2);
		$set_listcom .= " \],\n";
	}
	$bai = length($set_listcom);
	$set_listcom = substr($set_listcom, 0,$bai-2);
	if($HdefaultKind eq ''){ $default_Kind = 1;}
	else{ $default_Kind = $HdefaultKind; }

	out(<<END);
<CENTER>
${HtagBig_}${HtagName_}${HcurrentName}��${H_tagName}��ȯ�ײ�${H_tagBig}<BR>
$HtempBack<BR>
</CENTER>
<SCRIPT Language="JavaScript">
<!--
comlist = [
$set_listcom];

function ps(x, y) {
	document.forms[0].elements[5].options[x].selected = true;
	document.forms[0].elements[6].options[y].selected = true;
	return true;
}

function ns(x) {
	document.forms[0].elements[2].options[x].selected = true;
	return true;
}
function ShowMsg(n){
		status = n;
}

function SelectList(theForm){
	var u, selected_ok;
	if(!theForm){s = ''}
	else { s = theForm.menu.options[theForm.menu.selectedIndex].value; }
	if(s == ''){
		u = 0; selected_ok = 0;
		document.my_form.COMMAND.options.length = $All_listCom;
		for (i=0; i<comlist.length; i++) {
			var command = comlist[i];
			for (a=0; a<command.length; a++) {
				comName = command[a][1] + "(" + command[a][2] + ")";
				document.my_form.COMMAND.options[u].value = command[a][0];
				document.my_form.COMMAND.options[u].text = comName;
				if(command[a][0] == $default_Kind){
					document.my_form.COMMAND.options[u].selected = true;
					selected_ok = 1;
				}
				u++;
			}
		}
		if(selected_ok == 0)
		document.my_form.COMMAND.selectedIndex = 0;
	} else {
		var command = comlist[s];
		document.my_form.COMMAND.options.length = command.length;
		for (i=0; i<command.length; i++) {
			comName = command[i][1] + "(" + command[i][2] + ")";
			document.my_form.COMMAND.options[i].value = command[i][0];
			document.my_form.COMMAND.options[i].text = comName;
			if(command[i][0] == $default_Kind){
				document.my_form.COMMAND.options[i].selected = true;
				selected_ok = 1;
			}
		}
		if(selected_ok == 0)
		document.my_form.COMMAND.selectedIndex = 0;
	}
}


//-->
</SCRIPT>
END

	islandInfo();

	out(<<END);
<CENTER>
<TABLE BORDER CELLSPACING=0>
<TR>
<TD $HbgInputCell WIDTH=200>
<CENTER>
<FORM action="$HthisFile" method=POST NAME="my_form">
<INPUT TYPE=submit VALUE="�ײ�����" NAME=CommandButton$Hislands[$HcurrentNumber]->{'id'}>
<HR>
<B>�ѥ����</B></BR>
<INPUT TYPE=password NAME=PASSWORD VALUE="$HdefaultPassword">
<HR>
<B>�ײ��ֹ�</B><SELECT NAME=NUMBER>
END
	# �ײ��ֹ�
	my($j, $i);
	for($i = 0; $i < $HcommandMax; $i++) {
		$j = $i + 1;
		out("<OPTION VALUE=$i>$j\n");
	}

	out(<<END);
</SELECT><BR>
<HR>
<B>��ȯ�ײ衧</B>
<SELECT NAME=menu onchange="SelectList(my_form)">
<OPTION VALUE=>������
END
	for($i = 0; $i < $com_count; $i++) {
		($aa) = split(/,/,$HcommandDivido[$i]);
		out("<OPTION VALUE=$i>$aa\n");
	}
    out(<<END);
</SELECT><br>
<SELECT NAME=COMMAND>
END

	#���ޥ��
	my($kind, $cost, $s);
	for($i = 0; $i < $HcommandTotal; $i++) {
		$kind = $HcomList[$i];
		$cost = $HcomCost[$kind];
		if($cost == 0) {
			$cost = '̵��'
		} elsif($cost < 0) {
			$cost = - $cost;
			$cost .= $HunitFood;
		} else {
			$cost .= $HunitMoney;
		}
		if($kind == $HdefaultKind) {
			$s = 'SELECTED';
		} else {
			$s = '';
		}
#		print "<OPTION VALUE=$kind $s>$HcomName[$kind]($cost)\n";
		out("<OPTION VALUE=$kind $s>$HcomName[$kind]($cost)\n");
	}

	out(<<END);
</SELECT>
<HR>
<B>��ɸ(</B>
<SELECT NAME=POINTX>

END
	for($i = 0; $i < $HislandSize; $i++) {
		if($i == $HdefaultX) {
			out("<OPTION VALUE=$i SELECTED>$i\n");
		} else {
			out("<OPTION VALUE=$i>$i\n");
		}
	}

	out(<<END);
</SELECT>, <SELECT NAME=POINTY>
END

	for($i = 0; $i < $HislandSize; $i++) {
		if($i == $HdefaultY) {
			out("<OPTION VALUE=$i SELECTED>$i\n");
		} else {
			out("<OPTION VALUE=$i>$i\n");
		}
	}
	out(<<END);
</SELECT><B>)</B>
<HR>
<B>����</B><SELECT NAME=AMOUNT>
END

	# ����
	for($i = 0; $i < 100; $i++) {
		out("<OPTION VALUE=$i>$i\n");
	}

	out(<<END);
</SELECT>
<HR>
<B>��ɸ����</B><BR>
<SELECT NAME=TARGETID>
$HislandList<BR>
</SELECT>
<HR>
<B>ư��</B><BR>
<INPUT TYPE=radio NAME=COMMANDMODE VALUE=insert CHECKED>����
<INPUT TYPE=radio NAME=COMMANDMODE VALUE=write>���<BR>
<INPUT TYPE=radio NAME=COMMANDMODE VALUE=delete>���
<HR>
<INPUT TYPE=submit VALUE="�ײ�����" NAME=CommandButton$Hislands[$HcurrentNumber]->{'id'}>

</CENTER>
</FORM>
<nobr><center>�ߥ�����ȯ�;�¿�[<b> $Hislands[$HcurrentNumber]->{'fire'} </b>]ȯ</center></nobr>
</TD>
<TD $HbgMapCell>
END
	islandMap(1);	# ����Ͽޡ���ͭ�ԥ⡼��
	out(<<END);
</TD>
<TD $HbgCommandCell>
END
	for($i = 0; $i < $HcommandMax; $i++) {
		tempCommand($i, $Hislands[$HcurrentNumber]->{'command'}->[$i]);
	}

	out(<<END);

</TD>
</TR>
</TABLE>
</CENTER>
<HR>
<CENTER>
${HtagBig_}�����ȹ���${H_tagBig}<BR>
<FORM action="$HthisFile" method="POST">
������<INPUT TYPE=text NAME=MESSAGE SIZE=80><BR>
�ѥ����<INPUT TYPE=password NAME=PASSWORD VALUE="$HdefaultPassword">
<INPUT TYPE=submit VALUE="�����ȹ���" NAME=MessageButton$Hislands[$HcurrentNumber]->{'id'}>
</FORM>
</CENTER>
END

}

# ���ϺѤߥ��ޥ��ɽ��
sub tempCommand {
	my($number, $command) = @_;
	my($kind, $target, $x, $y, $arg) =
		(
		 $command->{'kind'},
		 $command->{'target'},
		 $command->{'x'},
		 $command->{'y'},
		 $command->{'arg'}
		 );
	my($name) = "$HtagComName_${HcomName[$kind]}$H_tagComName";
	my($point) = "$HtagName_($x,$y)$H_tagName";
	$target = $HidToName{$target};
	if($target eq '') {
		$target = "̵��";
	}
	$target = "$HtagName_${target}��$H_tagName";
	my($value) = $arg * $HcomCost[$kind];
	if($value == 0) {
		$value = $HcomCost[$kind];
	}
	if($value < 0) {
		$value = -$value;
		$value = "$value$HunitFood";
	} else {
		$value = "$value$HunitMoney";
	}
	$value = "$HtagName_$value$H_tagName";

	my($j) = sprintf("%02d��", $number + 1);

	out("<A STYlE=\"text-decoration:none\" HREF=\"JavaScript:void(0);\" onClick=\"ns($number)\"><NOBR>$HtagNumber_$j$H_tagNumber<FONT COLOR=\"$HnormalColor\">");

	if(($kind == $HcomDoNothing) ||
	   ($kind == $HcomGiveup)) {
		out("$name");
	} elsif(($kind == $HcomMissileNM) ||
			($kind == $HcomMissilePP)) {
		# �ߥ������
		my($n) = ($arg == 0 ? '̵����' : "${arg}ȯ");
		out("$target$point��$name($HtagName_$n$H_tagName)");
	} elsif($kind == $HcomSell) {
		# ����͢��
		out("$name$value");
	} elsif($kind == $HcomPropaganda) {
		# Ͷ�׳�ư
		out("$name");
	} elsif(($kind == $HcomMoney) ||
			($kind == $HcomFood)) {
		# ���
		out("$target��$name$value");
	} elsif($kind == $HcomDestroy) {
		# ����
		if($arg != 0) {
			out("$point��$name(ͽ��${value})");
		} else {
			out("$point��$name");
		}
	} elsif(($kind == $HcomFarm) ||
			 ($kind == $HcomFactory) ||
			 ($kind == $HcomMountain)) {
		# ����դ�
		if($arg == 0) {
			out("$point��$name");
		} else {
			out("$point��$name($arg��)");
		}
	} else {
		# ��ɸ�դ�
		out("$point��$name");
	}

	out("</FONT></NOBR></A><BR>");
}

# ������Ǽ���
sub tempLbbsHead {
	out(<<END);
<HR>
<CENTER>
${HtagBig_}${HtagName_}${HcurrentName}��${H_tagName}�Ѹ����̿�${H_tagBig}<BR>
</CENTER>
END
}

# ������Ǽ������ϥե�����
sub tempLbbsInput {
	out(<<END);
<CENTER>
<FORM action="$HthisFile" method="POST">
<font color=red><B>�礬̵�����⵭Ģ�Ǥ��ޤ����������������Ƥ˴ط���̵��ȯ���ϡ�����������${bbsname}�ؤ��ꤤ���ޤ���</b></font>
<TABLE BORDER CELLSPACING=0>
<TR>
<TH>̾��</TH>
<TH>����</TH>
</TR>
<TR>
<TD><INPUT TYPE="text" SIZE=32 MAXLENGTH=32 NAME="LBBSNAME" VALUE="$HdefaultName"></TD>
<TD><INPUT TYPE="text" SIZE=80 NAME="LBBSMESSAGE"></TD>
</TR>
<TR>
<TD colspan="2">��ʬ���硧
<SELECT NAME="ISLANDID">
<OPTION value="0">��̵���Ѹ���
$HislandList</SELECT>
���ѥ���ɡ�<INPUT TYPE="password" SIZE=32 MAXLENGTH=32 NAME=PASSWORD VALUE="$HdefaultPassword">
<INPUT TYPE="submit" VALUE="��Ģ����" NAME="LbbsButtonFO$HcurrentID"></TD>
</TR>
</TABLE>
</FORM>
</CENTER>
END
}

# ������Ǽ������ϥե����� owner mode��
sub tempLbbsInputOW {
	out(<<END);
<CENTER>
<FORM action="$HthisFile" method="POST">
<TABLE BORDER CELLSPACING=0>
<TR>
<TH>̾��</TH>
<TH COLSPAN=2>����</TH>
</TR>
<TR>
<TD><INPUT TYPE="text" SIZE=32 MAXLENGTH=32 NAME="LBBSNAME" VALUE="$HdefaultName"></TD>
<TD COLSPAN=2><INPUT TYPE="text" SIZE=80 NAME="LBBSMESSAGE"></TD>
</TR>
<TR>
<TH>�ѥ����</TH>
<TH COLSPAN=2>ư��</TH>
</TR>
<TR>
<TD><INPUT TYPE=password SIZE=32 MAXLENGTH=32 NAME=PASSWORD VALUE="$HdefaultPassword"></TD>
<TD align=right>
<INPUT TYPE="submit" VALUE="��Ģ����" NAME="LbbsButtonOW$HcurrentID">
</TD>
<TD align=right>
�ֹ�
<SELECT NAME=NUMBER>
END
	# ȯ���ֹ�
	my($j, $i);
	for($i = 0; $i < $HlbbsMax; $i++) {
		$j = $i + 1;
		out("<OPTION VALUE=$i>$j\n");
	}
	out(<<END);
</SELECT>
<INPUT TYPE="submit" VALUE="�������" NAME="LbbsButtonDL$HcurrentID">
</TD>
</TR>
</TABLE>
</FORM>
</CENTER>
END
}

# ������Ǽ�������
sub tempLbbsContents {
	my($lbbs, $line);
	$lbbs = $Hislands[$HcurrentNumber]->{'lbbs'};
	out(<<END);
<CENTER>
<TABLE BORDER CELLSPACING=0>
<TR>
<TH>�ֹ�</TH>
<TH>��Ģ����</TH>
</TR>
END

	my($i);
	for($i = 0; $i < $HlbbsMax; $i++) {
		$line = $lbbs->[$i];
		if($line =~ /([0-9]*)\>(.*)\>(.*)$/) {
			my($j) = $i + 1;
			out("<TR><TD align=center>$HtagNumber_$j$H_tagNumber</TD>");
			if($1 == 0) {
				# �Ѹ���
				out("<TD>$HtagLbbsSS_$2 > $3$H_tagLbbsSS</TD></TR>");
			} elsif($1 == 3) {
				# ��̵���Ѹ���
				out("<TD>$HtagLbbsSK_$2 > $3$H_tagLbbsSK</TD></TR>");
			} else {
				# ���
				out("<TD>$HtagLbbsOW_$2 > $3$H_tagLbbsOW</TD></TR>");
			}
		}
	}

	out(<<END);
</TD></TR></TABLE></CENTER>
END
}

# ������Ǽ��Ĥ�̾������å��������ʤ����
sub tempLbbsNoMessage {
	out(<<END);
${HtagBig_}̾���ޤ������Ƥ��󤬶���Ǥ���${H_tagBig}$HtempBack
END
}

# �񤭤��ߺ��
sub tempLbbsDelete {
	out(<<END);
${HtagBig_}��Ģ���Ƥ������ޤ���${H_tagBig}<HR>
END
}

# ���ޥ����Ͽ
sub tempLbbsAdd {
	out(<<END);
${HtagBig_}��Ģ��Ԥ��ޤ���${H_tagBig}<HR>
END
}

# ���ޥ�ɺ��
sub tempCommandDelete {
	out(<<END);
${HtagBig_}���ޥ�ɤ������ޤ���${H_tagBig}<HR>
END
}

# ���ޥ����Ͽ
sub tempCommandAdd {
	out(<<END);
${HtagBig_}���ޥ�ɤ���Ͽ���ޤ���${H_tagBig}<HR>
END
}

# �������ѹ�����
sub tempComment {
	out(<<END);
${HtagBig_}�����Ȥ򹹿����ޤ���${H_tagBig}<HR>
END
}

# �ᶷ
sub tempRecent {
	my($mode) = @_;
	out(<<END);
<HR>
${HtagBig_}${HtagName_}${HcurrentName}��${H_tagName}�ζᶷ${H_tagBig}<BR>
END
	logPrintLocal($mode);
}

1;
