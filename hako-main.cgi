#!/usr/bin/perl
# ���ϥ����С��˹�碌���ѹ����Ʋ�������
# perl5�ѤǤ���

#----------------------------------------------------------------------
# Ȣ����� ver2.30
# �ᥤ�󥹥���ץ�
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# ���Τ����
#----------------------------------------------------------------------

require ('hako-ini.cgi');

#----------------------------------------------------------------------
# ����ʹߤΥ�����ץȤϡ��ѹ�����뤳�Ȥ����ꤷ�Ƥ��ޤ��󤬡�
# �����äƤ⤫�ޤ��ޤ���
# ���ޥ�ɤ�̾�������ʤʤɤϲ��䤹���Ȼפ��ޤ���
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �Ƽ����
#----------------------------------------------------------------------
# ���Υե�����
$HthisFile = "$baseDir/hako-main.cgi";

# �Ϸ��ֹ�
$HlandSea		= 0;  # ��
$HlandWaste		= 1;  # ����
$HlandPlains	= 2;  # ʿ��
$HlandTown		= 3;  # Į��
$HlandForest	= 4;  # ��
$HlandFarm		= 5;  # ����
$HlandFactory	= 6;  # ����
$HlandBase		= 7;  # �ߥ��������
$HlandDefence	= 8;  # �ɱһ���
$HlandMountain	= 9;  # ��
$HlandMonster	= 10; # ����
$HlandSbase		= 11; # �������
$HlandOil		= 12; # ��������
$HlandMonument	= 13; # ��ǰ��
$HlandHaribote	= 14; # �ϥ�ܥ�

# ���ޥ��
$HcommandTotal = 36; # ���ޥ�ɤμ���

# ���ޥ��ʬ��
# ���Υ��ޥ��ʬ������ϡ���ư���ϷϤΥ��ޥ�ɤ����ꤷ�ʤ��ǲ�������
@HcommandDivido = 
		(
		'��ȯ,0,10',  # �ײ��ֹ�00��10
		'����,11,24', # �ײ��ֹ�11��30
		'���Τ�,25,34',# �ײ��ֹ�25��34
		'����,35,40', # �ײ��ֹ�31��40
		'����,41,60'  # �ײ��ֹ�41��60
		);
# ��ա����ڡ���������ʤ��褦��
# ����		'��ȯ,0,10',		# �ײ��ֹ�00��10
# �ߢ�		'��ȯ, 0  ,10  ',	# �ײ��ֹ�00��10

# �ײ��ֹ������
# ���Ϸ�
$HcomPrepare  = 01; # ����
$HcomPrepare2 = 02; # �Ϥʤ餷
$HcomReclaim  = 03; # ���Ω��
$HcomDestroy  = 04; # ����
$HcomSellTree = 05; # Ȳ��
$HcomFastRec  = 06; # ��®���Ω��
$HcomFastDes  = 07; # ��®����

# ����
$HcomPlant		= 11; # ����
$HcomFarm		= 12; # ��������
$HcomFactory	= 13; # �������
$HcomMountain	= 14; # �η�������
$HcomBase		= 15; # �ߥ�������Ϸ���
$HcomDbase		= 16; # �ɱһ��߷���
$HcomSbase		= 17; # ������Ϸ���
$HcomMonument	= 18; # ��ǰ���¤
$HcomHaribote	= 19; # �ϥ�ܥ�����
$HcomFastPlant	= 20; # ��®����
$HcomFastFarm	= 21; # ��®��������
$HcomFastFact	= 22; # ��®�������
$HcomFastBase	= 23; # ��®�ߥ�������Ϸ���
$HcomFastDbase	= 24; # ��®�ɱһ��߷���

# ���Τ��
$HcomSchool	  = 25; # ���Τ�ع�
$HcomEste	  = 26; # ���Τ饨����
$HcomTreaning = 27; # ���Τ饸��
$HcomRest	  = 28; # ���Τ�����
$HcomPlay	  = 29; # ���Τ�ͷ��

# ȯ�ͷ�
$HcomMissileNM  = 35; # �ߥ�����ȯ��
$HcomMissilePP  = 36; # PP�ߥ�����ȯ��

# ���ķ�
$HcomDoNothing	= 41; # ��ⷫ��
$HcomSell		= 42; # ����͢��
$HcomMoney		= 43; # �����
$HcomFood		= 44; # �������
$HcomPropaganda	= 45; # Ͷ�׳�ư
$HcomGiveup		= 46; # �������

# ��ư���Ϸ�
$HcomAutoPrepare  = 61; # �ե�����
$HcomAutoPrepare2 = 62; # �ե��Ϥʤ餷
$HcomAutoDelete   = 63; # �����ޥ�ɾõ�

# ����
@HcomList =
	($HcomPrepare, $HcomSell, $HcomPrepare2, $HcomReclaim, $HcomDestroy,
	 $HcomSellTree, $HcomFastRec, $HcomFastDes, $HcomPlant, $HcomFarm, 
	 $HcomFactory, $HcomMountain, $HcomBase, $HcomDbase, $HcomFastPlant,
	 $HcomFastFarm, $HcomFastFact, $HcomFastBase, 
	 $HcomFastDbase, $HcomMonument, $HcomHaribote,
	 $HcomSchool, $HcomEste, $HcomTreaning, $HcomRest, $HcomPlay,
	 $HcomMissileNM, $HcomMissilePP, $HcomDoNothing,
	 $HcomMoney, $HcomFood, $HcomPropaganda, $HcomGiveup,
	 $HcomAutoPrepare, $HcomAutoPrepare2, $HcomAutoDelete);



# �ײ��̾��������
$HcomName[$HcomPrepare]		= '����';
$HcomCost[$HcomPrepare]		= 1;
$HcomName[$HcomPrepare2]	= '�Ϥʤ餷';
$HcomCost[$HcomPrepare2]	= 30;
$HcomName[$HcomReclaim]		= '���Ω��';
$HcomCost[$HcomReclaim]		= 100;
$HcomName[$HcomDestroy]		= '����';
$HcomCost[$HcomDestroy]		= 300;
$HcomName[$HcomSellTree]	= 'Ȳ��';
$HcomCost[$HcomSellTree]	= 0;
$HcomName[$HcomPlant]		= '����';
$HcomCost[$HcomPlant]		= 50;
$HcomName[$HcomFarm]		= '��������';
$HcomCost[$HcomFarm]		= 10;
$HcomName[$HcomFactory]		= '�������';
$HcomCost[$HcomFactory]		= 50;
$HcomName[$HcomMountain]	= '�η�������';
$HcomCost[$HcomMountain]	= 300;
$HcomName[$HcomBase]		= '�ߥ�������Ϸ���';
$HcomName2[$HcomBase]		= '�ߥ��������';
$HcomCost[$HcomBase]		= 200;
$HcomName[$HcomDbase]		= '�ɱһ��߷���';
$HcomName2[$HcomDbase]		= '�ɱһ���';
$HcomCost[$HcomDbase]		= 500;
$HcomName[$HcomFastRec]		= '��®���Ω��';
$HcomName2[$HcomFastRec]	= '��®��Ω';
$HcomCost[$HcomFastRec]		= 500;
$HcomName[$HcomFastDes]		= '��®����';
$HcomCost[$HcomFastDes]		= 1500;
$HcomName[$HcomFastPlant]	= '��®����';
$HcomCost[$HcomFastPlant]	= 1000;
$HcomName[$HcomFastFarm]	= '��®��������';
$HcomName2[$HcomFastFarm]	= '��®����';
$HcomCost[$HcomFastFarm]	= 500;
$HcomName[$HcomFastFact]	= '��®��������';
$HcomName2[$HcomFastFact]	= '��®����';
$HcomCost[$HcomFastFact]	= 1000;
$HcomName[$HcomFastBase]	= '��®�ߥ�������Ϸ���';
$HcomName2[$HcomFastBase]	= '��®�ߴ���';
$HcomCost[$HcomFastBase]	= 900;
$HcomName[$HcomFastDbase]	= '��®�ɱһ��߷���';
$HcomName2[$HcomFastDbase]	= '��®�ɱ�';
$HcomCost[$HcomFastDbase]	= 2000;
$HcomName[$HcomSbase]		= '������Ϸ���';
$HcomCost[$HcomSbase]		= 999999;
$HcomName[$HcomMonument]	= '��ǰ���¤';
$HcomCost[$HcomMonument]	= 9999;
$HcomName[$HcomHaribote]	= '�ϥ�ܥ�����';
$HcomCost[$HcomHaribote]	= 1;
$HcomName[$HcomSchool]		= '���Τ�ع�';
$HcomName2[$HcomSchool]		= '�ع�';
$HcomCost[$HcomSchool]		= 300;
$HcomName[$HcomEste]		= '���Τ饨����';
$HcomName2[$HcomEste]		= '������';
$HcomCost[$HcomEste]		= 300;
$HcomName[$HcomTreaning]	= '���Τ饸��';
$HcomName2[$HcomTreaning]	= '����';
$HcomCost[$HcomTreaning]	= 800;
$HcomName[$HcomRest]		= '���Τ�����';
$HcomName2[$HcomRest]		= '����';
$HcomCost[$HcomRest]		= 500;
$HcomName[$HcomPlay]		= '���Τ�ͷ��';
$HcomName2[$HcomPlay]		= 'ͷ��';
$HcomCost[$HcomPlay]		= 400;
$HcomName[$HcomMissileNM]	= '�ߥ�����ȯ��';
$HcomCost[$HcomMissileNM]	= 20;
$HcomName[$HcomMissilePP]	= 'PP�ߥ�����ȯ��';
$HcomCost[$HcomMissilePP]	= 40;
$HcomName[$HcomDoNothing]	= '��ⷫ��';
$HcomCost[$HcomDoNothing]	= 0;
$HcomName[$HcomSell]		= '����͢��';
$HcomCost[$HcomSell]		= -100;
$HcomName[$HcomMoney]		= '�����';
$HcomCost[$HcomMoney]		= 100;
$HcomName[$HcomFood]		= '�������';
$HcomCost[$HcomFood]		= -100;
$HcomName[$HcomPropaganda]	= '���Τ���Կ�';
$HcomCost[$HcomPropaganda]	= 1000;
$HcomName[$HcomGiveup]		= '�������';
$HcomCost[$HcomGiveup]		= 0;
$HcomName[$HcomAutoPrepare]	= '���ϼ�ư����';
$HcomCost[$HcomAutoPrepare]	= 0;
$HcomName[$HcomAutoPrepare2]= '�Ϥʤ餷��ư����';
$HcomCost[$HcomAutoPrepare2]= 0;
$HcomName[$HcomAutoDelete]	= '���ײ�����ű��';
$HcomCost[$HcomAutoDelete]	=  0;

#----------------------------------------------------------------------
# �ѿ�
#----------------------------------------------------------------------

# COOKIE
my($defaultID);	   # ���̾��
my($defaultTarget);   # �������åȤ�̾��

# ��κ�ɸ��
$HpointNumber = $HislandSize * $HislandSize;

#----------------------------------------------------------------------
# �ᥤ��
#----------------------------------------------------------------------

# jcode.pl��require
require($jcode);

if($Href) {
	my($page) = $ENV{'HTTP_REFERER'};
	$page =~ tr/+/ /;
	$page =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	if (!($page =~ /$ref_page/i)) { &access; }
}

sub access {
	print "Content-type: text/html\n\n";
	out (<<'END');
<HTML><HEAD><TITLE>���������ػ�</TITLE></HEAD>
<BODY><BR><BR><center><H1>���������ػ�</H1><br>
<font size=+1>�ȥåץڡ�����ꤪ���꤯��������<BR><br>
<A HREF=$ref_main>$ref_main</A>
</font>
</BODY></HTML>
END
	exit;
}

# �����ץ��
$HtempBack = "<A HREF=\"$HthisFile\">${HtagBig_}�ȥåפ����${H_tagBig}</A>";
$BODY = "<BODY $htmlBody>";

# ��å��򤫤���
if(!hakolock()) {
	# ��å�����
	# �إå�����
	tempHeader();

	# ��å����ԥ�å�����
	tempLockFail();

	# �եå�����
	tempFooter();

	# ��λ
	exit(0);
}

# ����ν����
srand(time^$$);

# COOKIE�ɤߤ���
cookieInput();

# CGI�ɤߤ���
cgiInput();

# ��ǡ������ɤߤ���
if(readIslandsFile($HcurrentID) == 0) {
	unlock();
	tempHeader();
	tempNoDataFile();
	tempFooter();
	exit(0);
}

# �ƥ�ץ졼�Ȥ�����
tempInitialize();

# COOKIE����
cookieOutput();

# �إå�����
if($HmainMode eq 'owner' && $HjavaMode eq 'java' ||
   $HmainMode eq 'commandJava' || # ���ޥ�����ϥ⡼��
   $HmainMode eq 'comment' && $HjavaMode eq 'java' || #���������ϥ⡼��
   $HmainMode eq 'lbbs' && $HjavaMode eq 'java') { #���������ϥ⡼��
	$BODY = "<BODY onload=\"init()\" $htmlBody>";
	require('hako-js.cgi');
	require('hako-map.cgi');
	# �إå�����
	tempHeader();
	if($HmainMode eq 'commandJava') {
		# ��ȯ�⡼��
		commandJavaMain();
	} elsif($HmainMode eq 'comment') {
		# ���������ϥ⡼��
		commentMain();
	} elsif($HmainMode eq 'lbbs') {
		# ������Ǽ��ĥ⡼��
		localBbsMain();
	}else{
		ownerMain();
	}
	# �եå�����
	tempFooter();
	# ��λ
	exit(0);
}else{
	# �إå�����
	tempHeader();
}

if($HmainMode eq 'turn') {
	# ������ʹ�
	require('hako-turn.cgi');
	require('hako-top.cgi');
	turnMain();

} elsif($HmainMode eq 'new') {
	# ��ο�������
	require('hako-turn.cgi');
	require('hako-map.cgi');
	newIslandMain();

} elsif($HmainMode eq 'print') {
	# �Ѹ��⡼��
	require('hako-map.cgi');
	printIslandMain();

} elsif($HmainMode eq 'owner') {

	# ��ȯ�⡼��
	require('hako-map.cgi');
	ownerMain();

} elsif($HmainMode eq 'command') {
	# ���ޥ�����ϥ⡼��
	require('hako-map.cgi');
	commandMain();

} elsif($HmainMode eq 'comment') {
	# ���������ϥ⡼��
	require('hako-map.cgi');
	commentMain();

} elsif($HmainMode eq 'lbbs') {

	# ������Ǽ��ĥ⡼��
	require('hako-map.cgi');
	localBbsMain();

} elsif($HmainMode eq 'change') {
	# �����ѹ��⡼��
	require('hako-turn.cgi');
	require('hako-top.cgi');
	changeMain();

} elsif($HmainMode eq 'logView') {
	# LOG�⡼��
	require('hako-top.cgi');
	logViewMain();

} else {
	# ����¾�ξ��ϥȥåץڡ����⡼��
	require('hako-top.cgi');
	topPageMain();
}

# �եå�����
tempFooter();

# ��λ
exit(0);

# ���ޥ�ɤ����ˤ��餹
sub slideFront {
	my($command, $number) = @_;
	my($i);

	# ���줾�줺�餹
	splice(@$command, $number, 1);

	# �Ǹ�˻�ⷫ��
	$command->[$HcommandMax - 1] = {
		'kind' => $HcomDoNothing,
		'target' => 0,
		'x' => 0,
		'y' => 0,
		'arg' => 0
		};
}

# ���ޥ�ɤ��ˤ��餹
sub slideBack {
	my($command, $number) = @_;
	my($i);

	# ���줾�줺�餹
	return if $number == $#$command;
	pop(@$command);
	splice(@$command, $number, 0, $command->[$number]);
}

#----------------------------------------------------------------------
# ��ǡ���������
#----------------------------------------------------------------------

# ����ǡ����ɤߤ���
sub readIslandsFile {
	my($num) = @_; # 0�����Ϸ��ɤߤ��ޤ�
				   # -1�������Ϸ����ɤ�
				   # �ֹ���Ȥ�������Ϸ��������ɤߤ���

	# �ǡ����ե�����򳫤�
	if(!open(IN, "${HdirName}/hakojima.dat")) {
		rename("${HdirName}/hakojima.tmp", "${HdirName}/hakojima.dat");
		if(!open(IN, "${HdirName}/hakojima.dat")) {
			return 0;
		}
	}

	# �ƥѥ�᡼�����ɤߤ���
	$HislandTurn	 = int(<IN>); # �������
	if($HislandTurn == 0) {
		return 0;
	}
	$HislandLastTime = int(<IN>); # �ǽ���������
	if($HislandLastTime == 0) {
		return 0;
	}
	$HislandNumber   = int(<IN>); # ������
	$HislandNextID   = int(<IN>); # ���˳�����Ƥ�ID

	# ���������Ƚ��
	my($now) = time;
	if((($Hdebug == 1) && 
		($HmainMode eq 'Hdebugturn')) ||
	   (($now - $HislandLastTime) >= $HunitTime)) {
		if($HislandLastTurn > $HislandTurn) {
			$turnMode = "debug" if($HmainMode eq 'Hdebugturn');
			$HmainMode = 'turn';
			$num = -1; # �����ɤߤ���
		}
	}

	# ����ɤߤ���
	my($i);
	for($i = 0; $i < $HislandNumber; $i++) {
		 $Hislands[$i] = readIsland($num);
		 $HidToNumber{$Hislands[$i]->{'id'}} = $i;
	}

	# �ե�������Ĥ���
	close(IN);

	return 1;
}

# ��ҤȤ��ɤߤ���
sub readIsland {
	my($num) = @_;
	my($name, $id, $prize, $absent, $comment, $password, $money, $food,
	   $pop, $area, $farm, $factory, $mountain, $score, $fire, $ownername);
	my($i_name, $i_cont, $i_gene, $i_age, $i_type, $i_ang, $i_heal,
		 $i_hp, $i_cute, $i_arm, $i_int, $i_sleep);

	$name = <IN>; # ���̾��
	chomp($name);
	if($name =~ s/,(.*)$//g) {
		$score = int($1);
	} else {
		$score = 0;
	}
	$id = int(<IN>);		# ID�ֹ�
	$prize = <IN>;			# ����
	chomp($prize);
	$absent = int(<IN>);	# Ϣ³��ⷫ���
	$comment = <IN>;		# ������
	chomp($comment);
	$password = <IN>;		# �Ź沽�ѥ����
	chomp($password);
	$money = int(<IN>);		# ���
	$food = int(<IN>);		# ����
	$pop = int(<IN>);		# �͸�
	$area = int(<IN>);		# ����
	$farm = int(<IN>);		# ����
	$factory = int(<IN>);	# ����
	$mountain = int(<IN>);	# �η���
	$fire = int(<IN>);		# �ߥ�����ȯ�Ϳ�
	$ownername = <IN>;		# �����ʡ��͡���
	chomp($ownername);
	$i_name = <IN>;			# ���Τ��̾��
	chomp($i_name);
	$i_cont = <IN>;			# ���Τ饳��ƥ��ȼ��޿�
	chomp($i_cont);
	$i_gene = int(<IN>);	# ���Τ������
	$i_age = int(<IN>);		# ���Τ��ǯ
	$i_type = int(<IN>);	# ���Τ�μ���
	$i_ang = int(<IN>);		# ���Τ�ε���
	$i_heal = int(<IN>);	# ���Τ�η���
	$i_hp = int(<IN>);		# ���Τ������
	$i_cute = int(<IN>);	# ���Τ��̥��
	$i_arm = int(<IN>);		# ���Τ������
	$i_int = int(<IN>);		# ���Τ������
	$i_sleep = int(<IN>);	# ���Τ��̲�ե饰


	# HidToName�ơ��֥����¸
	$HidToName{$id} = $name;		# 

	# �Ϸ�
	my(@land, @landValue, $line, @command, @lbbs);

	if(($num == -1) || ($num == $id)) {
		if(!open(IIN, "${HdirName}/island.$id")) {
			rename("${HdirName}/islandtmp.$id", "${HdirName}/island.$id");
			if(!open(IIN, "${HdirName}/island.$id")) {
				exit(0);
			}
		}
		my($x, $y);
		for($y = 0; $y < $HislandSize; $y++) {
			$line = <IIN>;
			for($x = 0; $x < $HislandSize; $x++) {
				$line =~ s/^(.)(..)//;
				$land[$x][$y] = hex($1);
				$landValue[$x][$y] = hex($2);
			}
		}

		# ���ޥ��
		my($i);
		for($i = 0; $i < $HcommandMax; $i++) {
			$line = <IIN>;
			$line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),([0-9]*)$/;
			$command[$i] = {
				'kind' => int($1),
				'target' => int($2),
				'x' => int($3),
				'y' => int($4),
				'arg' => int($5)
				}
		}

		# ������Ǽ���
		for($i = 0; $i < $HlbbsMax; $i++) {
			$line = <IIN>;
			chomp($line);
			$lbbs[$i] = $line;
		}

		close(IIN);
	}

	# �緿�ˤ����֤�
	return {
		 'name' => $name,
		 'id' => $id,
		 'score' => $score,
		 'prize' => $prize,
		 'absent' => $absent,
		 'comment' => $comment,
		 'password' => $password,
		 'money' => $money,
		 'food' => $food,
		 'pop' => $pop,
		 'area' => $area,
		 'farm' => $farm,
		 'factory' => $factory,
		 'mountain' => $mountain,
		 'fire' => $fire,
		 'ownername' => $ownername,
		 'i_name' => $i_name,
		 'i_cont' => $i_cont,
		 'i_gene' => $i_gene,
		 'i_age'  => $i_age,
		 'i_type' => $i_type,
		 'i_ang'  => $i_ang,
		 'i_heal' => $i_heal,
		 'i_hp'   => $i_hp,
		 'i_cute' => $i_cute,
		 'i_arm'  => $i_arm,
		 'i_int'  => $i_int,
		 'i_sleep'  => $i_sleep,
		 'land' => \@land,
		 'landValue' => \@landValue,
		 'command' => \@command,
		 'lbbs' => \@lbbs,
	};
}

# ����ǡ����񤭹���
sub writeIslandsFile {
	my($num) = @_;

	# �ե�����򳫤�
	open(OUT, ">${HdirName}/hakojima.tmp");

	# �ƥѥ�᡼���񤭹���
	print OUT "$HislandTurn\n";
	print OUT "$HislandLastTime\n";
	print OUT "$HislandNumber\n";
	print OUT "$HislandNextID\n";

	# ��ν񤭤���
	my($i);
	for($i = 0; $i < $HislandNumber; $i++) {
		 writeIsland($Hislands[$i], $num);
	}

	# �ե�������Ĥ���
	close(OUT);

	# �����̾���ˤ���
	unlink("${HdirName}/hakojima.dat");
	rename("${HdirName}/hakojima.tmp", "${HdirName}/hakojima.dat");
}

# ��ҤȤĽ񤭹���
sub writeIsland {
	my($island, $num) = @_;
	my($score);
	$score = int($island->{'score'});
	print OUT $island->{'name'} . ",$score\n";
	print OUT $island->{'id'} . "\n";
	print OUT $island->{'prize'} . "\n";
	print OUT $island->{'absent'} . "\n";
	print OUT $island->{'comment'} . "\n";
	print OUT $island->{'password'} . "\n";
	print OUT $island->{'money'} . "\n";
	print OUT $island->{'food'} . "\n";
	print OUT $island->{'pop'} . "\n";
	print OUT $island->{'area'} . "\n";
	print OUT $island->{'farm'} . "\n";
	print OUT $island->{'factory'} . "\n";
	print OUT $island->{'mountain'} . "\n";
	print OUT $island->{'fire'} . "\n";
	print OUT $island->{'ownername'} . "\n";
	print OUT $island->{'i_name'} . "\n";
	print OUT $island->{'i_cont'} . "\n";
	print OUT $island->{'i_gene'} . "\n";
	print OUT $island->{'i_age'} . "\n";
	print OUT $island->{'i_type'} . "\n";
	print OUT $island->{'i_ang'} . "\n";
	print OUT $island->{'i_heal'} . "\n";
	print OUT $island->{'i_hp'} . "\n";
	print OUT $island->{'i_cute'} . "\n";
	print OUT $island->{'i_arm'} . "\n";
	print OUT $island->{'i_int'} . "\n";
	print OUT $island->{'i_sleep'} . "\n";

	# �Ϸ�
	if(($num <= -1) || ($num == $island->{'id'})) {
		open(IOUT, ">${HdirName}/islandtmp.$island->{'id'}");

		my($land, $landValue);
		$land = $island->{'land'};
		$landValue = $island->{'landValue'};
		my($x, $y);
		for($y = 0; $y < $HislandSize; $y++) {
			for($x = 0; $x < $HislandSize; $x++) {
				printf IOUT ("%x%02x", $land->[$x][$y], $landValue->[$x][$y]);
			}
			print IOUT "\n";
		}

		# ���ޥ��
		my($command, $cur, $i);
		$command = $island->{'command'};
		for($i = 0; $i < $HcommandMax; $i++) {
			printf IOUT ("%d,%d,%d,%d,%d\n", 
						 $command->[$i]->{'kind'},
						 $command->[$i]->{'target'},
						 $command->[$i]->{'x'},
						 $command->[$i]->{'y'},
						 $command->[$i]->{'arg'}
						 );
		}

		# ������Ǽ���
		my($lbbs);
		$lbbs = $island->{'lbbs'};
		for($i = 0; $i < $HlbbsMax; $i++) {
			print IOUT $lbbs->[$i] . "\n";
		}

		close(IOUT);
		unlink("${HdirName}/island.$island->{'id'}");
		rename("${HdirName}/islandtmp.$island->{'id'}", "${HdirName}/island.$island->{'id'}");
	}
}

#----------------------------------------------------------------------
# ������
#----------------------------------------------------------------------

# ɸ����Ϥؤν���
sub out {
	print STDOUT jcode::sjis($_[0]);
}

# �ǥХå���
sub HdebugOut {
   open(DOUT, ">>debug.log");
   print DOUT ($_[0]);
   close(DOUT);
}

# CGI���ɤߤ���
sub cgiInput {
	my($line, $getLine);

	# ���Ϥ������ä����ܸ쥳���ɤ�EUC��
	$line = <>;
	$line =~ tr/+/ /;
	$line =~ s/%([a-fA-F0-9][a-fA-F0-9])/pack("C", hex($1))/eg;
	$line = jcode::euc($line);
	$line =~ s/[\x00-\x1f\,]//g;

	# GET�Τ�Ĥ�������
	$getLine = $ENV{'QUERY_STRING'};

	# �оݤ���
	if($line =~ /CommandButton([0-9]+)=/) {
		# ���ޥ�������ܥ���ξ��
		$HcurrentID = $1;
		$defaultID = $1;
	}

	if($line =~ /ISLANDNAME=([^\&]*)\&/){
		# ̾������ξ��
		$HcurrentName = cutColumn($1, 32);
	}
	if($line =~ /MONSTERNAME=([^\&]*)\&/){
		# ̾������ξ��
		$Hi_name = cutColumn($1, 32);
	}

	if($line =~ /ISLANDID=([0-9]+)\&/){
		# ����¾�ξ��
		$HcurrentID = $1;
		$defaultID = $1;
	}

	# �ѥ����
	if($line =~ /OLDPASS=([^\&]*)\&/) {
		$HoldPassword = $1;
		$HdefaultPassword = $1;
	}
	if($line =~ /PASSWORD=([^\&]*)\&/) {
		$HinputPassword = $1;
		$HdefaultPassword = $1;
	}
	if($line =~ /PASSWORD2=([^\&]*)\&/) {
		$HinputPassword2 = $1;
	}

	# ��å�����
	if($line =~ /MESSAGE=([^\&]*)\&/) {
		$Hmessage = cutColumn($1, 80);
	}

	# ������Ǽ���
	if($line =~ /LBBSNAME=([^\&]*)\&/) {
		$HlbbsName = $1;
		$HdefaultName = $1;
	}
	if($line =~ /LBBSMESSAGE=([^\&]*)\&/) {
		$HlbbsMessage = cutColumn($1, 80);
	}

	if($line =~ /IMGLINEMAC=([^&]*)\&/){
		my($flag) = 'file:///' . $1;
		$HimgLine = $flag;
	}

	if($line =~ /IMGLINE=([^&]*)\&/){
		my($flag) = substr($1, 0 , -10);
		$flag =~ tr/\\/\//;
		if($flag eq 'del'){ $flag = $imageDir; } else { $flag = 'file:///' . $flag; }
		$HimgLine = $flag;
	}

	if($line =~ /OWNERNAME=([^\&]*)\&/){
		# �����ʡ�̾����ξ��
		$HownerName = cutColumn($1, 22);
	}
	# �ʣ���᥹����ץȥ⡼��
	if($line =~ /JAVAMODE=(cgi|java)/) {
		$HjavaMode = $1;
	}

	# ��Ʊ���̿��ե饰
	if($line =~ /async=true\&/) {
		$Hasync = 1;
	}

	if($line =~ /CommandJavaButton([0-9]+)=/) {
		# ���ޥ�������ܥ���ξ��ʣʣ���᥹����ץȡ�
		$HcurrentID = $1;
		$defaultID = $1;
	}
	# main mode�μ���
	if($line =~ /TurnButton/) {
		if($Hdebug == 1) {
			$HmainMode = 'Hdebugturn';
		}
	} elsif($line =~ /OwnerButton/) {
		$HmainMode = 'owner';
	} elsif($getLine =~ /Sight=([0-9]*)/) {
		$HmainMode = 'print';
		$HcurrentID = $1;
	} elsif($line =~ /ChangeOwnerName/) {
		$HmainMode = 'change';
	} elsif($getLine =~ /LogFileView=([0-9]*)/) {
		$HmainMode = 'logView';
		$Hlogturn = ($1 > $HlogMax) ? $HlogMax : $1;
	} elsif($line =~ /NewIslandButton/) {
		$HmainMode = 'new';
	} elsif($line =~ /LbbsButton(..)([0-9]*)/) {
		$HmainMode = 'lbbs';
		if($1 eq 'FO') {
			# �Ѹ���
			$HlbbsMode = 0;
			$HforID = $HcurrentID;
		} elsif($1 eq 'OW') {
			# ���
			$HlbbsMode = 1;
		} else {
			# ���
			$HlbbsMode = 2;
		}
		$HcurrentID = $2;

		# ������⤷��ʤ��Τǡ��ֹ�����
		$line =~ /NUMBER=([^\&]*)\&/;
		$HcommandPlanNumber = $1;

	} elsif($line =~ /ChangeInfoButton/) {
		$HmainMode = 'change';
	} elsif($line =~ /MessageButton([0-9]*)/) {
		$HmainMode = 'comment';
		$HcurrentID = $1;
	} elsif($line =~ /CommandJavaButton/) {
		$HmainMode = 'commandJava';
		$line =~ /COMARY=([^\&]*)\&/;
		$HcommandComary = $1;
	} elsif($line =~ /CommandButton/) {
		$HmainMode = 'command';

		# ���ޥ�ɥ⡼�ɤξ�硢���ޥ�ɤμ���
		$line =~ /NUMBER=([^\&]*)\&/;
		$HcommandPlanNumber = $1;
		$line =~ /COMMAND=([^\&]*)\&/;
		$HcommandKind = $1;
		$HdefaultKind = $1;
		$line =~ /AMOUNT=([^\&]*)\&/;
		$HcommandArg = $1;
		$line =~ /TARGETID=([^\&]*)\&/;
		$HcommandTarget = $1;
		$defaultTarget = $1;
		$line =~ /POINTX=([^\&]*)\&/;
		$HcommandX = $1;
		$HdefaultX = $1;
		$line =~ /POINTY=([^\&]*)\&/;
		$HcommandY = $1;
		$HdefaultY = $1;
		$line =~ /COMMANDMODE=(write|insert|delete)/;
		$HcommandMode = $1;

	} else {
		$HmainMode = 'top';
	}

}


#cookie����
sub cookieInput {
	my($cookie);

	$cookie = jcode::euc($ENV{'HTTP_COOKIE'});

	if($cookie =~ /${HthisFile}OWNISLANDID=\(([^\)]*)\)/) {
		$defaultID = $1;
	}
	if($cookie =~ /${HthisFile}OWNISLANDPASSWORD=\(([^\)]*)\)/) {
		$HdefaultPassword = $1;
	}
	if($cookie =~ /${HthisFile}LBBSNAME=\(([^\)]*)\)/) {
		$HdefaultName = $1;
	}
	if($cookie =~ /${HthisFile}POINTX=\(([^\)]*)\)/) {
		$HdefaultX = $1;
	}
	if($cookie =~ /${HthisFile}POINTY=\(([^\)]*)\)/) {
		$HdefaultY = $1;
	}
	if($cookie =~ /${HthisFile}KIND=\(([^\)]*)\)/) {
		$HdefaultKind = $1;
	}
	if($cookie =~ /${HthisFile}IMGLINE=\(([^\)]*)\)/) {
		$HimgLine = $1;
	}
	if($cookie =~ /${HthisFile}JAVAMODE=\(([^\)]*)\)/) {
		$makeMode = $1;
	}

}

#cookie����
sub cookieOutput {
	my($cookie, $info);

	# �ä�����¤�����
	my($sec, $min, $hour, $date, $mon, $year, $day, $yday, $dummy) =
		gmtime(time + 30 * 86400); # ���� + 30��

	# 2������
	$year += 1900;
	if ($date < 10) { $date = "0$date"; }
	if ($hour < 10) { $hour = "0$hour"; }
	if ($min < 10) { $min  = "0$min"; }
	if ($sec < 10) { $sec  = "0$sec"; }

	# ������ʸ����
	$day = ("Sunday", "Monday", "Tuesday", "Wednesday",
			"Thursday", "Friday", "Saturday")[$day];

	# ���ʸ����
	$mon = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
			"Jul", "Aug", "Sep", "Oct", "Nov", "Dec")[$mon];

	# �ѥ��ȴ��¤Υ��å�
	$info = "; expires=$day, $date\-$mon\-$year $hour:$min:$sec GMT\n";
	$cookie = '';
	
	if(($HcurrentID) && ($HmainMode eq 'owner')){
		$cookie .= "Set-Cookie: ${HthisFile}OWNISLANDID=($HcurrentID) $info";
	}
	if($HinputPassword) {
		$cookie .= "Set-Cookie: ${HthisFile}OWNISLANDPASSWORD=($HinputPassword) $info";
	}
	if($HlbbsName) {
		$cookie .= "Set-Cookie: ${HthisFile}LBBSNAME=($HlbbsName) $info";
	}
	if($HcommandX) {
		$cookie .= "Set-Cookie: ${HthisFile}POINTX=($HcommandX) $info";
	}
	if($HcommandY) {
		$cookie .= "Set-Cookie: ${HthisFile}POINTY=($HcommandY) $info";
	}
	if($HcommandKind) {
		# ��ư�ϰʳ�
		$cookie .= "Set-Cookie: ${HthisFile}KIND=($HcommandKind) $info";
	}
	if($HimgLine) {
		$cookie .= "Set-Cookie: ${HthisFile}IMGLINE=($HimgLine) $info";
	}
	if($HjavaMode) {
		$cookie .= "Set-Cookie: ${HthisFile}JAVAMODE=($HjavaMode) $info";
	}
	out($cookie);
}

#----------------------------------------------------------------------
# �桼�ƥ���ƥ�
#----------------------------------------------------------------------
sub hakolock {
	# ��å���
	$lfh = file_lock() or die return 0;
	return 1;
}

# ��å��򳰤�
sub unlock {
	# rename����å�
	rename($lfh->{current}, $lfh->{path});
}

# ����å�����
sub file_lock {
	my %lfh = (dir => "./", basename => "lock/lockfile", timeout => $unlockTime, trytime => 3, @_);
	$lfh{path} = $lfh{dir}.$lfh{basename};

	for (my $i = 0; $i < $lfh{trytime}; $i++, sleep 1) {
		return \%lfh if (rename($lfh{path}, $lfh{current} = $lfh{path} . time));
	}

	opendir(LOCKDIR, $lfh{dir});
	my @filelist = readdir(LOCKDIR);
	closedir(LOCKDIR);

	foreach (@filelist) {
		if (/^lockfile(\d+)/) {
			return \%lfh if (time - $1 > $lfh{timeout} and
			rename($lfh{dir} . $_, $lfh{current} = $lfh{path} . time));
			last;
		}
	}
	undef;
}

# �����������֤�
sub min {
	return ($_[0] < $_[1]) ? $_[0] : $_[1];
}

# �ѥ���ɥ��󥳡���
sub encode {
	if($cryptOn == 1) {
		return crypt($_[0], 'h2');
	} else {
		return $_[0];
	}
}

# �ѥ���ɥ����å�
sub checkPassword {
	my($p1, $p2) = @_;

	# null�����å�
	if($p2 eq '') {
		return 0;
	}

	# �ޥ������ѥ���ɥ����å�
	if($masterPassword eq $p2) {
		return 1;
	}

	# ����Υ����å�
	if($p1 eq encode($p2)) {
		return 1;
	}

	return 0;
}

# 1000��ñ�̴ݤ�롼����
sub aboutMoney {
	my($m) = @_;
	if($m < 500) {
		return "����500${HunitMoney}̤��";
	} else {
		$m = int(($m + 500) / 1000);
		return "����${m}000${HunitMoney}";
	}
}

# ����������ʸ���ν���
sub htmlEscape {
	my($s) = @_;
	$s =~ s/&/&amp;/g;
	$s =~ s/</&lt;/g;
	$s =~ s/>/&gt;/g;
	$s =~ s/\"/&quot;/g; #"
	return $s;
}

# 80�������ڤ�·��
sub cutColumn {
	my($s, $c) = @_;
	if(length($s) <= $c) {
		return $s;
	} else {
		# ���80�����ˤʤ�ޤ��ڤ���
		my($ss) = '';
		my($count) = 0;
		while($count < $c) {
			$s =~ s/(^[\x80-\xFF][\x80-\xFF])|(^[\x00-\x7F])//;
			if($1) {
				$ss .= $1;
				$count ++;
			} else {
				$ss .= $2;
			}
			$count ++;
		}
		return $ss;
	}
}

# ���̾�������ֹ������(ID����ʤ����ֹ�)
sub nameToNumber {
	my($name) = @_;

	# ���礫��õ��
	my($i);
	for($i = 0; $i < $HislandNumber; $i++) {
		if($Hislands[$i]->{'name'} eq $name) {
			return $i;
		}
	}

	# ���Ĥ���ʤ��ä����
	return -1;
}

# ���äξ���
sub monsterSpec {
	my($lv,$island) = @_;

	# ����
	my($kind) = int($lv / 10);

	# ̾��
	my($name);
	$name = $HmonsterName[$kind];

	# ����
	my($hp) = $lv - ($kind * 10);

	if($kind >= 4 and $island) {
		$kind = $island->{'i_type'};
		$hp = $island->{'i_hp'};
		$name = $island->{'i_name'};
	}

	return ($kind, $name, $hp);
}

# �и��Ϥ����٥�򻻽�
sub expToLevel {
	my($kind, $exp) = @_;
	my($i);
	if($kind == $HlandBase) {
		# �ߥ��������
		for($i = $maxBaseLevel; $i > 1; $i--) {
			if($exp >= $baseLevelUp[$i - 2]) {
				return $i;
			}
		}
		return 1;
	} else {
		# �������
		for($i = $maxSBaseLevel; $i > 1; $i--) {
			if($exp >= $sBaseLevelUp[$i - 2]) {
				return $i;
			}
		}
		return 1;
	}

}

# (0,0)����(size - 1, size - 1)�ޤǤο��������ŤĽФƤ���褦��
# (@Hrpx, @Hrpy)������
sub makeRandomPointArray {
	# �����
	my($y);
	@Hrpx = (0..$HislandSize-1) x $HislandSize;
	for($y = 0; $y < $HislandSize; $y++) {
		push(@Hrpy, ($y) x $HislandSize);
	}

	# ����åե�
	my ($i);
	for ($i = $HpointNumber; --$i; ) {
		my($j) = int(rand($i+1)); 
		if($i == $j) { next; }
		@Hrpx[$i,$j] = @Hrpx[$j,$i];
		@Hrpy[$i,$j] = @Hrpy[$j,$i];
	}
}

# 0����(n - 1)�����
sub random {
	return int(rand(1) * $_[0]);
}

#----------------------------------------------------------------------
# ��ɽ��
#----------------------------------------------------------------------
# �ե������ֹ����ǥ�ɽ��
sub logFilePrint {
	my($fileNumber, $id, $mode, $kankou) = @_;
	open(LIN, "${HdirName}/hakojima.log$_[0]");
	my($line, $m, $turn, $id1, $id2, $message);
	my($fi) = 0;

	while($line = <LIN>) {
		$line =~ /^([0-9]*),([0-9]*),([0-9]*),([0-9]*),(.*)$/;
		($m, $turn, $id1, $id2, $message) = ($1, $2, $3, $4, $5);

		# ��̩�ط�
		if($m == 1) {
			if(($mode == 0) || ($id1 != $id)) {
				# ��̩ɽ�������ʤ�
				next;
			}
			$m = '<B>(��̩)</B>';
		} else {
			$m = '';
		}

		# ɽ��Ū�Τ�
		if($id != 0) {
			if(($id != $id1) &&
			   ($id != $id2)) {
				next;
			}
		}

		# ɽ��
		if($kankou == 1) {

		out("<NOBR>${HtagNumber_}������$turn$m${H_tagNumber}��$message</NOBR><BR>\n");

	} elsif(($fi == 0) && ($mode == 0)) {
	 out("<NOBR><BR><B><I><FONT COLOR='#000000' SIZE=+2>������$turn$m��</FONT></I></B><BR><HR width=50% align=left>\n");
		out("<NOBR>${HtagNumber_}������$turn$m${H_tagNumber}��$message</NOBR><BR>\n");
		  $fi++;
		} else {
		out("<NOBR>${HtagNumber_}������$turn$m${H_tagNumber}��$message</NOBR><BR>\n");
		}
	}
#		out("<hr>\n");
	close(LIN);
}

#----------------------------------------------------------------------
# �ƥ�ץ졼��
#----------------------------------------------------------------------
# �����
sub tempInitialize {
	# �祻�쥯��(�ǥե���ȼ�ʬ)
	$HislandList = getIslandList($defaultID);
	$HtargetList = getIslandList($defaultID);
}

# ��ǡ����Υץ�������˥塼��
sub getIslandList {
	my($select) = @_;
	my($list, $name, $id, $s, $i);

	#��ꥹ�ȤΥ�˥塼
	$list = '';
	for($i = 0; $i < $HislandNumber; $i++) {
		$name = $Hislands[$i]->{'name'};
		$id = $Hislands[$i]->{'id'};
		if($id eq $select) {
			$s = 'SELECTED';
		} else {
			$s = '';
		}
		$list .=
			"<OPTION VALUE=\"$id\" $s>${name}��\n";
	}
	return $list;
}

# ��å�����
sub tempLockFail {
	# �����ȥ�
	out(<<END);
${HtagBig_}Ʊ�������������顼�Ǥ���<BR>
�֥饦���Ρ����ץܥ���򲡤���<BR>
���Ф餯�ԤäƤ�����٤����������${H_tagBig}$HtempBack
END
}

# �������
sub tempUnlock {
	# �����ȥ�
	out(<<END);
${HtagBig_}����Υ����������۾ｪλ���ä��褦�Ǥ���<BR>
��å�����������ޤ�����${H_tagBig}$HtempBack
END
}

# hakojima.dat���ʤ�
sub tempNoDataFile {
	out(<<END);
${HtagBig_}�ǡ����ե����뤬�����ޤ���${H_tagBig}$HtempBack
END
}

# �ѥ���ɴְ㤤
sub tempWrongPassword {
	out(<<END);
${HtagBig_}�ѥ���ɤ��㤤�ޤ���${H_tagBig}$HtempBack
END
}

# ��������ȯ��
sub tempProblem {
	out(<<END);
${HtagBig_}����ȯ�����Ȥꤢ������äƤ���������${H_tagBig}$HtempBack
END
}

# ���ּ���
sub get_time {
	my $time_;
	my $TZ_JST=3600*9;
	my($sec,$min,$hour,$mday,$mon,$year)=gmtime($_[0]+$TZ_JST);
	my $now=time();
	my($nsec,$nmin,$nhour,$nmday,$nmon,$nyear)=gmtime($now+$TZ_JST);
	if($_[0]<$now-12*3600 && ($nyear!=$year || $nmon!=$mon || $nmday!=$mday)) {
		$mon = ($mon < 9) ? "0".($mon+1) : $mon + 1;
		$mday = ($mday < 10) ? "0".$mday : $mday;
		$time_ = "(".$mon."/$mday)";
	} else {
		$hour = ($hour < 10) ? "0".$hour : $hour;
		$min = ($min < 10) ? "0".$min : $min;
		$time_ = "(<B>$hour:$min</B>)";
	}
	return $time_;
}
