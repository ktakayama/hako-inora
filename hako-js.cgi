#----------------------------------------------------------------------
# ＪＡＶＡスクリプト版 -ver1.11-
# 使用条件、使用方法等は、配布元でご確認下さい。
# 付属のjs-readme.txtもお読み下さい。
# あっぽー：http://appoh.execweb.cx/hakoniwa/
#----------------------------------------------------------------------
# いのら諸島
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
			$set_island .= "$l_id\:\'$l_name\'\n";
		}else{
			$set_island .= "$l_id\:\'$l_name\'\,\n";
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
var xmlhttp;
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

islname = {
$set_island
};

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

	SelectList();

	xmlhttp = new_http();

	if(document.layers) {
		document.captureEvents(Event.MOUSEMOVE | Event.MOUSEUP);
	}
	document.onmouseup   = Mup;
	document.onmousemove = Mmove;
	document.myForm.CommandJavaButton$Hislands[$HcurrentNumber]->{'id'}.disabled = true;
	ns(0);
}

function cominput(theForm, x, k, z) {
	a = theForm.NUMBER.options[theForm.NUMBER.selectedIndex].value;
	b = theForm.COMMAND.options[theForm.COMMAND.selectedIndex].value;
	c = theForm.POINTX.options[theForm.POINTX.selectedIndex].value;
	d = theForm.POINTY.options[theForm.POINTY.selectedIndex].value;
	e = theForm.AMOUNT.options[theForm.AMOUNT.selectedIndex].value;
	f = theForm.TARGETID.options[theForm.TARGETID.selectedIndex].value;
	var newNs = a;
	if (x == 1 || x == 2 || x == 6){
		if(x == 6) b = k;
		if(x != 2) {
			for(i = $HcommandMax - 1; i > a; i--) {
				command[i] = command[i-1];
				g[i] = g[i-1];
			}
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
		newNs++;
		menuclose();
	}else if(x == 3){
		var num = (k) ? k-1 : a;
		for(i = Math.floor(num); i < ($HcommandMax - 1); i++) {
			command[i] = command[i + 1];
			g[i] = g[i+1];
		}
		command[$HcommandMax-1] = [41,0,0,0,0];
		g[$HcommandMax-1] = '資金繰り';
	}else if(x == 4){
		i = Math.floor(a)
		if (i == 0){ return true; }
		i = Math.floor(a)
		tmpcom1[i] = command[i];tmpcom2[i] = command[i - 1];
		command[i] = tmpcom2[i];command[i-1] = tmpcom1[i];
		k1[i] = g[i];k2[i] = g[i - 1];
		g[i] = k2[i];g[i-1] = k1[i];
		newNs = i-1;
	}else if(x == 5){
		i = Math.floor(a)
		if (i == $HcommandMax-1){ return true; }
		tmpcom1[i] = command[i];tmpcom2[i] = command[i + 1];
		command[i] = tmpcom2[i];command[i+1] = tmpcom1[i];
		k1[i] = g[i];k2[i] = g[i + 1];
		g[i] = k2[i];g[i+1] = k1[i];
		newNs = i+1;
	}else if(x == 7){
		// 移動
		var ctmp = command[k];
		var gtmp = g[k];
		if(z > k) {
			// 上から下へ
			for(i = k; i < z-1; i++) {
				command[i] = command[i+1];
				g[i] = g[i+1];
			}
		} else {
			// 下から上へ
			for(i = k; i > z; i--) {
				command[i] = command[i-1];
				g[i] = g[i-1];
			}
		}
		command[i] = ctmp;
		g[i] = gtmp;
	}

	str = plchg();
	str = "<font color=red><b>−−−− 未送信 −−−−</b></font><br>"+str;
	disp(str, "#CCDDFF");
	outp();
	theForm.CommandJavaButton$Hislands[$HcurrentNumber]->{'id'}.disabled = false;
	ns(newNs);
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
		//for(j = 0; j < islname.length ; j++) {
			//if(tgt == islname[j][0]){
				tgt = '<FONT COLOR="#a06040"><B>' + islname[tgt] + "島" + '</B></FONT>';
			//}
		//}
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
        	'<div id="com_'+i+'" '+
            'onmouseover="mc_over('+i+');return false;" '+
			'><A STYLE="text-decoration:none;color:000000" HREF="JavaScript:void(0);" onClick="ns(' + i + ')" '+
            'onmousedown="return comListMove('+i+');" '+
            '><NOBR>' +

		tmpnum + (i + 1) + ':' +
		strn2 + '</NOBR></A></div>\\n';
	}
	return strn1;
}

function disp(str,bgclr){
	if(str==null)  str = "";

	if(document.getElementById || document.all){
		LayWrite('LINKMSG1', str);
		SetBG('plan', bgclr);
	} else if(document.layers) {
		lay = document.layers["PARENT_LINKMSG"].document.layers["LINKMSG1"];
		lay.document.open();
		lay.document.write("<font style='font-size:11pt'>"+str+"</font>");
		lay.document.close(); 
		SetBG("PARENT_LINKMSG", bgclr);
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
	document.myForm.POINTX.options[x].selected = true;
	document.myForm.POINTY.options[y].selected = true;
	document.myForm.POINTX.value = x;
	document.myForm.POINTY.value = y;
	if(!(document.myForm.MENUOPEN.checked))
		moveLAYER("menu",mx+10,my-50);
	return true;
}

function SelectPOINT(){
	document.myForm.POINTX.value = document.forms[0].elements[4].options[document.forms[0].elements[4].selectedIndex].value;
	document.myForm.POINTY.value = document.forms[0].elements[5].options[document.forms[0].elements[5].selectedIndex].value;
	document.myForm.submit();
}

function ns(x) {
	if (x == $HcommandMax){ return true; }
	document.myForm.NUMBER.options[x].selected = true;
	document.myForm.NUMBER.value = x;
	selCommand(x);
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
	window.status = com_str;
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
		el = document.getElementById(layName);
		el.style.left = x;
		el.style.top  = y;
	} else if(document.layers){				//NN4
		msgLay = document.layers[layName];
		msgLay.moveTo(x,y);
	} else if(document.all){				//IE4
		msgLay = document.all(layName).style;
		msgLay.pixelLeft = x;
		msgLay.pixelTop = y;
	}

}

function menuclose(){ 
	moveLAYER("menu",-500,-500);
}

function Mmove(e){
	if(document.all){
		mx = event.x + document.body.scrollLeft;
		my = event.y + document.body.scrollTop;
	}else if(document.layers){
		mx = e.pageX;
		my = e.pageY;
	}else if(document.getElementById){
		mx = e.pageX;
		my = e.pageY;
	}
	return moveLay.move();
}

function LayWrite(layName, str) {
   if(document.getElementById){
      document.getElementById(layName).innerHTML = str;
   } else if(document.all){
      document.all(layName).innerHTML = str;
   } else if(document.layers){
      lay = document.layers[layName];
      lay.document.open();
      lay.document.write(str);
      lay.document.close(); 
   }
}
 

function SetBG(layName, bgclr) {
   if(document.getElementById) document.getElementById(layName).style.backgroundColor = bgclr;
   else if(document.all)       document.all.layName.bgColor = bgclr;
   //else if(document.layers)    document.layers[layName].bgColor = bgclr;
}

var oldNum=0;
function selCommand(num) {
   document.getElementById('com_'+oldNum).style.backgroundColor = '';
   document.getElementById('com_'+num).style.backgroundColor = '#FFFFAA';
   oldNum = num;
}

/* コマンド ドラッグ＆ドロップ用追加スクリプト */
var moveLay = new MoveFalse();

var newLnum = -2;
var Mcommand = false;

function Mup() {
   moveLay.up();
   moveLay = new MoveFalse();
}

function setBorder(num, color) {
   if(document.getElementById) {
      if(color.length == 4) document.getElementById('com_'+num).style.borderTop = ' 1px solid '+color;
      else document.getElementById('com_'+num).style.border = '0px';
   }
}

function mc_out() {
   if(Mcommand && newLnum >= 0) {
      setBorder(newLnum, '');
      newLnum = -1;
   }
}

function mc_over(num) {
   if(Mcommand) {
      if(newLnum >= 0) setBorder(newLnum, '');
      newLnum = num;
      setBorder(newLnum, '#116');    // blue
   }
}

function comListMove(num) { moveLay = new MoveComList(num); return (document.layers) ? true : false; }

function MoveFalse() {
   this.move = function() { }
   this.up   = function() { }
}

function MoveComList(num) {
   var setLnum  = num;
   Mcommand = true;

   LayWrite('mc_div', '<NOBR><strong>'+(num+1)+': '+g[num]+'</strong></NOBR>');

   this.move = function() {
      moveLAYER('mc_div',mx+10,my-30);
      return false;
   }

   this.up   = function() {
      if(newLnum >= 0) {
         var com = command[setLnum];
         cominput(document.myForm,7,setLnum,newLnum);
      }
      else if(newLnum == -1) cominput(document.myForm,3,setLnum+1);

      mc_out();
      newLnum = -2;

      Mcommand = false;
      moveLAYER("mc_div",-50,-50);
   }
}


/* 画面遷移無しでのコマンド送信用追加スクリプト */

function new_http() {
   if(document.getElementById) {
      try{
         return new ActiveXObject("Msxml2.XMLHTTP");
      } catch (e){
         try {
            return new ActiveXObject("Microsoft.XMLHTTP");
         } catch (E){
            if(typeof XMLHttpRequest != 'undefined') return new XMLHttpRequest;
         }
      }
   }
}

function send_command(form) {
   if (!xmlhttp) return true;

   form.CommandJavaButton$Hislands[$HcurrentNumber]->{'id'}.disabled = true;

   var progress  = document.getElementById('progress');
   progress.innerHTML = '<blink>Sending...</blink>';

   if (xmlhttp.readyState == 1 || xmlhttp.readyState == 2 || xmlhttp.readyState == 3) return; 

   xmlhttp.open("POST", "$HthisFile", true);
   if(!window.opera) xmlhttp.setRequestHeader("referer", "$HthisFile");

   xmlhttp.onreadystatechange = function() {
      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
         var result = xmlhttp.responseText;
         if(result.indexOf('OK') == 0 || result.indexOf('OK') == 2048) {
            str = plchg();
            str = "<font color=blue>−−−− 送信済み −−−−</font><br>"+str;
            disp(str, "#CCFFDD");
         } else {
            alert("送信に失敗しました。");
            form.CommandJavaButton$Hislands[$HcurrentNumber]->{'id'}.disabled = false;
         }
         progress.innerHTML = '';
      }
   }

   var post;
   post += 'async=true&';
   post += 'CommandJavaButton$island->{'id'}=true&';
   post += 'JAVAMODE=java&';
   post += 'COMARY='+form.COMARY.value+'&';
   post += 'PASSWORD='+form.PASSWORD.value+'&';

   xmlhttp.send(post);
   return false;
}

//-->
</SCRIPT>
<DIV ID="mc_div" style="background-color:white;position:absolute;top:-50;left:-50;">&nbsp;</DIV>
<DIV ID="menu" style="position:absolute; top:-500;left:-500;"> 
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
<FORM name="myForm" action="$HthisFile" method=POST onsubmit="return send_command(this);">
<P>
<B>コマンド入力</B><BR><B>
<A HREF=JavaScript:void(0); onClick="cominput(myForm,1)">挿入</A>
　<A HREF=JavaScript:void(0); onClick="cominput(myForm,2)">上書き</A>
　<A HREF=JavaScript:void(0); onClick="cominput(myForm,3)">削除</A>
</B><HR>
<B>計画番号</B><SELECT NAME=NUMBER onchange="selCommand(this.selectedIndex)">
END
    # 計画番号
    my($j, $i);
    for($i = 0; $i < $HcommandMax; $i++) {
	$j = $i + 1;
	out("<OPTION VALUE=$i>$j\n");
    }

    out(<<END);
</SELECT><BR>
<HR>
<B>開発計画</B>
<INPUT TYPE="checkbox" NAME="MENUOPEN">非表\示<br>
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
<span id="progress"></span>
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
<TD $HbgCommandCell id="plan" onmouseout="mc_out();return false;">
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

	# データの書き出し
    writeIslandsFile($HcurrentID);

	if($Hasync) {
		unlock();
		out("Content-type: text/html\n\nOK");
	} else {
		tempCommandAdd();
		# owner modeへ
		ownerMain();
	}
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

