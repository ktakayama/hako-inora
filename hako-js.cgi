#----------------------------------------------------------------------
# ＪＡＶＡスクリプト版 -ver1.11-
# 使用条件、使用方法等は、配布元でご確認下さい。
# 付属のjs-readme.txtもお読み下さい。
# あっぽー：http://appoh.execweb.cx/hakoniwa/
#----------------------------------------------------------------------
# いのら諸島 ver1.03
# 箱庭緒島（http://espion.s7.xrea.com/tyotou/）
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# Ｊａｖａスクリプト開発画面
#----------------------------------------------------------------------
# ○○島開発計画
sub tempOwnerJava {
	$HcurrentNumber = $HidToNumber{$HcurrentID};
	my($island) = $Hislands[$HcurrentNumber];

	# コマンドセット
	$set_com = "";
	$com_max = "";
	for($i = 0; $i < $HcommandMax; $i++) {
		# 各要素の取り出し
		my($command) = $island->{'command'}->[$i];
		my($s_kind, $s_target, $s_x, $s_y, $s_arg) = 
		(
		$command->{'kind'},
		$command->{'target'},
		$command->{'x'},
		$command->{'y'},
		$command->{'arg'}
		);
		# コマンド登録
		if($i == $HcommandMax-1){
			$set_com .= "\[$s_kind\,$s_x\,$s_y\,$s_arg\,$s_target\]\n";
			$com_max .= "0"
		}else{
			$set_com .= "\[$s_kind\,$s_x\,$s_y\,$s_arg\,$s_target\]\,\n";
			$com_max .= "0,"
		}
	}

    #コマンドリストセット
	my($l_kind);
	$set_listcom = "";
	$click_com = "";
	$click_com2 = "";
	$click_com3 = "";
	$All_listCom = 0;
	$com_count = @HcommandDivido;
	for($m = 0; $m < $com_count; $m++) {
		($aa,$dd,$ff) = split(/,/,$HcommandDivido[$m]);
		$set_listcom .= "\[ ";
	    for($i = 0; $i < $HcommandTotal; $i++) {
			$l_kind = $HcomList[$i];
			$l_cost = $HcomCost[$l_kind];
			if($l_cost == 0) { $l_cost = '無料'	}
			elsif($l_cost < 0) { $l_cost = - $l_cost; $l_cost .= $HunitFood; }
			else { $l_cost .= $HunitMoney; }
			if($l_kind > $dd-1 && $l_kind < $ff+1) {
				$set_listcom .= "\[$l_kind\,\'$HcomName[$l_kind]\',\'$l_cost\'\]\,\n";
				my $com_name = ($HcomName2[$l_kind]) ? $HcomName2[$l_kind] : $HcomName[$l_kind];
				if($m == 0){
					$click_com .= "<a href='javascript:void(0);' onClick='cominput(myForm,6,$l_kind)' STYlE='text-decoration:none'>$com_name($HcomCost[$l_kind])</a><br>\n";
				}elsif($m == 1){
					$click_com2 .= "<a href='javascript:void(0);' onClick='cominput(myForm,6,$l_kind)' STYlE='text-decoration:none'>$com_name($HcomCost[$l_kind])</a><br>\n";
				}elsif($m == 2){
					$click_com3 .= "<a href='javascript:void(0);' onClick='cominput(myForm,6,$l_kind)' STYlE='text-decoration:none'>$com_name($HcomCost[$l_kind])</a><br>\n"; # ($l_cost)
				}
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

	#島リストセット
	my($set_island, $l_name, $l_id);
	$set_island = "";
	for($i = 0; $i < $HislandNumber; $i++) {
		$l_name = $Hislands[$i]->{'name'};
		$l_name =~ s/'/\\'/g;
		$l_id = $Hislands[$i]->{'id'};
		if($i == $HislandNumber-1){
			$set_island .= "\[$l_id\,\'$l_name\'\]\n";
		}else{
			$set_island .= "\[$l_id\,\'$l_name\'\]\,\n";
		}
	}

    out(<<END);
<CENTER>
${HtagBig_}${HtagName_}${HcurrentName}島${H_tagName}開発計画${H_tagBig}<BR>
$HtempBack<BR>
</CENTER>
<SCRIPT Language="JavaScript">
<!--
// ＪＡＶＡスクリプト開発画面配布元
// あっぽー庵箱庭諸島（ http://appoh.execweb.cx/hakoniwa/ ）
// Programmed by Jynichi Sakai(あっぽー)
// ↑ 削除しないで下さい。
var str;
g = [$com_max];
k1 = [$com_max];
k2 = [$com_max];
tmpcom1 = [ [0,0,0,0,0] ];
tmpcom2 = [ [0,0,0,0,0] ];
command = [
$set_com];

comlist = [
$set_listcom
];

islname = [
$set_island];

function init(){
	for(i = 0; i < command.length ;i++) {
		for(s = 0; s < $com_count ;s++) {
		var comlist2 = comlist[s];
		for(j = 0; j < comlist2.length ; j++) {
			if(command[i][0] == comlist2[j][0]) {
				g[i] = comlist2[j][1];
			}
		}
		}
	}
	outp();
	str = plchg();
	str = "<font color=blue>−−−− 送信済み −−−−</font><br>"+str;
	disp(str, "#ccffcc");

	check_menu();
	SelectList();

//	if((document.layers) || (document.all)){  // IE4、IE5、NN4
//		window.document.onmouseup = menuclose;
//	}
}

function cominput(theForm, x, k) {
	a = theForm.NUMBER.options[theForm.NUMBER.selectedIndex].value;
	b = theForm.COMMAND.options[theForm.COMMAND.selectedIndex].value;
	c = theForm.POINTX.options[theForm.POINTX.selectedIndex].value;
	d = theForm.POINTY.options[theForm.POINTY.selectedIndex].value;
	e = theForm.AMOUNT.options[theForm.AMOUNT.selectedIndex].value;
	f = theForm.TARGETID.options[theForm.TARGETID.selectedIndex].value;
	if(x == 6){ b = k; }
	if (x == 1 || x == 6){
		for(i = $HcommandMax - 1; i > a; i--) {
			command[i] = command[i-1];
			g[i] = g[i-1];
		}
	}else if(x == 3){
		for(i = Math.floor(a); i < ($HcommandMax - 1); i++) {
			command[i] = command[i + 1];
			g[i] = g[i+1];
		}
		command[$HcommandMax-1] = [41,0,0,0,0];
		g[$HcommandMax-1] = '資金繰り';
		str = plchg();
		str = "<font color=red><b>−−−−−未送信−−−−−−</b></font><br>"+str;
		disp(str,"white");
		outp();
		return true;
	}else if(x == 4){
		i = Math.floor(a)
		if (i == 0){ return true; }
		i = Math.floor(a)
		tmpcom1[i] = command[i];tmpcom2[i] = command[i - 1];
		command[i] = tmpcom2[i];command[i-1] = tmpcom1[i];
		k1[i] = g[i];k2[i] = g[i - 1];
		g[i] = k2[i];g[i-1] = k1[i];
		ns(--i);
		str = plchg();
		str = "<font color=red><b>−−−−−未送信−−−−−−</b></font><br>"+str;
		disp(str,"white");
		outp();
		return true;
	}else if(x == 5){
		i = Math.floor(a)
		if (i == $HcommandMax-1){ return true; }
		tmpcom1[i] = command[i];tmpcom2[i] = command[i + 1];
		command[i] = tmpcom2[i];command[i+1] = tmpcom1[i];
		k1[i] = g[i];k2[i] = g[i + 1];
		g[i] = k2[i];g[i+1] = k1[i];
		ns(++i);
		str = plchg();
		str = "<font color=red><b>−−−−−未送信−−−−−−</b></font><br>"+str;
		disp(str,"white");
		outp();
		return true;
	}

	for(s = 0; s < $com_count ;s++) {
	var comlist2 = comlist[s];
	for(i = 0; i < comlist2.length; i++){
		if(comlist2[i][0] == b){
			g[a] = comlist2[i][1];
			break;
		}
	}
	}
	command[a] = [b,c,d,e,f];
	ns(++a);
	str = plchg();
	str = "<font color=red><b>−−−−−未送信−−−−−−</b></font><br>"+str;
	disp(str, "white");
	outp();
	menuclose();
	return true;
}

function plchg(){
	strn1 = "";
	for(i = 0; i < $HcommandMax; i++)	{
		c = command[i];
		kind = '<FONT COLOR="#d08000"><B>' + g[i] + '</B></FONT>';
		x = c[1];
		y = c[2];
		tgt = c[4];
		point = '<FONT COLOR="#a06040"><B>' + "(" + x + "," + y + ")" + '</B></FONT>';
		for(j = 0; j < islname.length ; j++) {
			if(tgt == islname[j][0]){
				tgt = '<FONT COLOR="#a06040"><B>' + islname[j][1] + "島" + '</B></FONT>';
			}
		}
		if(c[0] == $HcomDoNothing || c[0] == $HcomGiveup){ // 資金繰り、島の放棄
			strn2 = kind;
		}else if(c[0] == $HcomMissileNM || // ミサイル関連
			c[0] == $HcomMissilePP){
			if(c[3] == 0){
				arg = "（無制限）";
			} else {
				arg = "（" + c[3] + "発）";
			}
			strn2 = tgt + point + "へ" + kind + arg;
		}else if(c[0] == $HcomSell){ // 食料輸出
			if(c[3] == 0){ c[3] = 1; }
			arg = c[3] * 100;
			arg = "（" + arg + "$HunitFood）";
			strn2 = kind + arg;
		}else if(c[0] == $HcomPropaganda){ // 誘致活動
			strn2 = kind;
		}else if(c[0] == $HcomMoney){ // 資金援助
			if(c[3] == 0){ c[3] = 1; }
			arg = c[3] * $HcomCost[$HcomMoney];
			arg = "（" + arg + "$HunitMoney）";
			strn2 = tgt + "へ" + kind + arg;
		}else if(c[0] == $HcomFood){ // 食料援助
			if(c[3] == 0){ c[3] = 1; }
			arg = c[3] * 100;
			arg = "（" + arg + "$HunitFood）";
			strn2 = tgt + "へ" + kind + arg;
		}else if(c[0] == $HcomDestroy){ // 掘削
			if(c[3] == 0){
				strn2 = point + "で" + kind;
			} else {
				arg = c[3] * $HcomCost[$HcomDestroy];
				arg = "（予\算" + arg + "$HunitMoney）";
				strn2 = point + "で" + kind + arg;
			}
		}else if(c[0] == $HcomFarm || // 農場、工場、採掘場整備
			c[0] == $HcomFactory ||
			c[0] == $HcomMountain) {
			if(c[3] != 0){
				arg = "（" + c[3] + "回）";
				strn2 = point + "で" + kind + arg;
			}else{
				strn2 = point + "で" + kind;
			}
		}else{
			strn2 = point + "で" + kind;
		}
		tmpnum = '';
		if(i < 9){ tmpnum = '0'; }
		strn1 += 
		'<A STYLE="text-decoration:none;color:000000" HREF="JavaScript:void(0);" onClick="ns(' + i + ')"><NOBR>' +
		tmpnum + (i + 1) + ':' +
		strn2 + '</NOBR></A><BR>\\n';
	}
	return strn1;
}

function disp(str,bgclr){
	if(str==null)  str = "";

	if(document.getElementById){
		document.getElementById("LINKMSG1").innerHTML = str;
		document.getElementById("plan").bgColor = bgclr;
	} else if(document.all){
		el = document.all("LINKMSG1");
		el.innerHTML = str;
		document.all.plan.bgColor = bgclr;
	} else if(document.layers) {
		lay = document.layers["PARENT_LINKMSG"].document.layers["LINKMSG1"];
		lay.document.open();
		lay.document.write("<font style='font-size:11pt'>"+str+"</font>");
		lay.document.close(); 
		document.layers["PARENT_LINKMSG"].bgColor = bgclr;
	}
}

function outp(){
	comary = "";

	for(k = 0; k < command.length; k++){
	comary = comary + command[k][0]
	+" "+command[k][1]
	+" "+command[k][2]
	+" "+command[k][3]
	+" "+command[k][4]
	+" ";
	}
	document.myForm.COMARY.value = comary;
}

function ps(x, y) {
	document.forms[0].elements[4].options[x].selected = true;
	document.forms[0].elements[5].options[y].selected = true;
	document.myForm.POINTX.value = x;
	document.myForm.POINTY.value = y;
	if(!(document.myForm.MENUOPEN.checked))
		moveLAYER("menu",mx,my);
	return true;
}

function SelectPOINT(){
	document.myForm.POINTX.value = document.forms[0].elements[4].options[document.forms[0].elements[4].selectedIndex].value;
	document.myForm.POINTY.value = document.forms[0].elements[5].options[document.forms[0].elements[5].selectedIndex].value;
	document.myForm.submit();
}

function ns(x) {
	if (x == $HcommandMax){ return true; }
	document.forms[0].elements[0].options[x].selected = true;
	document.myForm.NUMBER.value = x;
	return true;
}

function set_com(x, y, land) {
	com_str = land + "\\n";
	for(i = 0; i < $HcommandMax; i++)	{
		c = command[i];
		x2 = c[1];
		y2 = c[2];
		if(x == x2 && y == y2 && c[0] < 30){
			com_str += "[" + (i + 1) +"]" ;
			kind = g[i];
			if(c[0] == $HcomDestroy){
				if(c[3] == 0){
					com_str += kind;
				} else {
					arg = c[3] * 200;
					arg = "（予\算" + arg + "$HunitMoney）";
					com_str += kind + arg;
				}
			}else if(c[0] == $HcomFarm ||
				c[0] == $HcomFactory ||
				c[0] == $HcomMountain) {
				if(c[3] != 0){
					arg = "（" + c[3] + "回）";
					com_str += kind + arg;
				}else{
					com_str += kind;
				}
			}else{
				com_str += kind;
			}
			com_str += " ";
		}
	}
	status = com_str;
	document.myForm.COMSTATUS.value= com_str;
}

function not_com() {
//	document.myForm.COMSTATUS.value="";
}


function SelectList(theForm){
	var u, selected_ok;
	if(!theForm){s = ''}
	else { s = theForm.menu.options[theForm.menu.selectedIndex].value; }
	if(s == ''){
		u = 0; selected_ok = 0;
		document.myForm.COMMAND.options.length = $All_listCom;
		for (i=0; i<comlist.length; i++) {
			var command = comlist[i];
			for (a=0; a<command.length; a++) {
				comName = command[a][1] + "(" + command[a][2] + ")";
				document.myForm.COMMAND.options[u].value = command[a][0];
				document.myForm.COMMAND.options[u].text = comName;
				if(command[a][0] == $default_Kind){
					document.myForm.COMMAND.options[u].selected = true;
					selected_ok = 1;
				}
				u++;
			}
		}
		if(selected_ok == 0)
		document.myForm.COMMAND.selectedIndex = 0;
	} else {
		var command = comlist[s];
		document.myForm.COMMAND.options.length = command.length;
		for (i=0; i<command.length; i++) {
			comName = command[i][1] + "(" + command[i][2] + ")";
			document.myForm.COMMAND.options[i].value = command[i][0];
			document.myForm.COMMAND.options[i].text = comName;
			if(command[i][0] == $default_Kind){
				document.myForm.COMMAND.options[i].selected = true;
				selected_ok = 1;
			}
		}
		if(selected_ok == 0)
		document.myForm.COMMAND.selectedIndex = 0;
	}
}

function moveLAYER(layName,x,y){
	if(document.getElementById){		//NN6,IE5
		if(document.all){				//IE5
			el = document.getElementById(layName);
			el.style.left= event.clientX + document.body.scrollLeft + 10;
			el.style.top= event.clientY + document.body.scrollTop - 60;
			el.style.display = "block";
			el.style.visibility ='visible';
		}else{
			el = document.getElementById(layName);
			el.style.left=x+10;
			el.style.top=y-60;
			el.style.display = "block";
			el.style.visibility ='visible';
		}
	} else if(document.layers){				//NN4
		msgLay = document.layers[layName];
		msgLay.moveTo(x+10,y-60);
		msgLay.visibility = "show";
	} else if(document.all){				//IE4
		msgLay = document.all(layName);
		msgLay.style.pixelLeft = x+10;
		msgLay.style.pixelTop = y-60;
		msgLay.style.display = "block";
		msgLay.style.visibility = "visible";
	}

}

function menuclose(){ 
	if (document.getElementById){
		document.getElementById("menu").style.display = "none";
	} else if (document.layers){
		document.menu.visibility = "hide";
	} else if (document.all){
		window["menu"].style.display = "none";
	}
}

function Mmove(e){
	if(document.all){
		mx = event.x;
		my = event.y;
	}else if(document.layers){
		mx = e.pageX;
		my = e.pageY;
	}else if(document.getElementById){
		mx = e.pageX;
		my = e.pageY;
	}
}

function check_menu(){
	if(!(document.myForm.MENUOPEN.checked)){
		if(document.getElementById){
			document.onmousemove = Mmove;
		} else if(document.layers){
			window.captureEvents(Event.MOUSEMOVE);
			window.onMouseMove = Mmove;
		} else if(document.all){
			document.onmousemove = Mmove;
		}
		document.myForm.MENUOPEN.value="";
	}else{
		document.myForm.MENUOPEN.value="on";
	}
}

//-->
</SCRIPT>
<DIV ID="menu" style="position:absolute; visibility:hidden;"> 
<TABLE BORDER=1 BGCOLOR=#e0ffff CELLSPACING=1>
<TR><TD NOWRAP VALIGN=TOP NOWRAP>
$click_com
<TD VALIGN=TOP ROWSPAN=2 NOWRAP>
$click_com2
<TR><TD NOWRAP VALIGN=TOP>
$click_com3
<TR><TD COLSPAN=2 ALIGN=CENTER NOWRAP>
<a href="Javascript:void(0);" onClick="menuclose()" STYlE="text-decoration:none">メニューを閉じる</A>
</TD>
</TR>
</TABLE>
</DIV>
END

    islandInfo();

    out(<<END);
<CENTER>
<TABLE BORDER CELLSPACING=0>
<TR valign=top>
<TD $HbgInputCell width=200>
<CENTER>
<FORM name="myForm" action="$HthisFile" method=POST>
<P>
<B>コマンド入力</B><BR><B>
<A HREF=JavaScript:void(0); onClick="cominput(myForm,1)">挿入</A>
　<A HREF=JavaScript:void(0); onClick="cominput(myForm,2)">上書き</A>
　<A HREF=JavaScript:void(0); onClick="cominput(myForm,3)">削除</A>
</B><HR>
<B>計画番号</B><SELECT NAME=NUMBER>
END
    # 計画番号
    my($j, $i);
    for($i = 0; $i < $HcommandMax; $i++) {
	$j = $i + 1;
	out("<OPTION VALUE=$i>$j\n");
    }

    if ($HmenuOpen eq 'on') {
		$open = "CHECKED";
	}else{
		$open = "";
	}

    out(<<END);
</SELECT><BR>
<HR>
<B>開発計画</B>
<INPUT TYPE="checkbox" NAME="MENUOPEN"onClick="check_menu()" $open>非表\示<br>
<SELECT NAME=menu onchange="SelectList(myForm)">
<OPTION VALUE=>全種類
END
	for($i = 0; $i < $com_count; $i++) {
		($aa) = split(/,/,$HcommandDivido[$i]);
		out("<OPTION VALUE=$i>$aa\n");
	}
    out(<<END);
</SELECT><br>
<SELECT NAME=COMMAND>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
<option>　　　　　　　　　　</option>
</SELECT>
<HR>
<B>座標(</B>
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
<B>数量</B><SELECT NAME=AMOUNT>
END

    # 数量
    for($i = 0; $i < 100; $i++) {
	out("<OPTION VALUE=$i>$i\n");
    }

    out(<<END);
</SELECT>
<HR>
<B>目標の島</B>
<SELECT NAME=TARGETID>
$HtargetList<BR>
</SELECT>
<HR>
<B>コマンド移動</B>：
<BIG>
<A HREF=JavaScript:void(0); onClick="cominput(myForm,4)" STYlE="text-decoration:none"> ▲ </A>・・
<A HREF=JavaScript:void(0); onClick="cominput(myForm,5)" STYlE="text-decoration:none"> ▼ </A>
</BIG>
<HR>
<INPUT TYPE="hidden" NAME="COMARY" value="comary">
<INPUT TYPE="hidden" NAME="JAVAMODE" value="$HjavaMode">
<INPUT TYPE=submit VALUE="計画送信" NAME=CommandJavaButton$Hislands[$HcurrentNumber]->{'id'}>
<br><font size=2>最後に<font color=red>計画送信ボタン</font>を<br>押すのを忘れないように。</font>
<HR>
<B>パスワード</B></BR>
<INPUT TYPE=password NAME=PASSWORD VALUE="$HdefaultPassword">
</CENTER>
</TD>
<TD $HbgMapCell><center>
<TEXTAREA NAME="COMSTATUS" cols="48" rows="2" readonly></TEXTAREA>
</center>
END
    islandMapJava(1);    # 島の地図、所有者モード
    my $comment = $Hislands[$HcurrentNumber]->{'comment'};
    out(<<END);
</FORM>
</TD>
<TD $HbgCommandCell id="plan">
<ilayer name="PARENT_LINKMSG" width="100%" height="100%">
   <layer name="LINKMSG1" width="200"></layer>
   <span id="LINKMSG1"></span>
</ilayer>
</TD>
</TR>
</TABLE>
</CENTER>
<HR>
<CENTER>
${HtagBig_}コメント更新${H_tagBig}<BR>
<FORM action="$HthisFile" method="POST">
コメント<INPUT TYPE=text NAME=MESSAGE SIZE=80 VALUE="$comment"><BR>
パスワード<INPUT TYPE=password NAME=PASSWORD VALUE="$HdefaultPassword">
<INPUT TYPE="hidden" NAME=JAVAMODE VALUE="$HjavaMode">
<INPUT TYPE=submit VALUE="コメント更新" NAME=MessageButton$Hislands[$HcurrentNumber]->{'id'}>
</FORM>
</CENTER>
END

}

#----------------------------------------------------------------------
# ローカル掲示板入力フォーム Ｊａｖａスクリプト mode用
#----------------------------------------------------------------------
sub tempLbbsInputJava {
    out(<<END);
<CENTER>
<FORM action="$HthisFile" method="POST">
<TABLE BORDER CELLSPACING=0>
<TR>
<TH>名前</TH>
<TH COLSPAN=2>内容</TH>
</TR>
<TR>
<TD><INPUT TYPE="text" SIZE=32 MAXLENGTH=32 NAME="LBBSNAME" VALUE="$HdefaultName"></TD>
<TD COLSPAN=2><INPUT TYPE="text" SIZE=80 NAME="LBBSMESSAGE"></TD>
</TR>
<TR>
<TH>パスワード</TH>
<TH COLSPAN=2>動作</TH>
</TR>
<TR>
<TD><INPUT TYPE=password SIZE=32 MAXLENGTH=32 NAME=PASSWORD VALUE="$HdefaultPassword"></TD>
<TD align=right>
<INPUT TYPE="submit" VALUE="記帳する" NAME="LbbsButtonOW$HcurrentID">
</TD>
<TD align=right>
番号
<SELECT NAME=NUMBER>
END
    # 発言番号
    my($j, $i);
    for($i = 0; $i < $HlbbsMax; $i++) {
	$j = $i + 1;
	out("<OPTION VALUE=$i>$j\n");
    }
    out(<<END);
</SELECT>
<INPUT TYPE="submit" VALUE="削除する" NAME="LbbsButtonDL$HcurrentID">
<INPUT TYPE="hidden" NAME=JAVAMODE VALUE="$HjavaMode">
</TD>
</TR>
</TABLE>
</FORM>
</CENTER>
END
}

#----------------------------------------------------------------------
# コマンドモード
#----------------------------------------------------------------------
sub commandJavaMain {
    # idから島を取得
    $HcurrentNumber = $HidToNumber{$HcurrentID};
    my($island) = $Hislands[$HcurrentNumber];
    $HcurrentName = $island->{'name'};

    # パスワード
    if(!checkPassword($island->{'password'},$HinputPassword)) {
	# password間違い
	unlock();
	tempWrongPassword();
	return;
    }

    # モードで分岐
    my($command) = $island->{'command'};
	for($i = 0; $i < $HcommandMax; $i++) {
		# コマンド登録
		$HcommandComary =~ s/([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*) //;
	    if($1 == 0) {
			$1 = 41;
		}
		$command->[$i] = {
			'kind' => $1,
			'x' => $2,
			'y' => $3,
			'arg' => $4,
			'target' => $5
		};
	}
	tempCommandAdd();
	# データの書き出し
    writeIslandsFile($HcurrentID);

    # owner modeへ
    ownerMain();
}

#----------------------------------------------------------------------
# 地図の表示
#----------------------------------------------------------------------
sub islandMapJava {
    my($mode) = @_;
    my($island);
    $island = $Hislands[$HcurrentNumber];

    # 地形、地形値を取得
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($l, $lv);

    out(<<END);
<CENTER><TABLE BORDER CELLSPACING=1><TR><TD>
END
    # コマンド取得
    my($command) = $island->{'command'};
    my($com, @comStr, $i);
    if($HmainMode eq 'owner') {
	for($i = 0; $i < $HcommandMax; $i++) {
	    my($j) = $i + 1;
	    $com = $command->[$i];
	    if($com->{'kind'} < 21) {
		$comStr[$com->{'x'}][$com->{'y'}] .=
		    " [${j}]$HcomName[$com->{'kind'}]";
	    }
	}
    }

    # 座標(上)を出力
    out("<IMG SRC=\"xbar.png\" width=400 height=16><BR>");

    # 各地形および改行を出力
    my($x, $y);
    for($y = 0; $y < $HislandSize; $y++) {
	# 偶数行目なら番号を出力
        if(($y % 2) == 0) {
	    out("<IMG SRC=\"space${y}.gif\" width=16 height=32>");
	}

	# 各地形を出力
	for($x = 0; $x < $HislandSize; $x++) {
	    $l = $land->[$x][$y];
	    $lv = $landValue->[$x][$y];
	    landString($l, $lv, $x, $y, $mode, $comStr[$x][$y], 1, $island);
	}

	# 奇数行目なら番号を出力
        if(($y % 2) == 1) {
	    out("<IMG SRC=\"space${y}.gif\" width=16 height=32>");
	}

	# 改行を出力
	out("<BR>");
    }
    out("</TD></TR></TABLE></CENTER>\n");
}


1;

