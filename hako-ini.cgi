#----------------------------------------------------------------------
# Ȣ����� ver2.30
# ����ե�����
# ���Ѿ�������ˡ���ϡ�hako-readme.txt�ե�����򻲾�
#
# Ȣ�����Υڡ���: http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html
#----------------------------------------------------------------------
# ���Τ����
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �Ƽ�������
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �ʲ���ɬ�����ꤹ����ʬ
#----------------------------------------------------------------------

# ���Υե�������֤��ǥ��쥯�ȥ�
# $baseDir = 'http://�����С�/�ǥ��쥯�ȥ�';
#
# ��)
# http://cgi2.bekkoame.ne.jp/cgi-bin/user/u5534/hakoniwa/hako-main.cgi
# �Ȥ����֤���硢
# $baseDir = 'http://cgi2.bekkoame.ne.jp/cgi-bin/user/u5534/hakoniwa';
# �Ȥ��롣�Ǹ�˥���å���(/)���դ��ʤ���

$baseDir = 'http://localhost/~inora';

# �����ե�������֤��ǥ��쥯�ȥ�
# $imageDir = 'http://������';
$imageDir = 'http://localhost/~inora/hako/hakopng';

# �����Υ���������������ڡ���
$imageExp = 'http://localhost/~inora/hako/imgexp';

# jcode.pl�ΰ���
# $jcode = '/usr/libperl/jcode.pl';  # �٥å�����ξ��
# $jcode = './jcode.pl';			 # Ʊ���ǥ��쥯�ȥ���֤����
$jcode = './jcode.pl';

# �ޥ������ѥ����
# ���Υѥ���ɤϡ����٤Ƥ���Υѥ���ɤ����ѤǤ��ޤ���
# �㤨�С���¾����Υѥ�����ѹ�������Ǥ��ޤ���
$masterPassword = 'master';

# �ü�ѥ����
# ���Υѥ���ɤǡ�̾���ѹ��פ�Ԥ��ȡ�������λ�⡢�����������ͤˤʤ�ޤ���
# (�ºݤ�̾�����Ѥ���ɬ�פϤ���ޤ���)
$HspecialPassword = 'special';

# ������̾
$adminName = '������';

# �����ԤΥ᡼�륢�ɥ쥹
$email = '****@***.**.**';

# �Ǽ��Ĥ�̾��
$bbsname = '���Τ����Ǽ���';

# �Ǽ��ĥ��ɥ쥹
$bbs = 'http://localhost/~inora/bbs/petit.cgi';

# �Ǽ��ĤΥ��ե�����
$bbs_log = './bbs/petit.log';

# �ۡ���ڡ����Υ��ɥ쥹
$toppage = 'http://localhost/~inora/';

# �ޥ˥奢��Υ��ɥ쥹
$manual = 'http://localhost/~inora/man.html';

# �ǥ��쥯�ȥ�Υѡ��ߥå����
# �̾��0755�Ǥ褤����0777��0705��0704���Ǥʤ��ȤǤ��ʤ������С��⤢��餷��
$HdirMode = 0755;

# �ǡ����ǥ��쥯�ȥ��̾��
# ���������ꤷ��̾���Υǥ��쥯�ȥ�ʲ��˥ǡ�������Ǽ����ޤ���
# �ǥե���ȤǤ�'data'�ȤʤäƤ��ޤ������������ƥ��Τ���
# �ʤ�٤��㤦̾�����ѹ����Ƥ���������
$HdirName = 'data';

#----------------------------------------------------------------------
# ɬ�����ꤹ����ʬ�ϰʾ�
#----------------------------------------------------------------------

#----------------------------------------------------------------------
# �ʲ������ߤˤ�ä����ꤹ����ʬ
#----------------------------------------------------------------------
#----------------------------------------
# ������οʹԤ�ե�����ʤ�
#----------------------------------------
# 1�����󤬲��ä�
$HunitTime = 14400; # 4����

# �ǽ�������
$HislandLastTurn = 500;

# �۾ｪλ������
# (��å��岿�äǡ�����������뤫)
$unlockTime = 120;

# ��κ����
$HmaxIsland = 30;

# �ȥåץڡ�����ɽ��������Υ������
$HtopLogTurn = 1;

# ���ե������ݻ��������
$HlogMax = 8; 

# �Хå����åפ򲿥����󤪤��˼�뤫
$HbackupTurn = 12;

# �Хå����åפ򲿲�ʬ�Ĥ���
$HbackupTimes = 4;

# ȯ�����ݻ��Կ�
$HhistoryMax = 10;

# �������ޥ�ɼ�ư���ϥ������
$HgiveupTurn = 28;

# ���ޥ�����ϸ³���
# (�����ब�ϤޤäƤ����ѹ�����ȡ��ǡ����ե�����θߴ�����̵���ʤ�ޤ���)
$HcommandMax = 30;

# ������Ǽ��ĹԿ�����Ѥ��뤫�ɤ���(0:���Ѥ��ʤ���1:���Ѥ���)
$HuseLbbs = 1;

# ������Ǽ��ĹԿ�
$HlbbsMax = 10;

# ����礭��
# (�ѹ��Ǥ��ʤ�����)
$HislandSize = 12;

# ¾�ͤ�����򸫤��ʤ����뤫
# 0 �����ʤ�
# 1 ������
# 2 100�ΰ̤ǻͼθ���
$HhideMoneyMode = 2;

# �ѥ���ɤΰŹ沽(0���ȰŹ沽���ʤ���1���ȰŹ沽����)
$cryptOn = 1;

# �ǥХå��⡼��(1���ȡ��֥������ʤ��ץܥ��󤬻��ѤǤ���)
$Hdebug = 0;

# ---------------------------------------------------------------- 
# �������������ػ�������
# ¾�����С������Ȣ������ץȤؤ�ľ��󥯤�ػߤ�������Ǥ�
# �������Ѥ���ȡ���󥿥�Ǽ����������Ѥ��Ƥ�����ϡ����������ľ��󥯤����ʤ��ʤäƤ��ޤ��ޤ�
# ������ɤ�Ǥ褯�狼��ʤ����ϡ����ꤷ�ʤ�����̵��Ǥ�
# 
# 1�ξ���¾�����Ȥ���Υ��������ػ�
# 0�ʤ顢���Ѥ��ʤ�������
$Href = 0;

# Ȣ�����֥ڡ���
# ���֥����ȤΣգң̤���http://www.hakoniwa.com/~gabacho/hako/hako-main.cgi
# ���ä��顢http://www.hakoniwa.com/~gabacho/���Ȥʤ�ޤ�

$ref_page = 'http://localhost/';

# Ȣ��ȥåץڡ���
# �����������������ä����Υ����
# ���Τξ��ϡ��嵭��Ʊ���ˤʤ�ޤ�

$ref_main = 'http://localhost/';

# ---------------------------------------------------------------- 

#----------------------------------------
# ��⡢�����ʤɤ������ͤ�ñ��
#----------------------------------------
# ������
$HinitialMoney = 1000;

# �������
$HinitialFood = 3000;

# �����ñ��
$HunitMoney = '����';

# ������ñ��
$HunitFood = '00�ȥ�';

# �͸���ñ��
$HunitPop = '00��';

# ������ñ��
$HunitArea = '00����';

# �ڤο���ñ��
$HunitTree = '00��';

# �ڤ�ñ�������������
$HtreeValue = 5;

# ����������ڤ��������ܿ�
$HtreeUp = 1;

# ̾���ѹ��Υ�����
$HcostChangeName = 0;

# �͸�1ñ�̤�����ο���������
$HeatenFood = 0.2;

#----------------------------------------
# ���Ϥηи���
#----------------------------------------
# �и��ͤκ�����
$HmaxExpPoint = 200; # ������������Ǥ�255�ޤ�

# ��٥�κ�����
$maxBaseLevel = 5;  # �ߥ��������
$maxSBaseLevel = 3; # �������

# �и��ͤ������Ĥǥ�٥륢�åפ�
@baseLevelUp, @sBaseLevelUp;
@baseLevelUp = (20, 60, 120, 200); # �ߥ��������
@sBaseLevelUp = (50, 200);		 # �������

#----------------------------------------
# �ɱһ��ߤμ���
#----------------------------------------
# ���ä�Ƨ�ޤ줿����������ʤ�1�����ʤ��ʤ�0
$HdBaseAuto = 0;

#----------------------------------------
# �ҳ�
#----------------------------------------
# �̾�ҳ�ȯ��Ψ(��Ψ��0.1%ñ��)
$HdisEarthquake	= 3;  # �Ͽ�
$HdisTsunami	= 10; # ����
$HdisTyphoon	= 15; # ����
$HdisMeteo		= 15; # ���
$HdisHugeMeteo	= 0;  # �������
$HdisEruption	= 10; # ʮ��
$HdisFire		= 5;  # �к�
$HdisMaizo		= 20; # ��¢��
$HdisVirus		= 200;# ���Τ��µ�
$HdisTyphIno	= 300;# ���Τ�����������

# ���Τ���µ�
$VIRUS[0]	= '���٤�Ҥ���';
$VIRUS[1]	= '�����¤ˤ�����';
$VIRUS[2]	= '��Ĳ�ˤʤ�';
$VIRUS[3]	= 'Ƭ�ˤ��Ҥɤ���';
$VIRUS[4]	= 'ʢ�ˤ��Ҥɤ���';

# ��������
$HdisFallBorder = 200; # �����³��ι���(Hex��)
$HdisFalldown   = 0; # ���ι�����Ķ�������γ�Ψ

# ����
$HdisMonsBorder1 = 2000; # �͸����1(���å�٥�1)
$HdisMonsBorder2 = 3000; # �͸����2(���å�٥�2)
$HdisMonsBorder3 = 4000; # �͸����3(���å�٥�3)
$HdisMonster	 = 2;	 # ñ�����Ѥ�����νи�Ψ(0.01%ñ��)

# ����
$HmonsterNumber  = 4;

# �ƴ��ˤ����ƽФƤ�����ä��ֹ�κ�����
$HmonsterLevel1  = 1; # ���󥸥�ޤ�
$HmonsterLevel2  = 2; # ���Τ饴�����Ȥޤ�
$HmonsterLevel3  = 3; # ���󥰤��Τ�ޤ�(����)

# ̾��
@HmonsterName = 
	(
	 '�ᥫ���Τ�',			# 0(��¤)
	 '���å��󥸥�',		# 1
	 '���ä��Τ饴������',	# 2
	 '���å�����',			# 3
	 '�٥ӡ����Τ�',		# 4
	 '�������Τ�',			# 5
	 '���꡼�󤤤Τ�',		# 6
	 '��åɤ��Τ�',		# 7
	 '���������Τ�',		# 8
	 '���󥰤��Τ�',		# 9
	 '�������󤤤Τ�',		# 10
	 '���줤�Τ�'			# 11
);

# �������ϡ����Ϥ������ü�ǽ�ϡ��и��͡����Τ�����
@HmonsterBHP	 = ( 2, 1, 1, 4,  1, 1, 1, 1);
@HmonsterDHP	 = ( 0, 2, 0, 2,  0, 0, 0, 0);
@HmonsterSpecial = ( 0, 3, 2, 4,  2, 0, 0, 0, 1);
@HmonsterExp	 = ( 5, 7, 10,20);
@HmonsterValue   = ( 0, 500, 300, 1500);

# �ü�ǽ�Ϥ����Ƥϡ�
# 0 �äˤʤ�
# 1 ­��®��(����2�⤢�뤯)
# 2 ­���ȤƤ�®��(���粿�⤢�뤯������)
# 3 ���������ϹŲ�
# 4 ����������ϹŲ�
# 5 �ɤ�̲��
# 6 �����ܤ�

# �����ե�����
$HmonsterImage[0]	= 'monster0.png';
$HmonsterImage[1]	= 'monster1.png';
$HmonsterImage[2]	= 'monster2.png';
$HmonsterImage[3]	= 'monster3.png';
$HmonsterImage[4]	= 'monster5.png';
$HmonsterImage[5]	= 'monster6.png';
$HmonsterImage[6]	= 'monster7.png';
$HmonsterImage[7]	= 'monster8.png';
$HmonsterImage[8]	= 'monster9.png';
$HmonsterImage[9]	= 'monster10.png';
$HmonsterImage[10]	= 'monster11.png';
$HmonsterImage[11]	= 'monster6.png';


# �����ե����뤽��2(�Ų���)
@HmonsterImage2 =
	('', 'monster4.png', '', 'monster4.png');

# ���Τ���Ĺ�ٹ礤
$INORA[0] = 100;
$INORA[1] = 200;
$INORA[2] = 400;

# ��������Ψ������1�����Ϥ�Ʊ����
$FOOD[4]  = 5;  # �٥ӡ����Τ�
$FOOD[5]  = 20; # �������Τ�
$FOOD[6]  = 10; # ���꡼�󤤤Τ�
$FOOD[7]  = 10; # ��åɤ��Τ�
$FOOD[8]  = 10; # ���������Τ�
$FOOD[9]  = 15; # ���󥰤��Τ�
$FOOD[10] = 12; # �������󤤤Τ�
$FOOD[11] = 8;  # ���줤�Τ�

# ���ܿ�̲�������
$SLEEP[4]  = 6; # �٥ӡ����Τ�
$SLEEP[5]  = 7; # �������Τ�
$SLEEP[6]  = 3; # ���꡼�󤤤Τ�
$SLEEP[7]  = 3; # ��åɤ��Τ�
$SLEEP[8]  = 3; # ���������Τ�
$SLEEP[9]  = 4; # ���󥰤��Τ�
$SLEEP[10] = 4; # �������󤤤Τ�
$SLEEP[11] = 2; # ���줤�Τ�

# ���ܹ�ư��������ʤĤޤ굯���Ƥ���֡�
$WAKE[4]  = 4; # �٥ӡ����Τ�
$WAKE[5]  = 3; # �������Τ�
$WAKE[6]  = 7; # ���꡼�󤤤Τ�
$WAKE[7]  = 7; # ��åɤ��Τ�
$WAKE[8]  = 7; # ���������Τ�
$WAKE[9]  = 6; # ���󥰤��Τ�
$WAKE[10] = 6; # �������󤤤Τ�
$WAKE[11] = 8; # ���줤�Τ�

# ���ޥ�ɤˤ����Ĺ�μ��̽�����
@rebi_def	= (50, 100, 300, 0);
@rebi_ang	= (0,0,0,0, 0, 0, 1, 1, 1, 2, 0, 3);
@rebi_heal	= (0,0,0,0, 0, 0, 2, 2, 2, 1, 0, 3);
@rebi_hp	= (0,0,0,0, 1, 2, 1, 1, 1, 1, 0, 0);
@rebi_arm	= (0,0,0,0, 1, 1, 2, 1, 0, 1, 0, 2);
@rebi_cute	= (0,0,0,0, 1, 1, 0, 2, 1, 1, 0, 0);
@rebi_int	= (0,0,0,0, 1, 1, 1, 0, 2, 1, 0, 0);

# ���٥�ȡ�0.1%��
$HinoraEventQuake = 250;  # �����������Ͽ�

#----------------------------------------
# ����
#----------------------------------------
# ���Ĥμ���
$HoilMoney = 1000;

# ���Ĥθϳ��Ψ
$HoilRatio = 40;

#----------------------------------------
# ��ǰ��
#----------------------------------------
# �����ढ�뤫
$HmonumentNumber = 4;

# ̾��
@HmonumentName = 
	(
	 '��Υꥹ', 
	 'ʿ�µ�ǰ��', 
	 '�襤����',
	 '���Τ鵭ǰ��'
	);

# �����ե�����
@HmonumentImage = 
	(
	 'monument0.png',
	 'monument0.png',
	 'monument0.png',
	 'monument1.png'
	 );


#----------------------------------------
# �޴ط�
#----------------------------------------

$HturnPrizeUnit	= 100; # �������դ򲿥�������˽Ф���

# �ޤ�̾��
$Hprize[0] = '��������';
$Hprize[1] = '�˱ɾ�';
$Hprize[2] = 'Ķ�˱ɾ�';
$Hprize[3] = '����˱ɾ�';
$Hprize[4] = 'ʿ�¾�';
$Hprize[5] = 'Ķʿ�¾�';
$Hprize[6] = '���ʿ�¾�';
$Hprize[7] = '�����';
$Hprize[8] = 'Ķ�����';
$Hprize[9] = '��˺����';
$Hprize[10]= '���Τ��Ӽ���';
$Hprize[11]= '���Τ饳��ƥ���';
$Hprize[12]= '���Τ饯�������';

#----------------------------------------
# �����ط�
#----------------------------------------
# <BODY>�����Υ��ץ����
$htmlBody = 'BGCOLOR="#EEFFFF"';

# ������Υ����ȥ�ʸ��
$Htitle = '���Τ����';

# ����
# �����ȥ�ʸ��
$HtagTitle_ = '<FONT SIZE=7 COLOR="#8888ff">';
$H_tagTitle = '</FONT>';

# H1������
$HtagHeader_ = '<FONT COLOR="#4444ff">';
$H_tagHeader = '</FONT>';

# �礭��ʸ��
$HtagBig_ = '<FONT SIZE=6>';
$H_tagBig = '</FONT>';

# ���Τ��̾��
$HtagIName_ = '<FONT COLOR="#4444ff"><B>';
$H_tagIName = '</B></FONT>';

# ���̾���ʤ�
$HtagName_ = '<FONT COLOR="#a06040"><B>';
$H_tagName = '</B></FONT>';

# �����ʤä����̾��
$HtagName2_ = '<FONT COLOR="#808080"><B>';
$H_tagName2 = '</B></FONT>';

# ��̤��ֹ�ʤ�
$HtagNumber_ = '<FONT COLOR="#800000"><B>';
$H_tagNumber = '</B></FONT>';

# ���ɽ�ˤ����븫����
$HtagTH_ = '<FONT COLOR="#C00000"><B>';
$H_tagTH = '</B></FONT>';

# ��ȯ�ײ��̾��
$HtagComName_ = '<FONT COLOR="#d08000"><B>';
$H_tagComName = '</B></FONT>';

# �ҳ�
$HtagDisaster_ = '<FONT COLOR="#ff0000"><B>';
$H_tagDisaster = '</B></FONT>';

# ������Ǽ��ġ��Ѹ��Ԥν񤤤�ʸ��
$HtagLbbsSS_ = '<FONT COLOR="#0000ff"><B>';
$H_tagLbbsSS = '</B></FONT>';

# ������Ǽ��ġ����ν񤤤�ʸ��
$HtagLbbsOW_ = '<FONT COLOR="#ff0000"><B>';
$H_tagLbbsOW = '</B></FONT>';

# ������Ǽ��ġ���̵���Ѹ��Ԥν񤤤�ʸ��
$HtagLbbsSK_ = '<FONT COLOR="#003333"><B>';
$H_tagLbbsSK = '</B></FONT>';

# �̾��ʸ����(��������Ǥʤ���BODY�����Υ��ץ�����������ѹ����٤�
$HnormalColor = '#000000';

# ���ɽ�������°��
$HbgTitleCell   = 'BGCOLOR="#ccffcc"'; # ���ɽ���Ф�
$HbgNumberCell  = 'BGCOLOR="#ccffcc"'; # ���ɽ���
$HbgNameCell	= 'BGCOLOR="#ccffff"'; # ���ɽ���̾��
$HbgInfoCell	= 'BGCOLOR="#ccffff"'; # ���ɽ��ξ���
$HbgCommentCell = 'BGCOLOR="#ccffcc"'; # ���ɽ��������
$HbgInputCell   = 'BGCOLOR="#ccffcc"'; # ��ȯ�ײ�ե�����
$HbgMapCell		= 'BGCOLOR="#ccffcc"'; # ��ȯ�ײ��Ͽ�
$HbgCommandCell = 'BGCOLOR="#ccffcc"'; # ��ȯ�ײ����ϺѤ߷ײ�

#----------------------------------------
# �إå������եå���
#----------------------------------------
# �إå�
sub tempHeader {
	return if($Hasync);

	my($HimgFlag) = 0;
	if($HimgLine eq '' || $HimgLine eq $imageDir){
		$baseIMG = $imageDir;
		$HimgFlag = 1;
	} else {
		$baseIMG = $HimgLine;
	}
	# �����Υ���������Υ��顼����Ū�˲����ʸ����������ʤ��Ǥ���
	$baseIMG =~ s/�޽�į��/�ǥ����ȥå�/g;

	my $time_ = get_time((stat($bbs_log))[9],1);

	out(<<END);
Content-type: text/html

<HTML>
<HEAD>
<TITLE>
$Htitle
</TITLE>
<STYLE type="text/css">
<!--
a:link		{ color:#3300CC }
a:visited	{ color:#3300CC }
a:active	{ color:#FF0000 }
a:hover	    { color:#FF0000 }
th			{ filter:blur(direction=120,strength=2) }
-->
</STYLE>
<BASE HREF="$baseIMG/">
</HEAD>
$BODY
<A HREF="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html">Ȣ����祹����ץ����۸�</A>
��<A HREF="http://appoh.execweb.cx/hakoniwa/">Ȣ��Java������ץ��� ���۸�</A>
��<A HREF="http://espion.just-size.jp/archives/dist_hako/">���Τ���祹����ץ����۸�</A>
��<A HREF="$toppage">�ȥåץڡ���</A>
��<A HREF="$bbs">$bbsname</A>$time_
��<A HREF="$HthisFile?LogFileView=1" target=_blank>�Ƕ�ν����</A>
��<A HREF="$manual">�ޥ˥奢��</A>
</nobr>
<HR>
END
	if($HimgFlag) {
		out("<FONT COLOR=RED>�����С���ٷڸ��ΰ٤ˡ������Υ����������ԤäƲ�����褦�ˤ��ꤤ�פ��ޤ�</FONT>");
		out("<HR>");
	}
}

# �եå�
sub tempFooter {
	out(<<END);
<HR>
<P align=right>
<NOBR>
<A HREF="http://www.bekkoame.ne.jp/~tokuoka/hakoniwa.html" target=_blank>Ȣ����祹����ץ����۸�</A>
����<A HREF="$toppage">�ȥåץڡ���</A>
����<A HREF="$bbs">$bbsname</A>
����<A HREF="$HthisFile?LogFileView=1" target=_blank>�Ƕ�ν����</A>
</nobr><BR><BR>
������:$adminName(<A HREF="mailto:$email">$email</A>)<BR>
</P>
</BODY>
</HTML>
END

}


1;

