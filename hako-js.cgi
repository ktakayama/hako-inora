#----------------------------------------------------------------------
# �ʣ��֣�������ץ��� -ver1.11-
# ���Ѿ�������ˡ���ϡ����۸��Ǥ���ǧ��������
# ��°��js-readme.txt�⤪�ɤ߲�������
# ���äݡ���http://appoh.execweb.cx/hakoniwa/
#----------------------------------------------------------------------
# ���Τ����
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �ʣ���᥹����ץȳ�ȯ����
#----------------------------------------------------------------------
# �����糫ȯ�ײ�
sub tempOwnerJava {
	$HcurrentNumber = $HidToNumber{$HcurrentID};
	my($island) = $Hislands[$HcurrentNumber];

	# ���ޥ�ɥ��å�
	$set_com = "";
	$com_max = "";
	for($i = 0; $i < $HcommandMax; $i++) {
		# �����Ǥμ��Ф�
		my($command) = $island->{'command'}->[$i];
		my($s_kind, $s_target, $s_x, $s_y, $s_arg) = 
		(
		$command->{'kind'},
		$command->{'target'},
		$command->{'x'},
		$command->{'y'},
		$command->{'arg'}
		);
		# ���ޥ����Ͽ
		if($i == $HcommandMax-1){
			$set_com .= "\[$s_kind\,$s_x\,$s_y\,$s_arg\,$s_target\]\n";
			$com_max .= "0"
		}else{
			$set_com .= "\[$s_kind\,$s_x\,$s_y\,$s_arg\,$s_target\]\,\n";
			$com_max .= "0,"
		}
	}

    #���ޥ�ɥꥹ�ȥ��å�
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
			if($l_cost == 0) { $l_cost = '̵��'	}
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

	#��ꥹ�ȥ��å�
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
${HtagBig_}${HtagName_}${HcurrentName}��${H_tagName}��ȯ�ײ�${H_tagBig}<BR>
$HtempBack<BR>
</CENTER>
<SCRIPT Language="JavaScript">
<!--
// �ʣ��֣�������ץȳ�ȯ�������۸�
// ���äݡ���Ȣ������ http://appoh.execweb.cx/hakoniwa/ ��
// Programmed by Jynichi Sakai(���äݡ�)
// �� ������ʤ��ǲ�������
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
	str = "<font color=blue>�ݡݡݡ� �����Ѥ� �ݡݡݡ�</font><br>"+str;
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
		g[$HcommandMax-1] = '��ⷫ��';
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
		// ��ư
		var ctmp = command[k];
		var gtmp = g[k];
		if(z > k) {
			// �夫�鲼��
			for(i = k; i < z-1; i++) {
				command[i] = command[i+1];
				g[i] = g[i+1];
			}
		} else {
			// ��������
			for(i = k; i > z; i--) {
				command[i] = command[i-1];
				g[i] = g[i-1];
			}
		}
		command[i] = ctmp;
		g[i] = gtmp;
	}

	str = plchg();
	str = "<font color=red><b>�ݡݡݡ� ̤���� �ݡݡݡ�</b></font><br>"+str;
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
				tgt = '<FONT COLOR="#a06040"><B>' + islname[tgt] + "��" + '</B></FONT>';
			//}
		//}
		if(c[0] == $HcomDoNothing || c[0] == $HcomGiveup){ // ��ⷫ�ꡢ�������
			strn2 = kind;
		}else if(c[0] == $HcomMissileNM || // �ߥ������Ϣ
			c[0] == $HcomMissilePP){
			if(c[3] == 0){
				arg = "��̵���¡�";
			} else {
				arg = "��" + c[3] + "ȯ��";
			}
			strn2 = tgt + point + "��" + kind + arg;
		}else if(c[0] == $HcomSell){ // ����͢��
			if(c[3] == 0){ c[3] = 1; }
			arg = c[3] * 100;
			arg = "��" + arg + "$HunitFood��";
			strn2 = kind + arg;
		}else if(c[0] == $HcomPropaganda){ // Ͷ�׳�ư
			strn2 = kind;
		}else if(c[0] == $HcomMoney){ // �����
			if(c[3] == 0){ c[3] = 1; }
			arg = c[3] * $HcomCost[$HcomMoney];
			arg = "��" + arg + "$HunitMoney��";
			strn2 = tgt + "��" + kind + arg;
		}else if(c[0] == $HcomFood){ // �������
			if(c[3] == 0){ c[3] = 1; }
			arg = c[3] * 100;
			arg = "��" + arg + "$HunitFood��";
			strn2 = tgt + "��" + kind + arg;
		}else if(c[0] == $HcomDestroy){ // ����
			if(c[3] == 0){
				strn2 = point + "��" + kind;
			} else {
				arg = c[3] * $HcomCost[$HcomDestroy];
				arg = "��ͽ\��" + arg + "$HunitMoney��";
				strn2 = point + "��" + kind + arg;
			}
		}else if(c[0] == $HcomFarm || // ���졢���졢�η�������
			c[0] == $HcomFactory ||
			c[0] == $HcomMountain) {
			if(c[3] != 0){
				arg = "��" + c[3] + "���";
				strn2 = point + "��" + kind + arg;
			}else{
				strn2 = point + "��" + kind;
			}
		}else{
			strn2 = point + "��" + kind;
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
					arg = "��ͽ\��" + arg + "$HunitMoney��";
					com_str += kind + arg;
				}
			}else if(c[0] == $HcomFarm ||
				c[0] == $HcomFactory ||
				c[0] == $HcomMountain) {
				if(c[3] != 0){
					arg = "��" + c[3] + "���";
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

/* ���ޥ�� �ɥ�å����ɥ�å����ɲå�����ץ� */
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


/* ��������̵���ǤΥ��ޥ���������ɲå�����ץ� */

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
            str = "<font color=blue>�ݡݡݡ� �����Ѥ� �ݡݡݡ�</font><br>"+str;
            disp(str, "#CCFFDD");
         } else {
            alert("�����˼��Ԥ��ޤ�����");
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
<a href="Javascript:void(0);" onClick="menuclose()" STYlE="text-decoration:none">��˥塼���Ĥ���</A>
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
<B>���ޥ������</B><BR><B>
<A HREF=JavaScript:void(0); onClick="cominput(myForm,1)">����</A>
��<A HREF=JavaScript:void(0); onClick="cominput(myForm,2)">���</A>
��<A HREF=JavaScript:void(0); onClick="cominput(myForm,3)">���</A>
</B><HR>
<B>�ײ��ֹ�</B><SELECT NAME=NUMBER onchange="selCommand(this.selectedIndex)">
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
<B>��ȯ�ײ�</B>
<INPUT TYPE="checkbox" NAME="MENUOPEN">��ɽ\��<br>
<SELECT NAME=menu onchange="SelectList(myForm)">
<OPTION VALUE=>������
END
	for($i = 0; $i < $com_count; $i++) {
		($aa) = split(/,/,$HcommandDivido[$i]);
		out("<OPTION VALUE=$i>$aa\n");
	}
    out(<<END);
</SELECT><br>
<SELECT NAME=COMMAND>
<option>��������������������</option>
<option>��������������������</option>
<option>��������������������</option>
<option>��������������������</option>
<option>��������������������</option>
<option>��������������������</option>
<option>��������������������</option>
<option>��������������������</option>
<option>��������������������</option>
<option>��������������������</option>
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
<B>��ɸ����</B>
<SELECT NAME=TARGETID>
$HtargetList<BR>
</SELECT>
<HR>
<B>���ޥ�ɰ�ư</B>��
<BIG>
<A HREF=JavaScript:void(0); onClick="cominput(myForm,4)" STYlE="text-decoration:none"> �� </A>����
<A HREF=JavaScript:void(0); onClick="cominput(myForm,5)" STYlE="text-decoration:none"> �� </A>
</BIG>
<HR>
<INPUT TYPE="hidden" NAME="COMARY" value="comary">
<INPUT TYPE="hidden" NAME="JAVAMODE" value="$HjavaMode">
<INPUT TYPE=submit VALUE="�ײ�����" NAME=CommandJavaButton$Hislands[$HcurrentNumber]->{'id'}>
<span id="progress"></span>
<br><font size=2>�Ǹ��<font color=red>�ײ������ܥ���</font>��<br>�����Τ�˺��ʤ��褦�ˡ�</font>
<HR>
<B>�ѥ����</B></BR>
<INPUT TYPE=password NAME=PASSWORD VALUE="$HdefaultPassword">
</CENTER>
</TD>
<TD $HbgMapCell><center>
<TEXTAREA NAME="COMSTATUS" cols="48" rows="2" readonly></TEXTAREA>
</center>
END
    islandMapJava(1);    # ����Ͽޡ���ͭ�ԥ⡼��
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
${HtagBig_}�����ȹ���${H_tagBig}<BR>
<FORM action="$HthisFile" method="POST">
������<INPUT TYPE=text NAME=MESSAGE SIZE=80 VALUE="$comment"><BR>
�ѥ����<INPUT TYPE=password NAME=PASSWORD VALUE="$HdefaultPassword">
<INPUT TYPE="hidden" NAME=JAVAMODE VALUE="$HjavaMode">
<INPUT TYPE=submit VALUE="�����ȹ���" NAME=MessageButton$Hislands[$HcurrentNumber]->{'id'}>
</FORM>
</CENTER>
END

}

#----------------------------------------------------------------------
# ������Ǽ������ϥե����� �ʣ���᥹����ץ� mode��
#----------------------------------------------------------------------
sub tempLbbsInputJava {
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
<INPUT TYPE="hidden" NAME=JAVAMODE VALUE="$HjavaMode">
</TD>
</TR>
</TABLE>
</FORM>
</CENTER>
END
}

#----------------------------------------------------------------------
# ���ޥ�ɥ⡼��
#----------------------------------------------------------------------
sub commandJavaMain {
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
	for($i = 0; $i < $HcommandMax; $i++) {
		# ���ޥ����Ͽ
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

	# �ǡ����ν񤭽Ф�
    writeIslandsFile($HcurrentID);

	if($Hasync) {
		unlock();
		out("Content-type: text/html\n\nOK");
	} else {
		tempCommandAdd();
		# owner mode��
		ownerMain();
	}
}

#----------------------------------------------------------------------
# �Ͽޤ�ɽ��
#----------------------------------------------------------------------
sub islandMapJava {
    my($mode) = @_;
    my($island);
    $island = $Hislands[$HcurrentNumber];

    # �Ϸ����Ϸ��ͤ����
    my($land) = $island->{'land'};
    my($landValue) = $island->{'landValue'};
    my($l, $lv);

    out(<<END);
<CENTER><TABLE BORDER CELLSPACING=1><TR><TD>
END
    # ���ޥ�ɼ���
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
	    landString($l, $lv, $x, $y, $mode, $comStr[$x][$y], 1, $island);
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


1;

