#----------------------------------------------------------------------
# 箱庭諸島 ver2.30
# トップモジュール(ver1.00)
# 使用条件、使用方法等は、hako-readme.txtファイルを参照
#
# 箱庭諸島のページ: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# いのら諸島 ver1.04
# 箱庭緒島（http://espion.s7.xrea.com/tyotou/）
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# トップページモード
#----------------------------------------------------------------------
# メイン
sub topPageMain {
	# 開放
	unlock();

	# テンプレート出力
	tempTopPage();
}

# トップページ
sub tempTopPage {
	# タイトル
	out("${HtagTitle_}$Htitle${H_tagTitle}");

	# デバッグモードなら「ターンを進める」ボタン
	if($Hdebug == 1) {
		out(<<END);
<FORM action="$HthisFile" method="POST">
<INPUT TYPE="submit" VALUE="ターンを進める" NAME="TurnButton">
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
		$mStr1 = "<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}資金${H_tagTH}</NOBR></TH>";
	}

	# 時間表示
	my($hour, $min, $sec);
	my($now) = time;
	my($showTIME) = ($HislandLastTime + $HunitTime - $now);
	$hour = int($showTIME / 3600);
	$min  = int(($showTIME - ($hour * 3600)) / 60);
	$sec  = $showTIME - ($hour * 3600) - ($min * 60);

	if ($sec < 0){
		out(<<END);
<H1>${HtagHeader_}ターン$HislandTurn/$HislandLastTurn${H_tagHeader}　$fightmode</H1><B><font size=+1>（${HtagHeader_}更新して下さい${H_tagHeader}）</font></b>
END
	} else {
		out(<<END);
<H1>${HtagHeader_}ターン$HislandTurn/$HislandLastTurn${H_tagHeader} <font size=+1>（次のターンまで、あと $hour 時間 $min 分 $sec 秒）</font></b></H1>
END
	}

	# フォーム
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
<H1>${HtagHeader_}自分の島へ${H_tagHeader}</H1>
<FORM name="Island" action="$HthisFile" method="POST">
あなたの島の名前は？<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT><BR>

パスワードをどうぞ！！<BR>
<INPUT TYPE="password" NAME="PASSWORD" VALUE="$HdefaultPassword" SIZE=32 MAXLENGTH=32><BR>
<INPUT TYPE="submit" VALUE="開発しに行く" NAME="OwnerButton" onClick="develope()">
<INPUT TYPE="checkbox" NAME="CHBOX" VALUE="on">新しい画面で開発<BR>
<INPUT TYPE="radio" NAME=JAVAMODE VALUE=cgi${owner}>通常モード
<INPUT TYPE="radio" NAME=JAVAMODE VALUE=java${java}>Javaスクリプトモード
</FORM>

<HR>

<H1>${HtagHeader_}諸島の状況${H_tagHeader}</H1>
<P>
島の名前をクリックすると、<B>観光</B>することができます。
</P>
<TABLE BORDER CELLSPACING=1>
<TR>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}順位${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}島${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}いのら情報${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}人口${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}面積${H_tagTH}</NOBR></TH>
$mStr1
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}食料${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}農場規模${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}工場規模${H_tagTH}</NOBR></TH>
<TH $HbgTitleCell align=center nowrap=nowrap><NOBR>${HtagTH_}採掘場規模${H_tagTH}</NOBR></TH>
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
		$farm = ($farm == 0) ? "保有せず" : "${farm}0$HunitPop";
		$factory = ($factory == 0) ? "保有せず" : "${factory}0$HunitPop";
		$mountain = ($mountain == 0) ? "保有せず" : "${mountain}0$HunitPop";
		if($island->{'absent'}  == 0) {
			$name = "${HtagName_}$island->{'name'}島${H_tagName}";
		} else {
			$name = "${HtagName2_}$island->{'name'}島($island->{'absent'})${H_tagName2}";
		}

		$prize = $island->{'prize'};
		my($flags, $monsters, $turns);
		$prize =~ /([0-9]*),([0-9]*),(.*)/;
		$flags = $1;
		$monsters= $2;
		$turns = $3;
		$prize = '';

		# ターン杯の表示
		while($turns =~ s/([0-9]*),//) {
			$prize .= "<IMG SRC=\"prize0.png\" ALT=\"$1${Hprize[0]}\" WIDTH=16 HEIGHT=16> ";
		}

		# 名前に賞の文字を追加
		my($f) = 1;
		my($i);
		for($i = 1; $i < 10; $i++) {
			if($flags & $f) {
				$prize .= "<IMG SRC=\"prize${i}.png\" ALT=\"${Hprize[$i]}\" WIDTH=16 HEIGHT=16> ";
			}
			$f *= 2;
		}

		# 倒した怪獣リスト
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
			$prize .= "<IMG SRC=\"monster7.png\" ALT=\"${Hprize[10]}優勝\" WIDTH=16 HEIGHT=16> ";
		}
		for($co = 0;$co < $c_cute;$co++) {
			$prize .= "<IMG SRC=\"monster8.png\" ALT=\"${Hprize[11]}優勝\" WIDTH=16 HEIGHT=16> ";
		}
		for($co = 0;$co < $c_int;$co++) {
			$prize .= "<IMG SRC=\"monster9.png\" ALT=\"${Hprize[12]}優勝\" WIDTH=16 HEIGHT=16> ";
		}

		my($mStr1) = '';
		if($HhideMoneyMode == 1) {
			$mStr1 = "<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$island->{'money'}$HunitMoney</NOBR></TD>";
		} elsif($HhideMoneyMode == 2) {
			my($mTmp) = aboutMoney($island->{'money'});
			$mStr1 = "<TD $HbgInfoCell align=right nowrap=nowrap><NOBR>$mTmp</NOBR></TD>";
		}

		my($comname) ="${HtagTH_}コメント：${H_tagTH}";
		if(($island->{'ownername'} ne '0') && ($island->{'ownername'} ne "コメント")){
			$comname = "<FONT COLOR=\"blue\"><B>$island->{'ownername'}：</b></font>";
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
名前：${HtagIName_}$island->{'i_name'}${H_tagIName}<BR>
種類：$HmonsterName[$island->{'i_type'}]<BR>
体：${i_hp} </b>
腕：${i_arm} </b>
魅：${i_cute} </b>
知：${i_int}<BR></b>
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
<H1>${HtagHeader_}新しい島を探す${H_tagHeader}</H1>
END

	if($HislandNumber < $HmaxIsland) {
		out(<<END);
<FORM action="$HthisFile" method="POST">
島の名前<BR>
<INPUT TYPE="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>島<BR>
いのらの名前(<FONT COLOR=RED>途中変更不可　10文字程度が望ましい</FONT>)<BR>
<INPUT TYPE="text" NAME="MONSTERNAME" SIZE=32 MAXLENGTH=64><BR>
パスワードは？<BR>
<INPUT TYPE="password" NAME="PASSWORD" SIZE=32 MAXLENGTH=32><BR>
念のためパスワードをもう一回<BR>
<INPUT TYPE="password" NAME="PASSWORD2" SIZE=32 MAXLENGTH=32><BR>

<INPUT TYPE="submit" VALUE="探しに行く" NAME="NewIslandButton">
</FORM>
END
	} else {
		out(<<END);
		島の数が最大数です・・・現在登録できません。
END
	}

	my($Himfflag);
	if($HimgLine eq '' || $HimgLine eq $imageDir){
		$Himfflag = '<FONT COLOR=RED>未設定</FONT>';
	} else {
		$Himfflag = $baseIMG;
	}

	out(<<END);
<HR><P>
<TABLE>
<TR><TD WIDTH=420 ROWSPAN=2 VALIGN=TOP>
<H1>${HtagHeader_}島の名前とパスワードの変更${H_tagHeader}</H1>
<P>
(注意)名前の変更には$HcostChangeName${HunitMoney}かかります。
</P>
<FORM action="$HthisFile" method="POST">
どの島ですか？<BR>
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>
<BR>
どんな名前に変えますか？(変更する場合のみ)<BR>
<INPUT TYPE="text" NAME="ISLANDNAME" SIZE=32 MAXLENGTH=32>島<BR>
パスワードは？(必須)<BR>
<INPUT TYPE="password" NAME="OLDPASS" SIZE=32 MAXLENGTH=32><BR>
新しいパスワードは？(変更する時のみ)<BR>
<INPUT TYPE="password" NAME="PASSWORD" SIZE=32 MAXLENGTH=32><BR>
念のためパスワードをもう一回(変更する時のみ)<BR>
<INPUT TYPE="password" NAME="PASSWORD2" SIZE=32 MAXLENGTH=32><BR>

<INPUT TYPE="submit" VALUE="変更する" NAME="ChangeInfoButton">
</FORM>

</TD>

<TD VALIGN=TOP WIDTH=350>
<H1>${HtagHeader_}画像のローカル設定${H_tagHeader}</H1>
<NOBR>現在の設定<B>[</b> ${Himfflag} <B>]</B></NOBR>
<BR><A HREF=${imageExp} target=_blank><FONT SIZE=+1> 説 明 </FONT></A>
<form action=$HthisFile method=POST>
<INPUT TYPE=file NAME="IMGLINE">
<INPUT TYPE="submit" VALUE="設定" name=IMGSET>
</form>

<form action=$HthisFile method=POST>
Macユーザー用<BR>
<INPUT TYPE=text NAME="IMGLINEMAC">
<INPUT TYPE="submit" VALUE="設定" name=IMGSET><BR>
<FONT SIZE=-1>Macの方は、こちらを使用して下さい。</FONT>
</form>
</TD></TR>

<TR HEIGHT=100><TD ALIGN=CENTER>
<form action=$HthisFile method=POST>
<INPUT TYPE=hidden NAME="IMGLINE" value="deletemodenow">
<INPUT TYPE="submit" VALUE="設定を解除する" name=IMGSET>
</form>
</TD></TR>
</TABLE>
<HR>
<H1>${HtagHeader_}オーナーの名前決定！${H_tagHeader}</H1>
<FORM action="$HthisFile" method="POST">
あなたの島は？
<SELECT NAME="ISLANDID">
$HislandList
</SELECT>　　名前入力
<INPUT TYPE="text" NAME="OWNERNAME" SIZE=16 MAXLENGTH=32>
　　パスワード
<INPUT TYPE="password" NAME="OLDPASS" SIZE=16 MAXLENGTH=32>
<INPUT TYPE="submit" VALUE="これにする" NAME="ChangeOwnerName">
</form>
<HR>
<H1>${HtagHeader_}発見の記録${H_tagHeader}</H1>
END
	historyPrint();
}

# 記録ファイル表示
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
		out("<NOBR>${HtagNumber_}ターン${1}${H_tagNumber}：${2}</NOBR><BR>\n");
	}
	close(HIN);
}


#----------------------------------------------------------------------
# ログ表示モード
#----------------------------------------------------------------------
# メイン
sub logViewMain {

	# 開放
	unlock();

	# テンプレート出力
	tempLogPage();
}

sub tempLogPage {

	out(<<END);

<font size=+3><b>${HtagHeader_}最近の出来事${H_tagHeader}</b></font>　
　<a href="$HthisFile?LogFileView=1"><FONT COLOR="blue" size=2><B>現ターン</a>
　<a href="$HthisFile?LogFileView=2">2ターン分表示</a>
END
for($i = 3; $i -1 < $HlogMax; $i++) {
		out("　<a href=\"$HthisFile?LogFileView=${i}\">${i}ターン分</a>\n");
}
	out(<<END);
</b></font><br>
END
	logPrintTop();

}

# ログ表示
sub logPrintTop {
	my($i);
	for($i = 0; $i < $Hlogturn; $i++) {
		out("<hr>\n");
		logFilePrint($i, 0, 0);

	}
}

1;

